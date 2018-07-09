from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import TutorialSeries, Lesson


def tutorial_series_list(request):
    tutorial = TutorialSeries.objects.all().prefetch_related('tutorial')
    tutorial = tutorial.annotate(lesson=Count('tutorial'))


# PAGINATOR CODE FOR FUTURE USAGE

    paginator = Paginator(tutorial, 1)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)  # num_pages gives no of pages


    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >=5 else 0
    end_index = index +5 if index <= max_index-5 else max_index
    page_range = paginator.page_range[start_index:end_index]

    template = 'tutorial/tutorialseries_list.html'
    context = {
        'tutorial': tutorial,
        'items':items,
        'page_range': page_range,
    }
    return render(request, template, context)


# def tutorial_series_detail(request, slug):
#     series = get_object_or_404(TutorialSeries, slug=slug)
#     lessons = series.lesson_set.filter(tutorial_series = series)
#
#     template = 'tutorial/tutorialseries_detail.html'
#     context = {
#         'series': series,
#          'lessons': lessons,
#     }
#     return render(request, template, context)
#

class TutorialSeriesDetailView(DetailView):
    model = TutorialSeries

    def get_context_data(self, **kwargs):
        context = super(TutorialSeriesDetailView, self).get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(tutorial_series__name=self.object)
        return context


# class LessonDetailView(DetailView):
#     model = Lesson
#
#     def get_object(self, tutorial_series, slug):
#         tutorial_series = TutorialSeries.objects.filter(slug = tutorial_series).first()
#         object = get_object_or_404(Lesson,tutorial_series = tutorial_series, slug = slug)
#         return object
#
#
#     def get(self, request, tutorial_series, slug):
#         self.object = self.get_object(tutorial_series, slug)
#         context = self.get_context_data(object = self.object)
#         return self.render_to_response(context)


def lesson_detail(request, tutorial_series, slug):
    lesson = get_object_or_404(Lesson, tutorial_series__slug=tutorial_series, slug=slug)
    template = 'tutorial/lesson_detail.html'
    context = {
        'lesson': lesson,
    }
    return render(request, template, context)

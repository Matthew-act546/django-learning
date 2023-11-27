from django.shortcuts import render, get_object_or_404,redirect
from django.views import View

from .models import Course
from .forms import CourseModelForm
# Create your views here.

class CourseObjectMixin(object):
    model = Course
    def get_object(self):
        my_id = self.kwargs.get('my_id')
        obj = None
        if my_id is not None:
            obj = get_object_or_404(Course, id=my_id)
        return obj

class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)
    

class CourseDeleteView(CourseObjectMixin, View):
    template_name = 'courses/course_delete.html'

    def get(self, request, my_id=None, *args, **kwargs):
        """GET method"""
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)
    
    def post(self, request, my_id=None, *args, **kwargs):
        """POST method"""
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')
        return render(request, self.template_name, context)
        


class CourseUpdateView(CourseObjectMixin, View):
    template_name = 'courses/course_update.html'

    def get(self, request, my_id=None, *args, **kwargs):
        """GET method"""
        context = {}
        obj = self.get_object()

        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)
    
    def post(self, request, my_id=None, *args, **kwargs):
        """POST method"""
        context = {}
        obj = self.get_object()
        
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)
        

class CourseCreateView(View):
    template_name = 'courses/course_create.html'
    
    def get(self, request, my_id=None, *args, **kwargs):
        """GET method"""
        form = CourseModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)
    
    def post(self, request, my_id=None, *args, **kwargs):
        """POST method"""
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
            # return redirect('.') same as at the top
        context = {'form': form}
        return render(request, self.template_name, context)
    
class CourseView(CourseObjectMixin, View):
    template_name = 'courses/course_detail.html'
    
    def get(self, request, my_id=None, *args, **kwargs):
        context = {'object': self.get_object()}
        return render(request, self.template_name, context)
    
def my_fbv(request, *args, **kwargs):
    print(request.method)
    return render(request, 'about.html', {})
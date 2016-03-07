from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.forms import formset_factory, modelformset_factory
from .forms import CourseForm
from .models import Course

@login_required
def add_classes_page(request):
    quarter = "spring2016"
    CourseFormSet = modelformset_factory(Course, fields=('course',), max_num=4, extra=4)
    formset = CourseFormSet(queryset=Course.objects.filter(quarter=quarter, user=request.user.userprofile))
    # print formset





    # classes = Course.objects.filter(quarter=quarter, user=request.user.userprofile)
    # CourseFormSet = formset_factory(CourseForm, extra=4)
    # formset = CourseFormSet(initial=classes)

    # print classes

    context = {
        "formset" : formset,
        "quarter" : quarter,
    }


    return render(request, "classes/add_class.html", context)
    # return HttpResponse("yay")



@login_required
def quarter(request, quarter):
    print quarter

    CourseFormSet = modelformset_factory(Course, fields=('course',), max_num=4, extra=4)
    formset = CourseFormSet(queryset=Course.objects.filter(quarter=quarter, user=request.user.userprofile))



    # course_form = Course.objects.filter(quarter=quarter, user=request.user.userprofile)
    # CourseFormSet = formset_factory(CourseForm, instance=course_form)
    # form = CourseForm(instance=course_form)
    # classes = Course.objects.filter(quarter=quarter, user=request.user.userprofile)
    # CourseFormSet = formset_factory(CourseForm, extra=4)
    # formset = CourseFormSet(initial=Course.objects.filter(quarter=quarter, user=request.user.userprofile))

    # print formset
    # print formset
    # print CourseFormSet
    # print formset
    # print classes

    context = {
        "formset" : formset,
        "quarter" : quarter,
    }
    return render(request, "classes/add_class.html", context)



@login_required
def add_classes(request, quarter):
    CourseFormSet = formset_factory(CourseForm)
    if request.method == 'POST':
        formset = CourseFormSet(request.POST or None)
        if formset.is_valid():
            for form in formset:
                instance = form.save(commit=False)
                instance.quarter = quarter
                instance.user = request.user.userprofile
                instance.save()

                print "in formset form bitch!!!"
            print "weepieeee"
            # print formset


    return redirect('add_classes_page')

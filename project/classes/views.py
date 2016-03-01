from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.forms import formset_factory
from .forms import CourseForm

@login_required
def add_classes_page(request):
    CourseFormSet = formset_factory(CourseForm, extra=4)
    context = {
        "formset" : CourseFormSet,
    }
    return render(request, "classes/add_class.html", context)

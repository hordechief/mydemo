from django.shortcuts import render
from django.core.urlresolvers import reverse
from django import http


def home(request):
    return render(request, "base.html", {})
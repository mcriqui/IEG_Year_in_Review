from django.shortcuts import render


def get_template(request):
    return render(request, 'base.html')


def return_highlights(request):
    return render(request, 'highlights.html')


def return_new(request):
    return render(request, 'new.html')


def return_who_here(request):
    return render(request, 'who_here.html')


def return_types_of_events(request):
    return render(request, 'types_of_events.html')


def return_about_the_center(request):
    return render(request, 'about_the_center.html')


def return_facility(request):
    return render(request, 'facility.html')


def return_team(request):
    return render(request, 'team.html')
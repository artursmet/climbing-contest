#coding: utf-8
from __future__ import unicode_literals
import csv

from django.template.response import TemplateResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

from contest.models import Contest
from contest.forms import ContestantForm


def subscribe(request, contest_pk):
    contest = get_object_or_404(Contest, pk=contest_pk)
    if not contest.is_active():
        messages.error(request, 'Zapisy się zakończyły')
        return redirect('homepage')

    if request.method == 'POST':
        form = ContestantForm(contest=contest, data=request.POST)
        if form.is_valid():
            subscribtion = form.save(commit=False)
            # toDO e-mail
            subscribtion.save()
            messages.success(request, 'Dziękujemy za zgłoszenie')
            return redirect('all_groups', contest_pk=contest.pk)
    else:
        form = ContestantForm(contest=contest)

    return TemplateResponse(request, 'contest/form.html',
        {'form': form, 'contest': contest})


def all_groups(request, contest_pk):
    contest = Contest.objects.get(pk=contest_pk)
    return TemplateResponse(request, 'contest/all_groups.html',
        {'contest': contest})


@user_passes_test(lambda u: u.is_staff)
def create_csv_list(request, contest_pk):
    contest = get_object_or_404(Contest, pk=contest_pk)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment; filename='zawodnicy.csv'"
    writer = csv.writer(response)
    writer.writerow([
        'Imię'.encode('utf-8'),
        'Nazwisko',
        'Płeć',
        'Wiek',
        'Klub/Sponsor',
        'Koszulka',
        'Grupa']
    )
    for group in contest.group_set.all():
        for person in group.contestant_set.all():
            writer.writerow([
                person.first_name.encode('utf-8'),
                person.surname.encode('utf-8'),
                person.get_gender_display().encode('utf-8'),
                person.age,
                person.sponsor.encode('utf-8'),
                person.group.name.encode('utf-8'),
                person.shirt_size
            ])

    return response

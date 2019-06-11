from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def teamDetails(request):
    teamMembers = {
        'teamMembers': [
            {'firstName': 'Belciug',
            'lastName': 'Maria',
            'role':'Team leader/QA tester'},
            {'firstName': 'Bolohan',
             'lastName': 'Cosmin',
            'role':'Backend Developer'},
            {'firstName': 'Ciobanitei',
            'lastName': 'Cezar',
            'role':'Designer'},
            {'firstName': 'Hatnean',
            'lastName': 'Sebastian',
            'role':'Frontend Developer'},
            {'firstName': 'Leonte',
            'lastName': 'Andrei',
            'role':'Backend Developer'}
        ]}

    return render(request, 'schedular/team-details.html', teamMembers)


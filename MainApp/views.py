from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView
from .models import Party, Candidate
from datetime import datetime
from django.http import HttpResponseRedirect


def home(request):
    context = {
        'year': datetime.timetuple(datetime.now()).tm_year,
    }
    return render(request, 'MainApp/home.html', context)


class galleryList(ListView):
    model = Party
    context_object_name = 'parties'
    template_name = 'MainApp/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = datetime.timetuple(datetime.now()).tm_year
        return context


def regParty(request):
    context = {
        'year': datetime.timetuple(datetime.now()).tm_year,
    }
    if request.method == 'POST':
        party = Party(
            name=request.POST['party_name'],
            slogan=request.POST['party_slogan'],
            logo=request.FILES['party_logo']
        )
        party.save()
        return redirect('MainApp:viewPartyDetail', pk=party.pk)
    return render(request, 'MainApp/registerParty.html', context)


class viewPartyDetail(DetailView):
    model = Party
    template_name = 'MainApp/viewParty.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = datetime.timetuple(datetime.now()).tm_year
        return context


def regCandidate(request):
    parties = Party.objects.all()
    if request.method == 'POST':
        candidate = Candidate(
            name=request.POST['candidate_name'],
            party=Party.objects.get(name=request.POST['candidate_party']),
            position=request.POST['candidate_position'],
            img=request.FILES['candidate_img'],
            description=request.POST.get('candidate_description'),
        )
        candidate.save()
    context = {
        'parties': parties,
        'year': datetime.timetuple(datetime.now()).tm_year,
    }
    return render(request, 'MainApp/registerCandidate.html', context)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

# Create your views here.

now = timezone.now()


def home(request):
    return render(request, 'padneb/home.html', {'padneb': home})


def contact_us(request):
    return render(request, 'padneb/contact_us.html', {'padneb': contact_us})


def about(request):
    return render(request, 'padneb/about.html', {'padneb': about})


@login_required
def member_list(request):
    member = Member.objects.filter(created_date__lte=timezone.now())
    return render(request, 'padneb/member_list.html', {'members': member})


@login_required
def member_edit(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        # update
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            member = form.save(commit=False)
            member.updated_date = timezone.now()
            member.save()
            member = Member.objects.filter(admission_date__lte=timezone.now())
            return render(request, 'padneb/member_list.html', {'members': member})
    else:
        # edit
        form = MemberForm(instance=member)
    return render(request, 'padneb/member_edit.html', {'form': form})


@login_required
def member_new(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.created_date = timezone.now()
            member.save()
            members = Member.objects.filter(created_date__lte=timezone.now())
            return render(request, 'padneb/member_list.html', {'members': members})
    else:
        form = MemberForm()
        # print("Else")
    return render(request, 'padneb/member_new.html', {'form': form})


@login_required
def contribution_list(request):
    contributions = Contribution.objects.filter(date__lte=timezone.now())
    return render(request, 'padneb/contribution_list.html', {'contributions': contributions})


@login_required
def contribution_edit(request, pk):
    contribution = get_object_or_404(Contribution, pk=pk)
    if request.method == "POST":
        form = ContributionForm(request.POST, instance=contribution)
        if form.is_valid():
            contribution = form.save()
            # service.customer = service.id
            contribution.updated_date = timezone.now()
            contribution.save()
            contributions = Contribution.objects.filter(date__lte=timezone.now())
            return render(request, 'padneb/contribution_list.html', {'contributions': contributions})
    else:
        # print("else")
        form = ContributionForm(instance=contribution)
    return render(request, 'padneb/contribution_edit.html', {'form': form})


@login_required
def contribution_new(request):
    if request.method == "POST":
        form = ContributionForm(request.POST)
        if form.is_valid():
            contribution = form.save(commit=False)
            contribution.date = timezone.now()
            contribution.save()
            contributions = Contribution.objects.filter(date=timezone.now())
            return render(request, 'padneb/contribution_list.html', {'contributions': contributions})
    else:
        form = ContributionForm()
        # print("Else")
    return render(request, 'padneb/contribution_new.html', {'form': form})


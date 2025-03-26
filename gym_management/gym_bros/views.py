from django.shortcuts import render, get_object_or_404, redirect
from .models import Member
from .forms import MemberForm

from django.http import HttpResponse



def home(request):
    return render(request, 'gym_bros/base.html')




def member_list(request):
    return HttpResponse("<h1>List of Gym Members</h1>")


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Member
from .forms import MemberForm  # Assuming you've created a form for Member

# List all members
def member_list(request):
    members = Member.objects.all()  # Fetch all members from the database
    return render(request, 'gym_bros/member_list.html', {'members': members})

# Add a new member
def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new member to the database
            return redirect('member_list')  # Redirect to the member list
    else:
        form = MemberForm()
    return render(request, 'gym_bros/member_form.html', {'form': form})

# Edit an existing member
def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)  # Fetch the member by primary key
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()  # Save changes to the database
            return redirect('member_list')  # Redirect to the member list
    else:
        form = MemberForm(instance=member)
    return render(request, 'gym_bros/member_form.html', {'form': form})

# Delete a member
def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)  # Fetch the member by primary key
    if request.method == 'POST':
        member.delete()  # Delete the member from the database
        return redirect('member_list')  # Redirect to the member list
    return render(request, 'gym_bros/member_confirm_delete.html', {'member': member})

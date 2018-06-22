from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from TwinBrooksUser.forms import MemberFormPersonal, MemberProfilePhotoForm


# Quick login redirect view, it can be used to add in new login add ons
# for the login attempts
@login_required
def login_redirect(request):
    return redirect('/calendar')


# Allows members to edit personal profile information
@login_required
def edit_profile_information(request):
    user = request.user
    form = MemberFormPersonal(request.POST or None,
                              request.FILES or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Successfully updated profile! ')
            return redirect("TwinBrooksUser:edit_profile_information")
    profile_active = True
    context = {
        'profile_active': profile_active,
        'form': form
    }
    return render(request, 'app/user/profile/edit_profile_information.html', context)


# Allows members to edit personal profile information
@login_required
def edit_profile_photo(request):
    user = request.user
    print user.profile_image
    form = MemberProfilePhotoForm(
        request.POST or None, request.FILES or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Successfully updated profile photo! ')
            return redirect("TwinBrooksUser:edit_profile_information")
    profile_active = True
    context = {
        'profile_active': profile_active,
        'form': form
    }
    return render(request, 'account/change_profile_photo.html', context)

from django.shortcuts import render
from blogging.forms import UserForm, UserProfileForm
from blogging.models import UserProfile,blogtext

from django.http import HttpResponse
# Create your views here.
def mainpage(request) :


     registered = False
     if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            slug=profile.slug
            registered = True
        else:
            print user_form.errors, profile_form.errors


     else:
        user_form = UserForm()
        profile_form = UserProfileForm()

     return render(request,
            'blogging/mainpage.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered,'slug':slug} )


def home(request,user_name_slug) :
    context_dict={}
    try:

        profile = UserProfile.objects.get(slug=user_name_slug)
        context_dict['profile_name'] =profile.user.username


        blogs = blogtext.objects.filter(username=profile.user.username)
        context_dict['blogs'] = blogs


    except UserProfile.DoesNotExist:

        pass
    return render(request,'blogging/home.html',context_dict)

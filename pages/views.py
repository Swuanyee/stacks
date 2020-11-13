from django.views.generic import TemplateView
from django.shortcuts import render
from allauth.account.decorators import verified_email_required
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import UserUploadForm 
from .handle_excel import handle_excel
from allauth.account.views import PasswordChangeView


class HomePageView(TemplateView):
    """Direct to login and registration page"""
    template_name = 'account/home.html'


@verified_email_required
def ProfileView(request):
    user = request.user
    full_name = user.first_name + ' ' + user.last_name
    if user.profile == "Public":
        profile = "Free Account"
    elif user.profile == "Teacher":
        profile = "Teacher Account"
    else:
        profile = f"{user.profile} Premium Account"
    context = {
        'user': user,
        'full_name': full_name,
        'profile': profile
    }
    return render(request, 'pages/logout.html', context)


@verified_email_required
def BulkAddUsers(request):
    user = request.user
    user_profile = user.profile
    print(user_profile)
    if request.method == "POST":
        excel_form = UserUploadForm(request.POST, request.FILES)
        if excel_form.is_valid():
            handle_excel(request.FILES['excelForm'])
            return HttpResponseRedirect('dashboard')
    if user_profile == "Teacher":
        excel_form = UserUploadForm()
        context = {
            'excel_form': excel_form,
            'user_profile': user_profile
        }
        return render(request, "pages/add_users.html", context)
    else:
        return HttpResponseRedirect(reverse('dashboard'))


class CustomPasswordChangeView(PasswordChangeView):
    template_name = "pages/change_password.html"
    success_url = reverse_lazy("dashboard")

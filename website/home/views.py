from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount

def home(request):
	if request.user.is_authenticated:
		user = request.user
		user_id = request.user.id
		social_accounts = SocialAccount.objects.get(user=user_id)


	return render(request, 'home/home.html')
# Create your views here.

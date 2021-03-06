'''
	Contains Project level views
'''

from django.shortcuts import render_to_response
from django.conf import settings

def main_router(request):
	'''
		Send user to SPA if logged in and landing page if not
	'''
	if request.user.is_authenticated():
		return render_to_response(settings.SPA_INDEX)
	else:
		return render_to_response(settings.LANDING_PAGE_URL)

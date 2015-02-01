'''
	Contains Project level views
'''

from django.http import HttpResponseRedirect
from django.conf import settings

def main_router(request):
	'''
		Send user to SPA if logged in and landing page if not
	'''
	if request.user.is_authenticated():
		return HttpResponseRedirect(settings.SPA_INDEX)
	else:
		return HttpResponseRedirect(settings.LANDING_PAGE_URL)
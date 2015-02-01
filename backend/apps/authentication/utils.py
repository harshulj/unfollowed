from django.http import HttpResponse

def supported_methods(*args):
	'''
		decorator to limit a view to only specified methods
	'''
	def decorator(fn):
		def decorated(request):
			if not request.method in args:
				return HttpResponse("Bad request : Http method not supported", 400)
			return fn(request)
		return decorated

	return decorator

def twitter_post_auth(user_data):
	'''
		Handles user flow post authentication for twitter.
	'''
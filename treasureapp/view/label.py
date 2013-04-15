from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.exceptions import PermissionDenied
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django import forms

from treasureapp.models import Label
from treasureapp.forms import LabelForm

from treasureapp.authenticators import authenticate_account

from django import forms

@login_required
def label_list(request, *args, **kargs):
	"""
	Render the listing of all labels.

	On GET, it will return a listing of all labels.
	"""
	
	label_list = Label.objects.all()

	# Recover the groups the accessor is in
	request_user = request.user

	# Page response set-up
	context = RequestContext(request, {"section":"label",
		"labels":label_list})
	return render_to_response("labels/list.html", context)

@login_required
def label_create(request, *args, **kargs):
	"""
	On GET, the label creation form will be loaded.
	On POST, the label creation will be attempted and the main label page will be loaded.
	"""

	next_form = LabelForm # Next LabelForm instance that the system will go to (by default, it is a new one)
	label_list = Label.objects.all()

	if request.method == 'POST':

		# Label validation
		label_form = LabelForm(request.POST) # The form that initiated the POST
		try:
			label_form.save()
			return HttpResponseRedirect('/labels/') # Label creation is valid
		except:
			next_form = label_form # Label creation failed

	else:
		label_form = LabelForm(request.GET)
		print 'Method is GET'

	# Recover the groups the accessor is in
	request_user = request.user

	# Update the CSRF token
	kargs.update(csrf(request))

	context = RequestContext(request, dict(section="label",
	labels=label_list, mode="create", form=next_form, **kargs))
	
	print 'Moving to LABEL LIST'
	return render_to_response("labels/form.html", context)

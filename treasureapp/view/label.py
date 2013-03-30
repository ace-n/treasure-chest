from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from django.template import RequestContext
from django.core.exceptions import PermissionDenied
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from treasureapp.models import Label
from treasureapp.forms import LabelForm

from treasureapp.authenticators import authenticate_account

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

	label_list = Label.objects.all()

	# On-POST logic
	if request.method == 'POST':
		label_form = LabelForm(request.POST) # The form that initiated the POST
		if label_form.is_valid():
			label_form.save()
			return HttpResponseRedirect('/label')


	# Recover the groups the accessor is in
	request_user = request.user

	# Update the CSRF token
	kargs.update(csrf(request))
	context = RequestContext(request, dict(section="label",
		labels=label_list, mode="create", form=LabelForm, **kargs))
	return render_to_response("labels/form.html", context)

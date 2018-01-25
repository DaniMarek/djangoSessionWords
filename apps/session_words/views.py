from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from json import dumps
from time import gmtime, strftime



def index(request):
	return render(request, 'session_words/index.html')

def addsesh(request):
	form_info = []
	try:
	
		if request.method == 'POST':
			request.session['word'] = request.POST['word']
			request.session['tries']+=1

			if 'color' in request.POST:
				request.session['color'] = request.POST['color']
			if 'bigger' in request.POST:
				request.session['bigger'] = request.POST['bigger']
			request.session['msg'] = '- added on'
			request.session['time'] = strftime(" %c ", gmtime())
			
		else:
			request.session['tries'] = 0
		
		
	except KeyError:
		request.session['tries']=0
		return redirect('/')

	return redirect('/')
		# return render(request, 'session_words/index.html')

def clearsesh(request):
	if request.method == 'POST':
		try:
			del request.session['word']
			del request.session['msg']
			del request.session['time']
			del request.session['bigger']
			del request.session['color']
			del request.session['tries']
		except KeyError:
			pass
		return redirect('/')
from django.shortcuts import render
from django.db.models.functions import Length
from search.models import Word_Freq
from django.http import HttpResponse, HttpResponseNotFound
from django.db.models import Q
import json

# Create your views here.

def search(request):
    """
    Returns a HttpResponse message when the submit button is clicked.
    """
    return HttpResponseNotFound("Search on submit is still WIP. Please try again later. Thank you!")

def auto_complete(request):
    """
    ## This view returns a JSON response with a list of the suggested words for the text entered in the search box.
    #  [GET /search/?term=]
    + Request (Ajax)
        ...
    + Response (application/json)
        ...
    """
    if request.is_ajax():
        # GET the term from the search box input feild        
        word_input = request.GET.get('term', '').capitalize() 

        # Query to fetch the EXACT word match       
        exactmatch_search_queryset = Word_Freq.objects.filter(word__exact=word_input)

        # Query to fetch list of words that STARTS WITH the argument 'word_input'
        startswith_search_queryset = Word_Freq.objects.order_by(Length('word').asc(), '-freq').filter(word__startswith=word_input)

        # Query to fetch list of words that CONTAINS the argument 'word_input' and DOES NOT start with the argument 'word_input'
        contains_search_queryset = Word_Freq.objects.order_by(Length('word').asc(), '-freq').filter(Q(word__contains=word_input) & ~Q(word__startswith=word_input))        

        results = []
        if exactmatch_search_queryset:
            for r in exactmatch_search_queryset:
                results.append(r.word)
        if startswith_search_queryset:
            for r in startswith_search_queryset:
                results.append(r.word)
        if contains_search_queryset:
            for r in contains_search_queryset:
                results.append(r.word)
        first_twenty_five_results = results[:25]
        if first_twenty_five_results:
            data = json.dumps(first_twenty_five_results)
        else:            
            data = json.dumps(['No matches found'])
    else:
        data = 'Ajax Request Failed!'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from pymongo import MongoClient
from datetime import datetime

def start( request ):
    x = 10
    return HttpResponse( 
        "<h1>Hello, world.</h1> You're at the workflow start.<br />" +
        '<a href="/requisition/">Raise a Requisition</a><br />' +
        '<a href="/progress/">Track Requisition Progress</a><br />' +
        '<a href="/authorise/">Authorise a Requisition</a><br />' )

def template( request ):
    template = loader.get_template( 'show_table.html' )
    context = {
        'product_list': [ [ "computer", 999 ], [ "paper", 10 ] ] }
    return HttpResponse( template.render( context, request ) )

def raise_req( request ):
    x = 10
    client = MongoClient()
    db = client.test
    first_name = request.GET[ "first_name" ]
    last_name = request.GET[ "last_name" ]
    number = request.GET["number"]
    supplier = request.GET[ "supplier" ]
    cost_code = request.GET[ "cost_code" ]
    insert = db.requisition.insert_one({"first_name": first_name, "last_name": last_name, "number":number, "supplier": supplier, "cost_code": cost_code, "progress":[{"event":"","currentDate":{"lastModified":True}}]})
    #update = db.requisition.update_one({"number":number},{"$set":{"$currentDate":{"lastModified":True}}})
    return HttpResponse( 
        "results: " + first_name + " " + last_name + " " +
        supplier + " " + cost_code+ "Go to authorisation page: " + '<a href="/authorise/">Authorise a Requisition</a><br />' )

def requisition( request ): 
    return HttpResponse( 
        ' <form action="/raise_req/" method="get"> \
            First Name: <input type="text" name="first_name"><br>\
            Last Name: <input type="text" name="last_name"><br>\
            Number: <input type="text" name="number"><br>\
            Supplier: \
            <select name="supplier">\
              <option value="dell">Dell</option>\
              <option value="amazon">Amazon</option>\
              <option value="microsoft">Microsoft</option>\
            </select><br>\
            Cost Code:\
            <select name="cost_code">\
              <option value="af00301">AF00301</option>\
              <option value="cs00201">CS00201</option>\
            </select><br>\
            etcetera...<br>\
            <input type="submit" value="OK">\
          </form> ' )

def progress( request ):
    
    client = MongoClient()
    db = client.test
    c=db.requisition.find()
    lis=[]
    number=request.GET["secure"]
    if (number==number):
        update=db.requisition.update_many({"number":number},{"$set":{"progress":[{"event":"approved","currentDate":{"lastModified":True}}]}})
    cursor = db.requisition.find( { "number": str(number) } )
    a_requisition = cursor[ 0 ]
    progress_list = a_requisition[ 'progress' ]
    progress_list_string = str( progress_list )

    for d in c:
        lis.append(d)
    a=str(lis).strip('[]')

    return HttpResponse(
        'Here we will track progress of a requisition.<br />' +
        'user inputs a req number using a form and we show the progess.<br />' +
        'Here is the successfull authentication on Requisitionfound in the mongo DB:<br />' +
        progress_list_string + '<br />' + 'If authorised elsewhere, then '+
        'under "authorise" page we can add another {...} to this and re-save ' +
        'in the DB.'+'<br />'+'Whole mongo DataBase'+'<br />'+
        a)

def authorise( request ):
    client = MongoClient()
    db=client.test
    cursor = db.requisition.find()
    lis=[]
    for d in cursor:
        lis.append(d)
    a=str(lis).strip('[]')
    return HttpResponse( 
        'Here we will authorise a requisition.<br />' +
        '<form action="/requisition_authorization/" method="get">\
        </br>Enter a number of requisition you want to authorize and approve: </br><input type="text" name="auth_token"><br>\
        <input type="submit" value="Continue">\
        </form>'+
        "A overview of all requisitions:</br>"+a
        )

def requisition_authorization( request ):
    client = MongoClient()
    db=client.mongo
    token=request.GET["auth_token"]
    cursor = db.requisitions.find({"number":str(token)})
    return HttpResponse(
        'This is the authentication for requisition screen:</br>'+
        '<form action="/progress/" method="get">\
        </br>Currently approving requisition:'+token+'\
        </br>Do you really want to approve this requisition?\
        </br>For security reasons please state requisition number again <input type="text" name="secure">\
        <input type="submit" value="Approve">\
        <input type="submit" value="Reject"></br>\
        </form>'
        )


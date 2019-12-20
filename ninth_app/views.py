from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewResumeUserForm
# weeasyprint
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.conf import settings
#qr Code
from qr_code.qrcode.utils import ContactDetail
from datetime import datetime
#Image
from PIL import Image
# import from Accounts
from accounts.forms import updatePicResumeForm , updateImageResumeForm
from accounts.models import Profile
from django.shortcuts import redirect
# TODO import from DocTag TAGDOC WITH URL VIEWS
from doctag.forms import docTaggForm
#TODO create query URL
from django.urls import resolve, get_resolver, URLResolver, URLPattern
# from ninth_app.urls import urlpatterns #ninth_app

#django_weasyprint
# from django.views.generic import DetailView
# from django_weasyprint import  WeasyTemplateResponseMixin

#ERROR weasyprint
import logging
logger = logging.getLogger('weasyprint')
logger.addHandler(logging.FileHandler('weasyprint.log'))

#TODO TAG TO SEARCH IN QUERY - CREATE FORM
#TODO dictionary of DOC - [{kinho: resume1,resume2}]

# Create your views here.

def index(request):
    # return HttpResponse("helooooo")
    # context = { 
    #         'urlpatterns': urlpatterns
    #     }
    # query = request.GET.get(search,none)
    # if query:
    #             urlpatternsList = urlpatterns.objects.all()
    #             urlpatternsList = urlpatternsList.filter(name=query) # ex: name='resume'

    # else:
    # urlpatternsList = urlpatterns.objects.all()
    #context = { 'urlpatternsList':urlpatternsList}
    # context = { 'urlpatterns':urlpatterns}
    return render(request, 'base/index.html') #, context)
            

def resume(request):
    # form = NewTemporaryUserForm()

    # if request.method == "POST":
    #     form = NewTemporaryUserForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=True)
    #         return index(request) #go to index
    #     else:
    #         print('ERROR FORM INVALID')

    return render(request, 'base/resume.html', {'form':form})


#Tested - OK
# def recibo(request):
#     # return HTML('pdfmodels/recibo.html').write_pdf('/tmp/TESTE.pdf')
#     return render(request,'pdfmodels/recibo.html')


def recibosimplesdados(request):
    return render(request, 'links/recibosimplesdados.html')

def recibo(request):
    # """Generate pdf."""
    # Model data (list)
    # list = list.objects.all().order_by('last_name')

    # Rendered
    html_string = render_to_string('pdfmodels/recibo.html') #, {'list': list})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    #CSS just in html           # cssName = CSS(string='/static/css/recibopdf.css', font_config=font_config)
    result = html.write_pdf()   #stylesheets=[CSS(settings.STATIC_ROOT +  'css/recibopdf.css')]) #stylesheets=[cssName],font_config=font_config)

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=recibo.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output.seek(0)
        response.write(output.read())
    return response

def contratosimples(request):
    # """Generate pdf."""
    name1 = request.POST.get('name1').upper()
    nphone1 = request.POST.get('nphone1')
    bornfrom1 = request.POST.get('bornfrom1')
    inputmaritalStatus1 = request.POST.get('inputmaritalStatus1')
    work1 = request.POST.get('work1')
    RG1 = request.POST.get('RG1')
    CPF1 = request.POST.get('CPF1')
    address1 = request.POST.get('address1')
    city1 = request.POST.get('city1').capitalize()
    state1 = request.POST.get('state1').upper()
    name2 = request.POST.get('name2').upper()
    nphone2 = request.POST.get('nphone2')
    bornfrom2 = request.POST.get('bornfrom2')
    inputmaritalStatus2 = request.POST.get('inputmaritalStatus2')
    work2 = request.POST.get('work2')
    RG2 = request.POST.get('RG2')
    CPF2 = request.POST.get('CPF2')
    address2 = request.POST.get('address2')
    datapicker = request.POST.get('datapicker')
    price = request.POST.get('price')
    textprice = request.POST.get('textprice')
    methodprice = request.POST.get('methodprice')

    context= {'name1':name1,'nphone1':nphone1,'bornfrom1':bornfrom1,'inputmaritalStatus1':inputmaritalStatus1,
    'work1':work1,'RG1':RG1,'CPF1':CPF1,'address1':address1,'city1':city1,'state1':state1,
    'name2':name2,'nphone2':nphone2,'bornfrom2':bornfrom2,'inputmaritalStatus2':inputmaritalStatus2,'work2':work2,
    'RG2':RG2,'CPF2':CPF2,'address2':address2,'datapicker':datapicker,'price':price,
    'textprice':textprice,'methodprice':methodprice}


    # Rendered
    html_string = render_to_string('pdfmodels/contratosimples.html',context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    #CSS just in html
    result = html.write_pdf()
    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=contratosimples.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output.seek(0)
        response.write(output.read())
    return response

def vveiculossimples(request):
    # Rendered
    html_string = render_to_string('pdfmodels/vveiculossimples.html')
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    #CSS just in html
    result = html.write_pdf()
    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=vveiculossimples.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output.seek(0)
        response.write(output.read())
    return response

def procsimples(request):
    # """Generate pdf."""
    name1 = request.POST.get('name1')
    bornfrom1 = request.POST.get('bornfrom1')
    inputmaritalStatus1 = request.POST.get('inputmaritalStatus1')
    work1 = request.POST.get('work1')
    RG1 = request.POST.get('RG1')
    RG1from = request.POST.get('RG1from')
    CPF1 = request.POST.get('CPF1')
    city1 = request.POST.get('city1')
    state1 = request.POST.get('state1')
    name2 = request.POST.get('name2')
    bornfrom2 = request.POST.get('bornfrom1')
    inputmaritalStatus2 = request.POST.get('inputmaritalStatus2')
    work2 = request.POST.get('work2')
    OAB1 = request.POST.get('OAB1')
    RG2 = request.POST.get('RG2')
    RG2from = request.POST.get('RG2from')
    address2 = request.POST.get('address2')
    city2 = request.POST.get('city2')
    state2 = request.POST.get('state2')
    localcity = request.POST.get('localcity')

    context= {'name1':name1,'bornfrom1':bornfrom1,'inputmaritalStatus1':inputmaritalStatus1,'work1':work1,
    'RG1':RG1,'RG1from':RG1from,'CPF1':CPF1,'city1':city1,'state1':state1,
    'name2':name2,'bornfrom2':bornfrom2,'inputmaritalStatus2':inputmaritalStatus2,'work2':work2,'OAB1':OAB1,
    'RG2':RG2,'RG2from':RG2from,'address2':address2,'city2':city2,'state2':state2,'localcity':localcity}

    # Rendered
    html_string = render_to_string('pdfmodels/procsimples.html', context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    #CSS just in html
    result = html.write_pdf()
    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=procsimples.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output.seek(0)
        response.write(output.read())
    return response

def automenor(request):
    # """Generate pdf."""
    name1 = request.POST.get('name1').upper()
    nphone1 = request.POST.get('nphone1')
    nphone2 = request.POST.get('nphone2')
    bornfrom1 = request.POST.get('bornfrom1')
    inputmaritalStatus1 = request.POST.get('inputmaritalStatus1')
    work1 = request.POST.get('work1')
    RG1 = request.POST.get('RG1')
    RG1from = request.POST.get('RG1from')
    CPF1 = request.POST.get('CPF1')
    address1 = request.POST.get('address1').capitalize()
    city1 = request.POST.get('city1').capitalize()
    state1 = request.POST.get('state1').upper()
    kinship = request.POST.get('kinship').capitalize()
    name2 = request.POST.get('name2').upper()
    age1 = request.POST.get('age1')
    RG2 = request.POST.get('RG2')
    RG2from = request.POST.get('RG2from')
    name3 = request.POST.get('name3').upper()
    nphone3 = request.POST.get('nphone3')
    age2 = request.POST.get('age2')
    RG3 = request.POST.get('RG3')
    RG3from = request.POST.get('RG3from')
    address2 = request.POST.get('address2').capitalize()
    city2 = request.POST.get('city2').capitalize()
    state2 = request.POST.get('state2').upper()
    party1 = request.POST.get('party1').upper()
    datapicker = request.POST.get('datapicker')
    address3 = request.POST.get('address3').capitalize()
    localcity = request.POST.get('localcity').capitalize()

    context= {'name1':name1,'nphone1':nphone1,'nphone2':nphone2,'bornfrom1':bornfrom1,'inputmaritalStatus1':inputmaritalStatus1,
        'work1':work1,'RG1':RG1,'RG1from':RG1from,'CPF1':CPF1,'address1':address1,'city1':city1,'state1':state1,'kinship':kinship,
        'name2':name2,'age1':age1,'RG2':RG2,'RG2from':RG2from,'name3':name3,'nphone3':nphone3,'age2':age2,'RG3':RG3,'RG3from':RG3from,
        'address2':address2,'city2':city2,'state2':state2,'party1':party1,'datapicker':datapicker,'address3':address3,'localcity':localcity}

    # Rendered
    html_string = render_to_string('pdfmodels/automenor.html',context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    #CSS just in html
    result = html.write_pdf()
    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=automenor.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output.seek(0)
        response.write(output.read())
    return response


def resumetemp(request):#, docName1='Curriculo'):
    
    # docName1 = string.format(Curriculo)
    picResume = updateImageResumeForm(data=request.POST, files=request.FILES) #, instance=request.user.profile)
    context = {'picResume': picResume} #, 'docName1': docName1} 

    return render(request, 'links/resumetemp.html', context)
    # return HttpResponseRedirect(reverse('resumetemp', context, args=(docName1,)))

def contratosimplesdados(request):
    return render(request, 'links/contratosimplesdados.html')
# def resumedownload(request):
#     return render(request, 'pdfmodels/resumedownload.html')
def automenordados(request):
    return render(request, 'links/automenordados.html')

def procsimplesdados(request):
    return render(request, 'links/procsimplesdados.html')

def teste1(request):
    return render(request, 'testes/teste1.html')

def teste2(request):
    return render(request, 'testes/teste2.html')


# def sucesso(request):
#     data= request.POST.get('textbox1')
#
#     context= {'data':data}
#     return render(request, 'base/sucesso.html', context)

def sucesso(request):
    # """Generate pdf."""
    # Model data (list)
    # list = list.objects.all().order_by('last_name')
    data= request.POST.get('textbox1')
    data1= request.POST.get('textbox2')

    respImage= request.POST.get('image')
    img = Image.open(respImage)
    img.save('sid.jpg', 'jpeg')
    image1 = img
    context= {'data':data,'data1':data1,'image1':image1}

    # Rendered
    html_string = render_to_string('base/sucesso.html', context) #, {'list': list})
    html = HTML(string=html_string)
    #CSS just in html           # cssName = CSS(string='/static/css/recibopdf.css', font_config=font_config)
    result = html.write_pdf()   #stylesheets=[CSS(settings.STATIC_ROOT +  'css/recibopdf.css')]) #stylesheets=[cssName],font_config=font_config)

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=recibo.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output.seek(0)
        response.write(output.read())
    return response



def resumedownload(request):

    # profile1 = Profile.objects.all()
    # """Generate pdf."""
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    nphone1 = request.POST.get('nphone1')
    nphone2 = request.POST.get('nphone2')
    email = request.POST.get('email')
    inputDriverslicense = request.POST.get('inputDriverslicense')
    address = request.POST.get('address')
    birthdate = request.POST.get('datapicker')
    neighborHood = request.POST.get('neighborHood')
    city = request.POST.get('city')
    state = request.POST.get('state')
    zip = request.POST.get('zip')
    inputmaritalStatus = request.POST.get('inputmaritalStatus')
    inputlevelStudy1 = request.POST.get('inputlevelStudy1')
    lInstitution1 = request.POST.get('lInstitution1')
    lyearFinish1 = request.POST.get('lyearFinish1')
    inputlevelStudy2 = request.POST.get('inputlevelStudy2')
    lInstitution2 = request.POST.get('lInstitution2')
    lyearFinish2 = request.POST.get('lyearFinish2')
    inputlevelStudy3 = request.POST.get('inputlevelStudy3')
    lInstitution3 = request.POST.get('lInstitution3')
    lyearFinish3 = request.POST.get('lyearFinish3')
    inputlevelStudy4 = request.POST.get('inputlevelStudy4')
    lInstitution4 = request.POST.get('lInstitution4')
    lyearFinish4 = request.POST.get('lyearFinish4')
    course1 = request.POST.get('course1')
    cInstitution1 = request.POST.get('cInstitution1')
    cyearFinish1 = request.POST.get('cyearFinish1')
    studyTime1 = request.POST.get('studyTime1')
    course2 = request.POST.get('course2')
    cInstitution2 = request.POST.get('cInstitution2')
    cyearFinish2 = request.POST.get('cyearFinish2')
    studyTime2 = request.POST.get('studyTime2')
    course3 = request.POST.get('course3')
    cInstitution3 = request.POST.get('cInstitution3')
    cyearFinish3 = request.POST.get('cyearFinish3')
    studyTime3 = request.POST.get('studyTime3')
    course4 = request.POST.get('course4')
    cInstitution4 = request.POST.get('cInstitution4')
    cyearFinish4 = request.POST.get('cyearFinish4')
    studyTime4 = request.POST.get('studyTime4')
    company1 = request.POST.get('company1')
    function1 = request.POST.get('function1')
    worktime1 = request.POST.get('worktime1')
    functionDescribe1 = request.POST.get('functionDescribe1')
    company2 = request.POST.get('company2')
    function2 = request.POST.get('function2')
    worktime2 = request.POST.get('worktime2')
    functionDescribe2 = request.POST.get('functionDescribe2')
    company3 = request.POST.get('company3')
    function3 = request.POST.get('function3')
    worktime3 = request.POST.get('worktime3')
    functionDescribe3 = request.POST.get('functionDescribe3')
    company4 = request.POST.get('company4')
    function4 = request.POST.get('function4')
    worktime4 = request.POST.get('worktime4')
    functionDescribe4 = request.POST.get('functionDescribe4')
    
    #TODO this work , save picture on server, ERROR if don't login.
    # if request.method == 'POST':
    #     # picResume = updatePicResumeForm( data=request.POST, files=request.FILES , instance=request.user)
    #     picResume = updateImageResumeForm(data=request.POST, files=request.FILES, instance=request.user.profile)
       
    #     if picResume.is_valid():
    #         picResume.save()


    contact_detail = ContactDetail(
        first_name= first_name,
        last_name= last_name,
        tel= nphone1,
        email= email,
        # url='http://www.company.com',
    )
    # print (picResume)

    context= {'first_name':first_name,'last_name':last_name,'nphone1':nphone1,'nphone2':nphone2,'email':email,'inputDriverslicense':inputDriverslicense,
    'birthdate':birthdate,'address':address,'neighborHood':neighborHood,'city':city,'state':state,'zip':zip,'inputmaritalStatus':inputmaritalStatus,
    'inputlevelStudy1':inputlevelStudy1,'lInstitution1':lInstitution1,'lyearFinish1':lyearFinish1,
    'inputlevelStudy2':inputlevelStudy2,'lInstitution2':lInstitution2,'lyearFinish2':lyearFinish2,
    'inputlevelStudy3':inputlevelStudy3,'lInstitution3':lInstitution3,'lyearFinish3':lyearFinish3,
    'inputlevelStudy4':inputlevelStudy4,'lInstitution4':lInstitution4,'lyearFinish4':lyearFinish4,
    'course1':course1,'cInstitution1':cInstitution1,'cyearFinish1':cyearFinish1,'studyTime1':studyTime1,
    'course2':course2,'cInstitution2':cInstitution2,'cyearFinish2':cyearFinish2,'studyTime2':studyTime2,
    'course3':course3,'cInstitution3':cInstitution3,'cyearFinish3':cyearFinish3,'studyTime3':studyTime3,
    'course4':course4,'cInstitution4':cInstitution4,'cyearFinish4':cyearFinish4,'studyTime4':studyTime4,
    'company1':company1,'function1':function1,'worktime1':worktime1,'functionDescribe1':functionDescribe1,
    'company2':company2,'function2':function2,'worktime2':worktime2,'functionDescribe2':functionDescribe2,
    'company3':company3,'function3':function3,'worktime3':worktime3,'functionDescribe3':functionDescribe3,
    'company4':company4,'function4':function4,'worktime4':worktime4,'functionDescribe4':functionDescribe4,
    'contact_detail':contact_detail} 

    # return render(request, 'pdfmodels/resumedownload.html', context) #open Html A4

    html_string = render_to_string('pdfmodels/resumedownload.html', context, request=request) # attachment --download pdf and inline --open reader pdf
    html = HTML(string=html_string,base_url=request.build_absolute_uri())
    # stylesheets1=[CSS(settings.STATIC_ROOT +  'css/pdfprint.css')]) #stylesheets=[cssName],font_config=font_config)
    result = html.write_pdf() #stylesheets=stylesheets1)

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=resumedownload.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output.seek(0)
        response.write(output.read())
    return response


# class MyModelView(request):
#     # vanilla Django DetailView
#     model = resumedownload
#     template_name = 'pdfmodels/resumedownload.html'


# class MyModelPrintView(WeasyTemplateResponseMixin, MyModelView):
#     # output of DetailView rendered as PDF
#     pdf_stylesheets = [
#         settings.STATIC_ROOT , #+ 'css/app.css',
#     ]

# MAYBE WILL CAN TAKE DIRECT FROM MODELFORM
# def resumedownload(request):
#     # """Generate pdf."""
#     # Model data (list)
#     model = NewTemporaryUserForm
#     # list = list.objects.all().order_by('last_name')
#     answerform = request.POST.get('textbox1')
#     context= {'answerform':answerform }
#     # Rendered
#     html_string = render_to_string('pdfmodels/resumedownload.html', context) #, {'list': list})
#     html = HTML(string=html_string)
#     #CSS just in html           # cssName = CSS(string='/static/css/recibopdf.css', font_config=font_config)
#     result = html.write_pdf()   #stylesheets=[CSS(settings.STATIC_ROOT +  'css/recibopdf.css')]) #stylesheets=[cssName],font_config=font_config)
#
#     # Creating http response
#     response = HttpResponse(content_type='application/pdf;')
#     response['Content-Disposition'] = 'inline; filename=recibo.pdf'
#     response['Content-Transfer-Encoding'] = 'binary'
#     with tempfile.NamedTemporaryFile(delete=True) as output:
#         output.write(result)
#         output.flush()
#         output.seek(0)
#         response.write(output.read())
#     return response

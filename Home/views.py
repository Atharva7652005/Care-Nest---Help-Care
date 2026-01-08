from django.shortcuts import render,redirect
from Home.models import *;
# Create your views here.
def Home(request):
    if request.method == "POST":
        queryset = Add_Orphanage.objects.all()

        if request.POST.get("filter"):
            queryset = Add_Orphanage.objects.filter(orpho_name__icontains = request.POST.get("filter"))
            print(queryset)
            return render(request,"Orphanage_home.html",{'orpho_info' : queryset})
        elif request.POST.get('district'):
            search_city = request.POST.get('district')
            if search_city == "All":
                print(search_city)
                return render(request,"Orphanage_home.html",{'orpho_info' : queryset})
            elif search_city:
                queryset = Add_Orphanage.objects.filter(orpho_city = search_city)
                return render(request,"Orphanage_home.html",{'orpho_info' : queryset})
            else:
                return render(request, "Orphanage_home.html",{'alert-message' : 'No Orphanage Found'})

    queryset = Add_Orphanage.objects.all()
    return render(request,"Orphanage_home.html",{'orpho_info':queryset})

def Add_Orpho(request):
    if request.method == "POST":
        orpho_name =  request.POST.get('orpho_name')
        orpho_type =  request.POST.get('orpho_type')
        orpho_city =  request.POST.get('orpho_city')
        orpho_email =  request.POST.get('orpho_email')
        orpho_caretaker_name =  request.POST.get('orpho_caretaker')
        orpho_no_residentials = request.POST.get('orpho_residents')
        orpho_contact_no =  request.POST.get('orpho_contact')
        orpho_address =  request.POST.get('orpho_address')
        orpho_description =  request.POST.get('orpho_description')
        orpho_requirements =  request.POST.get('orpho_requirements')
        orpho_image =  request.FILES.get('orpho_image')

        orphanage_info = Add_Orphanage.objects.create (
            orpho_name = orpho_name,
            orpho_type = orpho_type,  
            orpho_city = orpho_city,  
            orpho_email = orpho_email,   
            orpho_caretaker_name = orpho_caretaker_name, 
            orpho_no_residentials = orpho_no_residentials,      
            orpho_contact_no = orpho_contact_no,       
            orpho_address = orpho_address,      
            orpho_description = orpho_description,      
            orpho_requirements = orpho_requirements,    
            orpho_image = orpho_image
        )

        orphanage_info.save()
        return redirect('/')
    return render(request,"Add_Orphanage.html")

def Update_Orpho(request):
    return render(request,"Update_Orphanage.html")

def Feedback(request):
    if request.method == "POST":
        sender_name = request.POST.get('sender_name')
        sender_email = request.POST.get('sender_email')
        sender_desc = request.POST.get('sender_desc')
        sender_rating = request.POST.get('rating')

        feedback = Orphanage_Feedback.objects.create(
            sender_name = sender_name,
            sender_email = sender_email, 
            sender_message = sender_desc,
            sender_rating = sender_rating
        )
        feedback.save()
    return render(request,"Feedback_Form.html")

def Feedback_Details(request):
    queryset = Orphanage_Feedback.objects.all()
    return render(request,"Feedback_Details.html",{'feedback_data' : queryset})

def Orpho_Desc(request, id):
    queryset = Add_Orphanage.objects.get(id=id)
    return render(request,"Orphanage_Description.html",{'orpho_info':queryset})
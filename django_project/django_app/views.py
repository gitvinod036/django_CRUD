from django.shortcuts import render
import json
from django.views.decorators.csrf  import csrf_exempt
from django.http import HttpResponse,JsonResponse
from .serializer import Student_Seralizer
from .models import StudentDetails
import cloudinary

# Create your views here.
@csrf_exempt
def reg_user(req):
    try:
        if req.method=='POST':
         user_data=json.loads(req.body)
         created=Student_Seralizer(data=user_data)
         if created.is_valid():
            created.save()
            return HttpResponse("New user Added Succesfully")
         else:
            return HttpResponse("Not Valid")
    except Exception as e:
        return HttpResponse(f"Invalid Data {e}")
    

@csrf_exempt
def get_user(req,id=None):
    try:
      if req.method=="GET":
         if id:
           single_data=StudentDetails.objects.get(stu_id=id)
           single_user_data=Student_Seralizer(single_data)
           return JsonResponse({"details":single_user_data.data})
         else:
            user_data=StudentDetails.objects.all()
            all_user_data=Student_Seralizer(user_data,many=True)
            return JsonResponse({"details":all_user_data.data},safe=False)
      else:
         return HttpResponse("Invalid Method")
    except Exception as e:
       return HttpResponse(f"Invalid Data/{e}")
        

@csrf_exempt
def update_user(req,id):
   try: 
    given_data=json.loads(req.body)
    if req.method in ["PUT","PATCH"]:
       user_data=StudentDetails.objects.get(stu_id=id)
       seralized_data=Student_Seralizer(user_data,data=given_data,partial=True)
       if seralized_data.is_valid():
          seralized_data.save()
          return HttpResponse("Updated Successfully")
       else:
          return HttpResponse("Invalid Data")
    else:
       return HttpResponse("Invalid Method")
   except Exception as e:
      return HttpResponse(" Errot : {e}")
   

@csrf_exempt
def delete_user(req,id):
   if req.method=="DELETE":
    try:
       if id is not None:
         user_data=StudentDetails.objects.get(stu_id=id)
         user_data.delete()
         return HttpResponse("Deleted Successfully")
       else:
         return HttpResponse("Need Id to Delete")
    except Exception as e:
      return HttpResponse(f"Invalid Method  {e}")
       
def show(req):
   return JsonResponse({"Details":"User Details shown"})


@csrf_exempt
def reg_form(req):
      if req.method=="POST": 
        try:
          id=req.POST.get("id")
          user_name=req.POST.get("name")
          user_email=req.POST.get("email")
          user_mob=req.POST.get("mobile")
          img_url=req.FILES.get("profile")
          img_url=cloudinary.uploader.upload(img_url)
          Created=StudentDetails.objects.create(stu_id=id,stu_name=user_name,stu_email=user_email,stu_mobile=user_mob,profile_pic=img_url["secure_url"])
          return HttpResponse("New user Registered")
        except Exception as e:
           return HttpResponse(f"Invalid Data {e}")
      else:
         return HttpResponse("Method should be POST to add New USER")
 
 
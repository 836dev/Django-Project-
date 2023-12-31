from django.shortcuts import render
from.models import Contact,User

# Create your views here.
def index(request):
	return render(request,'index.html')

def contact(request):
	if request.method=="POST":
		Contact.objects.create(
				name=request.POST['name'],
				email=request.POST['email'],
				mobile=request.POST['mobile'],
				remarks=request.POST['remarks']


			)
		msg="Contact Saved Successfully"
		contacts=Contact.objects.all().order_by("-id")[:3]
		return render(request,"contact.html",{'msg':msg,'contacts':contacts})

	else:
		contacts=Contact.objects.all().order_by("-id")[:3]
		return render(request,"contact.html",{'contacts':contacts})


def signup(request):
	if request.method=="POST":
		try:
			User.objects.get(email==request.POST['email'])
			msg="Email Already Registered"
			

		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					address=request.POST['address'],
					password=request.POST['password'],
				)
				msg="User Sign Up Successfully"
				return render(request,"signup.html",{'msg':msg})
			else:
				msg="Password & Confirm Password doesn't match"
				return render(request,"signup.html",{'msg':msg})


	else:
		return render(request,'signup.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				request.session['email']=user.email
				request.session['fname']=user.fname
				return render(request,'index.html')
			else: 				
				msg="Incorrect Password"
				return render(request,'login.html',{'msg:msg'})
		except:
			msg="Email Not Registered"
			return render(request,'signup.html',{'msg':msg})

	else:
		return render(request,'login.html')	

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		return render(request,'login.html',{'msg':msg})	

	except:
		msg="User Logged Out Successfully"
		return render(request,'login.html',{'msg':msg})

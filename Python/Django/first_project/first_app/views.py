from django.shortcuts import render, HttpResponse, redirect
from .models import Post,User


# Create your views here.
def index(request):
   # POST.objects.count() - shows how many records are in the Blog table
   return render(request,'loginreg.html',context={"message": ""}) 

def login(request):
   if request.method == 'POST':
      email = request.POST['email']
      password = request.POST['password']

      users = User.objects.filter(email = email, password = password)

      if len(users) == 0 :
         return render(request,'loginreg.html',context={"message": "Invalid Email/Password Combination"})
      
      return redirect('/newsfeed')

   return redirect('/')

def register(request):
   if request.method == 'POST':
      firstname = request.POST['fname']
      lastname = request.POST['lname']
      email = request.POST['email']
      password = request.POST['password']

      User.objects.create(firstname = firstname, lastname = lastname, email = email, password = password)
      
      return redirect('/newsfeed')

   return redirect('/')


def newsfeed(request):
   return render(request, "index.html", context = {"all_posts": Post.objects.all()})


def addpost(request):
   if request.method == 'POST':
      title = request.POST['title']
      post = request.POST['post']

      Post.objects.create(title = title, post = post)
   
   return redirect('/newsfeed')

def editpost(request,id):
   if request.method == 'POST':
      post = Post.objects.get(id=id)
      post.title = request.POST['title']
      post.post = request.POST['post']
      post.save()
      
      return redirect('/')
 
   return render(request,'edit.html', context = {"post": Post.objects.get(id=id)})

def deletepost(request,id):
   post = Post.objects.get(id=id)
   
   post.delete()
      
   return redirect('/')


      



















# def showid(request,id):
#    return HttpResponse(f"Here is the id: {id}")


# def sessiondata(request):
#    if request.method == 'POST':

#       request.session['name'] = request.POST['name']
#       request.session['food'] = request.POST['food']
      
#    return redirect('/')

# def formdata(request):
#    if request.method == 'POST':

#       context = {
#          "name": request.POST['name'],
#          "food": request.POST['food']
#       }

#       return render(request, "data.html", context = context)
   
#    else:
#       return redirect('/')
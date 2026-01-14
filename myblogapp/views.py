


from django.shortcuts import render, redirect
from .models import User, blog_list
from django.contrib import messages
# Create your views here.
#Creating  a register view
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email = email).exists():
            return render(request, 'myblogapp/register.html', {'error' : "Already exists"})
        
        User.objects.create(username = username, email = email, password = password)
        return redirect('login')
    return render(request, 'myblogapp/register.html')
#Creating a login view
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email = email)
            if user.password == password:
                request.session['user_id'] = user.id
                messages.success(request, 'Login Successfully')
                return redirect('bloglist')
            else:
                messages.error(request, "Login Unsuccessful!")
                return redirect('register')
        except User.DoesNotExist:
            messages.error(request, "User does not exists")
            return redirect('register')
    return render(request, 'myblogapp/login.html')

#Create a logout view
def logout(request):
    request.session.flush()
    return redirect('login')

#Create a blog list with create blog in one view
def bloglist(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    #Handle the new blog creation
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        blog_list.objects.create(user_id = user_id, title = title, content = content)
        return redirect(bloglist)
    blogs = blog_list.objects.filter(user_id = user_id)
    return render(request, 'myblogapp/bloglist.html', {'blogs': blogs})

# create a update
def update(request, id):
    user_id = request.session.get('user_id')
    if  not user_id:
        return redirect('login')
    
    blog = blog_list.objects.get(id = id , user_id = user_id)
    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.content = request.POST.get('content')
        blog.save()
        return redirect('bloglist')
    
    blogs = blog_list.objects.filter(user_id = user_id)
    return render(request, 'myblogapp/update.html', {'blog' : blog, 'blogs': blogs})

#Create a Delete view
def delete(request, id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    blog = blog_list.objects.get(id = id , user_id = user_id)
    blog.delete()
    return redirect('bloglist')
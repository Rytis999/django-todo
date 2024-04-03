from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect 
from .forms import CreateForm
from django.contrib.auth import authenticate, login , logout
# from .forms import toDo
from .models import Task
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required





# Create your views here.


def index(request):
    return  render(request, 'todo/index.html')



def login(request):
     

    return render(request,'todo/login.html' )


def LogoutView(request):
    logout(request)
    return redirect('index')



def register(request):
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')
        

        
        


    context = {'form':form}
    return render(request, 'todo/register.html', context)

# @login_required   
def create(request):
    context = {}   

    if request.method == 'POST':
        task = request.POST.get('task')
        new_todo = Task(user=request.user, todo_name=task)
        new_todo.save()

    all_todos = Task.objects.filter(user=request.user)
    context['todos'] = all_todos   

    return render(request, 'todo/create.html', context)
  
# @login_required  
def DeleteTask(request,name):
    # Retrieve all task objects based on user and todo_name
    tasks_to_delete = Task.objects.filter(user=request.user, todo_name=name)
    
    # Check if any tasks were found
    if tasks_to_delete.exists():
        # Iterate over the tasks and delete each one
        for task in tasks_to_delete:
            task.delete()
    
    return redirect('create')


#    get_todo = Task.objects.get(user=request.user, todo_name=name)
#    get_todo.delete()
#    return redirect('create')

# @login_required  
def Update(request, name):
  get_todo = Task.objects.get(user=request.user, todo_name=name)
  get_todo.status = True
  get_todo.save()
  return redirect('create')
 




#    if request.method =='POST':
#         task = request.POST.get('task')
#         user = request.user
#         new_task = Task.objects.create( title=task, user=user)
#         new_task.save()



        # new_todo = Task(user=request.user, title=task)
        # new_todo.save

 
  



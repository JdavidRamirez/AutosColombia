from django.shortcuts import render, redirect  
from gestion.forms import UsuarioForm
from gestion.models import Usuario
# Create your views here.  

def emp(request):  
    if request.method == "POST":  
        form = UsuarioForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = UsuarioForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    usuarios= Usuario.objects.all()  
    return render(request,"show.html",{'usuarios': usuarios}) 

def edit(request, id):  
    usuario = Usuario.objects.get(id=id)  
    return render(request,'edit.html', {'usuario':usuario})  

def update(request, id):  
    usuario= Usuario.objects.get(id=id)  
    form = UsuarioForm(request.POST, instance = usuario)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'usuario': usuario})  
def destroy(request, id):  

    usuario = Usuario.objects.get(id=id)  
    usuario.delete()  
    return redirect("/show")  
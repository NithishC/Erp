from django.shortcuts import render,redirect
from django.views.generic import View
from skct.models import Proof,Staff,It,Cse,Civil,Ece,Eee,Ice,Mba,Mech,Sh,Hod
from Academics.models import Academics
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import get_user
from django.http import request,HttpResponse
from django.contrib.auth.models import User,Group


class LoginView(View):
    template_name ="login.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        return redirect(request,self.template_name)

class LogoutView(View):
    def get(self,request):
        logout(request)
        messages.info(request,"Logged Out Successfully")
        return redirect('login')

class Profile(View):
    template_name ="index3.html"
    flag=0
    flag1=0
    def get(self,request):
        userhere=get_user(request)
        print(userhere)
        ub = Proof.objects.all()
        ob=Proof.objects.all().filter(user=userhere)
        li=['IT','CSE','MECH','EEE','ECE','CIVIL','ICE','MBA','S&H']
        u=Staff.objects.all().filter(name=userhere)
        print(u)
        if Staff.objects.all().filter(name=userhere).exists():
            self.flag=1
            if Hod.objects.all().filter(name=userhere):
                self.flag1=1
                return render(request,self.template_name,{'ob':ob,'u':u,'user':userhere,'li':li,'flag':self.flag,'ub':ub,'flag1':self.flag1})
            return render(request,self.template_name,{'ob':ob,'u':u,'user':userhere,'li':li,'flag':self.flag})
        
        return render(request,self.template_name,{'ob':ob,'u':u,'user':userhere,'li':li,'flag':self.flag})
        
    def post(self,request):
        userhere=get_user(request)
        u=Staff.objects.all().filter(name=userhere)
        if Staff.objects.all().filter(name=userhere).exists():
            p =Proof()
            p.act=request.POST.get('act')
            p.des=request.POST.get('des')
            p.pdf=request.FILES.get('upload')
            p.user=get_user(request)
            p.save()
            userhere=get_user(request)
            ob=Proof.objects.all().filter(user=userhere)
        else:
            s=Staff()
            s.name=request.user
            s.dept=request.POST.get('dropdown')
            name = request.POST.get('dropdown')
            s.desig=request.POST.get('designation')

            if(name == 'IT'):
                it = It(name= request.user)
                it.save()

            elif(name == 'CSE'):
                cse = Cse(name= request.user)
                cse.save()

            elif(name == 'MECH'):
                mech = Mech(name= request.user)
                mech.save()

            elif(name == 'EEE'):
                eee = Eee(name= request.user)
                eee.save()

            elif(name == 'ECE'):
                ece = Ece(name= request.user)
                ece.save()

            elif(name == 'CIVIL'):
                civil = Civil(name= request.user)
                civil.save()

            elif(name == 'ICE'):
                ice = Ice(name= request.user)
                ice.save()

            elif(name == 'S&H'):
                sh = Sh(name= request.user)
                sh.save()

            elif(name == 'MBA'):
                mba = Mba(name= request.user)
                mba.save()

            s.save()
            ob=Proof.objects.all().filter(user=userhere)

        if Hod.objects.all().filter(name=userhere):
            self.flag1 = 1 
            return render(request,self.template_name,{'ob':ob,'u':u,'user':userhere,'flag1':self.flag1})
        return render(request,self.template_name,{'ob':ob,'u':u,'user':userhere})
        
def delete(request,pk):
    if (request.method) == 'POST':
        name =Proof.objects.get(pk=pk)
        name.delete()
    return redirect('profile')


class APIview(View):
    template_name ="api_list.html"
    def get(self,request):
        flag2=0
        if(Hod.objects.all().filter(name=get_user(request))):
            flag2=1
            return render(request,self.template_name,{'flag2':flag2})
        else:
            return render(request,self.template_name)
    def post(self,request):
        flag2=0
        if(Hod.objects.all().filter(name=get_user(request))):
            flag2=1
            return render(request,self.template_name,{'flag2':flag2})
        else:
            return render(request,self.template_name)

class UserProfile(View):
    template_name ="user_profile.html"
    li = [i for i in range(1,11)]
    def get(self,request,user):
        name=Proof.objects.all().filter(user=user)
        return render(request,self.template_name,{'ob':name,'i':[i for i in range(1,11)]})
    def post(self,request,user):
        name =Proof.objects.all().filter(user=user)
        return render(request,self.template_name,{'ob':name,'i':[i for i in range(1,11)]})


class ProfileList(View):
    template_name="profile_list.html"

    def get(self,request):
        user1 = get_user(request)
        ob =It.objects.all().order_by('name')
        if(Hod.objects.all().filter(name=user1) and It.objects.all().filter(name = user1)):
            return render(request,self.template_name,{'ob':ob,})
        return render(request,self.template_name,{'ob':ob,})

    def post(self,request):
        ob = It.objects.all()
        return render(request,self.template_name,{'ob':ob,})
      



from django.shortcuts import render,redirect
from django.views.generic import View
from Research.models import SCI,ESCI,RIP,RNP,ISBN,IEEE,Guideship,GuideshipPursuing,Patents,Applied,Received,Consultancy,DCM,SubjectExpert,WOS
from skct.models import Proof,Staff,Hod,It,Cse,Mech,Eee,Ece,Ice,Civil,Mba,Sh
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import get_user
from django.http import request,HttpResponse
from django.contrib.auth.models import User,Group

# Create your views here.


def delete2(request,pk):
    if (request.method) == 'POST':
        name =SCI.objects.get(pk=pk)
        name.delete()
    return redirect('responses_view3')

def delete3(request,pk):
    if (request.method) == 'POST':
        name =ESCI.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view3')

def delete4(request,pk):
    if (request.method) == 'POST':
        name =RIP.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view3')

def delete5(request,pk):
    if (request.method) == 'POST':
        name =RNP.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view3')

def delete6(request,pk):
    if (request.method) == 'POST':
        name =ISBN.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view3')

def delete7(request,pk):
    if (request.method) == 'POST':
        name =IEEE.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view3')

def delete8(request,pk):
    if (request.method) == 'POST':
        name =Guideship.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view3')

def delete9(request,pk):
    if (request.method) == 'POST':
        name =GuideshipPursuing.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view3')

def delete10(request,pk):
    if (request.method) == 'POST':
        name =Patents.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view3')

def delete11(request,pk):
    if (request.method) == 'POST':
        name =Applied.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view3')

def delete12(request,pk):
    if (request.method) == 'POST':
        name =Received.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view3')

def delete13(request,pk):
    if (request.method) == 'POST':
        name =Consultancy.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view3')

def delete14(request,pk):
    if (request.method) == 'POST':
        name =DCM.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view3')

def delete15(request,pk):
    if (request.method) == 'POST':
        name =SubjectExpert.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view3')

def delete16(request,pk):
    if (request.method) == 'POST':
        name =WOS.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view3')


#------------------------------Delete---------------------------------------------


class AcademicView(View):
    template_name =["Research/index2.html"]
    def get(self,request):
        userhere=get_user(request)
        flag=0
        flag2=0
        li = [i for i in range(1,11)]
        li.reverse()

        if(Hod.objects.all().filter(name=userhere)):
            flag2=1
            return render(request,self.template_name[0],{'flag2':flag2,'li':li})
        else:
            return render(request,self.template_name[0],{'li':li})

    def post(self,request):
        if(request.POST.get('des')):
            name =SCI()
            name.des=request.POST.get('des')
            name.pdf=request.FILES.get('upload')
            name.user=get_user(request)
            name.points=request.POST.get('dropdown')
            if(It.objects.all().filter(name=get_user(request))):
                name.dept = "IT"
            elif(Cse.objects.all().filter(name=get_user(request))):
                name.dept = "CSE"
            elif(Mech.objects.all().filter(name=get_user(request))):
                name.dept = "MECH"
            elif(Eee.objects.all().filter(name=get_user(request))):
                name.dept = "EEE"
            elif(Ece.objects.all().filter(name=get_user(request))):
                name.dept = "ECE"
            elif(Ice.objects.all().filter(name=get_user(request))):
                name.dept = "ICE"
            elif(Civil.objects.all().filter(name=get_user(request))):
                name.dept = "CIVIL"
            elif(Mba.objects.all().filter(name=get_user(request))):
                name.dept = "MBA"
            elif(Sh.objects.all().filter(name=get_user(request))):
                name.dept = "SH"
            name.save()
            
            userhere=get_user(request)
          
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des1')):
            name1 = ESCI()
            name1.des = request.POST.get('des1')
            name1.pdf = request.FILES.get('upload1')
            name1.user = get_user(request)
            name1.points = request.POST.get('dropdown1')
            if(It.objects.all().filter(name=get_user(request))):
                name1.dept = "IT"
            elif(Cse.objects.all().filter(name=get_user(request))):
                name1.dept = "CSE"
            elif(Mech.objects.all().filter(name=get_user(request))):
                name1.dept = "MECH"
            elif(Eee.objects.all().filter(name=get_user(request))):
                name1.dept = "EEE"
            elif(Ece.objects.all().filter(name=get_user(request))):
                name1.dept = "ECE"
            elif(Ice.objects.all().filter(name=get_user(request))):
                name1.dept = "ICE"
            elif(Civil.objects.all().filter(name=get_user(request))):
                name1.dept = "CIVIL"
            elif(Mba.objects.all().filter(name=get_user(request))):
                name1.dept = "MBA"
            elif(Sh.objects.all().filter(name=get_user(request))):
                name1.dept = "SH"
            name1.save()

            userhere=get_user(request)
           
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des2')):
            name2 = RIP()
            name2.des = request.POST.get('des2')
            name2.pdf = request.FILES.get('upload2')
            name2.user = get_user(request)
            name2.points = request.POST.get('dropdown2')
            if(It.objects.all().filter(name=get_user(request))):
                name2.dept = "IT"
            elif(Cse.objects.all().filter(name=get_user(request))):
                name2.dept = "CSE"
            elif(Mech.objects.all().filter(name=get_user(request))):
                name2.dept = "MECH"
            elif(Eee.objects.all().filter(name=get_user(request))):
                name2.dept = "EEE"
            elif(Ece.objects.all().filter(name=get_user(request))):
                name2.dept = "ECE"
            elif(Ice.objects.all().filter(name=get_user(request))):
                name2.dept = "ICE"
            elif(Civil.objects.all().filter(name=get_user(request))):
                name2.dept = "CIVIL"
            elif(Mba.objects.all().filter(name=get_user(request))):
                name2.dept = "MBA"
            elif(Sh.objects.all().filter(name=get_user(request))):
                name2.dept = "SH"
            name2.save()

            userhere=get_user(request)
           
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des3')):
            name3 = RNP()
            name3.des = request.POST.get('des3')
            name3.pdf = request.FILES.get('upload3')
            name3.user = get_user(request)
            name3.points = request.POST.get('dropdown3')
            if(It.objects.all().filter(name=get_user(request))):
                name3.dept = "IT"
            elif(Cse.objects.all().filter(name=get_user(request))):
                name3.dept = "CSE"
            elif(Mech.objects.all().filter(name=get_user(request))):
                name3.dept = "MECH"
            elif(Eee.objects.all().filter(name=get_user(request))):
                name3.dept = "EEE"
            elif(Ece.objects.all().filter(name=get_user(request))):
                name3.dept = "ECE"
            elif(Ice.objects.all().filter(name=get_user(request))):
                name3.dept = "ICE"
            elif(Civil.objects.all().filter(name=get_user(request))):
                name3.dept = "CIVIL"
            elif(Mba.objects.all().filter(name=get_user(request))):
                name3.dept = "MBA"
            elif(Sh.objects.all().filter(name=get_user(request))):
                name3.dept = "SH"
            name3.save()

            userhere=get_user(request)
            
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})
        
        elif(request.POST.get('des4')):
            name4 = ISBN()
            name4.des = request.POST.get('des4')
            name4.pdf = request.FILES.get('upload4')
            name4.user = get_user(request)
            name4.points = request.POST.get('dropdown4')
            if(It.objects.all().filter(name=get_user(request))):
                name4.dept = "IT"
            elif(Cse.objects.all().filter(name=get_user(request))):
                name4.dept = "CSE"
            elif(Mech.objects.all().filter(name=get_user(request))):
                name4.dept = "MECH"
            elif(Eee.objects.all().filter(name=get_user(request))):
                name4.dept = "EEE"
            elif(Ece.objects.all().filter(name=get_user(request))):
                name4.dept = "ECE"
            elif(Ice.objects.all().filter(name=get_user(request))):
                name4.dept = "ICE"
            elif(Civil.objects.all().filter(name=get_user(request))):
                name4.dept = "CIVIL"
            elif(Mba.objects.all().filter(name=get_user(request))):
                name4.dept = "MBA"
            elif(Sh.objects.all().filter(name=get_user(request))):
                name4.dept = "SH"
            name4.save()

            userhere=get_user(request)
          
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des5')):
            name5 = IEEE()
            name5.des = request.POST.get('des5')
            name5.pdf = request.FILES.get('upload5')
            name5.user = get_user(request)
            name5.points = request.POST.get('dropdown5')
            if(It.objects.all().filter(name=get_user(request))):
                name5.dept = "IT"
            elif(Cse.objects.all().filter(name=get_user(request))):
                name5.dept = "CSE"
            elif(Mech.objects.all().filter(name=get_user(request))):
                name5.dept = "MECH"
            elif(Eee.objects.all().filter(name=get_user(request))):
                name5.dept = "EEE"
            elif(Ece.objects.all().filter(name=get_user(request))):
                name5.dept = "ECE"
            elif(Ice.objects.all().filter(name=get_user(request))):
                name5.dept = "ICE"
            elif(Civil.objects.all().filter(name=get_user(request))):
                name5.dept = "CIVIL"
            elif(Mba.objects.all().filter(name=get_user(request))):
                name5.dept = "MBA"
            elif(Sh.objects.all().filter(name=get_user(request))):
                name5.dept = "SH"
            name5.save()

            userhere=get_user(request)
           
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des6')):
            name6 = Guideship()
            name6.des = request.POST.get('des6')
            name6.pdf = request.FILES.get('upload6')
            name6.user = get_user(request)
            name6.points = request.POST.get('dropdown6')
            if(It.objects.all().filter(name=get_user(request))):
                name6.dept = "IT"
            elif(Cse.objects.all().filter(name=get_user(request))):
                name6.dept = "CSE"
            elif(Mech.objects.all().filter(name=get_user(request))):
                name6.dept = "MECH"
            elif(Eee.objects.all().filter(name=get_user(request))):
                name6.dept = "EEE"
            elif(Ece.objects.all().filter(name=get_user(request))):
                name6.dept = "ECE"
            elif(Ice.objects.all().filter(name=get_user(request))):
                name6.dept = "ICE"
            elif(Civil.objects.all().filter(name=get_user(request))):
                name6.dept = "CIVIL"
            elif(Mba.objects.all().filter(name=get_user(request))):
                name6.dept = "MBA"
            elif(Sh.objects.all().filter(name=get_user(request))):
                name6.dept = "SH"
            name6.save()

            userhere=get_user(request)
          
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des7')):
            name7 = GuideshipPursuing()
            name7.des = request.POST.get('des7')
            name7.pdf = request.FILES.get('upload7')
            name7.user = get_user(request)
            name7.points = request.POST.get('dropdown7')
            if(It.objects.all().filter(name=get_user(request))):
                name7.dept = "IT"
            elif(Cse.objects.all().filter(name=get_user(request))):
                name7.dept = "CSE"
            elif(Mech.objects.all().filter(name=get_user(request))):
                name7.dept = "MECH"
            elif(Eee.objects.all().filter(name=get_user(request))):
                name7.dept = "EEE"
            elif(Ece.objects.all().filter(name=get_user(request))):
                name7.dept = "ECE"
            elif(Ice.objects.all().filter(name=get_user(request))):
                name7.dept = "ICE"
            elif(Civil.objects.all().filter(name=get_user(request))):
                name7.dept = "CIVIL"
            elif(Mba.objects.all().filter(name=get_user(request))):
                name7.dept = "MBA"
            elif(Sh.objects.all().filter(name=get_user(request))):
                name7.dept = "SH"
            name7.save()

            userhere=get_user(request)
            
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des8')):
            name8 = Patents()
            name8.des = request.POST.get('des8')
            name8.pdf = request.FILES.get('upload8')
            name8.user = get_user(request)
            name8.points = request.POST.get('dropdown8')
            if(It.objects.all().filter(name=get_user(request))):
                name8.dept = "IT"
            elif(Cse.objects.all().filter(name=get_user(request))):
                name8.dept = "CSE"
            elif(Mech.objects.all().filter(name=get_user(request))):
                name8.dept = "MECH"
            elif(Eee.objects.all().filter(name=get_user(request))):
                name8.dept = "EEE"
            elif(Ece.objects.all().filter(name=get_user(request))):
                name8.dept = "ECE"
            elif(Ice.objects.all().filter(name=get_user(request))):
                name8.dept = "ICE"
            elif(Civil.objects.all().filter(name=get_user(request))):
                name8.dept = "CIVIL"
            elif(Mba.objects.all().filter(name=get_user(request))):
                name8.dept = "MBA"
            elif(Sh.objects.all().filter(name=get_user(request))):
                name8.dept = "SH"
            name8.save()

            userhere=get_user(request)
           
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des9')):
            name9 = Applied()
            name9.des = request.POST.get('des9')
            name9.pdf = request.FILES.get('upload9')
            name9.user = get_user(request)
            name9.points = request.POST.get('dropdown9')
            if(It.objects.all().filter(name=get_user(request))):
                name9.dept = "IT"
            elif(Cse.objects.all().filter(name=get_user(request))):
                name9.dept = "CSE"
            elif(Mech.objects.all().filter(name=get_user(request))):
                name9.dept = "MECH"
            elif(Eee.objects.all().filter(name=get_user(request))):
                name9.dept = "EEE"
            elif(Ece.objects.all().filter(name=get_user(request))):
                name9.dept = "ECE"
            elif(Ice.objects.all().filter(name=get_user(request))):
                name9.dept = "ICE"
            elif(Civil.objects.all().filter(name=get_user(request))):
                name9.dept = "CIVIL"
            elif(Mba.objects.all().filter(name=get_user(request))):
                name9.dept = "MBA"
            elif(Sh.objects.all().filter(name=get_user(request))):
                name9.dept = "SH"
            name9.save()

            userhere=get_user(request)
           
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des10')):
            name10 = Received()
            name10.des = request.POST.get('des10')
            name10.pdf = request.FILES.get('upload10')
            name10.user = get_user(request)
            name10.points = request.POST.get('dropdown10')
            if(It.objects.all().filter(name=get_user(request))):
                name10.dept = "IT"
            elif(Cse.objects.all().filter(name=get_user(request))):
                name10.dept = "CSE"
            elif(Mech.objects.all().filter(name=get_user(request))):
                name10.dept = "MECH"
            elif(Eee.objects.all().filter(name=get_user(request))):
                name10.dept = "EEE"
            elif(Ece.objects.all().filter(name=get_user(request))):
                name10.dept = "ECE"
            elif(Ice.objects.all().filter(name=get_user(request))):
                name10.dept = "ICE"
            elif(Civil.objects.all().filter(name=get_user(request))):
                name10.dept = "CIVIL"
            elif(Mba.objects.all().filter(name=get_user(request))):
                name10.dept = "MBA"
            elif(Sh.objects.all().filter(name=get_user(request))):
                name10.dept = "SH"
            name10.save()

            userhere=get_user(request)
           
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des11')):
            name11 = Consultancy()
            name11.des = request.POST.get('des11')
            name11.pdf = request.FILES.get('upload11')
            name11.user = get_user(request)
            name11.points = request.POST.get('dropdown11')
            if(It.objects.all().filter(name=get_user(request))):
                name11.dept = "IT"
            elif(Cse.objects.all().filter(name=get_user(request))):
                name11.dept = "CSE"
            elif(Mech.objects.all().filter(name=get_user(request))):
                name11.dept = "MECH"
            elif(Eee.objects.all().filter(name=get_user(request))):
                name11.dept = "EEE"
            elif(Ece.objects.all().filter(name=get_user(request))):
                name11.dept = "ECE"
            elif(Ice.objects.all().filter(name=get_user(request))):
                name11.dept = "ICE"
            elif(Civil.objects.all().filter(name=get_user(request))):
                name11.dept = "CIVIL"
            elif(Mba.objects.all().filter(name=get_user(request))):
                name11.dept = "MBA"
            elif(Sh.objects.all().filter(name=get_user(request))):
                name11.dept = "SH"
            name11.save()

            userhere=get_user(request)
   
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des12')):
            name12 = DCM()
            name12.des = request.POST.get('des12')
            name12.pdf = request.FILES.get('upload12')
            name12.user = get_user(request)
            name12.points = request.POST.get('dropdown12')
            if(It.objects.all().filter(name=get_user(request))):
                name12.dept = "IT"
            elif(Cse.objects.all().filter(name=get_user(request))):
                name12.dept = "CSE"
            elif(Mech.objects.all().filter(name=get_user(request))):
                name12.dept = "MECH"
            elif(Eee.objects.all().filter(name=get_user(request))):
                name12.dept = "EEE"
            elif(Ece.objects.all().filter(name=get_user(request))):
                name12.dept = "ECE"
            elif(Ice.objects.all().filter(name=get_user(request))):
                name12.dept = "ICE"
            elif(Civil.objects.all().filter(name=get_user(request))):
                name12.dept = "CIVIL"
            elif(Mba.objects.all().filter(name=get_user(request))):
                name12.dept = "MBA"
            elif(Sh.objects.all().filter(name=get_user(request))):
                name12.dept = "SH"
            name12.save()

            userhere=get_user(request)
           
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des13')):
            name13 = SubjectExpert()
            name13.des = request.POST.get('des13')
            name13.pdf = request.FILES.get('upload13')
            name13.user = get_user(request)
            name13.points = request.POST.get('dropdown13')
            if(It.objects.all().filter(name=get_user(request))):
                name13.dept = "IT"
            elif(Cse.objects.all().filter(name=get_user(request))):
                name13.dept = "CSE"
            elif(Mech.objects.all().filter(name=get_user(request))):
                name13.dept = "MECH"
            elif(Eee.objects.all().filter(name=get_user(request))):
                name13.dept = "EEE"
            elif(Ece.objects.all().filter(name=get_user(request))):
                name13.dept = "ECE"
            elif(Ice.objects.all().filter(name=get_user(request))):
                name13.dept = "ICE"
            elif(Civil.objects.all().filter(name=get_user(request))):
                name13.dept = "CIVIL"
            elif(Mba.objects.all().filter(name=get_user(request))):
                name13.dept = "MBA"
            elif(Sh.objects.all().filter(name=get_user(request))):
                name13.dept = "SH"
            name13.save()

            userhere=get_user(request)
           
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des14')):
            name14 = WOS()
            name14.des = request.POST.get('des14')
            name14.pdf = request.FILES.get('upload14')
            name14.user = get_user(request)
            name14.points = request.POST.get('dropdown14')
            if(It.objects.all().filter(name=get_user(request))):
                name14.dept = "IT"
            elif(Cse.objects.all().filter(name=get_user(request))):
                name14.dept = "CSE"
            elif(Mech.objects.all().filter(name=get_user(request))):
                name14.dept = "MECH"
            elif(Eee.objects.all().filter(name=get_user(request))):
                name14.dept = "EEE"
            elif(Ece.objects.all().filter(name=get_user(request))):
                name14.dept = "ECE"
            elif(Ice.objects.all().filter(name=get_user(request))):
                name14.dept = "ICE"
            elif(Civil.objects.all().filter(name=get_user(request))):
                name14.dept = "CIVIL"
            elif(Mba.objects.all().filter(name=get_user(request))):
                name14.dept = "MBA"
            elif(Sh.objects.all().filter(name=get_user(request))):
                name14.dept = "SH"
            name14.save()
            userhere=get_user(request)
            
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})



class AcadListView(View):
    template_name = "Research/academics_list.html"
    def get(self,request):
        flag=0
        if(Hod.objects.all().filter(name=get_user(request)) and It.objects.all().filter(name=get_user(request))):
            li = It.objects.all()
            flag=1
            return render(request,self.template_name,{'i':li,'flag2':flag})

    def post(self,request):
        flag=0
        if(Hod.objects.all().filter(name=get_user(request)) and It.objects.all().filter(name=get_user(request))):
            li = It.objects.all()
            flag=1
            return render(request,self.template_name,{'i':li,'flag2':flag})

class FacAcadListView(View):
    template_name = "Research/fac_academics_list.html"
    flag2=0
    def get(self,request,user,pk):
        user1=user
        if(Hod.objects.all().filter(name=get_user(request))):
            i = SCI.objects.all().filter(user=user)
            i2 = ESCI.objects.all().filter(user=user)
            i3 = RIP.objects.all().filter(user=user)
            i4 = RNP.objects.all().filter(user=user)
            i5 = ISBN.objects.all().filter(user=user)
            i6 = IEEE.objects.all().filter(user=user)
            i7 = Guideship.objects.all().filter(user=user)
            i8 = GuideshipPursuing.objects.all().filter(user= user)
            i9 = Patents.objects.all().filter(user=user)
            i10 = Applied.objects.all().filter(user=user)
            i11 = Received.objects.all().filter(user=user)
            i12 = Consultancy.objects.all().filter(user=user)
            i13 = DCM.objects.all().filter(user=user)
            i14 = SubjectExpert.objects.all().filter(user=user)
            i15 = WOS.objects.all().filter(user=user)
            flag2=1
        return render(request,self.template_name,{'i15':i15,'i14':i14,'i13':i13,'i12':i12,'i11':i11,'i10':i10,'i9':i9,'i8':i8,'i6':i6,'i7':i7,'i':i,'i2':i2,'i3':i3,'i4':i4,'i5':i5,'flag2':flag2,'user1':user1})

    def post(self,request,user,pk):
        user1=user
        if(Hod.objects.all().filter(name=get_user(request))):
            i = SCI.objects.all().filter(user=user)
            i2 = ESCI.objects.all().filter(user=user)
            i3 = RIP.objects.all().filter(user=user)
            i4 = RNP.objects.all().filter(user=user)
            i5 = ISBN.objects.all().filter(user=user)
            i6 = IEEE.objects.all().filter(user=user)
            i7 = Guideship.objects.all().filter(user=user)
            i8 = GuideshipPursuing.objects.all().filter(user= user)
            i9 = Patents.objects.all().filter(user=user)
            i10 = Applied.objects.all().filter(user=user)
            i11 = Received.objects.all().filter(user=user)
            i12 = Consultancy.objects.all().filter(user=user)
            i13 = DCM.objects.all().filter(user=user)
            i14 = SubjectExpert.objects.all().filter(user=user)
            i15 = WOS.objects.all().filter(user=user)
            value=request.POST.get('points')
            value1=request.POST.get('points1')
            value2=request.POST.get('points2')
            value3=request.POST.get('points3')
            value4=request.POST.get('points4')
            value5=request.POST.get('points5')
            value6=request.POST.get('points6')
            value7=request.POST.get('points7')
            value8=request.POST.get('points8')
            value9=request.POST.get('points9')
            value10=request.POST.get('points10')
            value11=request.POST.get('points11')
            value12=request.POST.get('points12')
            value13=request.POST.get('points13')
            value14=request.POST.get('points14')
            if(request.POST.get('points')):
                a=SCI.objects.filter(pk=pk).update(pointsaward=value)
            elif(request.POST.get('points1')):
                b=ESCI.objects.filter(pk=pk).update(pointsaward=value1)
            elif(request.POST.get('points2')):
                c=RIP.objects.filter(pk=pk).update(pointsaward=value2)
            elif(request.POST.get('points3')):
                d=RNP.objects.all().filter(pk=pk).update(pointsaward=value3)
            elif(request.POST.get('points4')):
                e=ISBN.objects.all().filter(pk=pk).update(pointsaward=value4)
            elif(request.POST.get('points5')):
                f=IEEE.objects.all().filter(pk=pk).update(pointsaward=value5)
            elif(request.POST.get('points6')):
                f=Guideship.objects.all().filter(pk=pk).update(pointsaward=value6)
            elif(request.POST.get('points7')):
                f=GuideshipPursuing.objects.all().filter(pk=pk).update(pointsaward=value7)
            elif(request.POST.get('points8')):
                f=Patents.objects.all().filter(pk=pk).update(pointsaward=value8)
            elif(request.POST.get('points9')):
                f=Applied.objects.all().filter(pk=pk).update(pointsaward=value9)
            elif(request.POST.get('points10')):
                f=Received.objects.all().filter(pk=pk).update(pointsaward=value10)
            elif(request.POST.get('points11')):
                f=Consultancy.objects.all().filter(pk=pk).update(pointsaward=value11)
            elif(request.POST.get('points12')):
                f=DCM.objects.all().filter(pk=pk).update(pointsaward=value12)
            elif(request.POST.get('points13')):
                f=SubjectExpert.objects.all().filter(pk=pk).update(pointsaward=value13)
            elif(request.POST.get('points14')):
                f=WOS.objects.all().filter(pk=pk).update(pointsaward=value14)
        return render(request,self.template_name,{'i15':i15,'i14':i14,'i13':i13,'i12':i12,'i11':i11,'i10':i10,'i9':i9,'i8':i8,'i7':i7,'i6':i6,'i':i,'i2':i2,'i3':i3,'i4':i4,'i5':i5,'user1':user1})

class ResponsesView(View):
    template_name = "Research/responses_view.html"
    flag2=0
    def get(self,request):
        user = get_user(request)
        i = SCI.objects.all().filter(user=user)
        i2 = ESCI.objects.all().filter(user=user)
        i3 = RIP.objects.all().filter(user=user)
        i4 = RNP.objects.all().filter(user=user)
        i5 = ISBN.objects.all().filter(user=user)
        i6 = IEEE.objects.all().filter(user=user)
        i7 = Guideship.objects.all().filter(user=user)
        i8 = GuideshipPursuing.objects.all().filter(user= user)
        i9 = Patents.objects.all().filter(user=user)
        i10 = Applied.objects.all().filter(user=user)
        i11 = Received.objects.all().filter(user=user)
        i12 = Consultancy.objects.all().filter(user=user)
        i13 = DCM.objects.all().filter(user=user)
        i14 = SubjectExpert.objects.all().filter(user=user)
        i15 = WOS.objects.all().filter(user=user)
        flag2=1
        return render(request,self.template_name,{'i15':i15,'i14':i14,'i13':i13,'i12':i12,'i11':i11,'i10':i10,'i9':i9,'i8':i8,'i6':i6,'i7':i7,'i':i,'i2':i2,'i3':i3,'i4':i4,'i5':i5,'flag2':flag2})

    def post(self,request):
        user = get_user(request)
        i = SCI.objects.all().filter(user=user)
        i2 = ESCI.objects.all().filter(user=user)
        i3 = RIP.objects.all().filter(user=user)
        i4 = RNP.objects.all().filter(user=user)
        i5 = ISBN.objects.all().filter(user=user)
        i6 = IEEE.objects.all().filter(user=user)
        i7 = Guideship.objects.all().filter(user=user)
        i8 = GuideshipPursuing.objects.all().filter(user= user)
        i9 = Patents.objects.all().filter(user=user)
        i10 = Applied.objects.all().filter(user=user)
        i11 = Received.objects.all().filter(user=user)
        i12 = Consultancy.objects.all().filter(user=user)
        i13 = DCM.objects.all().filter(user=user)
        i14 = SubjectExpert.objects.all().filter(user=user)
        i15 = WOS.objects.all().filter(user=user)
    
        return render(request,self.template_name,{'i15':i15,'i14':i14,'i13':i13,'i12':i12,'i11':i11,'i10':i10,'i9':i9,'i8':i8,'i7':i7,'i6':i6,'i':i,'i2':i2,'i3':i3,'i4':i4,'i5':i5})


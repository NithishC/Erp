from django.shortcuts import render,redirect
from django.views.generic import View
from Events.models import Grant,InternationalConf,NationalConf,Workshop,FDP,InterCollege,InternationalConf2,InterCollege2,Workshop2,FDP2,NationalConf2
from skct.models import Proof,Staff,Hod,It,Cse,Mech,Eee,Ece,Ice,Civil,Mba,Sh
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import get_user
from django.http import request,HttpResponse
from django.contrib.auth.models import User

# Create your views here.



def delete2(request,pk):
    if (request.method) == 'POST':
        name =Grant.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('events_responses_view')

def delete3(request,pk):
    if (request.method) == 'POST':
        name =InternationalConf.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('events_responses_view')

def delete4(request,pk):
    if (request.method) == 'POST':
        name =NationalConf.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('events_responses_view')

def delete5(request,pk):
    if (request.method) == 'POST':
        name =Workshop.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('events_responses_view')

def delete6(request,pk):
    if (request.method) == 'POST':
        name =FDP.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('events_responses_view')

def delete7(request,pk):
    if (request.method) == 'POST':
        name =InterCollege.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('events_responses_view')

def delete8(request,pk):
    if (request.method) == 'POST':
        name =InternationalConf2.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('events_responses_view')

def delete9(request,pk):
    if (request.method) == 'POST':
        name =NationalConf2.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('events_responses_view')

def delete10(request,pk):
    if (request.method) == 'POST':
        name =Workshop2.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('events_responses_view')

def delete11(request,pk):
    if (request.method) == 'POST':
        name =FDP2.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('events_responses_view')

def delete12(request,pk):
    if (request.method) == 'POST':
        name =InterCollege2.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('events_responses_view')


#------------------------------------------delete----------------------------------------

class EventsView(View):
    template_name="Events_Organized/events_index.html"
    def get(self,request):
        userhere=get_user(request)
        flag=0
        flag2=0
        li = [i for i in range(1,11)]
        li.reverse()

        if(Hod.objects.all().filter(name=userhere)):
            flag2=1
            return render(request,self.template_name,{'flag2':flag2,'li':li})
        else:
            return render(request,self.template_name,{'li':li})
    def post(self,request):
        if(request.POST.get('des')):
            name =Grant()
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
            ob=Grant.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name,{'flag2':flag2,'li':li})
            return render(request,self.template_name,{'li':li,})

        elif(request.POST.get('des1')):
            name1 = InternationalConf()
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
            ob=InternationalConf.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name,{'flag2':flag2,'li':li})
            return render(request,self.template_name,{'li':li,})

        elif(request.POST.get('des2')):
            name2 = NationalConf()
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
            ob=NationalConf.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name,{'flag2':flag2,'li':li})
            return render(request,self.template_name,{'li':li,})

        elif(request.POST.get('des3')):
            name3 = Workshop()
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
            ob=Workshop.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name,{'flag2':flag2,'li':li})
            return render(request,self.template_name,{'li':li,})
        
        elif(request.POST.get('des4')):
            name4 = FDP()
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
            ob=FDP.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name,{'flag2':flag2,'li':li})
            return render(request,self.template_name,{'li':li,})

        elif(request.POST.get('des5')):
            name5 = InterCollege()
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
            ob=InterCollege.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name,{'flag2':flag2,'li':li})
            return render(request,self.template_name,{'li':li,})

        elif(request.POST.get('des6')):
            name6 = InternationalConf2()
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
            ob=InternationalConf2.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name,{'flag2':flag2,'li':li})
            return render(request,self.template_name,{'li':li,})

        elif(request.POST.get('des7')):
            name7 = NationalConf2()
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
            ob=NationalConf2.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name,{'flag2':flag2,'li':li})
            return render(request,self.template_name,{'li':li,})

        elif(request.POST.get('des8')):
            name8 = Workshop2()
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
            ob=Workshop2.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name,{'flag2':flag2,'li':li})
            return render(request,self.template_name,{'li':li,})

        elif(request.POST.get('des9')):
            name9 = FDP2()
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
            ob=FDP2.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name,{'flag2':flag2,'li':li})
            return render(request,self.template_name,{'li':li,})

        elif(request.POST.get('des10')):
            name10 = InterCollege2()
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
            ob=InterCollege2.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name,{'flag2':flag2,'li':li})
            return render(request,self.template_name,{'li':li,})

class ResponsesView(View):
    template_name = "Events_Organized/events_responses_view.html"
    flag2=0
    def get(self,request):
        user = get_user(request)
        if(Hod.objects.all().filter(name=get_user(request))):
            self.flag2 = 1
        i = Grant.objects.all().filter(user=user)
        i2 = InternationalConf.objects.all().filter(user=user)
        i3 = NationalConf.objects.all().filter(user=user)
        i4 = Workshop.objects.all().filter(user=user)
        i5 = FDP.objects.all().filter(user=user)
        i6 = InterCollege.objects.all().filter(user=user)
        i7 = InternationalConf2.objects.all().filter(user=user)
        i8 = NationalConf2.objects.all().filter(user= user)
        i9 = Workshop2.objects.all().filter(user=user)
        i10 = FDP2.objects.all().filter(user=user)
        i11 = InterCollege2.objects.all().filter(user=user)
        return render(request,self.template_name,{'i11':i11,'i10':i10,'i9':i9,'i8':i8,'i6':i6,'i7':i7,'i':i,'i2':i2,'i3':i3,'i4':i4,'i5':i5,'flag2':self.flag2})

    def post(self,request):
        user = get_user(request)
        if(Hod.objects.all().filter(name=get_user(request))):
            self.flag2 = 1
        i = Grant.objects.all().filter(user=user)
        i2 = InternationalConf.objects.all().filter(user=user)
        i3 = NationalConf.objects.all().filter(user=user)
        i4 = Workshop.objects.all().filter(user=user)
        i5 = FDP.objects.all().filter(user=user)
        i6 = InterCollege.objects.all().filter(user=user)
        i7 = InternationalConf2.objects.all().filter(user=user)
        i8 = NationalConf2.objects.all().filter(user= user)
        i9 = Workshop2.objects.all().filter(user=user)
        i10 = FDP2.objects.all().filter(user=user)
        i11 = InterCollege2.objects.all().filter(user=user)
     
        return render(request,self.template_name,{'i11':i11,'i10':i10,'i9':i9,'i8':i8,'i7':i7,'i6':i6,'i':i,'i2':i2,'i3':i3,'i4':i4,'i5':i5,'flag2':self.flag2})

class EventsList(View):
    template_name="Events_Organized/events_list.html"
    def get(self,request):
        flag=0
        flag2=0
        if(Hod.objects.all().filter(name=get_user(request)) and It.objects.all().filter(name=get_user(request))):
            li = It.objects.all()
            flag=1
            flag2=1
            return render(request,self.template_name,{'i':li,'flag':flag,'flag2':flag2})

    def post(self,request):
        flag=0
        flag2=0
        if(Hod.objects.all().filter(name=get_user(request)) and It.objects.all().filter(name=get_user(request))):
            li = It.objects.all()
            flag=1
            flag2=1
            return render(request,self.template_name,{'i':li,'flag':flag,'flag2':flag2})

class FacEventsList(View):
    template_name = "Events_Organized/fac_events_list.html"
    flag2=0
    def get(self,request,user,pk):
        user1=user
        if(Hod.objects.all().filter(name=get_user(request))):
            i = Grant.objects.all().filter(user=user)
            i2 = InternationalConf.objects.all().filter(user=user)
            i3 = NationalConf.objects.all().filter(user=user)
            i4 = Workshop.objects.all().filter(user=user)
            i5 = FDP.objects.all().filter(user=user)
            i6 = InterCollege.objects.all().filter(user=user)
            i7 = InternationalConf2.objects.all().filter(user=user)
            i8 = NationalConf2.objects.all().filter(user= user)
            i9 = Workshop2.objects.all().filter(user=user)
            i10 = FDP2.objects.all().filter(user=user)
            i11 = InterCollege2.objects.all().filter(user=user)
            flag2=1
            return render(request,self.template_name,{'user1':user,'i11':i11,'i10':i10,'i9':i9,'i8':i8,'i6':i6,'i7':i7,'i':i,'i2':i2,'i3':i3,'i4':i4,'i5':i5,'flag2':flag2})

    def post(self,request,user,pk):
        if(Hod.objects.all().filter(name=get_user(request))):
            user1=user
            flag2=1
            i = Grant.objects.all().filter(user=user)
            i2 = InternationalConf.objects.all().filter(user=user)
            i3 = NationalConf.objects.all().filter(user=user)
            i4 = Workshop.objects.all().filter(user=user)
            i5 = FDP.objects.all().filter(user=user)
            i6 = InterCollege.objects.all().filter(user=user)
            i7 = InternationalConf2.objects.all().filter(user=user)
            i8 = NationalConf2.objects.all().filter(user= user)
            i9 = Workshop2.objects.all().filter(user=user)
            i10 = FDP2.objects.all().filter(user=user)
            i11 = InterCollege2.objects.all().filter(user=user)
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
            if(request.POST.get('points')):
                a=Grant.objects.filter(pk=pk).update(pointsaward=value)
            elif(request.POST.get('points1')):
                b=InternationalConf.objects.filter(pk=pk).update(pointsaward=value1)
            elif(request.POST.get('points2')):
                c=NationalConf.objects.filter(pk=pk).update(pointsaward=value2)
            elif(request.POST.get('points3')):
                d=Workshop.objects.all().filter(pk=pk).update(pointsaward=value3)
            elif(request.POST.get('points4')):
                e=FDP.objects.all().filter(pk=pk).update(pointsaward=value4)
            elif(request.POST.get('points5')):
                f=InterCollege.objects.all().filter(pk=pk).update(pointsaward=value5)
            elif(request.POST.get('points6')):
                f=InternationalConf2.objects.all().filter(pk=pk).update(pointsaward=value6)
            elif(request.POST.get('points7')):
                f=NationalConf2.objects.all().filter(pk=pk).update(pointsaward=value7)
            elif(request.POST.get('points8')):
                f=Workshop2.objects.all().filter(pk=pk).update(pointsaward=value8)
            elif(request.POST.get('points9')):
                f=FDP2.objects.all().filter(pk=pk).update(pointsaward=value9)
            elif(request.POST.get('points10')):
                f=InterCollege2.objects.all().filter(pk=pk).update(pointsaward=value10)
        return render(request,self.template_name,{'user1':user,'flag2':flag2,'i11':i11,'i10':i10,'i9':i9,'i8':i8,'i7':i7,'i6':i6,'i':i,'i2':i2,'i3':i3,'i4':i4,'i5':i5})

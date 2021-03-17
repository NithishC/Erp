from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth import get_user
from Contributions.models import CollegeContrib,DepartmentContrib,IndexedJournal
from skct.models import Proof,Staff,Hod,It,Cse,Mech,Eee,Ece,Ice,Civil,Mba,Sh

# Create your views here.


def delete2(request,pk):
    if (request.method) == 'POST':
        name = CollegeContrib.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('contribs_responses_view')

def delete3(request,pk):
    if (request.method) == 'POST':
        name =DepartmentContrib.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('contribs_responses_view')

def delete4(request,pk):
    if (request.method) == 'POST':
        name = IndexedJournal.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('contribs_responses_view')


class ContributionsView(View):
    template_name="Contributions/contrib_index.html"
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
            name = CollegeContrib()
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
            ob=CollegeContrib.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name,{'flag2':flag2,'li':li})
            return render(request,self.template_name,{'li':li,})

        elif(request.POST.get('des1')):
            name1 = DepartmentContrib()
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
            ob=DepartmentContrib.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name,{'flag2':flag2,'li':li})
            return render(request,self.template_name,{'li':li,})

        elif(request.POST.get('des2')):
            name2 = IndexedJournal()
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
            ob=IndexedJournal.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name,{'flag2':flag2,'li':li})
            return render(request,self.template_name,{'li':li,})

class ResponsesView(View):
    template_name = "Contributions/contribs_responses_view.html"
    flag2=0
    def get(self,request):
        user = get_user(request)
        i = CollegeContrib.objects.all().filter(user=user)
        i2 = DepartmentContrib.objects.all().filter(user=user)
        i3 = IndexedJournal.objects.all().filter(user=user)
        if(Hod.objects.all().filter(name=get_user(request))):
            self.flag2 = 1
        return render(request,self.template_name,{'i':i,'i2':i2,'i3':i3,'flag2':self.flag2})

    def post(self,request):
        user = get_user(request)
        i = CollegeContrib.objects.all().filter(user=user)
        i2 = DepartmentContrib.objects.all().filter(user=user)
        i3 = IndexedJournal.objects.all().filter(user=user)
        if(Hod.objects.all().filter(name=get_user(request))):
            self.flag2 = 1
        return render(request,self.template_name,{'i':i,'i2':i2,'i3':i3,'flag2':self.flag2})

class ContribsList(View):
    template_name="Contributions/contribs_list.html"
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

class FacContribsList(View):
    template_name = "Contributions/fac_contribs.html"
    flag2=0
    def get(self,request,user,pk):
        user1=user
        if(Hod.objects.all().filter(name=get_user(request))):
            i = CollegeContrib.objects.all().filter(user=user)
            i2 = DepartmentContrib.objects.all().filter(user=user)
            i3 = IndexedJournal.objects.all().filter(user=user)
            flag2=1
            return render(request,self.template_name,{'user1':user,'i':i,'i2':i2,'i3':i3,'flag2':flag2})

    def post(self,request,user,pk):
        if(Hod.objects.all().filter(name=get_user(request))):
            flag2=1
            user1=user
            i = CollegeContrib.objects.all().filter(user=user)
            i2 = DepartmentContrib.objects.all().filter(user=user)
            i3 = IndexedJournal.objects.all().filter(user=user)
            value=request.POST.get('points')
            value1=request.POST.get('points1')
            value2=request.POST.get('points2')
  
            if(request.POST.get('points')):
                a=CollegeContrib.objects.filter(pk=pk).update(pointsaward=value)
            elif(request.POST.get('points1')):
                b=DepartmentContrib.objects.filter(pk=pk).update(pointsaward=value1)
            elif(request.POST.get('points2')):
                c=IndexedJournal.objects.filter(pk=pk).update(pointsaward=value2)
        return render(request,self.template_name,{'user1':user,'flag2':flag2,'i':i,'i2':i2,'i3':i3,})

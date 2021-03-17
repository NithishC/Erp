from os import name
from django.shortcuts import render,redirect
from django.views.generic import View
from Academics.models import Academics,Feedback,Innovation,UG,PG,ExtraCurricular,AllClear,ThreeClear,Article,Competitive,Startups,Awards,Prizes,Internship,OnlineCertification
from skct.models import Proof,Staff,Hod,It,Cse,Mech,Eee,Ece,Ice,Civil,Mba,Sh
from django.contrib.auth import get_user
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from Contributions.models import CollegeContrib,DepartmentContrib,IndexedJournal
from Events.models import Grant,InternationalConf,NationalConf,Workshop,FDP,InterCollege,InternationalConf2,InterCollege2,Workshop2,FDP2,NationalConf2
from Research.models import SCI,ESCI,RIP,RNP,ISBN,IEEE,Guideship,GuideshipPursuing,Patents,Applied,Received,Consultancy,DCM,SubjectExpert,WOS
from SelfDevelopment.models import FacultyAttendance,GuestLecture,GuestLectureIndustry,PatentFiled,PatentPublished,PatentGranted,PlacementArranged,Events,MOU,Excellence,EventsParticipation,Awards,OnlineCourse
from SelfDevelopment.models import OnlineCertification as oc

#obj = SocialAccount.objects.all().filter(user = get_user(request))
#dictt = dict(obj[0].extra_data)
#print(dictt['email'])

def render_pdf_view(request):
    template_path = 'Pdfgen/pdfgen.html'
    user = get_user(request)
    i = Academics.objects.all().filter(user=user)
    i2 = Feedback.objects.all().filter(user=user)
    i3 = Innovation.objects.all().filter(user=user)
    i4 = UG.objects.all().filter(user=user)
    i5 = PG.objects.all().filter(user=user)
    i6 = ExtraCurricular.objects.all().filter(user=user)
    i7 = AllClear.objects.all().filter(user=user)
    i8 = ThreeClear.objects.all().filter(user= user)
    i9 = Article.objects.all().filter(user=user)
    i10 = Competitive.objects.all().filter(user=user)
    i11 = Startups.objects.all().filter(user=user)
    i12 = Awards.objects.all().filter(user=user)
    i13 = Prizes.objects.all().filter(user=user)
    i14 = Internship.objects.all().filter(user=user)
    i15 = OnlineCertification.objects.all().filter(user=user)
    sdi = FacultyAttendance.objects.all().filter(user=user)
    sdi2 = GuestLecture.objects.all().filter(user=user)
    sdi3 = GuestLectureIndustry.objects.all().filter(user=user)
    sdi4 = oc.objects.all().filter(user=user)
    sdi5 = PatentFiled.objects.all().filter(user=user)
    sdi6 = PatentPublished.objects.all().filter(user=user)
    sdi7 = PatentGranted.objects.all().filter(user=user)
    sdi8 = PlacementArranged.objects.all().filter(user= user)
    sdi9 = Events.objects.all().filter(user=user)
    sdi10 = MOU.objects.all().filter(user=user)
    sdi11 = Excellence.objects.all().filter(user=user)
    sdi12 = EventsParticipation.objects.all().filter(user=user)
    sdi13 = Awards.objects.all().filter(user=user)
    sdi14 = OnlineCourse.objects.all().filter(user=user)
    ci = CollegeContrib.objects.all().filter(user=user)
    ci2 = DepartmentContrib.objects.all().filter(user=user)
    ci3 = IndexedJournal.objects.all().filter(user=user)
    evi = Grant.objects.all().filter(user=user)
    evi2 = InternationalConf.objects.all().filter(user=user)
    evi3 = NationalConf.objects.all().filter(user=user)
    evi4 = Workshop.objects.all().filter(user=user)
    evi5 = FDP.objects.all().filter(user=user)
    evi6 = InterCollege.objects.all().filter(user=user)
    evi7 = InternationalConf2.objects.all().filter(user=user)
    evi8 = NationalConf2.objects.all().filter(user= user)
    evi9 = Workshop2.objects.all().filter(user=user)
    evi10 = FDP2.objects.all().filter(user=user)
    evi11 = InterCollege2.objects.all().filter(user=user)
    rei = SCI.objects.all().filter(user=user)
    rei2 = ESCI.objects.all().filter(user=user)
    rei3 = RIP.objects.all().filter(user=user)
    rei4 = RNP.objects.all().filter(user=user)
    rei5 = ISBN.objects.all().filter(user=user)
    rei6 = IEEE.objects.all().filter(user=user)
    rei7 = Guideship.objects.all().filter(user=user)
    rei8 = GuideshipPursuing.objects.all().filter(user= user)
    rei9 = Patents.objects.all().filter(user=user)
    rei10 = Applied.objects.all().filter(user=user)
    rei11 = Received.objects.all().filter(user=user)
    rei12 = Consultancy.objects.all().filter(user=user)
    rei13 = DCM.objects.all().filter(user=user)
    rei14 = SubjectExpert.objects.all().filter(user=user)
    rei15 = WOS.objects.all().filter(user=user)
    staff = Staff.objects.all().filter(name = str(user))[0]
    
    context = {'obj': i,'user' :user,'obj2': i2,'obj3': i3,'obj4': i4,'obj5': i5,'obj6': i6,'obj7': i7,'obj8': i8,'obj9': i9,'obj10': i10,'obj11': i11,'obj12': i12,'obj13': i13,'obj14': i14,'obj15': i15,
    'i14':sdi14,'i13':sdi13,'i12':sdi12,'i11':sdi11,'i10':sdi10,'i9':sdi9,'i8':sdi8,'i6':sdi6,'i7':sdi7,'sdi':sdi,'i2':sdi2,'i3':sdi3,'i4':sdi4,'i5':sdi5,
    'ci':ci,'ci2':ci2,'ci3':ci3,
    'evi11':evi11,'evi10':evi10,'evi9':evi9,'evi8':evi8,'evi6':evi6,'evi7':evi7,'evi':evi,'evi2':evi2,'evi3':evi3,'evi4':evi4,'evi5':evi5,
    'rei15':rei15,'rei14':rei14,'rei13':rei13,'rei12':rei12,'rei11':rei11,'rei10':rei10,'rei9':rei9,'rei8':rei8,'rei6':rei6,'rei7':rei7,'rei':rei,'rei2':rei2,'rei3':rei3,'rei4':rei4,'rei5':rei5,
    'staff':staff,}

    
    response = HttpResponse(content_type='application/pdf')
    
    template = get_template(template_path)
    html = template.render(context)

    
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def delete(request,pk):
    if (request.method) == 'POST':
        name =Proof.objects.get(pk=pk)
        name.delete()
    return redirect('profile')

def delete2(request,pk):
    if (request.method) == 'POST':
        name =Academics.objects.get(pk=pk)
        name.delete()
    return redirect('responses_view')

def delete3(request,pk):
    if (request.method) == 'POST':
        name =Feedback.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view')

def delete4(request,pk):
    if (request.method) == 'POST':
        name =Innovation.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view')

def delete5(request,pk):
    if (request.method) == 'POST':
        name =UG.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view')

def delete6(request,pk):
    if (request.method) == 'POST':
        name =PG.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view')

def delete7(request,pk):
    if (request.method) == 'POST':
        name =ExtraCurricular.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view')

def delete8(request,pk):
    if (request.method) == 'POST':
        name =AllClear.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view')

def delete9(request,pk):
    if (request.method) == 'POST':
        name =ThreeClear.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view')

def delete10(request,pk):
    if (request.method) == 'POST':
        name =Article.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view')

def delete11(request,pk):
    if (request.method) == 'POST':
        name =Competitive.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view')

def delete12(request,pk):
    if (request.method) == 'POST':
        name =Startups.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view')

def delete13(request,pk):
    if (request.method) == 'POST':
        name =Awards.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view')

def delete14(request,pk):
    if (request.method) == 'POST':
        name =Prizes.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view')

def delete15(request,pk):
    if (request.method) == 'POST':
        name =Internship.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view')

def delete16(request,pk):
    if (request.method) == 'POST':
        name =OnlineCertification.objects.get(pk=pk)
        name.delete()
        print(pk)
    return redirect('responses_view')


#------------------------------Delete---------------------------------------------


class AcademicView(View):
    template_name =["index2.html"]
    def get(self,request):
        userhere=get_user(request)
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
            name =Academics()
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
            name1 = Feedback()
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
            ob=Innovation.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des2')):
            name2 = Innovation()
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
            ob=Innovation.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des3')):
            name3 = UG()
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
            ob=UG.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})
        
        elif(request.POST.get('des4')):
            name4 = PG()
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
            ob=PG.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des5')):
            name5 = ExtraCurricular()
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
            ob=ExtraCurricular.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des6')):
            name6 = AllClear()
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
            ob=AllClear.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des7')):
            name7 = ThreeClear()
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
            ob=ThreeClear.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des8')):
            name8 = Article()
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
            ob=Article.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des9')):
            name9 = Competitive()
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
            ob=Competitive.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des10')):
            name10 = Startups()
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
            ob=Startups.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des11')):
            name11 = Awards()
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
            ob=Awards.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des12')):
            name12 = Prizes()
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
            ob=Prizes.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des13')):
            name13 = Internship()
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
            ob=Internship.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})

        elif(request.POST.get('des14')):
            name14 = OnlineCertification()
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
            ob=OnlineCertification.objects.all().filter(user=userhere)
            li = [i for i in range(1,11)]
            li.reverse()

            if(Hod.objects.all().filter(name=userhere)):
                flag2=1
                return render(request,self.template_name[0],{'flag2':flag2,'li':li})
            return render(request,self.template_name[0],{'li':li,})


class AcadListView(View):
    template_name = "academics_list.html"
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
    template_name = "fac_academics_list.html"
    flag2=0
    def get(self,request,user,pk):
        user1=user
        if(Hod.objects.all().filter(name=get_user(request))):
            i = Academics.objects.all().filter(user=user)
            i2 = Feedback.objects.all().filter(user=user)
            i3 = Innovation.objects.all().filter(user=user)
            i4 = UG.objects.all().filter(user=user)
            i5 = PG.objects.all().filter(user=user)
            i6 = ExtraCurricular.objects.all().filter(user=user)
            i7 = AllClear.objects.all().filter(user=user)
            i8 = ThreeClear.objects.all().filter(user= user)
            i9 = Article.objects.all().filter(user=user)
            i10 = Competitive.objects.all().filter(user=user)
            i11 = Startups.objects.all().filter(user=user)
            i12 = Awards.objects.all().filter(user=user)
            i13 = Prizes.objects.all().filter(user=user)
            i14 = Internship.objects.all().filter(user=user)
            i15 = OnlineCertification.objects.all().filter(user=user)
            flag2=1
        return render(request,self.template_name,{'i15':i15,'i14':i14,'i13':i13,'i12':i12,'i11':i11,'i10':i10,'i9':i9,'i8':i8,'i6':i6,'i7':i7,'i':i,'i2':i2,'i3':i3,'i4':i4,'i5':i5,'flag2':flag2,'user1':user1})

    def post(self,request,user,pk):
        user1=user
        if(Hod.objects.all().filter(name=get_user(request))):
            i = Academics.objects.all().filter(user = user)
            i2 = Feedback.objects.all().filter(user=user)
            i3 = Innovation.objects.all().filter(user=user)
            i4 = UG.objects.all().filter(user=user)
            i5 = PG.objects.all().filter(user=user)
            i6 = ExtraCurricular.objects.all().filter(user=user)
            i7 = AllClear.objects.all().filter(user=user)
            i8 = ThreeClear.objects.all().filter(user=user)
            i9 = Article.objects.all().filter(user=user)
            i10 = Competitive.objects.all().filter(user=user)
            i11 = Startups.objects.all().filter(user=user)
            i12 = Awards.objects.all().filter(user=user)
            i13 = Prizes.objects.all().filter(user=user)
            i14 = Internship.objects.all().filter(user=user)
            i15 = OnlineCertification.objects.all().filter(user=user)
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
                a=Academics.objects.filter(pk=pk).update(pointsaward=value)
            elif(request.POST.get('points1')):
                b=Feedback.objects.filter(pk=pk).update(pointsaward=value1)
            elif(request.POST.get('points2')):
                c=Innovation.objects.filter(pk=pk).update(pointsaward=value2)
            elif(request.POST.get('points3')):
                d=UG.objects.all().filter(pk=pk).update(pointsaward=value3)
            elif(request.POST.get('points4')):
                e=PG.objects.all().filter(pk=pk).update(pointsaward=value4)
            elif(request.POST.get('points5')):
                f=ExtraCurricular.objects.all().filter(pk=pk).update(pointsaward=value5)
            elif(request.POST.get('points6')):
                f=AllClear.objects.all().filter(pk=pk).update(pointsaward=value6)
            elif(request.POST.get('points7')):
                f=ThreeClear.objects.all().filter(pk=pk).update(pointsaward=value7)
            elif(request.POST.get('points8')):
                f=Article.objects.all().filter(pk=pk).update(pointsaward=value8)
            elif(request.POST.get('points9')):
                f=Competitive.objects.all().filter(pk=pk).update(pointsaward=value9)
            elif(request.POST.get('points10')):
                f=Startups.objects.all().filter(pk=pk).update(pointsaward=value10)
            elif(request.POST.get('points11')):
                f=Awards.objects.all().filter(pk=pk).update(pointsaward=value11)
            elif(request.POST.get('points12')):
                f=Prizes.objects.all().filter(pk=pk).update(pointsaward=value12)
            elif(request.POST.get('points13')):
                f=Internship.objects.all().filter(pk=pk).update(pointsaward=value13)
            elif(request.POST.get('points14')):
                f=OnlineCertification.objects.all().filter(pk=pk).update(pointsaward=value14)
        return render(request,self.template_name,{'i15':i15,'i14':i14,'i13':i13,'i12':i12,'i11':i11,'i10':i10,'i9':i9,'i8':i8,'i7':i7,'i6':i6,'i':i,'i2':i2,'i3':i3,'i4':i4,'i5':i5,'user1':user1})

class ResponsesView(View):
    template_name = "responses_view.html"
    flag2=0
    def get(self,request):
        user = get_user(request)
        if(Hod.objects.all().filter(name=get_user(request))):
            self.flag2 = 1
        i = Academics.objects.all().filter(user=user)
        i2 = Feedback.objects.all().filter(user=user)
        i3 = Innovation.objects.all().filter(user=user)
        i4 = UG.objects.all().filter(user=user)
        i5 = PG.objects.all().filter(user=user)
        i6 = ExtraCurricular.objects.all().filter(user=user)
        i7 = AllClear.objects.all().filter(user=user)
        i8 = ThreeClear.objects.all().filter(user= user)
        i9 = Article.objects.all().filter(user=user)
        i10 = Competitive.objects.all().filter(user=user)
        i11 = Startups.objects.all().filter(user=user)
        i12 = Awards.objects.all().filter(user=user)
        i13 = Prizes.objects.all().filter(user=user)
        i14 = Internship.objects.all().filter(user=user)
        i15 = OnlineCertification.objects.all().filter(user=user)
        return render(request,self.template_name,{'i15':i15,'i14':i14,'i13':i13,'i12':i12,'i11':i11,'i10':i10,'i9':i9,'i8':i8,'i6':i6,'i7':i7,'i':i,'i2':i2,'i3':i3,'i4':i4,'i5':i5,'flag2':self.flag2})

    def post(self,request):
        user = get_user(request)
        if(Hod.objects.all().filter(name=get_user(request))):
            self.flag2 = 1
        i = Academics.objects.all().filter(user = user)
        i2 = Feedback.objects.all().filter(user=user)
        i3 = Innovation.objects.all().filter(user=user)
        i4 = UG.objects.all().filter(user=user)
        i5 = PG.objects.all().filter(user=user)
        i6 = ExtraCurricular.objects.all().filter(user=user)
        i7 = AllClear.objects.all().filter(user=user)
        i8 = ThreeClear.objects.all().filter(user=user)
        i9 = Article.objects.all().filter(user=user)
        i10 = Competitive.objects.all().filter(user=user)
        i11 = Startups.objects.all().filter(user=user)
        i12 = Awards.objects.all().filter(user=user)
        i13 = Prizes.objects.all().filter(user=user)
        i14 = Internship.objects.all().filter(user=user)
        i15 = OnlineCertification.objects.all().filter(user=user)
        return render(request,self.template_name,{'i15':i15,'i14':i14,'i13':i13,'i12':i12,'i11':i11,'i10':i10,'i9':i9,'i8':i8,'i7':i7,'i6':i6,'i':i,'i2':i2,'i3':i3,'i4':i4,'i5':i5,'flag2':self.flag2})

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from allauth.socialaccount.models import SocialAccount



def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    
    user = get_user(request)
    obj = Academics.objects.all().filter(user = user)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(250,800,str(user)+"report")
    for i in range(len(obj)):
        p.drawString(i*200+100, i*40+100, obj[i].des)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    fname = 'report.pdf'
    return FileResponse(buffer, as_attachment=False, filename=fname)



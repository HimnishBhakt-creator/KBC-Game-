from django.shortcuts import render
from .models import Questions


# Create your views here.

flipQuestion = Questions.objects.get(id=11)
correct_answer_flip=flipQuestion.correctAnswer
fivtyFityid1=flipQuestion.fiftyFiftyId1
fivtyFityid2=flipQuestion.fiftyFiftyId2
fivtyFityids_flip=[fivtyFityid1,fivtyFityid2]
print(flipQuestion)
def home_page(request):
    q_ans = Questions.objects.get(id=1)
    correct_answer=q_ans.correctAnswer
    fivtyFityid1=q_ans.fiftyFiftyId1
    fivtyFityid2=q_ans.fiftyFiftyId2
    fivtyFityids=[fivtyFityid1,fivtyFityid2]
    return render(request, "index.html", {'op':q_ans,'correctAns':correct_answer,'fiftyFifty':fivtyFityids,'fiftyUsed':0,'nxtQuestion':'2','op_flip':flipQuestion,'correctAns_flip':correct_answer_flip,'fiftyFifty_flip':fivtyFityids_flip,'flipUsed':0} )

def Q2(request):
      fiftyUsedView=request.GET.get('f-fifty-used','')
      flipUsedView=request.GET.get('flip-used','')
      q_ans = Questions.objects.get(id=2)
      correct_answer=q_ans.correctAnswer
      fivtyFityid1=q_ans.fiftyFiftyId1
      fivtyFityid2=q_ans.fiftyFiftyId2
      fivtyFityids=[fivtyFityid1,fivtyFityid2]
      return render(request, "index.html", {'op':q_ans,'correctAns':correct_answer,'nxtQuestion':'3','fiftyFifty':fivtyFityids,'fiftyUsed':fiftyUsedView,'op_flip':flipQuestion,'correctAns_flip':correct_answer_flip,'fiftyFifty_flip':fivtyFityids_flip,'flipUsed':flipUsedView}  )

def Q3(request):
    flipUsedView=request.GET.get('flip-used','') 
    fiftyUsedView=request.GET.get('f-fifty-used','')
    q_ans = Questions.objects.get(id=3)
    correct_answer=q_ans.correctAnswer
    fivtyFityid1=q_ans.fiftyFiftyId1
    fivtyFityid2=q_ans.fiftyFiftyId2
    fivtyFityids=[fivtyFityid1,fivtyFityid2]
    return render(request, "index.html", {'op':q_ans,'correctAns':correct_answer,'nxtQuestion':'4','fiftyFifty':fivtyFityids,'fiftyUsed':fiftyUsedView,'op_flip':flipQuestion,'correctAns_flip':correct_answer_flip,'fiftyFifty_flip':fivtyFityids_flip,'flipUsed':flipUsedView} )

def Q4(request):
    flipUsedView=request.GET.get('flip-used','')
    fiftyUsedView=request.GET.get('f-fifty-used','')
    q_ans = Questions.objects.get(id=4)
    correct_answer=q_ans.correctAnswer
    fivtyFityid1=q_ans.fiftyFiftyId1
    fivtyFityid2=q_ans.fiftyFiftyId2
    fivtyFityids=[fivtyFityid1,fivtyFityid2]
    return render(request, "index.html", {'op':q_ans,'correctAns':correct_answer,'nxtQuestion':'5','fiftyFifty':fivtyFityids,'fiftyUsed':fiftyUsedView,'op_flip':flipQuestion,'correctAns_flip':correct_answer_flip,'fiftyFifty_flip':fivtyFityids_flip,'flipUsed':flipUsedView} )

def Q5(request):
    flipUsedView=request.GET.get('flip-used','')
    fiftyUsedView=request.GET.get('f-fifty-used','')
    q_ans = Questions.objects.get(id=5)
    correct_answer=q_ans.correctAnswer
    fivtyFityid1=q_ans.fiftyFiftyId1
    fivtyFityid2=q_ans.fiftyFiftyId2
    fivtyFityids=[fivtyFityid1,fivtyFityid2]
    return render(request, "index.html", {'op':q_ans,'correctAns':correct_answer,'nxtQuestion':'6','fiftyFifty':fivtyFityids,'fiftyUsed':fiftyUsedView,'op_flip':flipQuestion,'correctAns_flip':correct_answer_flip,'fiftyFifty_flip':fivtyFityids_flip,'flipUsed':flipUsedView} )

def Q6(request):
    flipUsedView=request.GET.get('flip-used','')
    fiftyUsedView=request.GET.get('f-fifty-used','')
    q_ans = Questions.objects.get(id=6)
    correct_answer=q_ans.correctAnswer
    fivtyFityid1=q_ans.fiftyFiftyId1
    fivtyFityid2=q_ans.fiftyFiftyId2
    fivtyFityids=[fivtyFityid1,fivtyFityid2]
    return render(request, "index.html", {'op':q_ans,'correctAns':correct_answer,'nxtQuestion':'7','fiftyFifty':fivtyFityids,'fiftyUsed':fiftyUsedView,'op_flip':flipQuestion,'correctAns_flip':correct_answer_flip,'fiftyFifty_flip':fivtyFityids_flip,'flipUsed':flipUsedView} )

def Q7(request):
    flipUsedView=request.GET.get('flip-used','')
    fiftyUsedView=request.GET.get('f-fifty-used','')
    q_ans = Questions.objects.get(id=7)
    correct_answer=q_ans.correctAnswer
    fivtyFityid1=q_ans.fiftyFiftyId1
    fivtyFityid2=q_ans.fiftyFiftyId2
    fivtyFityids=[fivtyFityid1,fivtyFityid2]
    return render(request, "index.html", {'op':q_ans,'correctAns':correct_answer,'nxtQuestion':'8','fiftyFifty':fivtyFityids,'fiftyUsed':fiftyUsedView,'op_flip':flipQuestion,'correctAns_flip':correct_answer_flip,'fiftyFifty_flip':fivtyFityids_flip,'flipUsed':flipUsedView} )

def Q8(request):
    flipUsedView=request.GET.get('flip-used','')
    fiftyUsedView=request.GET.get('f-fifty-used','')
    q_ans = Questions.objects.get(id=8)
    correct_answer=q_ans.correctAnswer
    fivtyFityid1=q_ans.fiftyFiftyId1
    fivtyFityid2=q_ans.fiftyFiftyId2
    fivtyFityids=[fivtyFityid1,fivtyFityid2]
    return render(request, "index.html", {'op':q_ans,'correctAns':correct_answer,'nxtQuestion':'9','fiftyFifty':fivtyFityids,'fiftyUsed':fiftyUsedView,'op_flip':flipQuestion,'correctAns_flip':correct_answer_flip,'fiftyFifty_flip':fivtyFityids_flip,'flipUsed':flipUsedView} )

def Q9(request):
    flipUsedView=request.GET.get('flip-used','')
    fiftyUsedView=request.GET.get('f-fifty-used','')
    q_ans = Questions.objects.get(id=9)
    correct_answer=q_ans.correctAnswer
    fivtyFityid1=q_ans.fiftyFiftyId1
    fivtyFityid2=q_ans.fiftyFiftyId2
    fivtyFityids=[fivtyFityid1,fivtyFityid2]
    return render(request, "index.html", {'op':q_ans,'correctAns':correct_answer,'nxtQuestion':'10','fiftyFifty':fivtyFityids,'fiftyUsed':fiftyUsedView,'op_flip':flipQuestion,'correctAns_flip':correct_answer_flip,'fiftyFifty_flip':fivtyFityids_flip,'flipUsed':flipUsedView} )

def Q10(request):
    flipUsedView=request.GET.get('flip-used','')
    fiftyUsedView=request.GET.get('f-fifty-used','')
    q_ans = Questions.objects.get(id=10)
    correct_answer=q_ans.correctAnswer
    fivtyFityid1=q_ans.fiftyFiftyId1
    fivtyFityid2=q_ans.fiftyFiftyId2
    fivtyFityids=[fivtyFityid1,fivtyFityid2]
    return render(request, "index.html", {'op':q_ans,'correctAns':correct_answer,'nxtQuestion':'win','fiftyFifty':fivtyFityids,'fiftyUsed':fiftyUsedView,'op_flip':flipQuestion,'correctAns_flip':correct_answer_flip,'fiftyFifty_flip':fivtyFityids_flip,'flipUsed':flipUsedView} )


def lost(request):
    return render(request,"lost.html")

def win(request):
    return render(request,"win.html")

def quit(request):
    won=request.GET.get('won','')
    return render(request,"quit.html",{"won":won})

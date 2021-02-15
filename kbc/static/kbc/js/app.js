function play() {
        var audio = document.getElementById("audio");
        audio.play();
        location.replace("q2");
        alert("hub");
        }

function check(answer,correctAnswer,nxtQuestion){
    var a = confirm("Lock Answer?")
    if(a==true){
        if(answer==correctAnswer){
            alert("Right Answer")
            location.replace(nxtQuestion);
        }
        else{
            location.replace("lost");
        }
    }
}

function showQuestion(){
    var x=document.getElementById("question").style.visibility="visible";
    document.getElementById("show").innerHTML="SHOW OPTIONS";
    alert("Show Options");
    document.getElementById(divId).style.background-color="blue";
    document.getElementById("1").style.visibility="visible";
}

function fiftyFifty(firstId,secondId){
    document.getElementById(firstId).style.visibility="hidden";
    document.getElementById(secondId).style.visibility="hidden";
}








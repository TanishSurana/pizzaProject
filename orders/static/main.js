function disableScroll() { 
    document.body.classList.add("stop-scrolling"); 
} 

function enableScroll() { 
    document.body.classList.remove("stop-scrolling"); 
} 

function currentYPosition() {
    // Firefox, Chrome, Opera, Safari
    if (self.pageYOffset) return self.pageYOffset;
    // Internet Explorer 6 - standards mode
    if (document.documentElement && document.documentElement.scrollTop)
        return document.documentElement.scrollTop;
    // Internet Explorer 6, 7 and 8
    if (document.body.scrollTop) return document.body.scrollTop;
    return 0;
}


function elmYPosition(eID) {
    var elm = document.getElementById(eID);
    var y = elm.offsetTop;
    var node = elm;
    while (node.offsetParent && node.offsetParent != document.body) {
        node = node.offsetParent;
        y += node.offsetTop;
    } return y;
}


function smoothScroll(eID){
    var startY = currentYPosition();
    var stopY = elmYPosition(eID);
    var distance = stopY > startY ? stopY - startY : startY - stopY;
    if (distance < 100) {
        scrollTo(0, stopY); return;
    }
    var speed = Math.round(distance / 100);
    if (speed >= 20) speed = 20;
    var step = Math.round(distance / 25);
    var leapY = stopY > startY ? startY + step : startY - step;
    var timer = 0;
    if (stopY > startY) {
        for ( var i=startY; i<stopY; i+=step ) {
            setTimeout("window.scrollTo(0, "+leapY+")", timer * speed);
            leapY += step; if (leapY > stopY) leapY = stopY; timer++;
        } return;
    }
    for ( var i=startY; i>stopY; i-=step ) {
        setTimeout("window.scrollTo(0, "+leapY+")", timer * speed);
        leapY -= step; if (leapY < stopY) leapY = stopY; timer++;
    }
}


document.addEventListener('DOMContentLoaded', function(){




    document.querySelectorAll(".blogin").forEach(a => {
        a.onclick = function(){
            document.querySelector(".bg-modal").style.display = "flex";
            disableScroll();
        };
    });
    
    
    document.querySelector(".closelogin").onclick = function(){
        document.querySelector(".bg-modal").style.display = "none";
        enableScroll();
    };




        document.querySelectorAll(".signup").forEach(a => {
        a.onclick = function(){
            document.querySelector(".bg-modal-r").style.display = "flex";
            disableScroll();
        };
    });
    

    document.querySelectorAll(".closereg").forEach(a => {
        a.onclick = ()=>
        {
            document.querySelector(".bg-modal-r").style.display = "none";
            enableScroll();
        }
    })







    var password = document.getElementById("password")
  , confirm_password = document.getElementById("confirm_password");

    function validatePassword(){
    if(password.value != confirm_password.value) {
        confirm_password.setCustomValidity("Passwords Don't Match");
    } else {
        confirm_password.setCustomValidity('');
    }
    }

    password.onchange = validatePassword;
    confirm_password.onkeyup = validatePassword;



    document.querySelector(".rl").onclick = function(){
        document.querySelector(".bg-modal-r").style.display = "none";
        document.querySelector(".bg-modal").style.display = "flex";
    }

    document.querySelector(".lr").onclick = function(){
        document.querySelector(".bg-modal-r").style.display = "flex";
        document.querySelector(".bg-modal").style.display = "none";
    }


    document.querySelectorAll(".closecustomize").forEach(a => {
        a.onclick = ()=>
        {
            document.querySelector(".bg-modal-m").style.display = "none";
            enableScroll();
        }
    })
    
})
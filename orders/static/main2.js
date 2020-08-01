document.addEventListener('DOMContentLoaded', function(){
    let ecost = 0;
    let scost = parseFloat(document.querySelector('#cost').innerHTML);

    document.querySelector("#sizeSelect").onchange = function(){
        var e1 = document.getElementById("sizeSelect");
        var strUser1 = e1.options[e1.selectedIndex].dataset.cost;
        scost = parseFloat(strUser1);
        document.querySelector("#cost").innerHTML = ecost + scost;
    }


    document.querySelector('#extras').onchange = function(){
            var e = document.getElementById("extras");
            var strUser = e.options[e.selectedIndex].dataset.cost;    
            ecost = parseFloat(strUser);    

            document.querySelector("#cost").innerHTML = ecost + scost;
    }
});
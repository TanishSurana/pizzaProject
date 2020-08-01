from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from datetime import datetime, date


from .models import *

em = "-1"

# Create your views here.
def index(request):
    context = {
        "error_message": "-1",
        "ecode": 0
    }
    return render(request, "orders/index.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/index.html", {"error_message": "Invalid credentials.", "ecode": -1})

def logout_view(request):
    logout(request)
    context = {
        "error_message": "-1",
        "ecode": 0
    }
    return render(request, "orders/index.html", context)

def register_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    email = request.POST["email"]
    fn = request.POST["fn"]
    ln = request.POST["ln"]
    if User.objects.filter(username=username).exists():
        print("you messed up")
        context = {
            "error_message": "username already taken",
            "ecode": -2
        }
        return render(request, "orders/index.html", context)
    else:
        user = User.objects.create_user(username=username, password=password, email=email, first_name=fn, last_name=ln)
        login(request, user)
        return HttpResponseRedirect(reverse("index"))



def menu(request):
    context = {
        "error_message": "-1",
        "ecode": 0,
        "regularpizza": Regularpizza.objects.all(),
        "sicilianpizza": Sicilianpizza.objects.all(),
        "salad": Salad.objects.all(),
        "pasta": Pasta.objects.all(),
        "dinnerplatter": Dinnerplatter.objects.all(),
        "subs": Subs.objects.all(),
        "category": {'regularpizza':Regularpizza.objects.all(),'sicilianpizza':Sicilianpizza.objects.all(), 'subs': Subs.objects.all(), 'pasta':Pasta.objects.all(), 'salad':Salad.objects.all(), 'dinnerplatter':Dinnerplatter.objects.all()}
    }
    return render(request, "orders/menu.html", context)
    
def verzeo(request):
    return render(request, "orders/layout.html")





def customize(request, cat,itemname):
    #print(cat, itemname)
    #check the category and itemname if valid and then get data
    #pass in n topping and extras along with the extras and topping table if required
    category = cat
    itemname1 = itemname

    if request.user.is_authenticated:
        try:
            if category == "regularpizza":
                print("hello there")
                menu=Regularpizza.objects.get(itemname = itemname1)
            elif category == "sicilianpizza":
                menu=Sicilianpizza.objects.get(itemname = itemname1)
            elif category == "subs":
                menu=Subs.objects.get(itemname = itemname1)
            elif category == "pasta":
                menu=Pasta.objects.get(itemname = itemname1)
            elif category == "salad":
                menu=Salad.objects.get(itemname = itemname1)
            elif category == "dinnerplatter":
                menu=Dinnerplatter.objects.get(itemname = itemname1)
            #print(menu)
        except:
            context = {
                'message':'You messed up',
            }
            return render(request, 'orders/error.html', context)

        #print(menu)

        tops = list()
        for i in range(menu.ntoppings):
            tops.append("top" + str(i+1))

        #print(tops)

        context = {
            'cat': cat,
            'itemname': itemname,
            'item': menu,
            "topping": Topping.objects.all(),
            "extra": Extra.objects.all(),
            'tops':tops,
        }
        return render(request, "orders\customize.html", context)

    else:
        context = {
            'message':'you are not logged in',
        }
        return render(request, 'orders/error.html', context)


def add(request, cat, itemname):
    if request.user.is_authenticated:
        # get the category and itemname
        category = cat
        itemname1 = itemname

        try:
            if category == "regularpizza":
                menu=Regularpizza.objects.get(itemname = itemname1)
            elif category == "sicilianpizza":
                menu=Sicilianpizza.objects.get(itemname = itemname1)
            elif category == "subs":
                menu=Subs.objects.get(itemname = itemname1)
            elif category == "pasta":
                menu=Pasta.objects.get(itemname = itemname1)
            elif category == "salad":
                menu=Salad.objects.get(itemname = itemname1)
            elif category == "dinnerplatter":
                menu=Dinnerplatter.objects.get(itemname = itemname1)
            #print(menu)
        except:
            context = {
                'message':'You messed up',
            }
            return render(request, 'orders/error.html', context)
        
        mitn = itemname
        scost = 0
        sname = ""
        if menu.sizeEnable == True:
            sizeSel = request.POST["size"]
            if sizeSel == "large":
                sname = ' Large'
                scost = menu.largecost
            else:
                sname=" Small"
                scost = menu.smallcost
        else:
            scost = menu.smallcost

        mitn = mitn + sname
        #print(scost)

        ecost = 0
        if menu.extrasEnable == True:
            eid = request.POST['extras']
            #print(eid)
            if eid != 'none':
                tempe = Extra.objects.get(itemname=eid)
                ecost = tempe.smallcost
        
        ### make a menuitem

        newMenuItem = Menuitem.objects.create(itemname=mitn, cat = category, cost = scost + ecost)
        print(newMenuItem.cost)

        # get the topping if toppings were enabled
        for i in range(menu.ntoppings):
            temp1 = "top" + str(i+1)
            pid = request.POST[temp1]
            ### add toppings to the database here only
            temptop = Topping.objects.get(toppingname = pid)
            newMenuItem.toppings.add(temptop)

        # get the extras if extras were enabled
        ecost = 0
        if menu.extrasEnable == True:   
            eid = request.POST['extras']
            if eid != 'none':
                tempe = Extra.objects.get(itemname=eid)
                newMenuItem.extras.add(tempe)

        newMenuItem.cost = scost + ecost
        idm = newMenuItem.id

        # put menuitem into orders with a status of in cart
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        today = date.today()

        #get orders which are in cart 
        try:
            cart = Order.objects.get(status='cart', user=request.user)
            cart.items.add(newMenuItem)
            ogcost = cart.cost
            Order.objects.filter(status='cart').update(cost = ogcost + newMenuItem.cost)
        except Order.DoesNotExist:
            cart = Order.objects.create(status = 'cart', cost = scost + ecost, time=current_time, date=today, user=request.user)
            menuitemtemp = Menuitem.objects.get(id=idm)
            cart.items.add(menuitemtemp)

        
            #add things into it
        # if no orders were there then create new


        #newOrder = Order.objects.create(status = 'cart', cost = scost + ecost, time=current_time, date=today, user=request.user)
        #newOrder.items.add(newMenuItem)
        return HttpResponseRedirect(reverse("cart"))

    else:
        context = {
            'message':'you are not logged in',
        }
        return render(request, 'orders/error.html', context)


def cart(request):
    try:
        cc = Order.objects.get(status='cart', user=request.user)
        menu = cc.items.all()
        print(menu)
        context ={
            'cart': cc,
            'menu': menu,
        }
        return render(request, 'orders/cart.html', context)
    except:
        context = {
            'message':'you do not have any items in your cart',
        }
        return render(request, 'orders/error.html', context)


def place(request):
    try:
        Order.objects.filter(status='cart', user=request.user).update(status='pending')
        return HttpResponseRedirect(reverse("menu"))
    except:
        context = {
            'message':'you do not have any items in your cart or you messed up',
        }
        return render(request, 'orders/error.html', context)


def ordershow(request):
    pords = Order.objects.filter(user=request.user, status='pending').order_by('-id')
    cords = Order.objects.filter(user=request.user, status='completed').order_by('-id')
    context = {
        'pords':pords,
        'cords':cords,
    }
    return render(request, 'orders/odr.html', context)



def adminview(request):
    if request.user.is_superuser:
        pords = Order.objects.filter(status='pending').order_by('id')
        cords = Order.objects.filter(status='completed').order_by('-id')
        context = {
            'pords':pords,
            'cords':cords,
        }
        return render(request, 'orders/adminview.html', context)
    else:
        context={
            'message': "you must be an admin to see this shit"
        }
        return render(request, 'orders/error.html', context)


def complete(request, oid):
    if request.user.is_superuser:
        # check if the order exists
        try:
            cc = Order.objects.get(id=oid, status="pending")
        except:
            context={
                'message': "you must be an admin to complete an order"
            }
            return render(request, 'orders/error.html', context)
        
        Order.objects.filter(id=oid, status="pending").update(status='completed')
        return HttpResponseRedirect(reverse("adminview"))
    else:
        context={
            'message': "you must be an admin to see this shit"
        }
        return render(request, 'orders/error.html', context)






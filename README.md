# Project 3

Web Programming with Python and JavaScript


### Getting Started
This is a website for ordering pizzas from Pinnochio's Pizza and Subs where customers can sign in/up, customize their order, add it to cart, check out from cart and see all the past orders with their status. 

Also the admins aka superusers can modify the menu like changing whether extra's are allowed, what are the number of toppings, cost of the items, etc. Plus the personal touch is that admins can change the status of pending orders to completed and the users can also see the status of their orders. 


## **Files modified**
## Backend
these are the order app filess
### views.py
- This file handles all the post queries, getting data from the database, redering templates, etc.
### models.py
- This file has all tables, its attributes, relations with other tables, etc. Basically all things related to the database
### urls.py
- This file handles all the paths for the app orders.
### admin.py
    connects database models to Django Admin, where admins can login to modify the database.
## Temlpates
### layout.html
- basic layout for all the file which contains a navbar, a footer and modal forms for login and sign up
### index.html
- this is the home page
### menu.html
- this has all the items of the menu displayed with their prices and a customize button
### cusmtomize.html
- here the user can select the size of the item, toppings and extras w.r.t. to the item.
- as the user customizes the price is also changed accordingly
### cart.html
- only authenticated user can view this page
- here they can all the items in cart and the cart total
- here user can place a order which will contain all the items in the cart
### odr.html
- this displays all orders the has placed and classifies them according to the order status
- all the details about the order like the time places and all are there
### adminview.html
- this is only there for superusers
- they can see all the pending and completed orders the store has
- also they can complete the pending orders here.
### error.html
- displays all the error messages
## Static
- this folder contains all the images the website uses
### style.css 
- has all the styling apllied to the templates
### main.js and main2.js
- these two contains all the javascripts used by this application.
- handles the login/signup modal view and its button when the user is logged in and many more thing are in it.


## Personal touch
In personal touch admins (superuser) can change the status of pending orders to completed and the users can also see the status of their orders. 



### **Licensing: &copy; Tanish Surana**




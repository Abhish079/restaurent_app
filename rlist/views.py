from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from rlist.models import Entry
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def homepage(request):
    return render(request, "homepage.html")


def SignupPage(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")

        if User.objects.filter(username=uname):
            return HttpResponse(
                "Username already exist! Please try some other username."
            )

        if User.objects.filter(email=email):
            return HttpResponse("Email already exist! Please try some other email.")

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect("login")
    return render(request, "signup.html")


def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("pass")
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect("restaurent")
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, "login.html")


def change_password(request):
    context = {}
    if request.method == "POST":
        current = request.POST["cpwd"]
        new_pas = request.POST["npwd"]

        user = User.objects.get(id=request.user.id)
        uname = user.username
        check = user.check_password(current)
        if check == True:
            user.set_password(new_pas)
            user.save()
            context["msz"] = "Now Password has been Changed Successfully!!!"
            context["col"] = "alert-success"
            user = User.objects.get(username=uname)
            login(request, user)
        else:
            context["msz"] = "Incorrect Current Password"
            context["col"] = "alert-danger"
    return render(request, "change_password.html", context)


def forgotpassword(request):
    if request.method == "POST":
        uname= request.POST["username"]
        pwd = request.POST["npass"]

        user = get_object_or_404(User, username=uname)
        user.set_password(pwd)
        user.save()

        login(request, user)
        if user.is_superuser:
            return HttpResponse("password changed successfully!!!")
        else:
            return HttpResponseRedirect(" ")

    return render(request, "forgot_password.html" )


def LogoutPage(request):
    logout(request)
    return redirect("login")


def show(request):
    data = Entry.objects.all()
    return render(request, "restaurents.html", {"data": data})


def details(request):
    return render(request, "details.html")


def send(request):
    if request.method == "POST":
        Name = request.POST["Name"]
        Address = request.POST["Address"]
        City = request.POST["City"]
        State = request.POST["State"]
        Owner = request.POST["Owner"]
        Phone = request.POST["Phone"]
        Type = request.POST["type"]
        Date = request.POST["Date"]
        Entry(
            Name=Name,
            Address=Address,
            City=City,
            State=State,
            Owner=Owner,
            Phone=Phone,
            Type=Type,
            Date=Date,
        ).save()
        messege = "congratulations! you have registered successfully"
        return render(request, "homepage.html", {"messege": messege})

    else:
        return HttpResponse("<h1>404 ---NOT FOUND----</h1>")


def delete(request):
    Name = request.GET["Name"]
    Entry.objects.filter(Name=Name).delete()
    return HttpResponseRedirect("/")


def update(request):
    Name = request.GET["Name"]
    Address = City = State = Owner = Phone = Type = Date = "Not Available"
    for data in Entry.objects.filter(Name=Name):
        Address = data.Address
        City = data.City
        State = data.State
        Owner = data.Owner
        Phone = data.Phone
        Type = data.Type
        Date = data.Date
        return render(
            request,
            "update.html",
            {
                "Name": Name,
                "Address": Address,
                "City": City,
                "State": State,
                "Owner": Owner,
                "Phone": Phone,
                "Type": Type,
                "Date": Date,
            },
        )


def recordupdated(request):
    if request.method == "POST":
        Name = request.POST["Name"]
        Address = request.POST["Address"]
        City = request.POST["City"]
        State = request.POST["State"]
        Owner = request.POST["Owner"]
        Phone = request.POST["Phone"]
        Type = request.POST["type"]
        Date = request.POST["Date"]
        Entry.objects.filter(Name=Name).update(
            Address=Address,
            City=City,
            State=State,
            Owner=Owner,
            Phone=Phone,
            Type=Type,
            Date=Date,
        )
        return HttpResponseRedirect("/")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")

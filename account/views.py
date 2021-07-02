from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import AccountForm, AddAccountForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

class AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
            "AccountCreate":False,
            "account_form":AccountForm(),
            "add_account_form":AddAccountForm(),
        }
    
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render (request, "signup.html",context=self.params)

    def post(self, request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            account = self.params["account_form"].save()
            account.set_password(account.password)
            account.save()

            add_account = self.params["add_account_form"].save(commit=False)
            add_account.user = account

            if 'account_image' in request.FILES:
                add_account.account_image = request.FILES['account_image']

            add_account.save()

            self.params["AccountCreate"] = True

        else:
            print(self.params["account_form"].errors)

        return render(request,"signup.html",context=self.params)

def user_login(request):
    if request.method == 'POST':
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        user = authenticate(username=ID, password=Pass)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("アカウントが有効ではありません")
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    else:
        return render(request, 'login.html')

@login_required
def logout(request):
    logout(request)
    return HttpResponse("ログアウトしました")


@login_required
def index(request):
    params = {"UserID":request.user,}
    return render(request, "index.html", context=params)






# Create your views here.

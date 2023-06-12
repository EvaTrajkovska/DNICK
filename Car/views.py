from django.shortcuts import render,redirect
from .models import Fix
from .forms import FixForm
# Create your views here.


def index(request):
    return render(request, "index.html")


def repairs(request):
    if request.method == "POST":
        form_data = FixForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            fix = form_data.save(commit=False)
            fix.user = request.user
            fix.image = form_data.cleaned_data['image']
            fix.save()
            return redirect("repairs")
    qs = Fix.objects.filter(user=request.user, fix_car__manufacturer__manuf_name="Mercedes").all()
    context = {"repairs": qs, "form": FixForm}
    return render(request, "repairs.html", context)

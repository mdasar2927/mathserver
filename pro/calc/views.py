from django.shortcuts import render

def azar(request):
    result = None
    if request.method == "POST":
        try:
            I = float(request.POST.get("intensity"))
            R = float(request.POST.get("resistance"))
            result = (I ** 2) * R
        except:
            result = "Invalid input"
    return render(request, "calc/mohamed.html", {"result": result})

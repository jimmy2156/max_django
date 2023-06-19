from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthly_task = {
    "january": "Use stairs instead of elevators for a month",
    "february": "Declutter one thing from your house every day",
    "march": "Drink only water (drop all of the sugary fizzy drinks)",
    "april": "Track your habits",
    "may": "Walk for 30 minutes every day",
    "june": "Zero Eating Out",
    "july": "Track Your Spending",
    "august": "Try a No-Spend Month",
    "september": "No Retail Shopping",
    "october": "Pay In Cash Only",
    "November": "Avoid Social Media While Working",
    "december": None

}

def index(request):
    months = list(monthly_task.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })
    


def monthly_challenges(request, month):
    try: 
        monthly = monthly_task[month]
        return render(request, "challenges/challenge.html", {
            "text": monthly,
            "month_name": month.capitalize()
        })
    except:
        raise Http404()
        
    
def monthly_challenges_by_number(request, month_int):
    months = list(monthly_task.keys())
    if month_int > len(months):
      return HttpResponseNotFound("invalid month")
    redirect_month = months[month_int - 1]
    redirect_path = reverse("number_challenge", args=[redirect_path])
    return HttpResponseRedirect(redirect_path)

    

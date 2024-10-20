from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserCycleDataForm
from .models import UserCycleData

# from .models import Event # Calendar
import calendar

def calendar_view(request):
    events = Event.objects.all()
    year = request.GET.get('year', 2024) 
    month = request.GET.get('month', 10)

    # Create a calendar
    cal = calendar.monthcalendar(int(year), int(month))
    return render(request, 'calendarapp/calendar.html', {'cal': cal, 'events': events})

@login_required
def home(request):
    if request.method == 'POST':
        form = UserCycleDataForm(request.POST)
        if form.is_valid():
            cycle_data = form.save(commit=False) 
            cycle_data.user = request.user 
            cycle_data.save() 
            return redirect('/')
    else:
        previous_response = UserCycleData.objects.filter(user=request.user).last()
        form = UserCycleDataForm(instance=previous_response)

    return render(request, 'home.html', {'form': form})

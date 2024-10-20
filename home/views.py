from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserCycleDataForm
from .models import UserCycleData
from .utils import Calendar

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

class CalendarView(ListView):
    model = Event
    template_name = 'components/calendar.html'
    success_url = reverse_lazy("calendar")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context
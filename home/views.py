from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserCycleDataForm
from .models import UserCycleData
import pandas as pd
import datetime

@login_required
def home(request):
    df = pd.read_csv('./model/predicted_cycle_data.csv')

    predicted_data = {
        'user_id': df['User ID'].iloc[0],
        'last_cycle_date': df['Last Cycle Date'].iloc[0],
        'predicted_next_cycle_start': df['Predicted Next Cycle Start'].iloc[0],
    }

    user_cycle_data = UserCycleData.objects.filter(user_id=predicted_data['user_id']).last()

    if user_cycle_data:
        user_cycle_data_predicted_cycle_length = predicted_data['last_cycle_date']
        user_cycle_data_str = predicted_data['predicted_next_cycle_start']
        last_cycle = datetime.datetime.strptime(user_cycle_data_predicted_cycle_length, '%Y-%m-%d').date()
        user_cycle_data.last_cycle_date = last_cycle
        next_cycle_start_date = datetime.datetime.strptime(user_cycle_data_str, '%Y-%m-%d').date()
        user_cycle_data.predicted_next_cycle_start = next_cycle_start_date
        user_cycle_data.save()
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

    return render(request, 'home.html', {'form': form, 'user_cycle_data':user_cycle_data})

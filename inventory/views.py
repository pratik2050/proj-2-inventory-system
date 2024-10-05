from django.shortcuts import render, redirect, get_object_or_404
from .models import Monument
from .forms import MonumentForm
from django.db.models import Count

def monument_list(request):
    monuments = Monument.objects.all()
    return render(request, 'inventory/monument_list.html', {'monuments': monuments})

def monument_create(request):
    if request.method == 'POST':
        form = MonumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('monument_list')
    else:
        form = MonumentForm()
    return render(request, 'inventory/monument_form.html', {'form': form})

def monument_update(request, pk):
    monument = get_object_or_404(Monument, pk=pk)
    if request.method == 'POST':
        form = MonumentForm(request.POST, instance=monument)
        if form.is_valid():
            form.save()
            return redirect('monument_list')
    else:
        form = MonumentForm(instance=monument)
    return render(request, 'inventory/monument_form.html', {'form': form})

def monument_delete(request, pk):
    monument = get_object_or_404(Monument, pk=pk)
    if request.method == 'POST':
        monument.delete()
        return redirect('monument_list')
    return render(request, 'inventory/monument_confirm_delete.html', {'monument': monument})

# Dashboard view for analytics
def dashboard(request):
    status_counts = Monument.objects.values('status').annotate(count=Count('status'))
    return render(request, 'inventory/dashboard.html', {'status_counts': status_counts})

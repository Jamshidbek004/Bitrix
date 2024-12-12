from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from .models import Royxat, Viloyat, Aperator
from .forms import RoyxatForm  # Create this form for Royxat model


# Superuser check decorator
def is_superuser(user):
    return user.is_superuser


# List all Royxat entries grouped by status

def royxat_list(request):
    search_ism = request.GET.get('ism', '')
    search_familya = request.GET.get('familya', '')
    search_raqam = request.GET.get('raqam', '')
    search_viloyat = request.GET.get('viloyat', '')
    search_operator = request.GET.get('operator', '')
    search_royxat_vaqti = request.GET.get('royxat_vaqti', '')

    royxatga_olingan = Royxat.objects.filter(status='RO')
    tayyor = Royxat.objects.filter(status='YT')
    bekor_qilingan = Royxat.objects.filter(status='BK')

    if search_ism:
        royxatga_olingan = royxatga_olingan.filter(ism__icontains=search_ism)
        tayyor = tayyor.filter(ism__icontains=search_ism)
        bekor_qilingan = bekor_qilingan.filter(ism__icontains=search_ism)

    if search_familya:
        royxatga_olingan = royxatga_olingan.filter(familya__icontains=search_familya)
        tayyor = tayyor.filter(familya__icontains=search_familya)
        bekor_qilingan = bekor_qilingan.filter(familya__icontains=search_familya)

    if search_raqam:
        royxatga_olingan = royxatga_olingan.filter(raqam__icontains=search_raqam)
        tayyor = tayyor.filter(raqam__icontains=search_raqam)
        bekor_qilingan = bekor_qilingan.filter(raqam__icontains=search_raqam)

    if search_viloyat:
        royxatga_olingan = royxatga_olingan.filter(viloyat__icontains=search_viloyat)
        tayyor = tayyor.filter(viloyat__icontains=search_viloyat)
        bekor_qilingan = bekor_qilingan.filter(viloyat__icontains=search_viloyat)

    if search_operator:
        royxatga_olingan = royxatga_olingan.filter(operator__icontains=search_operator)
        tayyor = tayyor.filter(operator__icontains=search_operator)
        bekor_qilingan = bekor_qilingan.filter(operator__icontains=search_operator)

    if search_royxat_vaqti:
        royxatga_olingan = royxatga_olingan.filter(royxat_vaqti__icontains=search_royxat_vaqti)
        tayyor = tayyor.filter(royxat_vaqti__icontains=search_royxat_vaqti)
        bekor_qilingan = bekor_qilingan.filter(royxat_vaqti__icontains=search_royxat_vaqti)

    return render(request, 'royxta_list.html', {
        'royxatga_olingan': royxatga_olingan,
        'tayyor': tayyor,
        'bekor_qilingan': bekor_qilingan,
    })


# Create a new Royxat entry

def create_royxat(request):
    if request.method == 'POST':
        form = RoyxatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('royxat_list'))
    else:
        form = RoyxatForm()

    return render(request, 'royxta_form.html', {'form': form})


# Update an existing Royxat entry (Superuser only)
@user_passes_test(is_superuser)
def update_royxat(request, pk):
    royxat = get_object_or_404(Royxat, pk=pk)

    if request.method == 'POST':
        # Update status and sharx fields
        royxat.status = request.POST.get('status', royxat.status)
        royxat.sharx = request.POST.get('sharx', royxat.sharx)
        royxat.save()
        return redirect('royxat_list')

    return render(request, 'update_royxat.html', {'royxat': royxat})


def filter_royxat_by_status(request, status):
    valid_statuses = dict(Royxat.STATUS_CHOICES)  # Convert STATUS_CHOICES to a dictionary
    if status not in valid_statuses:
        return render(request, '404.html', status=404)  # Show 404 page if status is invalid

    filtered_royxat = Royxat.objects.filter(status=status)
    return render(
        request,
        'filtered_royxat_list.html',
        {'filtered_royxat': filtered_royxat, 'status_display': valid_statuses[status]}
    )

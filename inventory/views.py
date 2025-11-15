from django.shortcuts import render, redirect, get_object_or_404
from .models import Material, StockEntry, Category

def dashboard(request):
    materials = Material.objects.select_related('category').all()
    return render(request, 'inventory/dashboard.html', {'materials': materials})

def stock_entry(request):
    if request.method == "POST":
        material_id = request.POST.get('material')
        qty = float(request.POST.get('qty', '0') or 0)
        typ = request.POST.get('type')

        material = get_object_or_404(Material, id=material_id)

        if typ == "IN":
            material.total_stock += qty
        else:
            material.total_stock -= qty

        material.save()

        StockEntry.objects.create(
            material=material,
            quantity=qty,
            type=typ
        )
        return redirect('dashboard')

    return render(request, 'inventory/stock_entry.html', {
        'materials': Material.objects.all(),
        'categories': Category.objects.all()
    })

def stock_report(request):
    entries = StockEntry.objects.select_related('material').order_by('-date')[:500]
    totals = Material.objects.values('id','name','unit','total_stock')
    return render(request, 'inventory/report.html', {'entries': entries, 'totals': totals})

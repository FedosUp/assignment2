from django.shortcuts import render
from airplanes.models import Vehicle
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import airplanes.models

def index(request):


    # return render(request, 'index.html', {})
    vehicles = Vehicle.objects.all()
    print('start index')
    context = {
        'vehicles': vehicles
    }
    p = Paginator(vehicles, 15)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    # sending the page object to index.html
    return render(request, 'index.html', context=context)

def vehicle_detail(request, pk):
    vehicle = (Vehicle.objects.get(pk=pk))
    try:

        context = {
            'vehicle': vehicle
        }
        return render(request, template_name='vehicle_detail.html', context=context)
    except Exception as err:
        print(f"Ошибка1 {err}, {type(err)}")
        return None
    except airplanes.models.Vehicle.DoesNotExist as err:
        print(f"Ошибка2 {err}, {type(err)}")
        return None
    except Exception as err:
        print(f"Ошибка3 {err}, {type(err)}")
        return None

'Функция поиска по самолета по icao24'
def vehicle_find_icao24(request):

    print('start find')
    query = request.GET.get('icao24')
    print(query)
    try:
        vehicle = (Vehicle.objects.get(icao24=query))
        context = {
            'vehicle': vehicle
        }
        return render(request, template_name='vehicle_detail.html', context=context)
    except Exception as err:
        print(f"Ошибка {err}, {type(err)}")
        return render(request, template_name='nothingfound.html', context={})

def vehicle_find_origin_country(request):
    print('start find country')
    query = request.GET.get('origin_country')
    print(query)

    vehicles = (Vehicle.objects.filter(origin_country=query))
    context = {
        'vehicles': vehicles,
        'query': query
    }
    print(context)
    # p = Paginator(vehicles, 30)  # creating a paginator object
    # # getting the desired page number from url
    # page_number = request.GET.get('page')
    # try:
    #     page_obj = p.get_page(page_number)  # returns the desired page object
    # except PageNotAnInteger:
    #     # if page_number is not an integer then assign the first page
    #     page_obj = p.page(1)
    # except EmptyPage:
    #     # if page is empty then return last page
    #     page_obj = p.page(p.num_pages)
    # context = {'page_obj': page_obj}
    # # sending the page object to index.html
    return render(request, 'findbycountry.html', context=context)



# def index(request):
#     posts = Post.objects.all()  # fetching all post objects from database
#     p = Paginator(posts, 5)  # creating a paginator object
#     # getting the desired page number from url
#     page_number = request.GET.get('page')
#     try:
#         page_obj = p.get_page(page_number)  # returns the desired page object
#     except PageNotAnInteger:
#         # if page_number is not an integer then assign the first page
#         page_obj = p.page(1)
#     except EmptyPage:
#         # if page is empty then return last page
#         page_obj = p.page(p.num_pages)
#     context = {'page_obj': page_obj}
#     # sending the page object to index.html
#     return render(request, 'index.html', context)

# def vehicle_find_icao24(request):
#
#     return render(request, template_name='find.html')

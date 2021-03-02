import json

from django.shortcuts import render
from django.views     import View
from django.http      import JsonResponse

from .models import Drink, Category, Menu


class CategoryView(View):
    def get(self, request):
        # drinks has a list of QuerySet Objects, It should be converted to dict() type.
        categories    = Category.objects.all()
        category_list = list()

        for category in categories:
            category_dict = dict(name=category.name)
            category_list.append(category_dict)
        
        return JsonResponse(category_list, status=200, safe=False)

    def post(self, request):
        # create a row in a name column in Allergy Table
        data      = request.body
        json_data = json.loads(data)

        name      = json_data['name']
        menu      = json_data['menu']

        menu_id = Menu.objects.get(name=menu)
        Category.objects.create(name=name, menu=menu_id)
        return JsonResponse({'message': 'SUCCESS'}, status=201)


class DrinkView(View):
    def get(self, request):
        drinks     = Drink.objects.all()
        drink_list = list()

        for drink in drinks:
            drink_dict = dict(korean_name =drink.korean_name,
                              english_name=drink.english_name,
                              description =drink.description)
            drink_list.append(drink_dict)
        
        return JsonResponse(drink_list, status=200, safe=False)
    
    def post(self, request):
        data      = request.body
        json_data = json.loads(data)

        korean_name  = json_data['korean_name']
        english_name = json_data['english_name']
        description  = json_data['description']
        category     = json_data['category']

        # get QueryString object from categories table
        category_id = Category.objects.get(name=category)

        Drink.objects.create(korean_name =korean_name,
                             english_name=english_name,
                             description =description,
                             category    =category_id)

        return JsonResponse({'message': 'SUCCESS'}, status=201)

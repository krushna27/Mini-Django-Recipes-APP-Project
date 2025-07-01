# from django.shortcuts import render, redirect
# from .models import *
# # Create your views here.
# def receips(request):
#     if request.method == "POST":
#         data = request.POST
#         recipe_img = request.FILES.get('recipe_img')
#         recipe_name = data.get('recipe_name')
#         recipe_desc = data.get('recipe_desc')

#         Recipe.objects.create(
#         recipe_img= recipe_img,
#         recipe_name = recipe_name,
#         recipe_desc= recipe_desc,
#         )
#         print(recipe_desc)

        
#         return redirect('/receips/')
#     print("Recipe Name:", recipe_name)
# # 
#     queryset = Recipe.objects.all()
#     context = {'receipes':queryset}
#     return render(request, 'receips.html', context)





from django.shortcuts import render, redirect
from .models import *

def receips(request):
    if request.method == "POST":
        data = request.POST
        recipe_img = request.FILES.get('recipe_img')
        recipe_name = data.get('recipe_name')
        recipe_desc = data.get('recipe_desc')

        Recipe.objects.create(
            recipe_img=recipe_img,
            recipe_name=recipe_name,
            recipe_desc=recipe_desc,
        )
        print("Recipe Name:", recipe_name)
        print("Recipe Desc:", recipe_desc)
        return redirect('/receips/')

    queryset = Recipe.objects.all()


    if request.GET.get('search'):
        search_query = request.GET.get('search')
        queryset = queryset.filter(recipe_name__icontains=search_query)

  
    context = {'receipes': queryset}
    return render(request, 'ui.html', context)


def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        recipe_img = request.FILES.get('recipe_img')
        recipe_name = data.get('recipe_name')
        recipe_desc = data.get('recipe_desc')

        queryset.recipe_name = recipe_name
        queryset.recipe_desc = recipe_desc
        if recipe_img:
            queryset.recipe_img = recipe_img
        queryset.save()
        return redirect('/receips/')

    context = {'receipe': queryset}
    return render(request, 'update_recipe.html', context)



def delete_recipe(request,id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receips/')
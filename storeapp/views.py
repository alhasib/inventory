from django.shortcuts import render, HttpResponse

# Create your views here.
from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import *
from .models import *

# Create your views here.

def create_user(request):
    if request.method == "POST":
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            p = form.cleaned_data.get('permission')
            # print(p)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            u = User.objects.create_user(username = username, password=password)
            u.user_permissions.set(p)
            
            return HttpResponse("Done")
    else:
        form = UserForm()
    context = {'form':form}
    return render(request, 'create_user.html', context)


def caregory_wise_product(request, name):
    try:
        category = Category.objects.get(name = name)
        if category:
            sub_category_count = category.subcategory_set.all().count()
            if sub_category_count > 0:
                print(1)
                sub_category = SubCategory.objects.filter(category = category)
                print(2)
                context = {'sub_category':sub_category}
                print(3)
                print(context)
                return render(request, 'category_wise_product.html', context)

            else:
                try:
                    product = Item.objects.filter(category = category)
                    if product:
                        context = {'product':product}
                        print(context)
                        return render(request, 'category_wise_product.html', context)
                    else:
                        #done
                        print("ace")
                        context = {'message':"No Product Or Sub Category Is Available To Show"}
                        print(3)
                        print(context)
                        return render(request, 'category_wise_product.html', context)
                except:
                    print("ac")
                    context = {'message':"No Product Or Sub Category Is Available To Show"}
                    print(3)
                    print(context)
                    return render(request, 'category_wise_product.html', context)
    
        else:
            context = {'message':"No Item Is Available To Show"}
            print(3)
            print(context)
            return render(request, 'category_wise_product.html', context)
    
    except:
        print("jaki")
        try:
            s_category = SubCategory.objects.get(name = name)
            if s_category:
                product = Item.objects.filter(sub_category = s_category)
                if product:
                    context = {'product':product}
                    print(context)
                    return render(request, 'category_wise_product.html', context)
                else:
                    #done
                    context = {'message':"No Product Is Available To Show"}
                    print(context)
                    return render(request, 'category_wise_product.html', context)
            else:
                print('gt')
                context = {'message':"No Product Is Available To Show"}
                print(3)
                print(context)
                return render(request, 'category_wise_product.html', context)

        except:
            #done
            context = {'message':"No Product Or Sub Category Is Available To Show"}
            
            return render(request, 'category_wise_product.html', context)



def proposal(request):
    print("proposal")
    try:
        proposals = ProposeItem.objects.filter(checked_in_status = False)
        print("proposal1")
        if proposals:
            
            context = {'proposals':proposals}
            return render(request, 'proposals.html', context)
        else:
            message = "No Proposal Is Available Now"
            context = {'message':message}
            return render(request, 'proposals.html', context)
    except:
        print("proposal2")
        message = "No Proposal Is Available Now"
        context = {'message':message}
        return render(request, 'proposals.html', context)

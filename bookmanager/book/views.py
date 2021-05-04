from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest
from django.http import HttpResponse


# hope consumer input 172.0.0.1:8000/index/
# to visit views
def index(request):
    # return HttpResponse('OK!')

    # 模拟数据查询
    context = {
        'name': 'Double eleven now，Click to have surprise!'
    }

    return render(request, 'book/index.html', context=context)

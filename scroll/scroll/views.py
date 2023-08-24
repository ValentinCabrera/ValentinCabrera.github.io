from django.shortcuts import render
from django.http import HttpResponse
from pyautogui import scroll
from time import sleep

def main_view(request):
    if request.method == 'POST':
        distance = 7
        pause = 0.0001

        if (request.POST.get("down")) == '':
            for i in range(distance):
                scroll(-1, _pause=False)
                sleep(pause)

        elif (request.POST.get("up")) == '':
              for i in range(distance):
                scroll(1, _pause=False)
                sleep(pause)

    return render(request, 'main.html')

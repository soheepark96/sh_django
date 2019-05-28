from django.shortcuts import render

# Create your views here.
def main(request):
    text = '결과보기'
    context = {'text':text}
    # text="멋사만세"
    # text2="만세만세"
    # text3="멋사7기"
    # furit=['사과', '배', '감', '귤']
    # context={'text':text,'text2':text2,'text3':text3, 'furit':furit}
    # return render(request,'secondapps/index.html',context)
    return render(request, 'secondapps/index.html', context)

def result(request):
    text = request.GET.get('text')
    wordcnt = {}
    words = []
    if text is not None:
        words = text.split(' ') #이 부분에서 따옴표 사이에 space 넣기
        for i in words:
            if i in wordcnt:
                wordcnt[i] = wordcnt[i]+1
            else:
                wordcnt[i] = 1
    # 이거를 context에 담아서 위의 for문을 html에서 처리한다.
    context = {'text':text, 'words':words, 'wordcnt_item':wordcnt.items()}
    return render(request, 'secondapps/index.html', context)

def menu(request):
    text = "menu입니다."
    context = {'text':text}
    return render(request, "secondapps/menu.html")

def about(request): 
    return render(request, "secondapps/about.html")
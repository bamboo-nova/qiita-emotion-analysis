from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import MeCab

# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def test(request):
    now = datetime.now()
    mecab=MeCab.Tagger()
    mecab.parse("")

    line = '東京特許許可局でサラダとトマトソースのパスタを食べた。'
    node = mecab.parseToNode(line)
    output = []
    while node:
        hinshi = node.feature.split(",")[0]
        if hinshi == '形容詞' or hinshi == '名詞' or hinshi == '副詞' and node.surface not in stopwords or (len(node.feature.split(",")[6])>1):
            output.append(node.surface)
        node = node.next
    context = {
        'text': ' '.join(output),
        'time': now,
    }
    return render(request, 'tweets/test.html', context)

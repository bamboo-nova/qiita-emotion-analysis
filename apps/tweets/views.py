from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import MeCab

import ipadic
import MeCab
from mlask import MLAsk
emotion_analyzer = MLAsk(ipadic.MECAB_ARGS)

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
    result = emotion_analyzer.analyze('彼のことは嫌いではない！')
    context = {
        'text': ' '.join(output) + '\n' + '\n'.join(result['emotion'].keys()),
        'time': now,
    }
    return render(request, 'tweets/test.html', context)

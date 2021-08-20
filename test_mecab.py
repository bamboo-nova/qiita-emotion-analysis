import MeCab
mecab=MeCab.Tagger("-Owakati -d '/usr/lib/aarch64-linux-gnu/mecab/dic/mecab-ipadic-neologd'")

mecab.parse("")
line = '東京特許許可局でサラダとトマトソースのパスタを食べた。'
node = mecab.parseToNode(line)
while node:
    hinshi = node.feature.split(",")[0]
    if hinshi == '形容詞' or hinshi == '名詞' or hinshi == '副詞' and node.surface not in stopwords or (len(node.feature.split(",")[6])>1):
        print(node.feature.split(",")[6])
    node = node.next

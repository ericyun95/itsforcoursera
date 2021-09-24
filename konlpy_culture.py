import konlpy
from konlpy.tag import Okt
from konlpy.utils import pprint
okt = Okt()
text = []
stopwords = ['영화', '보고','하는', '같다', '였다', '않는다', '되는','입니다','있다','볼때','또한','진짜','한편','무엇','같습니다','어떻게','라면','정말','너무','대에는','봤다','이영화','있었고','나올','아니라','같아서','때문','합니다','했다','대한','무슨','계속','보니','하게','않고','']
movieorder = ['국제시장', '택시운전사', '광해', '동주', '명량', '암살', '최종병기활', '군함도', '자전차왕엄복동', '강남1970'] 
for i in movieorder:
    with open('/Users/hyunwoongyun/Downloads/{}.txt'.format(i), 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            a = line.replace('\n','')
            print(a)
            b = okt.pos(a)
            print(b)
            c = ''
            for word, pos in b:
                if pos in ['Noun', 'Adjective', 'Adverb', 'Verb']:
                    if len(word) != 1:
                        if word not in stopwords:
                            c += word
                            c += ' '
            text.append(c)
    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer(ngram_range=(1, 1))
    dt = cv.fit_transform(text)
    print(cv.get_feature_names())
    tt = (dt.T * dt)
    tt.setdiag(0)
    import pandas as pd
    names = cv.get_feature_names()
    words_text = pd.DataFrame(data = tt.toarray(), columns= names, index = names)
    words_text.to_csv('./{}.csv'.format(i), sep=',')
    text = []
line = ''
for a in text:
    line += a
textinoneline = line.split()
from collections import Counter
counter = Counter(textinoneline)
counter.most_common(20)







import konlpy
from konlpy.tag import Okt
from konlpy.utils import pprint
okt = Okt()
text = []
stopwords = ['영화', '보고','하는', '같다', '였다', '않는다', '되는','입니다','있다','볼때','또한','진짜','한편','무엇','같습니다','어떻게','라면','정말','너무','대에는','봤다','이영화','있었고','나올','아니라','같아서','때문','합니다','했다','대한','무슨','계속','보니','하게','않고','']
movieorder = ['국제시장', '택시운전사', '광해', '동주', '명량', '암살', '최종병기활', '군함도', '자전차왕엄복동', '강남1970'] 
for i in movieorder:
    with open('/Users/hyunwoongyun/Downloads/{}.txt'.format(i), 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            a = line.replace('\n','')
            print(a)
            b = okt.pos(a)
            print(b)
            c = ''
            for word, pos in b:
                if pos in ['Noun', 'Adjective', 'Adverb', 'Verb']:
                    if len(word) != 1:
                        if word not in stopwords:
                            c += word
                            c += ' '
            text.append(c)
    line = ''
    for a in text:
        line += a
    textinoneline = line.split()
    from collections import Counter
    counter = Counter(textinoneline)
    with open("./mostwordsfrommovie.txt",'a') as w:
        w.write(i)
        for wordandcount in counter.most_common(20):
            w.write(wordandcount[0])
            w.write(',')
            w.write(str(wordandcount[1]))
            w.write('\n')
    text = []


from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer(ngram_range=(1, 1))
    dt = cv.fit_transform(text)
    print(cv.get_feature_names())
    tt = (dt.T * dt)
    tt.setdiag(0)
    import pandas as pd
    names = cv.get_feature_names()
    words_text = pd.DataFrame(data = tt.toarray(), columns= names, index = names)
    words_text.to_csv('./{}.csv'.format(i), sep=',')
    text = []
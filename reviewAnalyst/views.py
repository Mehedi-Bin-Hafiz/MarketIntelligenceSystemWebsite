from django.shortcuts import render
import joblib
from nltk.stem.porter import PorterStemmer

porter = PorterStemmer()
def tokenizer_porter(text):
     return [porter.stem(word) for word in text.split()]

def PunctuationRemover(my_str):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = " "
    for char in my_str:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct


def review_input(request):
    return render(request,'reviewInput.html')
def review_result(request):
    myinput = request.GET['Review']
    print(myinput)
    myinputclean = PunctuationRemover(myinput)

    check2 = [w for w in tokenizer_porter(myinputclean)]
    withoutstopword = ' '.join(check2)

    # print(ManipulatedPosts)
    from sklearn.feature_extraction.text import TfidfVectorizer
    tfidf = TfidfVectorizer(strip_accents=None,
                            lowercase=False,
                            preprocessor=None,
                            tokenizer=tokenizer_porter,
                            use_idf=True,
                            norm='l2',
                            smooth_idf=True)

    predictable = tfidf.fit_transform(withoutstopword)  # we can not use fit_transform here
    # print(predictable)

    clf = joblib.load('ProductModel.sav')
    result = clf.predict(predictable)
    pred = result[0]
    print('\nPrediction: ')
    if pred == 0:
        conv='It is positive Review'
    elif pred == 1:
       conv='It is Negative Review'
    else:
        pass

    context = {
        'result': conv
    }
    return  render(request, 'reviewResult.html',context)
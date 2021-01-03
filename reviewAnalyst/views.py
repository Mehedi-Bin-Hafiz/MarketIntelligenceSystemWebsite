from django.shortcuts import render,HttpResponse
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
    import joblib
    myinput = request.GET['Review']
    myinputclean = PunctuationRemover(myinput)
    check2 = [w for w in tokenizer_porter(myinputclean)]
    withoutstopword = ' '.join(check2)
    predictionlist = []
    tfidf = joblib.load('tfidf.sav')
    predictable = tfidf.transform([withoutstopword])
    Logistic = joblib.load('ProductModel.sav')
    pred = Logistic.predict(predictable)
    predictionlist.append(pred[0])
    totallen = len(predictionlist)
    zero = predictionlist.count(0)
    one = predictionlist.count(1)
    posReview = "Positive review {:.2f}%".format((zero * 100) / totallen, )
    negReview = "Negative review {:.2f}%".format((one * 100) / totallen, )

    context = {

        "posReview": posReview,
        "negReview": negReview

    }

    return render(request, 'priceResult.html',context)




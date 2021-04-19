from django.shortcuts import render
from django.shortcuts import render
from .offersControl import imageUploadTODB, createOffer, getOffers


def addoffer(request):

    print("in add offer")

    offerInfos = getOffers()
    if offerInfos is None:
        lastofferId = 0
    else:
        lastofferId = offerInfos[0]['offerId']
    if request.method == "POST":

        offerId = int(lastofferId) + 1

        print("offerId", offerId)

        url = imageUploadTODB(request.FILES)

        offerInfo = {
            'offerId' : offerId,
            'url': url,
        }
        createOffer(offerInfo)
    return render(request, "Offers/addoffer.html")

# Create your views here.

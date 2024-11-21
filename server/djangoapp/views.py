#from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate
from .models import CarMake, CarModel
from .restapis import get_request, analyze_review_sentiments, post_review

# Get an instance of a logger
logger = logging.getLogger(__name__)


@csrf_exempt
def login_user(request):
    """Handle user login."""
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to authenticate the user
    user = authenticate(username=username, password=password)
    response_data = {"userName": username}
    
    if user is not None:
        # If user is valid, log in and send status as authenticated
        login(request, user)
        response_data["status"] = "Authenticated"
    
    return JsonResponse(response_data)


# Create a `logout_request` view to handle sign-out request
def logout_request(request):
    """Handle user logout."""
    logout(request)
    return JsonResponse({"userName": ""})


# Create a `registration` view to handle sign-up request
@csrf_exempt
def registration(request):
    """Handle user registration."""
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    
    username_exist = False
    
    # Check if user already exists
    try:
        User.objects.get(username=username)
        username_exist = True
    except User.DoesNotExist:
        logger.debug(f"{username} is a new user.")
    
    if not username_exist:
        # Create user if new
        user = User.objects.create_user(username=username, first_name=first_name,
                                        last_name=last_name, password=password,
                                        email=email)
        login(request, user)
        return JsonResponse({"userName": username, "status": "Authenticated"})
    else:
        return JsonResponse({"userName": username, "error": "Already Registered"})


def get_cars(request):
    """Fetch car models and makes."""
    count = CarMake.objects.filter().count()
    
    if count == 0:
        initiate()
    
    car_models = CarModel.objects.select_related('car_make')
    cars = [{"CarModel": car_model.name, "CarMake": car_model.car_make.name}
            for car_model in car_models]
    
    return JsonResponse({"CarModels": cars})


def get_dealerships(request, state="All"):
    """Fetch dealerships."""
    endpoint = f"/fetchDealers/{state}" if state != "All" else "/fetchDealers"
    
    dealerships = get_request(endpoint)
    logger.debug(f"Dealerships data received: {dealerships}")
    
    if not dealerships:
        logger.error("No dealerships found or data fetch error occurred.")
    
    return JsonResponse({"status": 200, "dealers": dealerships})


def get_dealer_details(request, dealer_id):
    """Fetch dealer details by ID."""
    if dealer_id:
        endpoint = f"/fetchDealer/{dealer_id}"
        dealership = get_request(endpoint)
        return JsonResponse({"status": 200, "dealer": dealership})
    else:
        return JsonResponse({"status": 400, "message": "Bad Request"})


def get_dealer_reviews(request, dealer_id):
    """Fetch reviews of a dealer."""
    if dealer_id:
        endpoint = f"/fetchReviews/dealer/{dealer_id}"
        reviews = get_request(endpoint)
        
        for review in reviews:
            sentiment = analyze_review_sentiments(review['review'])
            review['sentiment'] = sentiment['sentiment']
        
        return JsonResponse({"status": 200, "reviews": reviews})
    else:
        return JsonResponse({"status": 400, "message": "Bad Request"})


def add_review(request):
    """Submit a review."""
    if request.user.is_authenticated:
        data = json.loads(request.body)
        try:
            post_review(data)
            return JsonResponse({"status": 200})
        except Exception as e:
            logger.error(f"Error in posting review: {e}")
            return JsonResponse({"status": 401, "message": "Error in posting review"})
    else:
        return JsonResponse({"status": 403, "message": "Unauthorized"})

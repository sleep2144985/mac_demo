from django.shortcuts import render
import json
import random
# Create your views here.
def get_image(request):
    sample_data = json.load(open("sample.json", "r")) 
    image_id = sample_data['question'][random.randint(0,500)]['imageId']
    
from flask import Flask, request, render_template
import json
from pymongo import MongoClient
from bson import ObjectId
import requests

app = Flask(__name__)

client = MongoClient("mongodb+srv://suminkim:miknimus@honey-irl-ywt1c.mongodb.net/test?retryWrites=true&w=majority")
honey_db = client['honey_db']

api_key = 'MBjxxSsO'


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/coupons/<coupon_id>", methods=["POST"])
def favoriteCoupon(coupon_id):
    return coupon_id

@app.route('/coupons', methods=['GET'])
def coupons():
    results = get_coupons(22101)
    return render_template("coupons.html", coupons=results)


def get_coupons(zip_code):
    url = 'https://api.discountapi.com/v2/deals?location=' + str(zip_code) + '&api_key=' + api_key
    return requests.get(url).json()['deals']

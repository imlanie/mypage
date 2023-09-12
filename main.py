import os
import awsgi
import requests
from flask import Flask, flash, jsonify, make_response, request, redirect, render_template, render_template_string, session, url_for
from flask_paranoid import Paranoid
import json
import boto3
import datetime
from datetime import timedelta, datetime

app = Flask(__name__)


@ app.route('/index', methods=['POST', 'GET'])
def index():

    return_msg = "You have been logged out.."
    options = 'return to home'
    return render_template("index.html")


def main(event, context):

    print("Lambda Flask Website Event: ")
    print(event)
    # print("requestContext:  " + event['requestContext'])

    return awsgi.response(app, event, context)

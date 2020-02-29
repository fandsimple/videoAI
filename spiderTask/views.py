#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import pdb
import hashlib
import requests
import json

from django.urls import reverse



def index(request):
    return HttpResponse('fanding')



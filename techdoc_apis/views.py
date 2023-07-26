from django.shortcuts import render
import requests
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.
JSON_SERVICE_URL = "https://webservice.tecalliance.services/pegasus-3-0/services/TecdocToCatDLB.jsonEndpoint"
TECDOC_MANDATOR = 23479 

def http_json_request(service_url, json_param):
    # Create a new HTTP request to call the given service URL
    headers = {
    'authority': 'webservice.tecalliance.services',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,de;q=0.8,hi;q=0.7,nl;q=0.6',
    'content-type': 'application/json',
    'origin': 'https://web.tecalliance.net',
    'referer': 'https://web.tecalliance.net/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'x-api-key': '2BeBXg6LNe9gMds4MBLduudVkbwBTb8ES5sPyiP13DG1rVSMJNHZ',
    }

    response = requests.post(service_url, data=json_param, headers=headers)

    # Read the response content
    return response.text


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def find_manufactures(request, *args, **kwargs):
    operation_name = "getManufacturers2"
    
    # Using a dictionary to generate the request payload
    parameters = {
        operation_name: {
            "country": "KE",
            "lang": "en",
            "countryGroupFlag":False,
            "favouredList":2,
            "provider": TECDOC_MANDATOR,
            "linkingTargetType": "P"
        }
    }
    
    # Serialize the dictionary as JSON
    json_param = json.dumps(parameters)
    
    # Perform a JSON-Web request
    result = http_json_request(JSON_SERVICE_URL, json_param)
    result_dict = json.loads(result)
    return Response(result_dict)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def find_model(request, *args, **kwargs):
    mfid = request.GET.get('mfid')
    operation_name = "getLinkageTargets"
    if mfid !=None:
        # Using a dictionary to generate the request payload
        parameters = {
        operation_name: {
            "filterMode":"all",
            "includeAllFacets":False,
            "includeVehicleModelSeriesFacets":True,
            "linkageTargetCountry": "KE",
            "lang": "en",
            "linkageTargetCountryGroupFlag": False,
            "favouredList": 2,
            "provider": TECDOC_MANDATOR,
            "linkageTargetType": "P",
            "perPage":1,
            "mfrIds":[mfid]  # manufatcure id variable
        }
    }
        
        # Serialize the dictionary as JSON
        json_param = json.dumps(parameters)
        
        # Perform a JSON-Web request
        result = http_json_request(JSON_SERVICE_URL, json_param)
        result_dict = json.loads(result)
        return Response(result_dict)
    return Response({'error':'manufacture id not found'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def find_type(request, *args, **kwargs):
    mfid = request.GET.get('mfid')  
    modelseriesid = request.GET.get('modelseriesid')

    if (mfid !=None) and (modelseriesid != None):

        operation_name = "getLinkageTargets"

        # Using a dictionary to generate the request payload
        parameters = {
            operation_name: {
                "linkageTargetCountry": "KE",
                "lang": "en",
                "linkageTargetCountryGroupFlag": False,
                "provider": TECDOC_MANDATOR,
                "linkageTargetType": "P",
                "page":1,
                "perPage": 100,
                "mfrIds": [mfid],  # manufatcure id variable
                "vehicleModelSeriesIds":[modelseriesid],
                "sort":[
                    {"field": "mfrName", "direction": "asc"},
                    {"field": "description", "direction": "asc"}
                ]

            }
        }
        
        # Serialize the dictionary as JSON
        json_param = json.dumps(parameters)
        
        # Perform a JSON-Web request
        result = http_json_request(JSON_SERVICE_URL, json_param)
        result_dict = json.loads(result)
        return Response(result_dict)
    return Response({'error':'manufacture id and model id not found'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def find_sidebar(request, *args, **kwargs):
    linkageTargetIds = request.GET.get('linkageTargetIds')

    if linkageTargetIds !=None:
        operation_name = "getLinkageTargets"

        # Using a dictionary to generate the request payload
        parameters = {
            operation_name: {
                "linkageTargetCountry": "KE",
                "lang": "en",
                "linkageTargetCountryGroupFlag": False,
                "provider": TECDOC_MANDATOR,
                "page": 1,
                "perPage": 100,
                "linkageTargetIds":{"type": "P", "id": linkageTargetIds}  #3822 is  Type Id

            }
        }
        
        # Serialize the dictionary as JSON
        json_param = json.dumps(parameters)
        
        # Perform a JSON-Web request
        result = http_json_request(JSON_SERVICE_URL, json_param)
        result_dict = json.loads(result)
        return Response(result_dict)
    return Response({'error':'linkageTarget id not found'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def find_categories_subcategories(request, *args, **kwargs):
    linkageTargetIds = request.GET.get('linkageTargetIds')
    print(linkageTargetIds)
    if linkageTargetIds !=None:


        operation_name = "getArticles"

        # Using a dictionary to generate the request payload
        parameters = {
            operation_name: {
                "articleCountry": "KE",
                "assemblyGroupFacetOptions": {"enabled": True,"assemblyGroupType": "P","includeCompleteTree": True},
                "dataSupplierIds": [],
                "filterQueries": ["(dataSupplierId NOT IN (4978,4982))"],
                "includeDataSupplierFacets": True,
                "includeGenericArticleFacets":True,
                "lang": "en",
                "linkageTargetId":linkageTargetIds,
                "linkageTargetType":"P",
                "provider": TECDOC_MANDATOR,
                "perPage": 0,


            }
        }
        
        # Serialize the dictionary as JSON
        json_param1 = json.dumps(parameters)
        
        # Perform a JSON-Web request
        result = http_json_request(JSON_SERVICE_URL, json_param1)

        only_categories = []
        for loop in json.loads(result)['assemblyGroupFacets']['counts']:
            try:
                parent_node = loop['parentNodeId']
            except:
                only_categories.append(loop)
        for loop_only_cat in only_categories:
            loop_only_cat['children'] = []
            for loop1 in json.loads(result)['assemblyGroupFacets']['counts']:
                try:
                    if loop1['parentNodeId'] == loop_only_cat['assemblyGroupNodeId']:
                        loop_only_cat['children'].append(loop1)
                        pass
                except:
                    pass

        return Response(only_categories)
    return Response({'error':'linkageTarget id not found'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def find_subcategories_subcategories(request, *args, **kwargs):
    selected_subcategory = request.GET.get('selected_subcategory')
    linkageTargetIds = request.GET.get('linkageTargetIds')
    if (linkageTargetIds !=None) and  (selected_subcategory!=None):
        # selected_subcategory = 101340
        operation_name = "getArticles"

        # Using a dictionary to generate the request payload
        parameters = {
            operation_name: {
                "articleCountry": "KE",
                "assemblyGroupFacetOptions": {"enabled": True,"assemblyGroupType": "P","includeCompleteTree": True},
                "dataSupplierIds": [],
                "filterQueries": ["(dataSupplierId NOT IN (4978,4982))"],
                "includeDataSupplierFacets": True,
                "includeGenericArticleFacets":True,
                "lang": "en",
                "linkageTargetId":linkageTargetIds,
                "linkageTargetType":"P",
                "provider": TECDOC_MANDATOR,
                "perPage": 0,

            }
        }

        # Serialize the dictionary as JSON
        json_param1 = json.dumps(parameters)

        # Perform a JSON-Web request
        result = http_json_request(JSON_SERVICE_URL, json_param1)
        child_sub = []
        for loo3 in json.loads(result)['assemblyGroupFacets']['counts']:
            try:
                if loo3['parentNodeId'] == int(selected_subcategory):
                    child_sub.append(loo3)
            except:
                pass
        return Response(child_sub)
    return Response({'error':'linkageTarget selected_subcategory id not found'})





    
@api_view(['GET'])    
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def find_articles_from_categories(request,*args,**kwargs):
    linkageTargetIds = request.GET.get('linkageTargetIds')
    assemblyGroupNodeIds = request.GET.get('assemblyGroupNodeIds')

    if (linkageTargetIds !=None) and (assemblyGroupNodeIds!=None):
        operation_name = "getArticles"
    #
    # # Using a dictionary to generate the request payload
        parameters = {
            operation_name: {
                "articleCountry": "KE",
                "assemblyGroupFacetOptions": {"enabled": True},
                "dataSupplierIds": [],
                "filterQueries": ["(dataSupplierId NOT IN (4978,4982))"],
                "lang": "en",
                "linkingTargetId": str(linkageTargetIds),
                "linkingTargetType": "P",
                "provider": TECDOC_MANDATOR,
                'assemblyGroupNodeIds':str(assemblyGroupNodeIds),
                'page': 1,
                'perPage': 100,
                'sort': [
                    {
                        'field': 'mfrName',
                        'direction': 'asc',
                    },
                    {
                        'field': 'linkageSortNum',
                        'direction': 'asc',
                    },
                    {
                        'field': 'score',
                        'direction': 'desc',
                    },
                ],
                'genericArticleIds': [],
                'includeAll': False,
                'includeLinkages': True,
                'linkagesPerPage': 100,
                'includeGenericArticles': True,
                'includeArticleCriteria': True,
                'includeMisc': True,
                'includeImages': True,
                'includePDFs': True,
                'includeLinks': True,
                'includeArticleText': True,
                'includeOEMNumbers': True,
                'includeReplacedByArticles': True,
                'includeReplacesArticles': True,
                'includeComparableNumbers': True,
                'includeGTINs': True,
                'includeTradeNumbers': True,
                'includePrices': False,
                'includePartsListArticles': False,
                'includeAccessoryArticles': False,
                'includeArticleLogisticsCriteria': True,
                'includeDataSupplierFacets': True,
                'includeGenericArticleFacets': True,
                'includeCriteriaFacets': False,
            }
        }
        
        json_param = json.dumps(parameters)
        result = http_json_request(JSON_SERVICE_URL, json_param)
        return Response(json.loads(result))
    return Response({'error':'linkageTarget assemblyGroupNodeIds id not found'})

@api_view(['GET'])    
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def find_article_information(request,*args,**kwargs):
    searchQuery = request.GET.get('searchquery')
    if (searchQuery!=None):
        operation_name = "getArticles"
        # # Using a dictionary to generate the request payload
        parameters = {
            operation_name: {
                'articleCountry': 'KE',
                'provider': TECDOC_MANDATOR,
                'lang': 'en',
                'searchQuery': str(searchQuery),
                'searchMatchType': 'exact',
                'searchType': 0,
                'page': 1,
                'perPage': 10,
                'includeAll':True
            }
        }
        # # Serialize the dictionary as JSON
        json_param = json.dumps(parameters)
        result = http_json_request(JSON_SERVICE_URL, json_param)  
        
        return Response(json.loads(result))
        
    else:
        return Response({'error':'linkageTarget, supplierIds, searchQuery not found'})












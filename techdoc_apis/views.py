from django.shortcuts import render
import requests
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import Eztb3105Serializer
from .models import Eztb3105
import scrapy
from django.db.models import Q
import re
import copy
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
# @permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def find_manufactures(request, *args, **kwargs):
    try:
        operation_name = "getManufacturers2"
        
        # Using a dictionary to generate the request payload
        parameters = {
            operation_name: {
                "country": "KE",
                "lang": "en",
                "countryGroupFlag":False,
                "favouredList":2,
                "provider": TECDOC_MANDATOR,
                "linkingTargetType": "V"
            }
        }
        
        # Serialize the dictionary as JSON
        json_param = json.dumps(parameters)
        
        # Perform a JSON-Web request
        result = http_json_request(JSON_SERVICE_URL, json_param)
        result_dict = json.loads(result)
        return Response(result_dict)
    except:
        return Response({'error':'something went wrong'})


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def find_model(request, *args, **kwargs):
    try:
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
                "linkageTargetType": "V",
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
    except:
        return Response({'error':'something went wrong'})


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def find_type(request, *args, **kwargs):
    try:
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
                    "linkageTargetType": "V",
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
    except:
        return Response({'error':'something went wrong'})    

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def find_sidebar(request, *args, **kwargs):
    try:
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
                    "linkageTargetIds":{"type": "V", "id": linkageTargetIds}  #3822 is  Type Id

                }
            }
            
            # Serialize the dictionary as JSON
            json_param = json.dumps(parameters)
            
            # Perform a JSON-Web request
            result = http_json_request(JSON_SERVICE_URL, json_param)
            result_dict = json.loads(result)
            return Response(result_dict)
        return Response({'error':'linkageTarget id not found'})
    except:
        return Response({'error':'something went wrong'})

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def find_categories_subcategories(request, *args, **kwargs):
    try:
        linkageTargetIds = request.GET.get('linkageTargetIds')
        
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
                    "linkageTargetType":"V",
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
            # add assembly group factes as well
            # assembly_groups1 = json.loads(result)['assemblyGroupFacets']['counts']
            # for loop_cat in assembly_groups1:
            #     try:
            #         parent_node = loop_cat['parentNodeId']
            #     except:
            #         parent_node = ""

            #     assembly_groups = json.loads(result)['assemblyGroupFacets']['counts']
            #     if parent_node!="":
            #         for loop_cat2 in assembly_groups:
            #             try:
            #                 assemb = loop_cat2['assemblyGroupNodeId']
            #             except:
            #                 assemb = ""
            #             if assemb!=""  and loop_cat2['assemblyGroupNodeId'] == parent_node:
            #                 loop_cat['assemblyGroupName'] =  loop_cat['assemblyGroupName'] + " " +'['+loop_cat2['assemblyGroupName']+']'
            #                 break
            try:
                assembly_groups1 = json.loads(result)['genericArticleFacets']['counts']
            except:
                assembly_groups1 = []
   


            response_main = dict()
            response_main['categories'] = only_categories
            response_main['genericArticleFacets'] = assembly_groups1

            return Response(response_main)
        return Response({'error':'linkageTarget id not found'})
    except:
        return Response({'error':'something went wrong'})

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def find_subcategories_subcategories(request, *args, **kwargs):
    try:
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
                    "linkageTargetType":"V",
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
    except:
        return Response({'error':'something went wrong'})


    
@api_view(['GET'])    
# @permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def find_articles_from_categories(request,*args,**kwargs):
    try:
        linkageTargetIds = request.GET.get('linkageTargetIds')
        assemblyGroupNodeIds = request.GET.get('assemblyGroupNodeIds')
        genericArticleId = request.GET.get('genericArticleId')
        criteriaFilter = request.GET.get('criteriaFilter')
        rawValue = request.GET.get('rawValue')
        manufacture = request.GET.get('manufacture')

        if ((linkageTargetIds !=None) and (assemblyGroupNodeIds!=None)) or ((linkageTargetIds !=None) and (genericArticleId!=None)):
            operation_name = "getArticles"            
            if genericArticleId == None:                                                       
                parameters2 = {
                    operation_name: {
                    'articleCountry': 'KE',
                    'provider': TECDOC_MANDATOR,
                    'lang': 'en',
                    'assemblyGroupNodeIds': [
                        int(assemblyGroupNodeIds),
                    ],
                    'linkageTargetId': int(linkageTargetIds),
                    'linkageTargetType': 'V',
                    'linkageTargetCountry': 'KE',
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
                    'filterQueries': [
                        '(dataSupplierId NOT IN (4978,4982))',
                    ],
                    'dataSupplierIds': [],
                    'genericArticleIds': [
                    ],
                    'criteriaFilters': [],
                    'articleStatusIds': [],
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
                    'includeArticleStatusFacets': True,
                    'includeCriteriaFacets': True,
                }
                }

            elif (genericArticleId !=None)  and (assemblyGroupNodeIds ==None):
                
                parameters2 = {
                    operation_name: {
                        'articleCountry': 'KE',
                        'provider': TECDOC_MANDATOR,
                        'lang': 'en',
                        'linkageTargetId': int(linkageTargetIds),
                        'linkageTargetType': 'V',
                        'linkageTargetCountry': 'KE',
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
                        'filterQueries': [
                            '(dataSupplierId NOT IN (4978,4982))',
                        ],
                        'dataSupplierIds': [],
                        'genericArticleIds': [
                            int(genericArticleId),
                        ],
                        'criteriaFilters': [],
                        'articleStatusIds': [],
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
                        'includeArticleStatusFacets': True,
                        'includeCriteriaFacets': True,
                    },
            }
                
            elif genericArticleId != None:
                parameters2 = {
                    operation_name: {
                    'articleCountry': 'KE',
                    'provider': TECDOC_MANDATOR,
                    'lang': 'en',
                    'assemblyGroupNodeIds': [
                        int(assemblyGroupNodeIds),
                    ],
                    'linkageTargetId': int(linkageTargetIds),
                    'linkageTargetType': 'V',
                    'linkageTargetCountry': 'KE',
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
                    'filterQueries': [
                        '(dataSupplierId NOT IN (4978,4982))',
                    ],
                    'dataSupplierIds': [],
                    'genericArticleIds': [
                        int(genericArticleId),
                    ],
                    'criteriaFilters': [],
                    'articleStatusIds': [],
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
                    'includeArticleStatusFacets': True,
                    'includeCriteriaFacets': True,
                }
                }

            elif (genericArticleId !=None) and (criteriaFilter !=None):
                parameters2 = {
                    operation_name: {
                    'articleCountry': 'KE',
                    'provider': TECDOC_MANDATOR,
                    'lang': 'en',
                    'assemblyGroupNodeIds': [
                        int(assemblyGroupNodeIds),
                    ],
                    'linkageTargetId': int(linkageTargetIds),
                    'linkageTargetType': 'V',
                    'linkageTargetCountry': 'KE',
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
                    'filterQueries': [
                        '(dataSupplierId NOT IN (4978,4982))',
                    ],
                    'dataSupplierIds': [],
                    'genericArticleIds': [
                        int(genericArticleId),
                    ],
                    'criteriaFilters': [
                        {
                        'criteriaId': int(criteriaFilter),
                        'rawValue': f'{rawValue}',
                        },
                    ],
                    'articleStatusIds': [],
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
                    'includeArticleStatusFacets': True,
                    'includeCriteriaFacets': True,
                }
                }

            
            json_param2 = json.dumps(parameters2)
            result2 = http_json_request(JSON_SERVICE_URL, json_param2)


            macthed_oem_db = []
            already_done = []
            filter_done = []
            

            for article_list in json.loads(result2)['articles']:        
                try:                   
                    for oem_loop in  article_list['oemNumbers']:
                        
                        if oem_loop['mfrName'] == manufacture:
                                                
                            if oem_loop['articleNumber'] not in already_done:                                                    
                                oem_number = oem_loop['articleNumber']                           
                                already_done.append(oem_number)                                          
                    if (len(already_done)>0):
                        # search_database = Eztb3105.objects.filter(searchfield__icontains=oem_number)
                        search_database = Eztb3105.objects.filter(ref2__in=already_done)
                        search_database_serializer = Eztb3105Serializer(search_database,many=True)
                        

                        if len(search_database_serializer.data) > 0:                                                                                                        
                            find_unique_id = [v.get('uniqueid') for v in search_database_serializer.data if v.get('uniqueid')!=0]
                            find_unique_id_zero = [v.get('uniqueid') for v in search_database_serializer.data if v.get('uniqueid')==0]
                             
                            search_database1 = Eztb3105.objects.filter(uniqueid__in=find_unique_id)
                            search_database_serializer1 = Eztb3105Serializer(search_database1,many=True)                                        
                            for new_loop in search_database_serializer1.data:                                
                                new_data = new_loop.copy()
                                new_data['Quantity_article'] = int(new_data['loc01'])+int(new_data['loc02'])+int(new_data['loc03'])+int(new_data['loc04'])+int(new_data['loc05'])+int(new_data['loc06'])+int(new_data['loc07'])+int(new_data['loc08'])+int(new_data['loc09'])+int(new_data['loc10'])+int(new_data['loc11'])+int(new_data['loc12'])+int(new_data['loc13'])+int(new_data['loc14'])+int(new_data['loc15'])+int(new_data['loc16'])+int(new_data['loc17'])+int(new_data['loc18'])+int(new_data['loc19'])+int(new_data['loc20'])+int(new_data['loc21'])+int(new_data['loc22'])+int(new_data['loc23'])+int(new_data['loc24'])+int(new_data['loc25'])+int(new_data['loc26'])+int(new_data['loc27'])+int(new_data['loc28'])+int(new_data['loc29'])+int(new_data['loc30'])+int(new_data['loc31'])+int(new_data['loc32'])+int(new_data['loc33'])+int(new_data['loc34'])+int(new_data['loc35'])+int(new_data['loc36'])+int(new_data['loc37'])+int(new_data['loc38'])+int(new_data['loc39'])+int(new_data['loc40'])
                                if (new_data['Quantity_article'] != 0) and (new_data['price2'] != 0):
                                    new_data['images'] = article_list['images']                                    
                                    if new_data['id'] not in filter_done:                                        
                                        macthed_oem_db.append(new_data)
                                        filter_done.append(new_data['id'])
                            if len(find_unique_id_zero) > 0:                                
                                for new_loop in search_database_serializer.data:
                                    if new_loop.get('uniqueid')==0:                                           
                                                                            
                                        new_data = new_loop.copy()
                                        new_data['Quantity_article'] = int(new_data['loc01'])+int(new_data['loc02'])+int(new_data['loc03'])+int(new_data['loc04'])+int(new_data['loc05'])+int(new_data['loc06'])+int(new_data['loc07'])+int(new_data['loc08'])+int(new_data['loc09'])+int(new_data['loc10'])+int(new_data['loc11'])+int(new_data['loc12'])+int(new_data['loc13'])+int(new_data['loc14'])+int(new_data['loc15'])+int(new_data['loc16'])+int(new_data['loc17'])+int(new_data['loc18'])+int(new_data['loc19'])+int(new_data['loc20'])+int(new_data['loc21'])+int(new_data['loc22'])+int(new_data['loc23'])+int(new_data['loc24'])+int(new_data['loc25'])+int(new_data['loc26'])+int(new_data['loc27'])+int(new_data['loc28'])+int(new_data['loc29'])+int(new_data['loc30'])+int(new_data['loc31'])+int(new_data['loc32'])+int(new_data['loc33'])+int(new_data['loc34'])+int(new_data['loc35'])+int(new_data['loc36'])+int(new_data['loc37'])+int(new_data['loc38'])+int(new_data['loc39'])+int(new_data['loc40'])
                                        if (new_data['Quantity_article'] != 0) and (new_data['price2'] != 0):
                                            new_data['images'] = article_list['images']                                    
                                            if new_data['id'] not in filter_done:                                        
                                                macthed_oem_db.append(new_data)
                                                filter_done.append(new_data['id'])
                                                                                             
                except:
                    oem_number = None

            part_categories = dict()
            part_categories['parts'] = macthed_oem_db
            part_categories['part_subcategories'] = json.loads(result2)['genericArticleFacets']
            if genericArticleId !=None:
                try:
                    part_categories['part_criteriaFacets'] = json.loads(result2)['criteriaFacets']
                except:
                    part_categories['part_criteriaFacets'] = []

                
            
            return Response(part_categories)

        return Response({'error':'linkageTarget assemblyGroupNodeIds id not found'})
    except:
        return Response({'error':'something went wrong'})

@api_view(['GET'])    
# @permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def find_article_information(request,*args,**kwargs):
    try:
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
            return Response({'error':'SearchQuery not found'})
    except:
        return Response({'error':'something went wrong'})    



def convert_dict(data):
    item = dict()
    for v in data:
        try:
            oem = v['ref2'].split(' ')[0].split('/')[0].replace("-","").strip()
            if item[oem]:
                v['images'] = []
                v['Quantity_article'] = int(v['loc01'])+int(v['loc02'])+int(v['loc03'])+int(v['loc04'])+int(v['loc05'])+int(v['loc06'])+int(v['loc07'])+int(v['loc08'])+int(v['loc09'])+int(v['loc10'])+int(v['loc11'])+int(v['loc12'])+int(v['loc13'])+int(v['loc14'])+int(v['loc15'])+int(v['loc16'])+int(v['loc17'])+int(v['loc18'])+int(v['loc19'])+int(v['loc20'])+int(v['loc21'])+int(v['loc22'])+int(v['loc23'])+int(v['loc24'])+int(v['loc25'])+int(v['loc26'])+int(v['loc27'])+int(v['loc28'])+int(v['loc29'])+int(v['loc30'])+int(v['loc31'])+int(v['loc32'])+int(v['loc33'])+int(v['loc34'])+int(v['loc35'])+int(v['loc36'])+int(v['loc37'])+int(v['loc38'])+int(v['loc39'])+int(v['loc40'])
                v['flag'] = 1
                if (v['Quantity_article'] != 0) and (v['price2'] != 0):
                    item[str(oem)].append(v)
        except:
            v['images'] = []
            v['Quantity_article'] = int(v['loc01'])+int(v['loc02'])+int(v['loc03'])+int(v['loc04'])+int(v['loc05'])+int(v['loc06'])+int(v['loc07'])+int(v['loc08'])+int(v['loc09'])+int(v['loc10'])+int(v['loc11'])+int(v['loc12'])+int(v['loc13'])+int(v['loc14'])+int(v['loc15'])+int(v['loc16'])+int(v['loc17'])+int(v['loc18'])+int(v['loc19'])+int(v['loc20'])+int(v['loc21'])+int(v['loc22'])+int(v['loc23'])+int(v['loc24'])+int(v['loc25'])+int(v['loc26'])+int(v['loc27'])+int(v['loc28'])+int(v['loc29'])+int(v['loc30'])+int(v['loc31'])+int(v['loc32'])+int(v['loc33'])+int(v['loc34'])+int(v['loc35'])+int(v['loc36'])+int(v['loc37'])+int(v['loc38'])+int(v['loc39'])+int(v['loc40'])
            oem = v['ref2'].split(' ')[0].split('/')[0].replace("-","").strip()
            v['flag'] = 1
            if (v['Quantity_article'] != 0) and (v['price2'] != 0):
                item[str(oem)] = [v]
    return item

def get_data_list(item):
    data = []
    for key,value in item:
        data2 = []
        data2 = [v for v in item[key]]
        for d in data2:
            data.append(d)
    return data


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])

def AutoCompleteSuggestions(request,*args,**kwargs):        
        try:
            searchQuery = request.GET.get('searchquery')
            if (searchQuery!=None):
                if len(searchQuery) < 40:                   
                    search_query_keyword = Eztb3105.objects.filter(Q(stkgencode=searchQuery) | Q(itemid=searchQuery) | Q(ref1=searchQuery) | Q(ref2=searchQuery) | Q(ref3=searchQuery))                    
                    search_query_keyword_serializer = Eztb3105Serializer(search_query_keyword,many=True)                    

                elif searchQuery.count(' ') > 0:
                    # Split the input string by spaces
                    words = searchQuery.split()
                    # Use a set to remove duplicates and then join the words back together with spaces
                    new_search_c = ' '.join(set(words))
                    
                    new_search_c = re.sub(r'[^a-zA-Z0-9]', ' ', new_search_c).lower()

                    # Split the string into a list of words based on spaces
                    words_new_search_c = new_search_c.split()

                    q_objects = Q()
                    for word in words_new_search_c:
                        q_objects &= Q(searchfield__icontains=word)

                    # Use Django ORM to retrieve the records
                    selected_records = Eztb3105.objects.filter(q_objects).values()
                    search_query_keyword_serializer = Eztb3105Serializer(selected_records,many=True)
                finale_result = []    
                try:
                    oems_numbers = [v['ref2'] for v in search_query_keyword_serializer.data if v['images']==None]
                    print(oems_numbers)
                except:
                    oems_numbers = []

                
                if len(oems_numbers) > 0:
                    generic_ids = []
                    generic_ids_mapping = []
                    done_oems = []
                    operation_name = "getArticles"
                      
                    for oems_loop in oems_numbers:                                       
                        if oems_loop not in done_oems:                        
                            parameters = {
                                operation_name: {
                                    'arg0': {
                                        'articleCountry': 'KE',
                                        'provider': int(TECDOC_MANDATOR),
                                        'lang': 'en',
                                        'searchQuery': oems_loop,
                                        'searchMatchType': 'prefix_or_suffix',
                                        'searchType': 10,
                                        'page': 1,
                                        'perPage': 0,
                                        'sort': [
                                            {
                                                'field': 'score',
                                                'direction': 'desc',
                                            },
                                            {
                                                'field': 'mfrName',
                                                'direction': 'asc',
                                            },
                                            {
                                                'field': 'linkageSortNum',
                                                'direction': 'asc',
                                            },
                                        ],
                                        'filterQueries': [
                                            '(dataSupplierId NOT IN (4978,4982))',
                                        ],
                                        'dataSupplierIds': [],
                                        'genericArticleIds': [],
                                        'includeAll': False,
                                        'includeLinkages': True,
                                        'linkagesPerPage': 100,
                                        'includeGenericArticles': True,
                                        'includeArticleCriteria': True,
                                        'includeMisc': True,
                                        'includeImages': True,
                                        'includePDFs': False,
                                        'includeLinks': False,
                                        'includeArticleText': True,
                                        'includeOEMNumbers': False,
                                        'includeReplacedByArticles': True,
                                        'includeReplacesArticles': True,
                                        'includeComparableNumbers': True,
                                        'includeGTINs': True,
                                        'includeTradeNumbers': True,
                                        'includePrices': False,
                                        'includePartsListArticles': False,
                                        'includeAccessoryArticles': False,
                                        'includeArticleLogisticsCriteria': False,
                                        'includeDataSupplierFacets': False,
                                        'includeGenericArticleFacets': True,
                                        'includeCriteriaFacets': False,
                                    },
                                    },
                                    }

                            json_param = json.dumps(parameters)
                            result = http_json_request('https://webservice.tecalliance.services/pegasus-3-0/services/TecdocToCatDLW.jsonEndpoint', json_param)
                            try:
                                generic_articleId = json.loads(result)["genericArticleFacets"]["counts"][0]["genericArticleId"]                            
                                if generic_articleId not in generic_ids:
                                    item_generic_mapping = dict()
                                    item_generic_mapping['generic_id'] = generic_articleId
                                    item_generic_mapping['oem'] = oems_loop
                                    
                                    generic_ids_mapping.append(item_generic_mapping)

                                    generic_ids.append(generic_articleId)
                            except Exception as E:                      
                                print('Generic index',E)
                            done_oems.append(oems_loop)
                    print(generic_ids)   
                    if len(generic_ids) > 0:                    
                        parameters2 = {
                            operation_name: {
                                'arg0': {
                                    'articleCountry': 'KE',
                                    'provider': int(TECDOC_MANDATOR),
                                    'lang': 'en',
                                    'searchQuery': searchQuery,
                                    'searchMatchType': 'prefix_or_suffix',
                                    'searchType': 10,
                                    'page': 1,
                                    'perPage': 100,
                                    'sort': [
                                        {
                                            'field': 'score',
                                            'direction': 'desc',
                                        },
                                        {
                                            'field': 'mfrName',
                                            'direction': 'asc',
                                        },
                                        {
                                            'field': 'linkageSortNum',
                                            'direction': 'asc',
                                        },
                                    ],
                                    'filterQueries': [
                                        '(dataSupplierId NOT IN (4978,4982))',
                                    ],
                                    'dataSupplierIds': [],
                                    'genericArticleIds': generic_ids,
                                    'criteriaFilters': [],
                                    'articleStatusIds': [],
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
                                    'includeArticleStatusFacets': True,
                                    'includeCriteriaFacets': True,
                                },
                                },
                                }           

                        json_param2 = json.dumps(parameters2)
                        result2 = http_json_request('https://webservice.tecalliance.services/pegasus-3-0/services/TecdocToCatDLW.jsonEndpoint', json_param2)

                        update_dones = []
                        
                        print('search query data',[v['ref2'] for v in search_query_keyword_serializer.data])                
                        for loop_db_image in search_query_keyword_serializer.data:
                            
                            check_quantity = int(loop_db_image['loc01'])+int(loop_db_image['loc02'])+int(loop_db_image['loc03'])+int(loop_db_image['loc04'])+int(loop_db_image['loc05'])+int(loop_db_image['loc06'])+int(loop_db_image['loc07'])+int(loop_db_image['loc08'])+int(loop_db_image['loc09'])+int(loop_db_image['loc10'])+int(loop_db_image['loc11'])+int(loop_db_image['loc12'])+int(loop_db_image['loc13'])+int(loop_db_image['loc14'])+int(loop_db_image['loc15'])+int(loop_db_image['loc16'])+int(loop_db_image['loc17'])+int(loop_db_image['loc18'])+int(loop_db_image['loc19'])+int(loop_db_image['loc20'])+int(loop_db_image['loc21'])+int(loop_db_image['loc22'])+int(loop_db_image['loc23'])+int(loop_db_image['loc24'])+int(loop_db_image['loc25'])+int(loop_db_image['loc26'])+int(loop_db_image['loc27'])+int(loop_db_image['loc28'])+int(loop_db_image['loc29'])+int(loop_db_image['loc30'])+int(loop_db_image['loc31'])+int(loop_db_image['loc32'])+int(loop_db_image['loc33'])+int(loop_db_image['loc34'])+int(loop_db_image['loc35'])+int(loop_db_image['loc36'])+int(loop_db_image['loc37'])+int(loop_db_image['loc38'])+int(loop_db_image['loc39'])+int(loop_db_image['loc40'])                        
                            check_price = loop_db_image['price2']
                            check_point_flag = False
                            
                            if (check_quantity != 0) and (check_price != 0) and (loop_db_image['images']==None):
                                print('i am here for price')
                                
                                matched_done = []
                                seperator =json.loads(result2)['articles']

                                print(len(seperator))
                                
                                for generic_ids_map in seperator:                                
                                    for inner_images in generic_ids_map['oemNumbers']:
                                        print("ref2 matching",loop_db_image['ref2'].strip().lower())                                    
                                        print("articleNumber matching",inner_images['articleNumber'].strip().lower())                                    
                                        if (inner_images['articleNumber'] not in matched_done) and (loop_db_image['ref2'].strip().lower() ==  inner_images['articleNumber'].strip().lower()  ) :
                                                                                 
                                            try:                                            
                                                if len(generic_ids_map['images'])> 0:
                                                                                                 
                                                    loop_db_image['images']=str(copy.copy(generic_ids_map['images']))
                                                    
                                                    loop_db_image['Quantity_article'] = int(loop_db_image['loc01'])+int(loop_db_image['loc02'])+int(loop_db_image['loc03'])+int(loop_db_image['loc04'])+int(loop_db_image['loc05'])+int(loop_db_image['loc06'])+int(loop_db_image['loc07'])+int(loop_db_image['loc08'])+int(loop_db_image['loc09'])+int(loop_db_image['loc10'])+int(loop_db_image['loc11'])+int(loop_db_image['loc12'])+int(loop_db_image['loc13'])+int(loop_db_image['loc14'])+int(loop_db_image['loc15'])+int(loop_db_image['loc16'])+int(loop_db_image['loc17'])+int(loop_db_image['loc18'])+int(loop_db_image['loc19'])+int(loop_db_image['loc20'])+int(loop_db_image['loc21'])+int(loop_db_image['loc22'])+int(loop_db_image['loc23'])+int(loop_db_image['loc24'])+int(loop_db_image['loc25'])+int(loop_db_image['loc26'])+int(loop_db_image['loc27'])+int(loop_db_image['loc28'])+int(loop_db_image['loc29'])+int(loop_db_image['loc30'])+int(loop_db_image['loc31'])+int(loop_db_image['loc32'])+int(loop_db_image['loc33'])+int(loop_db_image['loc34'])+int(loop_db_image['loc35'])+int(loop_db_image['loc36'])+int(loop_db_image['loc37'])+int(loop_db_image['loc38'])+int(loop_db_image['loc39'])+int(loop_db_image['loc40'])                                                
                                                    print('final appending')                                        
                                                    finale_result.append(copy.copy(loop_db_image))
                                                                                        
                                                    check_point_flag = True
                                                    matched_done.append(inner_images['articleNumber'])
                                            except:
                                                print('i am exception')
                                        if check_point_flag == True:
                                            break
                                    if check_point_flag == True:
                                            if (loop_db_image['ref2'] not in update_dones) and (loop_db_image['ref2'] in oems_numbers):
                                                
                                                Eztb3105.objects.filter(ref2=loop_db_image['ref2']).update(images=generic_ids_map['images'])
                                                print('done updation')
                                                # for update_images_loop in update_images:
                                                #     update_images_loop.images = copy.copy(generic_ids_map['images'])
                                                #     update_images_loop.save()                                                    
                                                                                                                                           
                                                update_dones.append(loop_db_image['ref2'])  
                                            break    
                                                
                                                                                
                            if check_point_flag == False and (loop_db_image['images']==None):                            
                                loop_db_image['images'] = str([])
                                loop_db_image['Quantity_article'] = int(loop_db_image['loc01'])+int(loop_db_image['loc02'])+int(loop_db_image['loc03'])+int(loop_db_image['loc04'])+int(loop_db_image['loc05'])+int(loop_db_image['loc06'])+int(loop_db_image['loc07'])+int(loop_db_image['loc08'])+int(loop_db_image['loc09'])+int(loop_db_image['loc10'])+int(loop_db_image['loc11'])+int(loop_db_image['loc12'])+int(loop_db_image['loc13'])+int(loop_db_image['loc14'])+int(loop_db_image['loc15'])+int(loop_db_image['loc16'])+int(loop_db_image['loc17'])+int(loop_db_image['loc18'])+int(loop_db_image['loc19'])+int(loop_db_image['loc20'])+int(loop_db_image['loc21'])+int(loop_db_image['loc22'])+int(loop_db_image['loc23'])+int(loop_db_image['loc24'])+int(loop_db_image['loc25'])+int(loop_db_image['loc26'])+int(loop_db_image['loc27'])+int(loop_db_image['loc28'])+int(loop_db_image['loc29'])+int(loop_db_image['loc30'])+int(loop_db_image['loc31'])+int(loop_db_image['loc32'])+int(loop_db_image['loc33'])+int(loop_db_image['loc34'])+int(loop_db_image['loc35'])+int(loop_db_image['loc36'])+int(loop_db_image['loc37'])+int(loop_db_image['loc38'])+int(loop_db_image['loc39'])+int(loop_db_image['loc40'])
                                if (loop_db_image['Quantity_article'] != 0) and (loop_db_image['price2'] != 0):
                                    print('finale_result 2')
                                    finale_result.append(loop_db_image)         
                                
                    else:
                        for loop_db_image in search_query_keyword_serializer.data:
                            print('i am else')
                            if loop_db_image['images']==None:                    
                                loop_db_image['images']=str([])
                                loop_db_image['Quantity_article'] = int(loop_db_image['loc01'])+int(loop_db_image['loc02'])+int(loop_db_image['loc03'])+int(loop_db_image['loc04'])+int(loop_db_image['loc05'])+int(loop_db_image['loc06'])+int(loop_db_image['loc07'])+int(loop_db_image['loc08'])+int(loop_db_image['loc09'])+int(loop_db_image['loc10'])+int(loop_db_image['loc11'])+int(loop_db_image['loc12'])+int(loop_db_image['loc13'])+int(loop_db_image['loc14'])+int(loop_db_image['loc15'])+int(loop_db_image['loc16'])+int(loop_db_image['loc17'])+int(loop_db_image['loc18'])+int(loop_db_image['loc19'])+int(loop_db_image['loc20'])+int(loop_db_image['loc21'])+int(loop_db_image['loc22'])+int(loop_db_image['loc23'])+int(loop_db_image['loc24'])+int(loop_db_image['loc25'])+int(loop_db_image['loc26'])+int(loop_db_image['loc27'])+int(loop_db_image['loc28'])+int(loop_db_image['loc29'])+int(loop_db_image['loc30'])+int(loop_db_image['loc31'])+int(loop_db_image['loc32'])+int(loop_db_image['loc33'])+int(loop_db_image['loc34'])+int(loop_db_image['loc35'])+int(loop_db_image['loc36'])+int(loop_db_image['loc37'])+int(loop_db_image['loc38'])+int(loop_db_image['loc39'])+int(loop_db_image['loc40'])
                                if (loop_db_image['Quantity_article'] !=0) and (loop_db_image['price2']!=0):                                                                
                                    finale_result.append(copy.copy(loop_db_image))
                print('final result length',len(finale_result))
                print(oems_numbers)
                for again_else_loop in search_query_keyword_serializer.data:
                    print('i am printing')
                    if again_else_loop['ref2'] not in oems_numbers:                        
                        again_else_loop['Quantity_article'] = int(again_else_loop['loc01'])+int(again_else_loop['loc02'])+int(again_else_loop['loc03'])+int(again_else_loop['loc04'])+int(again_else_loop['loc05'])+int(again_else_loop['loc06'])+int(again_else_loop['loc07'])+int(again_else_loop['loc08'])+int(again_else_loop['loc09'])+int(again_else_loop['loc10'])+int(again_else_loop['loc11'])+int(again_else_loop['loc12'])+int(again_else_loop['loc13'])+int(again_else_loop['loc14'])+int(again_else_loop['loc15'])+int(again_else_loop['loc16'])+int(again_else_loop['loc17'])+int(again_else_loop['loc18'])+int(again_else_loop['loc19'])+int(again_else_loop['loc20'])+int(again_else_loop['loc21'])+int(again_else_loop['loc22'])+int(again_else_loop['loc23'])+int(again_else_loop['loc24'])+int(again_else_loop['loc25'])+int(again_else_loop['loc26'])+int(again_else_loop['loc27'])+int(again_else_loop['loc28'])+int(again_else_loop['loc29'])+int(again_else_loop['loc30'])+int(again_else_loop['loc31'])+int(again_else_loop['loc32'])+int(again_else_loop['loc33'])+int(again_else_loop['loc34'])+int(again_else_loop['loc35'])+int(again_else_loop['loc36'])+int(again_else_loop['loc37'])+int(again_else_loop['loc38'])+int(again_else_loop['loc39'])+int(again_else_loop['loc40'])
                        print('Ref2',again_else_loop['ref2'])
                        print('Quantity',again_else_loop['Quantity_article'])
                        if (again_else_loop['Quantity_article'] !=0) and (again_else_loop['price2']!=0) :
                            print('i am printing price') 
                            finale_result.append(again_else_loop)
                                    
                return Response({'parts':finale_result})
            else:
                return Response({'error':'searchQuery not found'})

            
        except Exception as E:            
            print("rooly",E)                        
            return Response({'error':'something went wrong'})        



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def SearchByVINNumber(request,*args,**kwargs):
    try:
        vinnumber = request.GET.get('vinnumber')
        if vinnumber !=None:
            operation_name = "getVehiclesByVIN"
            parameters = {
            operation_name: {
                'arg0': {
                    'country': 'KE',
                    'lang': 'en',
                    'vin': vinnumber,
                    'provider': TECDOC_MANDATOR,
                    'manuId': None,
                    'modelId': None,
                    'maxVehiclesToReturn': -1,
                },
            },
            }
            json_param = json.dumps(parameters)
            result = http_json_request('https://webservice.tecalliance.services/pegasus-3-0/services/TecdocToCatDLW.jsonEndpoint', json_param)
            return Response({'data':json.loads(result)})
        return Response({'error':'vinnumber not found'})
    except:
        return Response({'error':'something went wrong'})



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def allpartCategories(request,*args,**kwargs):     
     try:
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
        return Response({'data':only_categories})
     except:
        return Response({'error':'something went wrong'})
 

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def allpartSubCategories(request,*args,**kwargs):
    try:
        selected_subcategory = request.GET.get('selected_subcategory')
        if (selected_subcategory!=None):
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
    except:
        return Response({'error':'something went wrong'})
    


# SCRAPER EPC DATA TO FIND CAR USING FRAME NUMBER
# '---------------------------------------------------------------------------------------------------'
def epc_scraper_data(manufacture,framenumber):    
    
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,de;q=0.8,hi;q=0.7,nl;q=0.6',
        'Connection': 'keep-alive',
        'Referer': 'https://www.epc-data.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'frame_no': framenumber,
    }
    if manufacture.lower() == 'toyota':
        url = 'https://toyota.epc-data.com/search_frame/'
    elif  manufacture.lower() == 'nissan':
        url = 'https://nissan.epc-data.com/search_frame/'
    else:
        url = 'https://toyota.epc-data.com/search_frame/'

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        response_scrapy = scrapy.Selector(text=response.text)
        header_list =response_scrapy.css('div.path ::text').extract()
        item = dict()
        item['header_list'] = header_list
        item['full_heading'] = response_scrapy.css('h1 ::text').get()
        for index,loop in enumerate(response_scrapy.css('table.table tr')):

            try:
                if manufacture.lower() == 'nissan':
                    item['Production period'] = item['full_heading'][-1]
            except:
                pass
            for new_view_index ,new_view in enumerate(loop.css('td')):
                if new_view.css(' ::text').get() == 'Frame / Series':
                    try:
                        item['Frame/Series'] = loop.css('td')[new_view_index+1].css(' ::text').get()
                    except:
                        item['Frame/Series'] = ""

                if new_view.css(' ::text').get() == 'BODY':
                    try:
                        item['Body'] = loop.css('td')[new_view_index+1].css(' ::text').get()
                    except:
                        item['Body'] = ""
                if new_view.css(' ::text').get() == 'ENGINE':
                    try:
                        item['Engine'] = loop.css('td')[new_view_index+1].css(' ::text').get().split('(')[0].strip()
                    except:
                        item['Engine'] = ""
                if new_view.css(' ::text').get() == 'DRIVE':
                    try:
                        item['Drive'] = loop.css('td')[new_view_index+1].css(' ::text').get()
                    except:
                        item['Drive'] = ""
                if new_view.css(' ::text').get() == 'Production&nbsp;month':
                    try:
                        item['production month'] = loop.css('td')[new_view_index+1].css(' ::text').get()
                    except:
                        item['production month'] = ""
                if new_view.css(' ::text').get() == 'GRADE':
                    try:
                        item['Grade'] = loop.css('td')[new_view_index+1].css(' ::text').get()
                    except:
                        item['Grade'] = ""
                if new_view.css(' ::text').get() == 'TRANS':
                    try:
                        item['Transm'] = loop.css('td')[new_view_index+1].css(' ::text').get()
                    except:
                        item['Transm'] = ""

                if new_view.css(' ::text').get() == 'Interior&nbsp;color':
                    try:
                        item['Color code'] = loop.css('td')[new_view_index+1].css(' ::text').get()
                    except:
                        item['Color code'] = ""



            if  "Production period" in loop.css(' ::text').extract():
                try:
                    item['Production period'] = " ".join(loop.css(' ::text').extract()).split('Production period')[-1].strip()
                except:
                    item['Production period'] = ""

            if  "Catalog code" in loop.css(' ::text').extract():
                try:
                    item['Catalog code'] = " ".join(loop.css(' ::text').extract()).split('Catalog code')[-1].strip()
                except:
                    item['Catalog code'] = ""

            if "Complectation" in loop.css(' ::text').extract():
                try:
                    item['Complectation'] = " ".join(loop.css(' ::text').extract()).split('Complectation')[-1].strip()
                except:
                    item['Complectation'] = ""

            if "Characteristics" in loop.css(' ::text').extract():

                for type_index,types in enumerate(loop.css('td')[1:]):
                    if 'Engine' in types.css(' ::text').get():
                        try:
                            item['Engine'] = response_scrapy.css('table.table tr')[index + 1].css('td')[type_index].css('span ::text').get()

                        except:
                            item['Engine'] = ""


                    if 'Body' in types.css(' ::text').get():
                        try:
                            item['Body'] = response_scrapy.css('table.table tr')[index + 1].css('td')[type_index].css('span ::attr(title)').get()

                        except:
                            item['Body'] = ""
                    if 'Grade' in types.css(' ::text').get():
                        try:
                            item['Grade'] = response_scrapy.css('table.table tr')[index + 1].css('td')[type_index].css('span ::attr(title)').get()

                        except:
                            item['Grade'] = ""

                    if 'Transm.' in types.css(' ::text').get():
                        try:
                            item['Transm'] = response_scrapy.css('table.table tr')[index + 1].css('td')[type_index].css('span ::attr(title)').get()

                        except:
                            item['Transm'] = ""
                    if 'Options' in types.css(' ::text').get():
                        try:
                            item['Options'] = ' '.join(response_scrapy.css('table.table tr')[index + 1].css('td')[type_index].css('span ::attr(title)').extract())

                        except:
                            item['Options'] = ""


        for index2, loop2 in enumerate(response_scrapy.css('table.table')[-1].css('td')):
            if 'Color code:' in loop2.css(' ::text').get():
                try:
                    item['Color code'] = loop2.css(' ::text').get().split('Color code:')[-1].strip()
                except:
                    item['Color code'] = ""

            if 'Trim code:' in loop2.css(' ::text').get():
                try:
                    item['Trim code'] = loop2.css(' ::text').get().split('Trim code:')[-1].strip()
                except:
                    item['Trim code'] = ""
            if 'Manufacture date:' in loop2.css(' ::text').get():
                try:
                    item['Manufacture date'] = loop2.css(' ::text').get().split('Manufacture date:')[-1].strip()
                except:
                    item['Manufacture date'] = ""

        try:
            item['cc_type'] = int(item['Engine'].split('CC')[0])/1000
        except:
            item['cc_type'] = ""



        try:
            item['Complectation_type'] = response.url.split('/')[4]
        except:
            item['Complectation_type'] = ""


        try:
            item['match_Description'] = str(item['cc_type']) +' '+ '('+item['Complectation_type']+')'
        except:
            item['match_Description'] = ""

        try:
            item['car_name'] = response.url.split('/')[3].replace('_'," ")
        except:
            item['car_name'] = ""
        try:
            item['start_year'] = item['Production period'].split('-')[0].split('.')[-1]
        except:
            item['start_year'] = ""
        try:
            item['end_year'] = item['Production period'].split('-')[1].split('.')[-1]
        except:
            item['end_year'] = ""

        item['manufacture'] = manufacture.lower()

        return item


# '---------------------------------------------------------------------------------------------------'


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def searchbyframenumber(request,*args,**kwargs):
    try:   
        framenumber = request.GET.get('framenumber').lower()
        manufacture = request.GET.get('manufacture').lower()
        if (framenumber!=None) and ((manufacture!=None)):
            scarper_response = epc_scraper_data(manufacture,framenumber)

            manufacture_name = scarper_response['manufacture']
            full_description = scarper_response['full_heading']
            model_name = scarper_response['header_list'][2]
            model_code = scarper_response['header_list'][3]
            model_scraper_engine = scarper_response['Engine']


            # find_manufactures_ids
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
            find_manufacture_id = [v['manuId'] for v in result_dict['data']['array'] if v['manuName'].lower()==manufacture_name][0]

            # find_Models_id
            operation_name = "getLinkageTargets"

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
                "mfrIds":[find_manufacture_id]  # manufatcure id variable
            }
            }
            
            # Serialize the dictionary as JSON
            json_param = json.dumps(parameters)
            
            # Perform a JSON-Web request
            result = http_json_request(JSON_SERVICE_URL, json_param)
            result_dict = json.loads(result)

            
            match_name = ""
            for v in result_dict['vehicleModelSeriesFacets']['counts']:
                if model_name.lower() in v['name'].lower():
                    epec_code = v['name'].split('(')[-1].split(')')[0].replace('_','').strip()

                    if epec_code.lower() in full_description.lower():
                        match_name = v




            try:
                if match_name['name'] != "": 
                    matched_model_id = match_name['id']
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
                            "mfrIds": [find_manufacture_id],  # manufatcure id variable
                            "vehicleModelSeriesIds":[matched_model_id],
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

                    for enginess in  result_dict['linkageTargets']:
                        for inner_engine in enginess['engines']:
                            if inner_engine['code'].replace('-',"") in model_scraper_engine:
                                return Response({"result":enginess})

            except Exception as E:
                return Response({"result":'no match'})


                                

        return Response({'error':'framenumber or manufacture not found'})     
    except:
        return Response({'error':'something went wrong'})






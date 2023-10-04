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
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
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
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
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
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
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
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
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

            return Response(only_categories)
        return Response({'error':'linkageTarget id not found'})
    except:
        return Response({'error':'something went wrong'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
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
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def find_articles_from_categories(request,*args,**kwargs):
    try:
        linkageTargetIds = request.GET.get('linkageTargetIds')
        assemblyGroupNodeIds = request.GET.get('assemblyGroupNodeIds')
        genericArticleId = request.GET.get('genericArticleId')
        criteriaFilter = request.GET.get('criteriaFilter')

        if (linkageTargetIds !=None) and (assemblyGroupNodeIds!=None):
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

            if genericArticleId != None:
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

            if (genericArticleId !=None) and (criteriaFilter !=None):
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
                        'rawValue': 'VA',
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
                
                check_point_flag = False             
                try:                    
                    for oem_loop in  article_list['oemNumbers']:
                        # print('count 2')                       
                        if oem_loop['articleNumber'] not in already_done:                                                      
                            oem_number = oem_loop['articleNumber']                           
                            already_done.append(oem_number)  
                                                        
                            if (oem_number!=None) and (check_point_flag == False):
                                # search_database = Eztb3105.objects.filter(searchfield__icontains=oem_number)
                                search_database = Eztb3105.objects.filter(ref2=oem_number)
                                search_database_serializer = Eztb3105Serializer(search_database,many=True)
                                

                                if len(search_database_serializer.data) > 0:                                                                    
                                    find_unique_id = search_database_serializer.data[0].get('uniqueid')
                                    
                                    search_database1 = Eztb3105.objects.filter(uniqueid=find_unique_id)
                                    search_database_serializer1 = Eztb3105Serializer(search_database1,many=True)

                                    for new_loop in search_database_serializer1.data:
                                        check_point_flag = True
                                        new_data = new_loop.copy()
                                        new_data['Quantity_article'] = int(new_data['loc01'])+int(new_data['loc02'])+int(new_data['loc03'])+int(new_data['loc04'])+int(new_data['loc05'])+int(new_data['loc06'])+int(new_data['loc07'])+int(new_data['loc08'])+int(new_data['loc09'])+int(new_data['loc10'])+int(new_data['loc11'])+int(new_data['loc12'])+int(new_data['loc13'])+int(new_data['loc14'])+int(new_data['loc15'])+int(new_data['loc16'])+int(new_data['loc17'])+int(new_data['loc18'])+int(new_data['loc19'])+int(new_data['loc20'])+int(new_data['loc31'])+int(new_data['loc32'])+int(new_data['loc33'])+int(new_data['loc34'])+int(new_data['loc35'])+int(new_data['loc36'])+int(new_data['loc37'])+int(new_data['loc38'])+int(new_data['loc39'])+int(new_data['loc40'])
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
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def AutoCompleteSuggestions(request,*args,**kwargs):        
        try:
            searchQuery = request.GET.get('searchquery')
            if (searchQuery!=None):
                operation_name = "getArticles"

                parameters = {
                    operation_name: {
                        'arg0': {
                            'articleCountry': 'KE',
                            'provider': int(TECDOC_MANDATOR),
                            'lang': 'en',
                            'searchQuery': searchQuery,
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


                generic_articleId = json.loads(result)["genericArticleFacets"]["counts"][0]["genericArticleId"]

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
                            'genericArticleIds': [
                                generic_articleId,
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
                        },
                        }
                json_param2 = json.dumps(parameters2)
                result2 = http_json_request('https://webservice.tecalliance.services/pegasus-3-0/services/TecdocToCatDLW.jsonEndpoint', json_param2)

                # macthed_oem_db = []
                # already_done = []
                # for article_list in json.loads(result2)['articles']:
                #     try:
                #         if article_list['oemNumbers'][0]['articleNumber'] not in already_done:
                #             oem_number = article_list['oemNumbers'][0]['articleNumber']
                #             already_done.append(oem_number)
                #             if (oem_number!=None):            
                #                 search_database = Eztb3105.objects.filter(searchfield__icontains=oem_number)
                #                 search_database_serializer = Eztb3105Serializer(search_database,many=True)                
                #                 if len(search_database_serializer.data) > 0:
                #                     for new_loop in search_database_serializer.data:
                #                         new_data = new_loop.copy()
                #                         new_data['Quantity_article'] = int(new_data['loc01'])+int(new_data['loc02'])+int(new_data['loc03'])+int(new_data['loc04'])+int(new_data['loc05'])+int(new_data['loc06'])+int(new_data['loc07'])+int(new_data['loc08'])+int(new_data['loc09'])+int(new_data['loc10'])+int(new_data['loc11'])+int(new_data['loc12'])+int(new_data['loc13'])+int(new_data['loc14'])+int(new_data['loc15'])+int(new_data['loc16'])+int(new_data['loc17'])+int(new_data['loc18'])+int(new_data['loc19'])+int(new_data['loc20'])+int(new_data['loc31'])+int(new_data['loc32'])+int(new_data['loc33'])+int(new_data['loc34'])+int(new_data['loc35'])+int(new_data['loc36'])+int(new_data['loc37'])+int(new_data['loc38'])+int(new_data['loc39'])+int(new_data['loc40'])
                #                         new_data['images'] = article_list['images']
                #                         macthed_oem_db.append(new_data)
                #     except:
                #         oem_number = None

            macthed_oem_db = []
            already_done = []
            filter_done = []
            
            

            for article_list in json.loads(result2)['articles']:
                
                check_point_flag = False             
                try:                    
                    for oem_loop in  article_list['oemNumbers']:
                                              
                        if oem_loop['articleNumber'] not in already_done:                                                      
                            oem_number = oem_loop['articleNumber']                           
                            already_done.append(oem_number)  
                                                        
                            if (oem_number!=None) and (check_point_flag == False):
                                
                                search_database = Eztb3105.objects.filter(ref2=oem_number)
                                search_database_serializer = Eztb3105Serializer(search_database,many=True)
                                

                                if len(search_database_serializer.data) > 0:                                                                    
                                    find_unique_id = search_database_serializer.data[0].get('uniqueid')
                                    
                                    search_database1 = Eztb3105.objects.filter(uniqueid=find_unique_id)
                                    search_database_serializer1 = Eztb3105Serializer(search_database1,many=True)

                                    for new_loop in search_database_serializer1.data:
                                        check_point_flag = True
                                        new_data = new_loop.copy()
                                        new_data['Quantity_article'] = int(new_data['loc01'])+int(new_data['loc02'])+int(new_data['loc03'])+int(new_data['loc04'])+int(new_data['loc05'])+int(new_data['loc06'])+int(new_data['loc07'])+int(new_data['loc08'])+int(new_data['loc09'])+int(new_data['loc10'])+int(new_data['loc11'])+int(new_data['loc12'])+int(new_data['loc13'])+int(new_data['loc14'])+int(new_data['loc15'])+int(new_data['loc16'])+int(new_data['loc17'])+int(new_data['loc18'])+int(new_data['loc19'])+int(new_data['loc20'])+int(new_data['loc31'])+int(new_data['loc32'])+int(new_data['loc33'])+int(new_data['loc34'])+int(new_data['loc35'])+int(new_data['loc36'])+int(new_data['loc37'])+int(new_data['loc38'])+int(new_data['loc39'])+int(new_data['loc40'])
                                        new_data['images'] = article_list['images']                                    
                                        if new_data['id'] not in filter_done:                                        
                                            macthed_oem_db.append(new_data)
                                            filter_done.append(new_data['id'])
                                           
                            
                                  
                except:
                    oem_number = None

                            

                return Response(macthed_oem_db)

            else:
                return Response({'error':'searchQuery not found'})
        except Exception as E:            
            print(E)
            return Response({'error':'something went wrong'})        



@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
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
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
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
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
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
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
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






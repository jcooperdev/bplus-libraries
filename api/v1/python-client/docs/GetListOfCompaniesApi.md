# swagger_client.GetListOfCompaniesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_get**](GetListOfCompaniesApi.md#companies_get) | **GET** /companies | 
[**groups_get**](GetListOfCompaniesApi.md#groups_get) | **GET** /groups | 
[**users_get**](GetListOfCompaniesApi.md#users_get) | **GET** /users | 


# **companies_get**
> GeneralResponse companies_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetListOfCompaniesApi()

try:
    api_response = api_instance.companies_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetListOfCompaniesApi->companies_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get**
> GeneralResponse groups_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetListOfCompaniesApi()

try:
    api_response = api_instance.groups_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetListOfCompaniesApi->groups_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get**
> GeneralResponse users_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetListOfCompaniesApi()

try:
    api_response = api_instance.users_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetListOfCompaniesApi->users_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


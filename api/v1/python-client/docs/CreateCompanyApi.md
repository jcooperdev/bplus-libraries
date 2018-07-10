# swagger_client.CreateCompanyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_id_contact_get**](CreateCompanyApi.md#companies_id_contact_get) | **GET** /companies/{id}/contact | 
[**companies_id_contact_post**](CreateCompanyApi.md#companies_id_contact_post) | **POST** /companies/{id}/contact | 
[**companies_id_delete**](CreateCompanyApi.md#companies_id_delete) | **DELETE** /companies/{id} | 
[**companies_id_get**](CreateCompanyApi.md#companies_id_get) | **GET** /companies/{id} | 
[**companies_id_post**](CreateCompanyApi.md#companies_id_post) | **POST** /companies/{id} | 
[**companies_post**](CreateCompanyApi.md#companies_post) | **POST** /companies | 
[**groups_id_delete**](CreateCompanyApi.md#groups_id_delete) | **DELETE** /groups/{id} | 
[**groups_id_get**](CreateCompanyApi.md#groups_id_get) | **GET** /groups/{id} | 
[**groups_id_post**](CreateCompanyApi.md#groups_id_post) | **POST** /groups/{id} | 
[**groups_id_toggle_post**](CreateCompanyApi.md#groups_id_toggle_post) | **POST** /groups/{id}/toggle | 
[**groups_id_users_post**](CreateCompanyApi.md#groups_id_users_post) | **POST** /groups/{id}/users | 
[**groups_post**](CreateCompanyApi.md#groups_post) | **POST** /groups | 
[**payments_id_account_post**](CreateCompanyApi.md#payments_id_account_post) | **POST** /payments/{id}/account | 
[**payments_id_deposits_bank_post**](CreateCompanyApi.md#payments_id_deposits_bank_post) | **POST** /payments/{id}/deposits/bank | 
[**payments_id_documents_post**](CreateCompanyApi.md#payments_id_documents_post) | **POST** /payments/{id}/documents | 
[**payments_id_owner_address_post**](CreateCompanyApi.md#payments_id_owner_address_post) | **POST** /payments/{id}/owner/address | 
[**payments_id_owner_post**](CreateCompanyApi.md#payments_id_owner_post) | **POST** /payments/{id}/owner | 
[**payments_id_setting_post**](CreateCompanyApi.md#payments_id_setting_post) | **POST** /payments/{id}/setting | 
[**payments_id_transaction_post**](CreateCompanyApi.md#payments_id_transaction_post) | **POST** /payments/{id}/transaction | 
[**payments_post**](CreateCompanyApi.md#payments_post) | **POST** /payments | 
[**users_id_delete**](CreateCompanyApi.md#users_id_delete) | **DELETE** /users/{id} | 
[**users_id_get**](CreateCompanyApi.md#users_id_get) | **GET** /users/{id} | 
[**users_id_groups_post**](CreateCompanyApi.md#users_id_groups_post) | **POST** /users/{id}/groups | 
[**users_id_post**](CreateCompanyApi.md#users_id_post) | **POST** /users/{id} | 
[**users_id_reset_post**](CreateCompanyApi.md#users_id_reset_post) | **POST** /users/{id}/reset | 
[**users_id_toggle_post**](CreateCompanyApi.md#users_id_toggle_post) | **POST** /users/{id}/toggle | 
[**users_post**](CreateCompanyApi.md#users_post) | **POST** /users | 


# **companies_id_contact_get**
> GeneralResponse companies_id_contact_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 

try:
    api_response = api_instance.companies_id_contact_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->companies_id_contact_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_id_contact_post**
> GeneralResponse companies_id_contact_post(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 
body = swagger_client.Updatecontact() # Updatecontact |  (optional)

try:
    api_response = api_instance.companies_id_contact_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->companies_id_contact_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Updatecontact**](Updatecontact.md)|  | [optional] 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_id_delete**
> GeneralResponse companies_id_delete(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 

try:
    api_response = api_instance.companies_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->companies_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_id_get**
> GeneralResponse companies_id_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 

try:
    api_response = api_instance.companies_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->companies_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_id_post**
> GeneralResponse companies_id_post(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 
body = swagger_client.Updatecompany() # Updatecompany |  (optional)

try:
    api_response = api_instance.companies_id_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->companies_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Updatecompany**](Updatecompany.md)|  | [optional] 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_post**
> GeneralResponse companies_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
body = swagger_client.Createcompany() # Createcompany |  (optional)

try:
    api_response = api_instance.companies_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->companies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Createcompany**](Createcompany.md)|  | [optional] 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_id_delete**
> GeneralResponse groups_id_delete(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 

try:
    api_response = api_instance.groups_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->groups_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_id_get**
> GeneralResponse groups_id_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 

try:
    api_response = api_instance.groups_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->groups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_id_post**
> GeneralResponse groups_id_post(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 
body = swagger_client.Creategroup() # Creategroup |  (optional)

try:
    api_response = api_instance.groups_id_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->groups_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Creategroup**](Creategroup.md)|  | [optional] 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_id_toggle_post**
> GeneralResponse groups_id_toggle_post(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 

try:
    api_response = api_instance.groups_id_toggle_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->groups_id_toggle_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_id_users_post**
> GeneralResponse groups_id_users_post(id, body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 
body = swagger_client.Aclgroup() # Aclgroup | 

try:
    api_response = api_instance.groups_id_users_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->groups_id_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Aclgroup**](Aclgroup.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_post**
> GeneralResponse groups_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
body = swagger_client.Creategroup() # Creategroup |  (optional)

try:
    api_response = api_instance.groups_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Creategroup**](Creategroup.md)|  | [optional] 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_id_account_post**
> GeneralResponse payments_id_account_post(id, body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 
body = swagger_client.Account() # Account | 

try:
    api_response = api_instance.payments_id_account_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->payments_id_account_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Account**](Account.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_id_deposits_bank_post**
> GeneralResponse payments_id_deposits_bank_post(id, body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 
body = swagger_client.Deposits() # Deposits | 

try:
    api_response = api_instance.payments_id_deposits_bank_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->payments_id_deposits_bank_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Deposits**](Deposits.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_id_documents_post**
> GeneralResponse payments_id_documents_post(id, body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 
body = swagger_client.Documents() # Documents | 

try:
    api_response = api_instance.payments_id_documents_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->payments_id_documents_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Documents**](Documents.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_id_owner_address_post**
> GeneralResponse payments_id_owner_address_post(id, body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 
body = swagger_client.Owner() # Owner | 

try:
    api_response = api_instance.payments_id_owner_address_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->payments_id_owner_address_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Owner**](Owner.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_id_owner_post**
> GeneralResponse payments_id_owner_post(id, body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 
body = swagger_client.Ownerr() # Ownerr | 

try:
    api_response = api_instance.payments_id_owner_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->payments_id_owner_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Ownerr**](Ownerr.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_id_setting_post**
> GeneralResponse payments_id_setting_post(id, body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 
body = swagger_client.Setting() # Setting | 

try:
    api_response = api_instance.payments_id_setting_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->payments_id_setting_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Setting**](Setting.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_id_transaction_post**
> GeneralResponse payments_id_transaction_post(id, body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 
body = swagger_client.Transaction() # Transaction | 

try:
    api_response = api_instance.payments_id_transaction_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->payments_id_transaction_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Transaction**](Transaction.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_post**
> GeneralResponse payments_post(id, body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 
body = swagger_client.Merchant() # Merchant | 

try:
    api_response = api_instance.payments_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->payments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Merchant**](Merchant.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_delete**
> GeneralResponse users_id_delete(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 

try:
    api_response = api_instance.users_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->users_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_get**
> GeneralResponse users_id_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 

try:
    api_response = api_instance.users_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->users_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_groups_post**
> GeneralResponse users_id_groups_post(id, body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 
body = swagger_client.Acluser() # Acluser | 

try:
    api_response = api_instance.users_id_groups_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->users_id_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Acluser**](Acluser.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_post**
> GeneralResponse users_id_post(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 
body = swagger_client.Updateuser() # Updateuser |  (optional)

try:
    api_response = api_instance.users_id_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->users_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Updateuser**](Updateuser.md)|  | [optional] 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_reset_post**
> GeneralResponse users_id_reset_post(id, body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 
body = swagger_client.Reset() # Reset | 

try:
    api_response = api_instance.users_id_reset_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->users_id_reset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Reset**](Reset.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_toggle_post**
> GeneralResponse users_id_toggle_post(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
id = 56 # int | 

try:
    api_response = api_instance.users_id_toggle_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->users_id_toggle_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> GeneralResponse users_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateCompanyApi()
body = swagger_client.Createuser() # Createuser |  (optional)

try:
    api_response = api_instance.users_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateCompanyApi->users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Createuser**](Createuser.md)|  | [optional] 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


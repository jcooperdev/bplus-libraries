# PaysafeApi.CreateCompanyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companiesIdContactGet**](CreateCompanyApi.md#companiesIdContactGet) | **GET** /companies/{id}/contact | 
[**companiesIdContactPost**](CreateCompanyApi.md#companiesIdContactPost) | **POST** /companies/{id}/contact | 
[**companiesIdDelete**](CreateCompanyApi.md#companiesIdDelete) | **DELETE** /companies/{id} | 
[**companiesIdGet**](CreateCompanyApi.md#companiesIdGet) | **GET** /companies/{id} | 
[**companiesIdPost**](CreateCompanyApi.md#companiesIdPost) | **POST** /companies/{id} | 
[**companiesPost**](CreateCompanyApi.md#companiesPost) | **POST** /companies | 
[**groupsIdDelete**](CreateCompanyApi.md#groupsIdDelete) | **DELETE** /groups/{id} | 
[**groupsIdGet**](CreateCompanyApi.md#groupsIdGet) | **GET** /groups/{id} | 
[**groupsIdPost**](CreateCompanyApi.md#groupsIdPost) | **POST** /groups/{id} | 
[**groupsIdTogglePost**](CreateCompanyApi.md#groupsIdTogglePost) | **POST** /groups/{id}/toggle | 
[**groupsIdUsersPost**](CreateCompanyApi.md#groupsIdUsersPost) | **POST** /groups/{id}/users | 
[**groupsPost**](CreateCompanyApi.md#groupsPost) | **POST** /groups | 
[**paymentsIdAccountPost**](CreateCompanyApi.md#paymentsIdAccountPost) | **POST** /payments/{id}/account | 
[**paymentsIdDepositsBankPost**](CreateCompanyApi.md#paymentsIdDepositsBankPost) | **POST** /payments/{id}/deposits/bank | 
[**paymentsIdDocumentsPost**](CreateCompanyApi.md#paymentsIdDocumentsPost) | **POST** /payments/{id}/documents | 
[**paymentsIdOwnerAddressPost**](CreateCompanyApi.md#paymentsIdOwnerAddressPost) | **POST** /payments/{id}/owner/address | 
[**paymentsIdOwnerPost**](CreateCompanyApi.md#paymentsIdOwnerPost) | **POST** /payments/{id}/owner | 
[**paymentsIdSettingPost**](CreateCompanyApi.md#paymentsIdSettingPost) | **POST** /payments/{id}/setting | 
[**paymentsIdTransactionPost**](CreateCompanyApi.md#paymentsIdTransactionPost) | **POST** /payments/{id}/transaction | 
[**paymentsPost**](CreateCompanyApi.md#paymentsPost) | **POST** /payments | 
[**usersIdDelete**](CreateCompanyApi.md#usersIdDelete) | **DELETE** /users/{id} | 
[**usersIdGet**](CreateCompanyApi.md#usersIdGet) | **GET** /users/{id} | 
[**usersIdGroupsPost**](CreateCompanyApi.md#usersIdGroupsPost) | **POST** /users/{id}/groups | 
[**usersIdPost**](CreateCompanyApi.md#usersIdPost) | **POST** /users/{id} | 
[**usersIdResetPost**](CreateCompanyApi.md#usersIdResetPost) | **POST** /users/{id}/reset | 
[**usersIdTogglePost**](CreateCompanyApi.md#usersIdTogglePost) | **POST** /users/{id}/toggle | 
[**usersPost**](CreateCompanyApi.md#usersPost) | **POST** /users | 


<a name="companiesIdContactGet"></a>
# **companiesIdContactGet**
> GeneralResponse companiesIdContactGet(id)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.companiesIdContactGet(id, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="companiesIdContactPost"></a>
# **companiesIdContactPost**
> GeneralResponse companiesIdContactPost(id, opts)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 

var opts = { 
  'body': new PaysafeApi.Updatecontact() // Updatecontact | 
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.companiesIdContactPost(id, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 
 **body** | [**Updatecontact**](Updatecontact.md)|  | [optional] 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="companiesIdDelete"></a>
# **companiesIdDelete**
> GeneralResponse companiesIdDelete(id)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.companiesIdDelete(id, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="companiesIdGet"></a>
# **companiesIdGet**
> GeneralResponse companiesIdGet(id)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.companiesIdGet(id, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="companiesIdPost"></a>
# **companiesIdPost**
> GeneralResponse companiesIdPost(id, opts)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 

var opts = { 
  'body': new PaysafeApi.Updatecompany() // Updatecompany | 
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.companiesIdPost(id, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 
 **body** | [**Updatecompany**](Updatecompany.md)|  | [optional] 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="companiesPost"></a>
# **companiesPost**
> GeneralResponse companiesPost(opts)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var opts = { 
  'body': new PaysafeApi.Createcompany() // Createcompany | 
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.companiesPost(opts, callback);
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

<a name="groupsIdDelete"></a>
# **groupsIdDelete**
> GeneralResponse groupsIdDelete(id)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.groupsIdDelete(id, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="groupsIdGet"></a>
# **groupsIdGet**
> GeneralResponse groupsIdGet(id)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.groupsIdGet(id, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="groupsIdPost"></a>
# **groupsIdPost**
> GeneralResponse groupsIdPost(id, opts)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 

var opts = { 
  'body': new PaysafeApi.Creategroup() // Creategroup | 
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.groupsIdPost(id, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 
 **body** | [**Creategroup**](Creategroup.md)|  | [optional] 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="groupsIdTogglePost"></a>
# **groupsIdTogglePost**
> GeneralResponse groupsIdTogglePost(id)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.groupsIdTogglePost(id, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="groupsIdUsersPost"></a>
# **groupsIdUsersPost**
> GeneralResponse groupsIdUsersPost(id, body)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 

var body = new PaysafeApi.Aclgroup(); // Aclgroup | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.groupsIdUsersPost(id, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 
 **body** | [**Aclgroup**](Aclgroup.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="groupsPost"></a>
# **groupsPost**
> GeneralResponse groupsPost(opts)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var opts = { 
  'body': new PaysafeApi.Creategroup() // Creategroup | 
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.groupsPost(opts, callback);
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

<a name="paymentsIdAccountPost"></a>
# **paymentsIdAccountPost**
> GeneralResponse paymentsIdAccountPost(id, body)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 

var body = new PaysafeApi.Account(); // Account | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.paymentsIdAccountPost(id, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 
 **body** | [**Account**](Account.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="paymentsIdDepositsBankPost"></a>
# **paymentsIdDepositsBankPost**
> GeneralResponse paymentsIdDepositsBankPost(id, body)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 

var body = new PaysafeApi.Deposits(); // Deposits | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.paymentsIdDepositsBankPost(id, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 
 **body** | [**Deposits**](Deposits.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="paymentsIdDocumentsPost"></a>
# **paymentsIdDocumentsPost**
> GeneralResponse paymentsIdDocumentsPost(id, body)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 

var body = new PaysafeApi.Documents(); // Documents | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.paymentsIdDocumentsPost(id, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 
 **body** | [**Documents**](Documents.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="paymentsIdOwnerAddressPost"></a>
# **paymentsIdOwnerAddressPost**
> GeneralResponse paymentsIdOwnerAddressPost(id, body)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 

var body = new PaysafeApi.Owner(); // Owner | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.paymentsIdOwnerAddressPost(id, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 
 **body** | [**Owner**](Owner.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="paymentsIdOwnerPost"></a>
# **paymentsIdOwnerPost**
> GeneralResponse paymentsIdOwnerPost(id, body)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 

var body = new PaysafeApi.Ownerr(); // Ownerr | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.paymentsIdOwnerPost(id, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 
 **body** | [**Ownerr**](Ownerr.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="paymentsIdSettingPost"></a>
# **paymentsIdSettingPost**
> GeneralResponse paymentsIdSettingPost(id, body)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 

var body = new PaysafeApi.Setting(); // Setting | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.paymentsIdSettingPost(id, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 
 **body** | [**Setting**](Setting.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="paymentsIdTransactionPost"></a>
# **paymentsIdTransactionPost**
> GeneralResponse paymentsIdTransactionPost(id, body)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 

var body = new PaysafeApi.Transaction(); // Transaction | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.paymentsIdTransactionPost(id, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 
 **body** | [**Transaction**](Transaction.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="paymentsPost"></a>
# **paymentsPost**
> GeneralResponse paymentsPost(id, body)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 

var body = new PaysafeApi.Merchant(); // Merchant | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.paymentsPost(id, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 
 **body** | [**Merchant**](Merchant.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="usersIdDelete"></a>
# **usersIdDelete**
> GeneralResponse usersIdDelete(id)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.usersIdDelete(id, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="usersIdGet"></a>
# **usersIdGet**
> GeneralResponse usersIdGet(id)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.usersIdGet(id, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="usersIdGroupsPost"></a>
# **usersIdGroupsPost**
> GeneralResponse usersIdGroupsPost(id, body)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 

var body = new PaysafeApi.Acluser(); // Acluser | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.usersIdGroupsPost(id, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 
 **body** | [**Acluser**](Acluser.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="usersIdPost"></a>
# **usersIdPost**
> GeneralResponse usersIdPost(id, opts)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 

var opts = { 
  'body': new PaysafeApi.Updateuser() // Updateuser | 
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.usersIdPost(id, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 
 **body** | [**Updateuser**](Updateuser.md)|  | [optional] 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="usersIdResetPost"></a>
# **usersIdResetPost**
> GeneralResponse usersIdResetPost(id, body)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 

var body = new PaysafeApi.Reset(); // Reset | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.usersIdResetPost(id, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 
 **body** | [**Reset**](Reset.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="usersIdTogglePost"></a>
# **usersIdTogglePost**
> GeneralResponse usersIdTogglePost(id)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var id = 56; // Number | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.usersIdTogglePost(id, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="usersPost"></a>
# **usersPost**
> GeneralResponse usersPost(opts)



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.CreateCompanyApi();

var opts = { 
  'body': new PaysafeApi.Createuser() // Createuser | 
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.usersPost(opts, callback);
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


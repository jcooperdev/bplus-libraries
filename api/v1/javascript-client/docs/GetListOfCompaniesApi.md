# PaysafeApi.GetListOfCompaniesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companiesGet**](GetListOfCompaniesApi.md#companiesGet) | **GET** /companies | 
[**groupsGet**](GetListOfCompaniesApi.md#groupsGet) | **GET** /groups | 
[**usersGet**](GetListOfCompaniesApi.md#usersGet) | **GET** /users | 


<a name="companiesGet"></a>
# **companiesGet**
> GeneralResponse companiesGet()



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.GetListOfCompaniesApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.companiesGet(callback);
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

<a name="groupsGet"></a>
# **groupsGet**
> GeneralResponse groupsGet()



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.GetListOfCompaniesApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.groupsGet(callback);
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

<a name="usersGet"></a>
# **usersGet**
> GeneralResponse usersGet()



### Example
```javascript
var PaysafeApi = require('paysafe_api');

var apiInstance = new PaysafeApi.GetListOfCompaniesApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.usersGet(callback);
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


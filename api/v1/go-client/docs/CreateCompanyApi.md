# \CreateCompanyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CompaniesIdContactGet**](CreateCompanyApi.md#CompaniesIdContactGet) | **Get** /companies/{id}/contact | 
[**CompaniesIdContactPost**](CreateCompanyApi.md#CompaniesIdContactPost) | **Post** /companies/{id}/contact | 
[**CompaniesIdDelete**](CreateCompanyApi.md#CompaniesIdDelete) | **Delete** /companies/{id} | 
[**CompaniesIdGet**](CreateCompanyApi.md#CompaniesIdGet) | **Get** /companies/{id} | 
[**CompaniesIdPost**](CreateCompanyApi.md#CompaniesIdPost) | **Post** /companies/{id} | 
[**CompaniesPost**](CreateCompanyApi.md#CompaniesPost) | **Post** /companies | 
[**GroupsIdDelete**](CreateCompanyApi.md#GroupsIdDelete) | **Delete** /groups/{id} | 
[**GroupsIdGet**](CreateCompanyApi.md#GroupsIdGet) | **Get** /groups/{id} | 
[**GroupsIdPost**](CreateCompanyApi.md#GroupsIdPost) | **Post** /groups/{id} | 
[**GroupsIdTogglePost**](CreateCompanyApi.md#GroupsIdTogglePost) | **Post** /groups/{id}/toggle | 
[**GroupsIdUsersPost**](CreateCompanyApi.md#GroupsIdUsersPost) | **Post** /groups/{id}/users | 
[**GroupsPost**](CreateCompanyApi.md#GroupsPost) | **Post** /groups | 
[**PaymentsIdAccountPost**](CreateCompanyApi.md#PaymentsIdAccountPost) | **Post** /payments/{id}/account | 
[**PaymentsIdDepositsBankPost**](CreateCompanyApi.md#PaymentsIdDepositsBankPost) | **Post** /payments/{id}/deposits/bank | 
[**PaymentsIdDocumentsPost**](CreateCompanyApi.md#PaymentsIdDocumentsPost) | **Post** /payments/{id}/documents | 
[**PaymentsIdOwnerAddressPost**](CreateCompanyApi.md#PaymentsIdOwnerAddressPost) | **Post** /payments/{id}/owner/address | 
[**PaymentsIdOwnerPost**](CreateCompanyApi.md#PaymentsIdOwnerPost) | **Post** /payments/{id}/owner | 
[**PaymentsIdSettingPost**](CreateCompanyApi.md#PaymentsIdSettingPost) | **Post** /payments/{id}/setting | 
[**PaymentsIdTransactionPost**](CreateCompanyApi.md#PaymentsIdTransactionPost) | **Post** /payments/{id}/transaction | 
[**PaymentsPost**](CreateCompanyApi.md#PaymentsPost) | **Post** /payments | 
[**UsersIdDelete**](CreateCompanyApi.md#UsersIdDelete) | **Delete** /users/{id} | 
[**UsersIdGet**](CreateCompanyApi.md#UsersIdGet) | **Get** /users/{id} | 
[**UsersIdGroupsPost**](CreateCompanyApi.md#UsersIdGroupsPost) | **Post** /users/{id}/groups | 
[**UsersIdPost**](CreateCompanyApi.md#UsersIdPost) | **Post** /users/{id} | 
[**UsersIdResetPost**](CreateCompanyApi.md#UsersIdResetPost) | **Post** /users/{id}/reset | 
[**UsersIdTogglePost**](CreateCompanyApi.md#UsersIdTogglePost) | **Post** /users/{id}/toggle | 
[**UsersPost**](CreateCompanyApi.md#UsersPost) | **Post** /users | 


# **CompaniesIdContactGet**
> GeneralResponse CompaniesIdContactGet(ctx, id)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CompaniesIdContactPost**
> GeneralResponse CompaniesIdContactPost(ctx, id, optional)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 
 **optional** | ***CompaniesIdContactPostOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a CompaniesIdContactPostOpts struct

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **body** | [**optional.Interface of Updatecontact**](Updatecontact.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CompaniesIdDelete**
> GeneralResponse CompaniesIdDelete(ctx, id)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CompaniesIdGet**
> GeneralResponse CompaniesIdGet(ctx, id)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CompaniesIdPost**
> GeneralResponse CompaniesIdPost(ctx, id, optional)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 
 **optional** | ***CompaniesIdPostOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a CompaniesIdPostOpts struct

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **body** | [**optional.Interface of Updatecompany**](Updatecompany.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CompaniesPost**
> GeneralResponse CompaniesPost(ctx, optional)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***CompaniesPostOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a CompaniesPostOpts struct

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**optional.Interface of Createcompany**](Createcompany.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GroupsIdDelete**
> GeneralResponse GroupsIdDelete(ctx, id)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GroupsIdGet**
> GeneralResponse GroupsIdGet(ctx, id)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GroupsIdPost**
> GeneralResponse GroupsIdPost(ctx, id, optional)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 
 **optional** | ***GroupsIdPostOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a GroupsIdPostOpts struct

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **body** | [**optional.Interface of Creategroup**](Creategroup.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GroupsIdTogglePost**
> GeneralResponse GroupsIdTogglePost(ctx, id)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GroupsIdUsersPost**
> GeneralResponse GroupsIdUsersPost(ctx, id, body)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 
  **body** | [**Aclgroup**](Aclgroup.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GroupsPost**
> GeneralResponse GroupsPost(ctx, optional)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***GroupsPostOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a GroupsPostOpts struct

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**optional.Interface of Creategroup**](Creategroup.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **PaymentsIdAccountPost**
> GeneralResponse PaymentsIdAccountPost(ctx, id, body)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 
  **body** | [**Account**](Account.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **PaymentsIdDepositsBankPost**
> GeneralResponse PaymentsIdDepositsBankPost(ctx, id, body)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 
  **body** | [**Deposits**](Deposits.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **PaymentsIdDocumentsPost**
> GeneralResponse PaymentsIdDocumentsPost(ctx, id, body)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 
  **body** | [**Documents**](Documents.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **PaymentsIdOwnerAddressPost**
> GeneralResponse PaymentsIdOwnerAddressPost(ctx, id, body)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 
  **body** | [**Owner**](Owner.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **PaymentsIdOwnerPost**
> GeneralResponse PaymentsIdOwnerPost(ctx, id, body)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 
  **body** | [**Ownerr**](Ownerr.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **PaymentsIdSettingPost**
> GeneralResponse PaymentsIdSettingPost(ctx, id, body)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 
  **body** | [**Setting**](Setting.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **PaymentsIdTransactionPost**
> GeneralResponse PaymentsIdTransactionPost(ctx, id, body)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 
  **body** | [**Transaction**](Transaction.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **PaymentsPost**
> GeneralResponse PaymentsPost(ctx, id, body)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 
  **body** | [**Merchant**](Merchant.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UsersIdDelete**
> GeneralResponse UsersIdDelete(ctx, id)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UsersIdGet**
> GeneralResponse UsersIdGet(ctx, id)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UsersIdGroupsPost**
> GeneralResponse UsersIdGroupsPost(ctx, id, body)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 
  **body** | [**Acluser**](Acluser.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UsersIdPost**
> GeneralResponse UsersIdPost(ctx, id, optional)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 
 **optional** | ***UsersIdPostOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a UsersIdPostOpts struct

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **body** | [**optional.Interface of Updateuser**](Updateuser.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UsersIdResetPost**
> GeneralResponse UsersIdResetPost(ctx, id, body)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 
  **body** | [**Reset**](Reset.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UsersIdTogglePost**
> GeneralResponse UsersIdTogglePost(ctx, id)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **id** | **int32**|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UsersPost**
> GeneralResponse UsersPost(ctx, optional)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***UsersPostOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a UsersPostOpts struct

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**optional.Interface of Createuser**](Createuser.md)|  | 

### Return type

[**GeneralResponse**](GeneralResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# Tielin.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createlikes**](DefaultApi.md#createlikes) | **POST** /likes | Create a likes
[**createpickupLines**](DefaultApi.md#createpickupLines) | **POST** /pickup_lines | Create a pickup_lines
[**createprofiles**](DefaultApi.md#createprofiles) | **POST** /profiles | Create a profiles
[**deletelikes**](DefaultApi.md#deletelikes) | **DELETE** /likes/{likesId} | Delete a likes
[**deletepickupLines**](DefaultApi.md#deletepickupLines) | **DELETE** /pickup_lines/{pickup_linesId} | Delete a pickup_lines
[**deleteprofiles**](DefaultApi.md#deleteprofiles) | **DELETE** /profiles/{profilesId} | Delete a profiles
[**getalllikes**](DefaultApi.md#getalllikes) | **GET** /likes | List All likes
[**getallpickupLines**](DefaultApi.md#getallpickupLines) | **GET** /pickup_lines | List All pickup_lines
[**getallprofiles**](DefaultApi.md#getallprofiles) | **GET** /profiles | List All profiles
[**getlikes**](DefaultApi.md#getlikes) | **GET** /likes/{likesId} | Get a likes
[**getpickupLines**](DefaultApi.md#getpickupLines) | **GET** /pickup_lines/{pickup_linesId} | Get a pickup_lines
[**getprofiles**](DefaultApi.md#getprofiles) | **GET** /profiles/{profilesId} | Get a profiles
[**updatelikes**](DefaultApi.md#updatelikes) | **PUT** /likes/{likesId} | Update a likes
[**updatepickupLines**](DefaultApi.md#updatepickupLines) | **PUT** /pickup_lines/{pickup_linesId} | Update a pickup_lines
[**updateprofiles**](DefaultApi.md#updateprofiles) | **PUT** /profiles/{profilesId} | Update a profiles


<a name="createlikes"></a>
# **createlikes**
> createlikes(body)

Create a likes

Creates a new instance of a `likes`.

### Example
```javascript
var Tielin = require('tielin');

var apiInstance = new Tielin.DefaultApi();

var body = new Tielin.Likes(); // Likes | A new `likes` to be created.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.createlikes(body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Likes**](Likes.md)| A new `likes` to be created. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="createpickupLines"></a>
# **createpickupLines**
> createpickupLines(body)

Create a pickup_lines

Creates a new instance of a `pickup_lines`.

### Example
```javascript
var Tielin = require('tielin');

var apiInstance = new Tielin.DefaultApi();

var body = new Tielin.PickupLines(); // PickupLines | A new `pickup_lines` to be created.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.createpickupLines(body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PickupLines**](PickupLines.md)| A new `pickup_lines` to be created. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="createprofiles"></a>
# **createprofiles**
> createprofiles(body)

Create a profiles

Creates a new instance of a `profiles`.

### Example
```javascript
var Tielin = require('tielin');

var apiInstance = new Tielin.DefaultApi();

var body = new Tielin.Profiles(); // Profiles | A new `profiles` to be created.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.createprofiles(body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Profiles**](Profiles.md)| A new `profiles` to be created. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="deletelikes"></a>
# **deletelikes**
> deletelikes(likesId)

Delete a likes

Deletes an existing `likes`.

### Example
```javascript
var Tielin = require('tielin');

var apiInstance = new Tielin.DefaultApi();

var likesId = "likesId_example"; // String | A unique identifier for a `likes`.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.deletelikes(likesId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **likesId** | **String**| A unique identifier for a `likes`. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="deletepickupLines"></a>
# **deletepickupLines**
> deletepickupLines(pickupLinesId)

Delete a pickup_lines

Deletes an existing `pickup_lines`.

### Example
```javascript
var Tielin = require('tielin');

var apiInstance = new Tielin.DefaultApi();

var pickupLinesId = "pickupLinesId_example"; // String | A unique identifier for a `pickup_lines`.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.deletepickupLines(pickupLinesId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pickupLinesId** | **String**| A unique identifier for a `pickup_lines`. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="deleteprofiles"></a>
# **deleteprofiles**
> deleteprofiles(profilesId)

Delete a profiles

Deletes an existing `profiles`.

### Example
```javascript
var Tielin = require('tielin');

var apiInstance = new Tielin.DefaultApi();

var profilesId = "profilesId_example"; // String | A unique identifier for a `profiles`.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.deleteprofiles(profilesId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profilesId** | **String**| A unique identifier for a `profiles`. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getalllikes"></a>
# **getalllikes**
> [Likes] getalllikes()

List All likes

Gets a list of all `likes` entities.

### Example
```javascript
var Tielin = require('tielin');

var apiInstance = new Tielin.DefaultApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getalllikes(callback);
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[Likes]**](Likes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getallpickupLines"></a>
# **getallpickupLines**
> [PickupLines] getallpickupLines()

List All pickup_lines

Gets a list of all `pickup_lines` entities.

### Example
```javascript
var Tielin = require('tielin');

var apiInstance = new Tielin.DefaultApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getallpickupLines(callback);
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[PickupLines]**](PickupLines.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getallprofiles"></a>
# **getallprofiles**
> [Profiles] getallprofiles()

List All profiles

Gets a list of all `profiles` entities.

### Example
```javascript
var Tielin = require('tielin');

var apiInstance = new Tielin.DefaultApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getallprofiles(callback);
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[Profiles]**](Profiles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getlikes"></a>
# **getlikes**
> Likes getlikes(likesId)

Get a likes

Gets the details of a single instance of a `likes`.

### Example
```javascript
var Tielin = require('tielin');

var apiInstance = new Tielin.DefaultApi();

var likesId = "likesId_example"; // String | A unique identifier for a `likes`.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getlikes(likesId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **likesId** | **String**| A unique identifier for a `likes`. | 

### Return type

[**Likes**](Likes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getpickupLines"></a>
# **getpickupLines**
> PickupLines getpickupLines(pickupLinesId)

Get a pickup_lines

Gets the details of a single instance of a `pickup_lines`.

### Example
```javascript
var Tielin = require('tielin');

var apiInstance = new Tielin.DefaultApi();

var pickupLinesId = "pickupLinesId_example"; // String | A unique identifier for a `pickup_lines`.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getpickupLines(pickupLinesId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pickupLinesId** | **String**| A unique identifier for a `pickup_lines`. | 

### Return type

[**PickupLines**](PickupLines.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getprofiles"></a>
# **getprofiles**
> Profiles getprofiles(profilesId)

Get a profiles

Gets the details of a single instance of a `profiles`.

### Example
```javascript
var Tielin = require('tielin');

var apiInstance = new Tielin.DefaultApi();

var profilesId = "profilesId_example"; // String | A unique identifier for a `profiles`.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getprofiles(profilesId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profilesId** | **String**| A unique identifier for a `profiles`. | 

### Return type

[**Profiles**](Profiles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="updatelikes"></a>
# **updatelikes**
> updatelikes(likesId, body)

Update a likes

Updates an existing `likes`.

### Example
```javascript
var Tielin = require('tielin');

var apiInstance = new Tielin.DefaultApi();

var likesId = "likesId_example"; // String | A unique identifier for a `likes`.

var body = new Tielin.Likes(); // Likes | Updated `likes` information.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.updatelikes(likesId, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **likesId** | **String**| A unique identifier for a `likes`. | 
 **body** | [**Likes**](Likes.md)| Updated `likes` information. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="updatepickupLines"></a>
# **updatepickupLines**
> updatepickupLines(pickupLinesId, body)

Update a pickup_lines

Updates an existing `pickup_lines`.

### Example
```javascript
var Tielin = require('tielin');

var apiInstance = new Tielin.DefaultApi();

var pickupLinesId = "pickupLinesId_example"; // String | A unique identifier for a `pickup_lines`.

var body = new Tielin.PickupLines(); // PickupLines | Updated `pickup_lines` information.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.updatepickupLines(pickupLinesId, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pickupLinesId** | **String**| A unique identifier for a `pickup_lines`. | 
 **body** | [**PickupLines**](PickupLines.md)| Updated `pickup_lines` information. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="updateprofiles"></a>
# **updateprofiles**
> updateprofiles(profilesId, body)

Update a profiles

Updates an existing `profiles`.

### Example
```javascript
var Tielin = require('tielin');

var apiInstance = new Tielin.DefaultApi();

var profilesId = "profilesId_example"; // String | A unique identifier for a `profiles`.

var body = new Tielin.Profiles(); // Profiles | Updated `profiles` information.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.updateprofiles(profilesId, body, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profilesId** | **String**| A unique identifier for a `profiles`. | 
 **body** | [**Profiles**](Profiles.md)| Updated `profiles` information. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


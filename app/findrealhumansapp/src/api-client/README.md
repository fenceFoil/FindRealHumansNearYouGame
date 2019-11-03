# tielin

Tielin - JavaScript client for tielin
Tech is evil Love is not
This SDK is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/),
please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install tielin --save
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing 
into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

Finally, switch to the directory you want to use your tielin from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

You should now be able to `require('tielin')` in javascript files from the directory you ran the last 
command above from.

#### git
#
If the library is hosted at a git repository, e.g.
https://github.com/YOUR_USERNAME/tielin
then install it via:

```shell
    npm install YOUR_USERNAME/tielin --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file, that's to say your javascript file where you actually 
use this library):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var Tielin = require('tielin');

var api = new Tielin.DefaultApi()

var body = new Tielin.Likes(); // {Likes} A new `likes` to be created.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
api.createlikes(body, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*Tielin.DefaultApi* | [**createlikes**](docs/DefaultApi.md#createlikes) | **POST** /likes | Create a likes
*Tielin.DefaultApi* | [**createpickupLines**](docs/DefaultApi.md#createpickupLines) | **POST** /pickup_lines | Create a pickup_lines
*Tielin.DefaultApi* | [**createprofiles**](docs/DefaultApi.md#createprofiles) | **POST** /profiles | Create a profiles
*Tielin.DefaultApi* | [**deletelikes**](docs/DefaultApi.md#deletelikes) | **DELETE** /likes/{likesId} | Delete a likes
*Tielin.DefaultApi* | [**deletepickupLines**](docs/DefaultApi.md#deletepickupLines) | **DELETE** /pickup_lines/{pickup_linesId} | Delete a pickup_lines
*Tielin.DefaultApi* | [**deleteprofiles**](docs/DefaultApi.md#deleteprofiles) | **DELETE** /profiles/{profilesId} | Delete a profiles
*Tielin.DefaultApi* | [**getalllikes**](docs/DefaultApi.md#getalllikes) | **GET** /likes | List All likes
*Tielin.DefaultApi* | [**getallpickupLines**](docs/DefaultApi.md#getallpickupLines) | **GET** /pickup_lines | List All pickup_lines
*Tielin.DefaultApi* | [**getallprofiles**](docs/DefaultApi.md#getallprofiles) | **GET** /profiles | List All profiles
*Tielin.DefaultApi* | [**getlikes**](docs/DefaultApi.md#getlikes) | **GET** /likes/{likesId} | Get a likes
*Tielin.DefaultApi* | [**getpickupLines**](docs/DefaultApi.md#getpickupLines) | **GET** /pickup_lines/{pickup_linesId} | Get a pickup_lines
*Tielin.DefaultApi* | [**getprofiles**](docs/DefaultApi.md#getprofiles) | **GET** /profiles/{profilesId} | Get a profiles
*Tielin.DefaultApi* | [**updatelikes**](docs/DefaultApi.md#updatelikes) | **PUT** /likes/{likesId} | Update a likes
*Tielin.DefaultApi* | [**updatepickupLines**](docs/DefaultApi.md#updatepickupLines) | **PUT** /pickup_lines/{pickup_linesId} | Update a pickup_lines
*Tielin.DefaultApi* | [**updateprofiles**](docs/DefaultApi.md#updateprofiles) | **PUT** /profiles/{profilesId} | Update a profiles


## Documentation for Models

 - [Tielin.Likes](docs/Likes.md)
 - [Tielin.PickupLines](docs/PickupLines.md)
 - [Tielin.Profiles](docs/Profiles.md)


## Documentation for Authorization

 All endpoints do not require authorization.

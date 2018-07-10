/**
 * Paysafe Api
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 0.0.1
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.0-SNAPSHOT
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.PaysafeApi);
  }
}(this, function(expect, PaysafeApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new PaysafeApi.Setting();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('Setting', function() {
    it('should create an instance of Setting', function() {
      // uncomment below and update the code to test Setting
      //var instance = new PaysafeApi.Setting();
      //expect(instance).to.be.a(PaysafeApi.Setting);
    });

    it('should have the property currency (base name: "currency")', function() {
      // uncomment below and update the code to test the property currency
      //var instance = new PaysafeApi.Setting();
      //expect(instance).to.be();
    });

    it('should have the property amexId (base name: "amex_id")', function() {
      // uncomment below and update the code to test the property amexId
      //var instance = new PaysafeApi.Setting();
      //expect(instance).to.be();
    });

    it('should have the property descriptor (base name: "descriptor")', function() {
      // uncomment below and update the code to test the property descriptor
      //var instance = new PaysafeApi.Setting();
      //expect(instance).to.be();
    });

    it('should have the property locale (base name: "locale")', function() {
      // uncomment below and update the code to test the property locale
      //var instance = new PaysafeApi.Setting();
      //expect(instance).to.be();
    });

    it('should have the property lang (base name: "lang")', function() {
      // uncomment below and update the code to test the property lang
      //var instance = new PaysafeApi.Setting();
      //expect(instance).to.be();
    });

    it('should have the property descriptorPhone (base name: "descriptor_phone")', function() {
      // uncomment below and update the code to test the property descriptorPhone
      //var instance = new PaysafeApi.Setting();
      //expect(instance).to.be();
    });

  });

}));

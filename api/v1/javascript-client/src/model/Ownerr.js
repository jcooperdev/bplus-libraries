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
    // AMD. Register as an anonymous module.
    define(['ApiClient'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'));
  } else {
    // Browser globals (root is window)
    if (!root.PaysafeApi) {
      root.PaysafeApi = {};
    }
    root.PaysafeApi.Ownerr = factory(root.PaysafeApi.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';




  /**
   * The Ownerr model module.
   * @module model/Ownerr
   * @version 0.0.1
   */

  /**
   * Constructs a new <code>Ownerr</code>.
   * @alias module:model/Ownerr
   * @class
   * @param nameFirst {String} 
   * @param nameLast {String} 
   * @param jobTitle {String} 
   * @param day {String} 
   * @param month {String} 
   * @param year {String} 
   * @param gender {String} 
   * @param nationality {String} 
   * @param taxid {String} 
   * @param percentage {String} 
   */
  var exports = function(nameFirst, nameLast, jobTitle, day, month, year, gender, nationality, taxid, percentage) {
    var _this = this;

    _this['name_first'] = nameFirst;
    _this['name_last'] = nameLast;
    _this['job_title'] = jobTitle;
    _this['day'] = day;
    _this['month'] = month;
    _this['year'] = year;
    _this['gender'] = gender;
    _this['nationality'] = nationality;
    _this['taxid'] = taxid;
    _this['percentage'] = percentage;
  };

  /**
   * Constructs a <code>Ownerr</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/Ownerr} obj Optional instance to populate.
   * @return {module:model/Ownerr} The populated <code>Ownerr</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('name_first')) {
        obj['name_first'] = ApiClient.convertToType(data['name_first'], 'String');
      }
      if (data.hasOwnProperty('name_last')) {
        obj['name_last'] = ApiClient.convertToType(data['name_last'], 'String');
      }
      if (data.hasOwnProperty('job_title')) {
        obj['job_title'] = ApiClient.convertToType(data['job_title'], 'String');
      }
      if (data.hasOwnProperty('day')) {
        obj['day'] = ApiClient.convertToType(data['day'], 'String');
      }
      if (data.hasOwnProperty('month')) {
        obj['month'] = ApiClient.convertToType(data['month'], 'String');
      }
      if (data.hasOwnProperty('year')) {
        obj['year'] = ApiClient.convertToType(data['year'], 'String');
      }
      if (data.hasOwnProperty('gender')) {
        obj['gender'] = ApiClient.convertToType(data['gender'], 'String');
      }
      if (data.hasOwnProperty('nationality')) {
        obj['nationality'] = ApiClient.convertToType(data['nationality'], 'String');
      }
      if (data.hasOwnProperty('taxid')) {
        obj['taxid'] = ApiClient.convertToType(data['taxid'], 'String');
      }
      if (data.hasOwnProperty('percentage')) {
        obj['percentage'] = ApiClient.convertToType(data['percentage'], 'String');
      }
    }
    return obj;
  }

  /**
   * @member {String} name_first
   */
  exports.prototype['name_first'] = undefined;
  /**
   * @member {String} name_last
   */
  exports.prototype['name_last'] = undefined;
  /**
   * @member {String} job_title
   */
  exports.prototype['job_title'] = undefined;
  /**
   * @member {String} day
   */
  exports.prototype['day'] = undefined;
  /**
   * @member {String} month
   */
  exports.prototype['month'] = undefined;
  /**
   * @member {String} year
   */
  exports.prototype['year'] = undefined;
  /**
   * @member {String} gender
   */
  exports.prototype['gender'] = undefined;
  /**
   * @member {String} nationality
   */
  exports.prototype['nationality'] = undefined;
  /**
   * @member {String} taxid
   */
  exports.prototype['taxid'] = undefined;
  /**
   * @member {String} percentage
   */
  exports.prototype['percentage'] = undefined;



  return exports;
}));



import DS from "ember-data";
import Ember from 'ember';
import AppENV from "../config/environment";

export default DS.RESTAdapter.extend({
	host                 : AppENV.APP.apihost,
	namespace            : AppENV.APP.apinamespace,
	coalesceFindRequests : true,
});
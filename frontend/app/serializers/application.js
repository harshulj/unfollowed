import DS 	 from "ember-data";
import Ember from 'ember';

export default DS.RESTSerializer.extend({
	extractSingle :  function(store, primaryType, payload, recordId){
		var data = payload._data;
	    return this._super(store, type, data, id);
	},
	extractArray : function(store, primaryType, payload){
		var data = payload._data;
		return this._super(store, type, data);
	}
});
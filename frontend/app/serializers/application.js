import DS 	 from "ember-data";
import Ember from 'ember';

export default DS.RESTSerializer.extend({
	extractSingle : function(store, type, payload, id){
		var data = {};
		data[type.typeKey] = payload._data;
	    return this._super(store, type, data, id);
	},
	extractArray : function(store, type, payload){
		var data = {};
		if(!Ember.isArray(payload._data))
			payload._data = [payload._data];
		data[Ember.String.pluralize(type.typeKey)] = payload._data;
		return this._super(store, type, data);
	}
});
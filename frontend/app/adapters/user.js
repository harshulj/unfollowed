import Ember from 'ember';
import AppAdapter from './application';

export default AppAdapter.extend({
	find: function(store, type, id, record) {
		var url = this.buildURL(type.typeKey);
	    return this.ajax(url, 'GET');
	}
});
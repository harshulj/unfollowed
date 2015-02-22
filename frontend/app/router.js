import Ember from 'ember';
import config from './config/environment';

var Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
	this.resource('user',{path:'/:user_handle'},function(){
		this.route("settings", { path: "/settings"});
	});
	this.route('catchall', {path: '/*wildcard'});
});

export default Router;

import Ember 			from 'ember';
import Resolver 		from 'ember/resolver';
import loadInitializers from 'ember/load-initializers';
import config 			from './config/environment';

Ember.MODEL_FACTORY_INJECTIONS = true;

var App = Ember.Application.extend({
	modulePrefix    : config.modulePrefix,
	podModulePrefix : config.podModulePrefix,
	Resolver        : Resolver
});

loadInitializers(App, config.modulePrefix);

$(function(){
	if($.cookie && typeof $.cookie === 'function'){
		var token = $.cookie('csrftoken');
	  	$.ajaxPrefilter(function(options, originalOptions, xhr){
	    	if(["PUT","POST"].indexOf(originalOptions.type)!=-1) //set for PUT/POST requests only
	    		xhr.setRequestHeader('X-CSRF-Token', token)
	  	});	
	}
	else
		console.log("cookie plugin not found. PUT/POST requests might not work.");
	
});

export default App;

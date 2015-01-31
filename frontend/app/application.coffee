
Router = require 'router'

App = 
	event : _.extend({}, Backbone.Events)
	initialize : ->
		@router = new Router()

module.exports = App
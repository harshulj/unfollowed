App = require('application')

$ ->
	application = new App()
	application.initialize()
	Backbone.history.start()
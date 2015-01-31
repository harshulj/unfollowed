ApplicationView = require('./views/application')

class MainRouter extends Backbone.Router
	routes:
		'' : 'index'
	index : =>
		@index_view = new ApplicationView()

module.exports = MainRouter



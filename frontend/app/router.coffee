MainView = require './views/main'

class MainRouter extends Backbone.Router
	routes:
		'' : 'index'
	index : =>
		@index_view = new MainView()

module.exports = MainRouter



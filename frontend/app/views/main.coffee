template = require './templates/home'

class MainView extends Backbone.View
	template : template
	el       : "#application-container"
	
	project_name : 'Brunch with Backbone'

	initialize : ()=>
		@render()

	render : ()=>
		$('body').append(@template({project_name: @project_name}))

module.exports = MainView

	
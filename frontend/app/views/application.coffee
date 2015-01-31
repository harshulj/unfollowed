template = require './templates/application'

class ApplicationView extends Backbone.View
	template : template
	el       : "#application-container"
	
	project_name : 'Brunch with Backbone'

	initialize : ()=>
		@render()

	render : ()=>
		$('body').append(@template({project_name: @project_name}))

module.exports = ApplicationView

	
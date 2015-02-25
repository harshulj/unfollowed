import Ember from "ember";

export default Ember.Route.extend(TitledRoute,{
	header_text : "Settings",
	model: function(){
		return this.modelFor('user');
	}
});
import Ember from "ember";
import TitledRoute from 'unfollwed/mixins/titled-route';

export default Ember.Route.extend(TitledRoute,{
	header_text : "Settings",
	model: function(){
		return this.modelFor('user');
	}
});
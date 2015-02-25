import Ember from 'ember';
import TitledRoute from 'unfollwed/mixins/titled-route';

export default Ember.Route.extend(TitledRoute,{
	header_text : 'Followers',
	afterModel : function(){
		// return new Ember.RSVP.Promise(function(resolve,reject){
		// 	console.log('a');
		// });
		return this.store.findQuery('profile',{appendUrl:"twitter/follow"});
	},
	setupController : function(controller,model){
		this._super(controller,model);
		controller.set('profiles',this.store.all('profile'));
	}
});
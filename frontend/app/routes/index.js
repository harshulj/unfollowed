import Ember from "ember";

export default Ember.Route.extend({
	beforeModel: function(){
		var session = this.get('session'),
			self = this;

		return this.store.findQuery('user',{appendUrl:''}).then(function(data){
			var user = data.content[0];
			if(user){
				session.set('active_user',user);
				self.replaceWith('user',user);
			}
			else
				self.send('error');
			return user;
		},function(error){
			self.send('error',error);
			return error;
		});
	}
});
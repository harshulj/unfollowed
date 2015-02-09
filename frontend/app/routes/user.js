import Ember from 'ember';

export default Ember.Route.extend({
	beforeModel: function(){
		console.log('before model of user called');
		var session = this.get('session'),
			self = this;
		
		if(session.get('active_user'))
			return;

		return this.store.findQuery('user',{appendUrl:''}).then(function(data){
			var user = data.content[0];
			if(user)
				session.set('active_user',user);
			else
				self.send('error');
			return user;
		},function(error){
			self.send('error',error);
			return error;
		});
	},
	model: function(params){
		return this.get('session').get('active_user');
	},
	serialize : function(model){
		return {user_handle:model.get('handle')}
	}
});
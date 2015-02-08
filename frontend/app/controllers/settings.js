import Ember from 'ember';

export default Ember.Controller.extend({
	new_email: null,
	reset_hash : {
		new_email : null,
	},
	actions:{
		updateUser: function(){
			var user 			= this.get('model'),
				new_email 		= this.get('new_email'),
				current_email 	= user.get('email'),
				self 			= this;
			
			if(new_email){
				user.set('email',new_email);
				user.save().then(function(record){
					console.log(record);
					self.reset();
				},function(error){
					console.log(error,'error occured while updating user');
					user.set('email',current_email);
					console.log(user.get('errors'));
					return error;
				});
			}
		}
	},
	reset : function(){
		this.setProperties(this.get('reset_hash'));
	}
});
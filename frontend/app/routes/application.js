import Ember from "ember";

export default Ember.Route.extend({
	actions: {
		error: function(e){
			console.log(e,'error occured');
			if(e.status === 404)
				//reload the page and hit index if any errors occur due to unauthorized state of user.
				window.open("/","_self"); 
			else
				this.transitionTo('catchall', "application-error");
		}
	}
});
import Ember from 'ember';

export default Ember.Controller.extend({
	side_nav_on : false,
	actions : {
		toggleSideNav : function(){
			this.toggleProperty('side_nav_on');
		}
	}
});
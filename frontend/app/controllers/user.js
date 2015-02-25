import Ember from 'ember';

export default Ember.Controller.extend({
	header_text    : "",
	model          : null,
	show_user_menu : false,
	actions : {
		toggleUserMenu : function(){
			this.toggleProperty('show_user_menu');
			return false;
		}
	}
});
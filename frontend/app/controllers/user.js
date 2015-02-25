import Ember from 'ember';

export default Ember.Controller.extend({
	needs          : ['application'],
	header_text    : "",
	model          : null,
	show_user_menu : false,
	side_nav_on    : Ember.computed.alias('controllers.application.side_nav_on'),
	actions : {
		toggleUserMenu : function(){
			this.toggleProperty('show_user_menu');
		},
		toggleSideNav : function(){
			this.get('controllers.application').toggleProperty('side_nav_on');
		}
	}
});
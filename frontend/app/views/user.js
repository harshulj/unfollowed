import Ember from 'ember';

export default Ember.View.extend({
	click : function(evt){
		console.log('yo');
		if(!$(evt.target).hasClass('user-menu-toggle'))
			this.get('controller').set('show_user_menu',false);
	}
});
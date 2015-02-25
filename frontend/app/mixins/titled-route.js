import Ember from 'ember';

export default Ember.Mixin.create({
	beforeModel: function(){
		if(this.get('header_text') && this.controllerFor('user'))
			this.controllerFor('user').set('header_text',this.get('header_text'));
	},
});
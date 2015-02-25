import Ember from "ember";

export default Ember.View.extend({
	elementId         : 'application-container',
	classNameBindings : ['sideNavOn'],
	sideNavOn         : Ember.computed.alias('controller.side_nav_on')
});
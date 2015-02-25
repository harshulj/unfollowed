import DS from "ember-data";
import Em from "ember";

export default DS.Model.extend({
	name     : DS.attr('string'),
	username : DS.attr('string'),
	picture  : DS.attr('string'),
	email    : DS.attr('string'),
	profiles : DS.attr('raw'),
	handle : (function(){
		//for now prepend '@' as we have only twitter users. 
		return "@"+this.get('username');
	}).property('username')
});
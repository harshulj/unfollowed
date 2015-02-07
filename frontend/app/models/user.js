import DS from "ember-data";
import Em from "ember";

export default DS.Model.extend({
	name     : DS.attr('string'),
	username : DS.attr('string'),
	picture  : DS.attr('string'),
	email    : DS.attr('string')
});
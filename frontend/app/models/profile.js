import Ember from 'ember';
import DS from 'ember-data';
import AppENV from 'unfollwed/config/environment';

export default DS.Model.extend({
	username    : DS.attr('string'),
	picture     : DS.attr('string'),
	url         : DS.attr('string'),
	name        : DS.attr('string'),
	action_time : DS.attr('date'),
	action      : DS.attr('string'),
	json        : DS.attr('string'),
	network     : DS.attr('string',{defaultValue:'twitter'}), //currently hard coding twitter here later on get this from backend.
	banner_url  : DS.attr('string',{defaultValue:'https://pbs.twimg.com/profile_banners/35189167/1411753030/600x200'}),
	description : DS.attr('string',{defaultValue:'The best new products, every day. San Francisco, CA'}),
	profile_url : (function(){
		if(this.get('username') && this.get('network'))
			return AppENV.APP.profile_url_prefix_map[this.get('network')]+this.get('username');
		return "";
	}).property('username','network'),
	user_handle : (function(){
		if(this.get('network')=='twitter')
			return "@"+this.get('username');
		return this.get('username');
	}).property('network','username'),
	cover_url : (function(){
		return "background-image: url("+this.get('banner_url')+");";
	}).property('banner_url')
});
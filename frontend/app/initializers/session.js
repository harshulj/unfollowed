import Session from "../controllers/session";

export default {
   name: 'session',
   initialize: function(container, application) {
	    container.register('controller:session', Session, { singleton: true,instantiate: true });
	    application.inject('model', 'session', 'controller:session');
	    application.inject('route', 'session', 'controller:session');
   }
};
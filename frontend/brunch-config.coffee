exports.config =
  # See http://brunch.io/#documentation for docs.
  paths: 
    public : '../backend/static/'
  files:
    javascripts:
      joinTo:
        'javascripts/app.js': /^app/
        'javascripts/vendor.js': /^(?!app)/
      order:
        before: [
          'vendor/scripts/console-helper.js',
          'vendor/scripts/jquery-1.11.2.js',
          'vendor/scripts/underscore.js',
          'vendor/scripts/backbone.js',
          'vendor/scripts/rsvp.min.js'
        ]

    stylesheets:
      defaltExtension: 'less'
      joinTo: 
        'stylesheets/app.css' : /^app\/styles/
        'stylesheets/vendor.css' : /^vendor\/styles/

    templates:
      defaultExtension: 'hbs'
      joinTo: 'javascripts/app.js'

  framework: 'backbone'
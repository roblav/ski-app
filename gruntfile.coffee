module.exports = (grunt) ->

  # task configurations
  # initializing task configuration
  grunt.initConfig

    # configure nodemon
    nodemon:
      dev:
        script: 'server.js'

  # loading local tasks
  # grunt.loadTasks "tasks"

  # loading external tasks (aka: plugins)
  grunt.loadNpmTasks('grunt-nodemon');

  # creating workflows
  grunt.registerTask "default", ["nodemon"]

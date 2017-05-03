
module.exports = function(grunt) {

    var prod = 'prod/';
    var js = 'static/js/'
    var css = 'static/css/'
    var imgSrc = 'static/imgSrc/'
    var img = 'static/img/'


    grunt.initConfig({
        //JS-Linter
        jshint: {
            all: [js + '*.js']
        },

        // css-linter
        csslint: {
            strict: {
                options: {
                    important: 2
                },
            src: css + '*.css',
            }
        },

        //Minify js
        uglify: {
            my_target: {
                files: {
                    // 'prod/static/js/app.js': ['static/js/app.js']
                    prod + js + 'app.js': [js + '*.js']
                }
            }
        },

        // Post-css prefixes
        // runs autoprefixer and cssnano
        postcss: {
            options: {
              map: true,
              processors: [
                require('autoprefixer')({browsers: ['last 2 version']}),
                require('cssnano')()
              ]
            },

            dist: {
                src: css + '*.css',
                dest: prod + css + 'style.css'
            }
        },


          /* Clear out the images directory if it exists */
        clean: {
            dev: {
                src: [img],
            },
        },

        responsive_images: {
          dev: {
            options: {
              engine: 'gm',
              aspectRatio: false,
              upscale: true,
              sizes:[{
                name: 'sqtiny',
                width: '100px',
                height: '100px',
                quality: 40
              },{
                name: 'sqsmall',
                width: '200px',
                height: '200px',
                quality: 40
              },{
                name: 'sqmedium',
                width: '400px',
                height: '400px',
                quality: 40
              },{
                name: 'sqlarge',
                width: '600px',
                height: '600px',
                quality: 40
              },{
                name: 'small',
                width: '600px',
                quality: 70
              }
              ,{
                name: 'medium',
                width: '1200px',
                quality: 70
              },{
                name: 'large',
                width: '2400px',
                quality: 70
              }]
            },

            /*
            You don't need to change this part if you don't change
            the directory structure.
            */
            files: [{
              expand: true,
              src: ['*.{gif,jpg,png}'],
              cwd: imgSrc,
              dest: img
            }]
          }
        },



    });

    require('load-grunt-tasks')(grunt);
    grunt.registerTask('default', ['csslint', 'postcss', 'responsive_images']);
    grunt.registerTask('images', ['clean', 'responsive_images']);
    grunt.registerTask('lint', ['jshint', 'csslint']);
    grunt.registerTask('js', ['jshint', 'uglify']);

};

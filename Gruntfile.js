
module.exports = function(grunt) {

    var prod = 'prod/';
    var css = 'static/css/'
    var imgSrc = 'static/imgSrc/'
    var img = 'static/img/'

    grunt.initConfig({

        // css-linter
        csslint: {
          strict: {
            options: {
              important: 2
            },
            src: css + '*.css',
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


        responsive_images: {
          dev: {
            options: {
              engine: 'gm',
              sizes:[{
                name: 'small',
                width: '200px',
                upscale: 'true',
                quality: 40
              },{
                name: 'small2x',
                width: '400px',
                upscale: 'true',
                quality: 40
              },{
                name: 'medium',
                width: '300px',
                upscale: 'true',
                quality: 50
              },{
                name: 'medium2x',
                width: '600px',
                upscale: 'true',
                quality: 50
              },{
                name: 'large',
                width: '500px',
                upscale: 'true',
                quality: 60
              },{
                name: 'large2x',
                width: '1000px',
                upscale: 'true',
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

};

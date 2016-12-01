var gulp = require('gulp'),
    concat = require('gulp-concat'),
    del = require('del'),
    cssnano = require('gulp-cssnano'),
    concat = require('gulp-concat'),
    sass = require('gulp-sass'),
    watch = require('gulp-watch');


var root = './';
var assetsRoot = './assets/'
var staticRoot = './thirteen/static/';

var dependencyDirs = [
    root + 'bower_components/',
    root + 'node_modules/'
];

var staticDirs = {
    styles: staticRoot + 'styles/',
    images: staticRoot + 'images/',
    scripts: {

    }
};

// this is the default task that's run when you 
// run the command 'gulp'
gulp.task('default', ['sass', 'watch']);

gulp.task('clean', ['clean-static']);

gulp.task('clean-static', function () {
    return del(staticRoot + '**/*');
});


gulp.task('clean-dependencies', function () {
    return del(dependencyDirs.map(function(dir) {
        return dir + '**/*';
    }));
});

gulp.task('sass', function () {
    gulp.src(assetsRoot + 'style/**/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(concat('style.css'))
        .pipe(cssnano())
        .pipe(gulp.dest(staticDirs.styles));
});

gulp.task('watch', ['watch-sass']);

gulp.task('watch-sass', function () {
  gulp.watch(assetsRoot + 'style/**/*.scss', ['sass']);
});
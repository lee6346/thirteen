var gulp = require('gulp'),
    concat = require('gulp-concat'),
    cssMin = require('gulp-cssmin'),
    debug = require('gulp-debug'),
    del = require('del'),
    fileExists = require('file-exists'),
    less = require('gulp-less'),
    rename = require('gulp-rename'),
    sourcemaps = require('gulp-sourcemaps'),
    uglify = require('gulp-uglify'),
    wrapper = require('gulp-wrapper');

var webroot = 'root of static web';

// delete all dirs and files within the webroot/static
gulp.task('clean', function() {
    return del(webroot + '**/*');
});
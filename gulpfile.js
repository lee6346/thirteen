var gulp = require('gulp'),
    concat = require('gulp-concat'),
    del = require('del'),
    cssnano = require('gulp-cssnano'),
    concat = require('gulp-concat'),
    sass = require('gulp-sass'),
    watch = require('gulp-watch');

var root = './';
var assetsRoot = './thirteen/assets/';
var staticRoot = './thirteen/static/';
var imageDir = './thirteen/assets/images/';

var npmDir = root + 'node_modules/';

var staticDirs = {
    styles: staticRoot + 'styles/',
    images: staticRoot + 'images/',
    fonts: staticRoot + 'fonts/',
    scripts: {
        libraries: staticRoot + 'scripts/libraries/',
        custom: staticRoot + 'scripts/'
    }
};

var npm = {
    scripts: [
        npmDir + 'angular/angular.js',
        npmDir + 'angular-ui-router/release/angular-ui-router.js',
        npmDir + 'jquery/dist/jquery.js',
        npmDir + 'bootstrap/dist/js/bootstrap.js',
        npmDir + 'angular-ui-bootstrap/dist/ui-bootstrap-tpls.js'
    ],
    styles: [
        npmDir + 'bootstrap/dist/css/bootstrap.css',
        npmDir + 'font-awesome/css/font-awesome.css',
        npmDir + 'roboto-fontface/css/roboto/roboto-fontface.css'
    ],
    fonts: [
        npmDir + 'bootstrap/dist/fonts/',
        npmDir + 'font-awesome/fonts/',
        npmDir + 'roboto-fontface/fonts/Roboto/'
    ]
};

var getCustomScripts = function() {
    var baseJsDir = assetsRoot + 'js/';

    var moduleDirs = [
        'main',
        'lobby', 
        'table',
        'modals'
    ];

    return moduleDirs.map(function(dir) {
        return baseJsDir + dir + '/*.js';
    });
};




// this is the default task that's run when you 
// run the command 'gulp'
gulp.task('default', ['copy', 'watch']);

gulp.task('clean', ['clean-static']);

gulp.task('clean-static', function() {
    return del(staticRoot + '**/*');
});

// removes everything from node_modules
gulp.task('clean-dependencies', function() {
    return del([npmDir].map(function(dir) {
        return dir + '**/*';
    }));
});

gulp.task('copy', [
    'copy-custom-sass',
    'copy-library-scripts',
    'copy-custom-scripts',
    'copy-library-styles',
    'copy-fonts',
    'copy-images'
]);

gulp.task('copy-custom-sass', function() {
    gulp.src(assetsRoot + 'style/**/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(concat('style.css'))
        .pipe(cssnano())
        .pipe(gulp.dest(staticDirs.styles));
});

gulp.task('copy-library-scripts', function() {
    gulp.src(npm.scripts)
        //.pipe(concat('libraries.js'))
        .pipe(gulp.dest(staticDirs.scripts.libraries));
});

gulp.task('copy-custom-scripts', function() {
    gulp.src(getCustomScripts())
        .pipe(concat('tt-main.js'))
        .pipe(gulp.dest(staticDirs.scripts.custom));
});

gulp.task('copy-library-styles', function() {
    gulp.src(npm.styles)
        .pipe(concat('libraries.css'))
        .pipe(cssnano())
        .pipe(gulp.dest(staticDirs.styles));
});

gulp.task('copy-fonts', function() {
    var fontDirExpressions = npm.fonts.map(function(fontDir) {
        return fontDir + '**/*';
    });

    gulp.src(fontDirExpressions)
        .pipe(gulp.dest(staticDirs.fonts));
});

gulp.task('copy-images', function(){
    gulp.src(imageDir + '**/*')
        .pipe(gulp.dest(staticDirs.images));
});

gulp.task('watch', ['watch-sass', 'watch-custom-scripts']);

gulp.task('watch-sass', function() {
    gulp.watch(assetsRoot + 'style/**/*.scss', ['copy-custom-sass']);
});

gulp.task('watch-custom-scripts', function() {
    gulp.watch(assetsRoot + 'js/**/*.js', ['copy-custom-scripts']);
});
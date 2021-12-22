const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const sourcemaps = require('gulp-sourcemaps');


const SCSSCmplCmpr = () => {
    return gulp.src('./scss/**/*.scss')
        .pipe(sourcemaps.init())
        .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest('./css'));
}

const SCSSCmpl = () => {
    return gulp.src('./scss/*.scss')
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest('./css'));
}
exports.scss = SCSSCmplCmpr;

const watch = () => {
    gulp.watch('scss/**/*.scss', gulp.series(SCSSCmpl));
}

exports.watch = watch;

exports.default = gulp.series(
    SCSSCmplCmpr,
    watch
);
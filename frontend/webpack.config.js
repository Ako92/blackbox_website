var path = require('path');
var webpack = require('webpack');
var debug = process.env.NODE_ENV !== "production";

module.exports = {
  context: __dirname + "/src",
    devtool: debug ? "inline-sourcemap": null ,
      entry: "./js/client.js",
  module:{
    loaders: [
        {
          test: /\.css$/,
            loader:'style!css!',
        },

        {
          test:/\.js?$/,
            exclude: /(node_module|bower_components)/,
            loader: 'babel-loader',
            query:{
            presets:['react', 'es2015', 'stage-0'],
                plugins:['react-html-attrs', 'transform-class-properties', 'transform-decorators-legacy']
            }
        }
    ]

  },
    output: {
    path: __dirname + "/src/",
        filename: 'client.min.js'
  },
    plugins: debug ? [] : [
            new webpack.optimize.DedupePlugin(),
            new webpack.optimize.OccurrenceOrderPlugin,
            new webpack.optimize.UglifyJsPlugin({ mangle:false, sourcemap: false }),
        ],
};

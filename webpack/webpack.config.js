var SpritesmithPlugin = require('webpack-spritesmith');
module.exports = {
  entry: [
    './app/img/ministry-icon.png',
    './app/img/planalto-icon.png',
    './app/portalmdh.scss',
    './app/portalmdh.js',
  ],
  output: {
    filename: 'portalmdh.js',
    library: 'portalmdh',
    libraryTarget: 'umd',
    path: __dirname + '/../src/governo/mdh/portal/browser/static',
    pathinfo: true,
    publicPath: '/++resource++portalmdh/'
  },
  resolve: {
    extensions: ['.js'],
    modules: [
      __dirname,
      __dirname + './node_modules'
    ]
  },
  module: {
    rules: [{
      test: /\.html$/,
      use: [
        {
          loader: 'file-loader',
          options: {
            name: '[name].[ext]',
          }
        },
        'extract-loader',
        {
          loader: 'html-loader',
          options: {
            minimize: false
          }
        },
      ]
    }, {
      test: /\.js$/,
      exclude: /(\/node_modules\/|test\.js$|\.spec\.js$)/,
      use: 'babel-loader',
    }, {
      test: /\.scss$/,
      use: [
        {
          loader: 'file-loader',
          options: {
            name: '[name].css',
          }
        },
        'extract-loader',
        'css-loader',
        'postcss-loader',
        'sass-loader'
      ]
    }, {
      test: /.*\.(gif|png|jpe?g)$/i,
      use: [
        {
          loader: 'file-loader',
          options: {
            name: '[path][name].[ext]',
            context: 'app/'
          }
        },
        {
          loader: 'image-webpack-loader',
          query: {
            mozjpeg: {
              progressive: true,
            },
            pngquant: {
              quality: '65-90',
              speed: 4
            },
            gifsicle: {
              interlaced: false
            },
            optipng: {
              optimizationLevel: 7
            }
          }
        }
      ]
    }, {
      test: /\.svg/,
      exclude: /node_modules/,
      use: 'svg-url-loader'
    }]
  },
  devtool: 'source-map',
  plugins: [
    new SpritesmithPlugin({
      src: {
        cwd: 'app/sprite',
        glob: '*.png'
      },
      target: {
        image: 'app/img/sprite.png',
        css: 'app/scss/_sprite.scss'
      },
      apiOptions: {
        cssImageRef: './img/sprite.png'
      }
    })
  ]
}
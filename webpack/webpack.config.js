const makeConfig = require('sc-recipe-staticresources');
const CopyWebpackPlugin = require('copy-webpack-plugin');


module.exports = makeConfig(
  // name
  'governo.mdh.portal',

  // shortName
  'governomdhportal',

  // path
  `${__dirname}/../src/governo/mdh/portal/browser/static`,

  //publicPath
  '++resource++governo.mdh.portal/',
  
);

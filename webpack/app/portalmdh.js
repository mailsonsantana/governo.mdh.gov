import ContentCentral from './js/contentcentral.js';
import Ministers from './js/ministerios.js'
import SocialLike from './js/sociallike.js';

import CarouselTile from './js/tiles/carousel.js';
import GalleryTile from './js/tiles/gallery.js';
import NavigationTile from './js/tiles/navigation.js';
import PhotoDayTile from './js/tiles/photoday.js';
import PhotoGalleryTile from './js/tiles/photogallery.js';


// https://hacks.mozilla.org/2015/04/es6-in-depth-iterators-and-the-for-of-loop/
jQuery.prototype[Symbol.iterator] = Array.prototype[Symbol.iterator];


$(() => {
  for (let tile of $('.brasil-photoday-tile')) {
    new PhotoDayTile();
  }
  for (let tile of $('.brasil-photogallery-tile')) {
    new PhotoGalleryTile(tile);
  }
  if ($('.template-centrais-de-conteudo').length >= 0) {
    new ContentCentral();
  }
  if ($('.ministers-carousel').length > 0) {
    new Ministers();
  }
  if ($('.section-pagina-inicial').length > 0) {
    for (let tile of $('.cover-richtext-tile')) {
      if ($(tile).parent().hasClass('tile-default')) {
        continue;
      }
      new SocialLike(tile);
    }
    for (let tile of $('.nitf-basic-tile')) {
      new SocialLike(tile);
    }
  }
});


export default {
  PhotoDayTile,
  PhotoGalleryTile,
  Ministers,
  SocialLike,
};

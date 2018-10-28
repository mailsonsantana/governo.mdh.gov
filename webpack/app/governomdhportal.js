import Library from './js/pages/library.js';
import LatestNews from './js/pages/latest_news.js';

/* Tiles */
import CarouselTile from './js/tiles/carousel_mdh.js';
import CarouselVideosTile from './js/tiles/carousel_videos_mdh.js';
import ComposicaoTile from './js/tiles/composicao_mdh.js';

/* Modules */
import Youtube from './js/modules/youtube_mdh.js';

// https://hacks.mozilla.org/2015/04/es6-in-depth-iterators-and-the-for-of-loop/
jQuery.prototype[Symbol.iterator] = Array.prototype[Symbol.iterator];


$(() => {
  $('#viewlet-social-like').stop(true, true);
  for (let carousel of $('.brasil-carousel-tile')) {
    new CarouselTile(carousel);
  }

  for (let carousel of $('.brasil-carousel-tile')) {
    new CarouselTile(carousel);
  }
  if ($('.template-search-library')[0] != null) {
    new Library();
  }
  if ($('.template-latest-news')[0] != null) {
    new LatestNews();
  }
  for (let carouselvideos of $('.brasil-carouselvideos-tile')) {
    new CarouselVideosTile(carouselvideos);
    new Youtube(carouselvideos);
  }

});

export default {
  CarouselTile,
}
import ContentCentral from './js/contentcentral.js';
import Ministers from './js/ministerios.js'
import SocialLike from './js/sociallike.js';

import CarouselTile from './js/tiles/carousel.js';
import GalleryTile from './js/tiles/gallery.js';
import NavigationTile from './js/tiles/navigation.js';
import PhotoDayTile from './js/tiles/photoday.js';
import PhotoGalleryTile from './js/tiles/photogallery.js';
import TimeLineTile from './js/tiles/timeline.js';

import Contraste from './js/contrast.js';
import GaleriaDeFotos from './js/albuns.js';


// https://hacks.mozilla.org/2015/04/es6-in-depth-iterators-and-the-for-of-loop/
jQuery.prototype[Symbol.iterator] = Array.prototype[Symbol.iterator];


$(() => {
  $('#viewlet-social-like').stop(true, true);
  for (let carousel of $('.brasil-carousel-tile')) {
    new CarouselTile(carousel);
  }
  for (let tile of $('.brasil-photoday-tile')) {
    new PhotoDayTile();
  }
  for (let tile of $('.brasil-photogallery-tile')) {
    new PhotoGalleryTile(tile);
  }
  for (let timeline of $('.brasil-timeline-tile')) {
    new TimeLineTile(timeline);
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

$(document).ready(function(){
  $(".ico-navegacao").click(function(){
    $(".navigation-wrapper").toggleClass("ativo");
  });
  $(".ico-busca").click(function(){
    $("#main-header").toggleClass("busca-ativa");
    $("#portal-searchbox").toggleClass("ativo");
  });
  $('.tile-faq dt').on('click', function () {
    $(this).next("dd").slideToggle();
    $(this).toggleClass("aberto");
  });
  if ($('.template-galeria_de_fotos').length > 0) {
    new GaleriaDeFotos();
  }
});



export default {
  CarouselTile,
  PhotoDayTile,
  PhotoGalleryTile,
  TimeLineTile,
  Ministers,
  SocialLike,
};

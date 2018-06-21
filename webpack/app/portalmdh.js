import ContentCentral from './js/contentcentral.js';
import ResizeFont from './js/accessibility.js';
import Ministers from './js/ministerios.js'
import SocialLike from './js/sociallike.js';

import CarouselTile from './js/tiles/carousel.js';
import CarouselVideosTile from './js/tiles/carouselvideos.js';
import GalleryTile from './js/tiles/gallery.js';
import GallerySwiperVideosTile from './js/tiles/galleryswipervideos.js'
import NavigationTile from './js/tiles/navigation.js';
import PhotoDayTile from './js/tiles/photoday.js';
import PhotoGalleryTile from './js/tiles/photogallery.js';
import TimeLineTile from './js/tiles/timeline.js';
import ComposicaoTile from './js/tiles/composicao.js';

import Contraste from './js/contrast.js';
import GaleriaDeFotos from './js/albuns.js';
import Youtube from './js/youtube.js';
import DestaqueTopo from './js/destaquetopo.js';


// https://hacks.mozilla.org/2015/04/es6-in-depth-iterators-and-the-for-of-loop/
jQuery.prototype[Symbol.iterator] = Array.prototype[Symbol.iterator];


$(() => {
  $('#viewlet-social-like').stop(true, true);
  for (let carousel of $('.brasil-carousel-tile')) {
    new CarouselTile(carousel);
  }
  for (let carouselvideos of $('.brasil-carouselvideos-tile')) {
    new CarouselVideosTile(carouselvideos);
    new Youtube(carouselvideos);
  }
  if ($('#texttospeech-button').length > 0) {
    new ResizeFont();
  }
  for (let carousel of $('.brasil-carousel-tile')) {
    new CarouselTile(carousel);
  }
  for (let tile of $('.brasil-photoday-tile')) {
    new PhotoDayTile();
  }
  for (let tile of $('.brasil-photogallery-tile')) {
    new PhotoGalleryTile(tile);
  }
  for (let gallery of $('.brasil-gallery-tile')) {
    new GalleryTile(gallery);
  }
  for (let galleryswiper of $('.galleryswipervideos')) {
    new GallerySwiperVideosTile(galleryswiper);
    new Youtube(galleryswiper);
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
  if ($('.site-mdh').length > 0) {
    // for (let tile of $('.cover-richtext-tile')) {
    //   if ($(tile).parent().hasClass('tile-default')) {
    //     continue;
    //   }
    //   new SocialLike(tile);
    // }
    var path = window.location.pathname
    if (path == '/' || path == '/mdh'){
      $('#portal-breadcrumbs').hide()
    }


    for (let destaque of $('.linha-destaquetopo')){
      new DestaqueTopo(destaque);
    } 
    for (let tile of $('.nitf-basic-tile')) {
      new SocialLike(tile);
    }
    for (let relatedItem of $('#relatedItemBox .contenttype-collective-nitf-content')) {
      new SocialLike(relatedItem);
    }
  }
});

$(document).ready(function(){
  $(".ico-navegacao").click(function(){
    $(".navigation-wrapper").toggleClass("ativo");
    $(".ico-navegacao").toggleClass("ico-close");
    if ($(".inverter-white").length > 0){
      $(".ico-navegacao").removeClass("ico-navegacao").addClass('ico-close-white');
    }
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
  CarouselVideosTile,
  ComposicaoTile,
  DestaqueTopo,
  PhotoDayTile,
  PhotoGalleryTile,
  ResizeFont,
  TimeLineTile,
  Ministers,
  SocialLike,
  Youtube,
  GallerySwiperVideosTile,
};

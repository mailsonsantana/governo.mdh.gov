!function(e,t){"object"==typeof exports&&"object"==typeof module?module.exports=t():"function"==typeof define&&define.amd?define([],t):"object"==typeof exports?exports.portalmdh=t():e.portalmdh=t()}("undefined"!=typeof self?self:this,function(){return function(e){function t(i){if(n[i])return n[i].exports;var r=n[i]={i:i,l:!1,exports:{}};return e[i].call(r.exports,r,r.exports,t),r.l=!0,r.exports}var n={};return t.m=e,t.c=n,t.d=function(e,n,i){t.o(e,n)||Object.defineProperty(e,n,{configurable:!1,enumerable:!0,get:i})},t.n=function(e){var n=e&&e.__esModule?function(){return e.default}:function(){return e};return t.d(n,"a",n),n},t.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},t.p="/++resource++portalmdh/",t(t.s=1)}([,/*!*************************************************************************************************************!*\
  !*** multi ./app/img/ministry-icon.png ./app/img/planalto-icon.png ./app/portalmdh.scss ./app/portalmdh.js ***!
  \*************************************************************************************************************/
/*! dynamic exports provided */
/*! all exports used */
function(e,t,n){n(/*! ./app/img/ministry-icon.png */2),n(/*! ./app/img/planalto-icon.png */3),n(/*! ./app/portalmdh.scss */4),e.exports=n(/*! ./app/portalmdh.js */5)},/*!***********************************!*\
  !*** ./app/img/ministry-icon.png ***!
  \***********************************/
/*! dynamic exports provided */
/*! all exports used */
function(e,t,n){e.exports=n.p+"img/ministry-icon.png"},/*!***********************************!*\
  !*** ./app/img/planalto-icon.png ***!
  \***********************************/
/*! dynamic exports provided */
/*! all exports used */
function(e,t,n){e.exports=n.p+"img/planalto-icon.png"},/*!****************************!*\
  !*** ./app/portalmdh.scss ***!
  \****************************/
/*! dynamic exports provided */
/*! all exports used */
function(e,t,n){e.exports=n.p+"portalmdh.css"},/*!**************************!*\
  !*** ./app/portalmdh.js ***!
  \**************************/
/*! exports provided: default */
/*! all exports used */
function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var i=n(/*! ./js/contentcentral.js */6),r=n(/*! ./js/ministerios.js */7),a=n(/*! ./js/sociallike.js */8),o=(n(/*! ./js/tiles/carousel.js */9),n(/*! ./js/tiles/gallery.js */10),n(/*! ./js/tiles/navigation.js */11),n(/*! ./js/tiles/photoday.js */12)),l=n(/*! ./js/tiles/photogallery.js */13);jQuery.prototype[Symbol.iterator]=Array.prototype[Symbol.iterator],$(function(){var e=!0,t=!1,n=void 0;try{for(var s,u=$(".brasil-photoday-tile")[Symbol.iterator]();!(e=(s=u.next()).done);e=!0){s.value;new o.a}}catch(e){t=!0,n=e}finally{try{!e&&u.return&&u.return()}finally{if(t)throw n}}var c=!0,h=!1,f=void 0;try{for(var p,v=$(".brasil-photogallery-tile")[Symbol.iterator]();!(c=(p=v.next()).done);c=!0){var d=p.value;new l.a(d)}}catch(e){h=!0,f=e}finally{try{!c&&v.return&&v.return()}finally{if(h)throw f}}if($(".template-centrais-de-conteudo").length>=0&&new i.a,$(".ministers-carousel").length>0&&new r.a,$(".section-pagina-inicial").length>0){var y=!0,m=!1,b=void 0;try{for(var g,w=$(".cover-richtext-tile")[Symbol.iterator]();!(y=(g=w.next()).done);y=!0){var k=g.value;$(k).parent().hasClass("tile-default")||new a.a(k)}}catch(e){m=!0,b=e}finally{try{!y&&w.return&&w.return()}finally{if(m)throw b}}var x=!0,S=!1,C=void 0;try{for(var T,j=$(".nitf-basic-tile")[Symbol.iterator]();!(x=(T=j.next()).done);x=!0){var E=T.value;new a.a(E)}}catch(e){S=!0,C=e}finally{try{!x&&j.return&&j.return()}finally{if(S)throw C}}}}),t.default={PhotoDayTile:o.a,PhotoGalleryTile:l.a,Ministers:r.a,SocialLike:a.a}},/*!**********************************!*\
  !*** ./app/js/contentcentral.js ***!
  \**********************************/
/*! exports provided: default */
/*! exports used: default */
function(e,t,n){"use strict";function i(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}var r=function(){function e(e,t){for(var n=0;n<t.length;n++){var i=t[n];i.enumerable=i.enumerable||!1,i.configurable=!0,"value"in i&&(i.writable=!0),Object.defineProperty(e,i.key,i)}}return function(t,n,i){return n&&e(t.prototype,n),i&&e(t,i),t}}(),a=function(){function e(){i(this,e),$("#filter-toggle").on("click",this.hideFilter.bind(this))}return r(e,[{key:"hideFilter",value:function(e){e.preventDefault(),$("#filter-toggle").toggleClass("closed"),$("#results-bar dd.actionMenuContent").toggleClass("closed")}}]),e}();t.a=a},/*!*******************************!*\
  !*** ./app/js/ministerios.js ***!
  \*******************************/
/*! exports provided: default */
/*! exports used: default */
function(e,t,n){"use strict";function i(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}var r=function e(t){i(this,e),new Swiper(".ministers-carousel .carousel-thumbs",{navigation:{nextEl:".ministers-carousel .carousel-thumbs .swiper-button-next",prevEl:".ministers-carousel .carousel-thumbs .swiper-button-prev"},pagination:{el:".ministers-carousel .carousel-thumbs .swiper-pagination",clickable:!0}})};t.a=r},/*!******************************!*\
  !*** ./app/js/sociallike.js ***!
  \******************************/
/*! exports provided: default */
/*! exports used: default */
function(e,t,n){"use strict";function i(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}var r=function(){function e(e,t){for(var n=0;n<t.length;n++){var i=t[n];i.enumerable=i.enumerable||!1,i.configurable=!0,"value"in i&&(i.writable=!0),Object.defineProperty(e,i.key,i)}}return function(t,n,i){return n&&e(t.prototype,n),i&&e(t,i),t}}(),a=function(){function e(t){i(this,e),this.$tile=$(t);var n=!0,r=!1,a=void 0;try{for(var o,l=this.$("a")[Symbol.iterator]();!(n=(o=l.next()).done);n=!0){var s=o.value;s.host===location.host&&(this.$(".likes").lenght>0||this.$tile.append(this.template(s.href,s.innerText.trim())))}}catch(e){r=!0,a=e}finally{try{!n&&l.return&&l.return()}finally{if(r)throw a}}this.$(".likes-more").on("click",this.moreClick.bind(this))}return r(e,[{key:"$",value:function(e){function t(t){return e.apply(this,arguments)}return t.toString=function(){return e.toString()},t}(function(e){return $(e,this.$tile)})},{key:"fb",value:function(e){var t=$('meta[property="fb:app_id"]').attr("content");if(void 0===t)return"";var n={app_id:t,display:"popup",href:e,redirect_uri:location.href};return'<li class="likes-item likes-fb likes-pinned">\n      <a class="slPrivacy"\n         title="Share on Facebook (open in new window)"\n         href="https://www.facebook.com/dialog/share?'+$.param(n)+"\"\n         onclick=\"javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=600,width=600');return false;\">\n         Facebook\n      </a>\n    </li>"}},{key:"twitter",value:function(e,t){var n={text:t,url:e};return'<li class="likes-item likes-twitter likes-pinned">\n      <a class="slPrivacy"\n          title="Tweet (opens in new window)"\n          href="https://twitter.com/intent/tweet?'+$.param(n)+"\"\n          onclick=\"javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=600,width=600');return false;\">\n          Twitter\n      </a>\n    </li>"}},{key:"linkedin",value:function(e,t){var n={mini:"true",url:e,title:t};return'<li class="likes-item likes-linkedin">\n      <a class="slPrivacy"\n         title="Share on Linkedin (open in new window)"\n         href="https://www.linkedin.com/shareArticle?'+$.param(n)+"\"\n         onclick=\"javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=600,width=600');return false;\">\n        Linkedin\n      </a>\n    </li>"}},{key:"gplus",value:function(e){var t=$('meta[property="og:locale"]').attr("content");if(void 0===t)return"";var n={url:e,hl:t.replace("_","-")};return'<li class="likes-item likes-gplus">\n      <a class="slPrivacy"\n         title="Share on Google+ (open in new window)"\n         href="https://plus.google.com/share?'+$.param(n)+"\"\n         onclick=\"javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=600,width=600');return false;\">\n         Google Plus\n      </a>\n    </li>"}},{key:"template",value:function(e,t){var n=$('<ul class="likes">');return n.append(this.fb(e)),n.append(this.twitter(e,t)),n.append(this.linkedin(e,t)),n.append(this.gplus(e)),n.append('\n      <li class="likes-item likes-link">\n        <a href="'+e+'">Link</a>\n      </li>\n      <li class="likes-more likes-pinned">\n        <a href="#">...</a>\n      </li>\n    '),n}},{key:"moreToggle",value:function(e){e.hasClass("likes-open")?(e.removeClass("likes-open"),this.$(".likes-more").removeClass("likes-open"),this.$(".likes-more > a").html("...")):(e.addClass("likes-open"),this.$(".likes-more").addClass("likes-open"),this.$(".likes-more > a").html("x"))}},{key:"moreClick",value:function(e){e.preventDefault(),this.moreToggle(this.$(".likes-item:not(.likes-pinned)"))}}]),e}();t.a=a},/*!**********************************!*\
  !*** ./app/js/tiles/carousel.js ***!
  \**********************************/
/*! exports provided: default */
function(e,t,n){"use strict";function i(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}var r=function(){function e(e,t){for(var n=0;n<t.length;n++){var i=t[n];i.enumerable=i.enumerable||!1,i.configurable=!0,"value"in i&&(i.writable=!0),Object.defineProperty(e,i.key,i)}}return function(t,n,i){return n&&e(t.prototype,n),i&&e(t,i),t}}();!function(){function e(t){i(this,e),this.tile=t,this.initSwiper(),this.initSecondCarousel()}r(e,[{key:"initSwiper",value:function(){this.swiper=new Swiper("#"+this.tile.id+" .carousel-thumbs",{navigation:{nextEl:"#"+this.tile.id+" .carousel-thumbs .swiper-button-next",prevEl:"#"+this.tile.id+" .carousel-thumbs .swiper-button-prev"},pagination:{el:"#"+this.tile.id+" .carousel-thumbs .swiper-pagination",clickable:!0}})}},{key:"initSecondCarousel",value:function(){var e=$(this.tile).parents(".column");this.$tiles=$(".brasil-carousel-tile",e),2===this.$tiles.length&&(this.$otherTile=this.$tiles.not(this.tile),this.hideSecondCarusel(),this.initSwitCarousel())}},{key:"hideSecondCarusel",value:function(){if(!($("body.template-compose").length>0)){var e=this.$tiles.last();this.tile===e[0]&&e.hide()}}},{key:"initSwitCarousel",value:function(){var e=$("<ul>"),t=!0,n=!1,i=void 0;try{for(var r,a=this.$tiles[Symbol.iterator]();!(t=(r=a.next()).done);t=!0){var o=r.value,l=$(".switch-carousel",o).attr("data-text");if(void 0===l)return;var s=$("<li>"+l+"</li>");this.tile===o?s.addClass("active"):s.on("click",function(e){e.preventDefault(),$(this.tile).hide(),this.$otherTile.show()}.bind(this)),e.append(s)}}catch(e){n=!0,i=e}finally{try{!t&&a.return&&a.return()}finally{if(n)throw i}}$(".switch-carousel",this.tile).append(e)}}])}()},/*!*********************************!*\
  !*** ./app/js/tiles/gallery.js ***!
  \*********************************/
/*! exports provided: default */
function(e,t,n){"use strict";function i(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}var r=function(){function e(e,t){for(var n=0;n<t.length;n++){var i=t[n];i.enumerable=i.enumerable||!1,i.configurable=!0,"value"in i&&(i.writable=!0),Object.defineProperty(e,i.key,i)}}return function(t,n,i){return n&&e(t.prototype,n),i&&e(t,i),t}}();!function(){function e(t){i(this,e),this.tile=t,this.initSwiper(),this.composeMode()}r(e,[{key:"initSwiper",value:function(){this.galleryTop=new Swiper("#"+this.tile.id+" .gallery-top",{grabCursor:!0}),this.galleryThumbs=new Swiper("#"+this.tile.id+" .gallery-thumbs",{virtualTranslate:!0,navigation:{nextEl:"#"+this.tile.id+" .gallery-thumbs-container .swiper-button-next",prevEl:"#"+this.tile.id+" .gallery-thumbs-container .swiper-button-prev"},spaceBetween:30,centeredSlides:!0,slidesPerView:"auto",touchRatio:.2,slideToClickedSlide:!0}),this.galleryThumbs.on("slideChange",this.slideChange),this.galleryTop.controller.control=this.galleryThumbs,this.galleryThumbs.controller.control=this.galleryTop}},{key:"composeMode",value:function(){if(0!==$(".template-compose").length){$("#"+this.tile.id+" .gallery-thumbs").prepend('<div class="crop-warning">Recorte a imagem na opção "mini" para corrigir as miniaturas.</div>');var e=!0,t=!1,n=void 0;try{for(var i,r=$("#"+this.tile.id+" .gallery-thumbs .swiper-slide")[Symbol.iterator]();!(e=(i=r.next()).done);e=!0){var a=i.value,o=$(a),l=$("img",o),s=document.createElement("a");s.href=l.attr("src"),s.pathname=s.pathname.replace(/\@\@.*/,"@@croppingeditor"),s.search="scalename=mini",o.append('<a class="crop" target="_blank" href="'+s.href+'" title="Recortar imagem">✀</span>')}}catch(e){t=!0,n=e}finally{try{!e&&r.return&&r.return()}finally{if(t)throw n}}}}},{key:"slideChange",value:function(){var e=200*this.activeIndex;this.$wrapperEl.transform("translate(-"+e+"px)")}}])}()},/*!************************************!*\
  !*** ./app/js/tiles/navigation.js ***!
  \************************************/
/*! exports provided: default */
function(e,t,n){"use strict";function i(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}var r=function(){function e(e,t){for(var n=0;n<t.length;n++){var i=t[n];i.enumerable=i.enumerable||!1,i.configurable=!0,"value"in i&&(i.writable=!0),Object.defineProperty(e,i.key,i)}}return function(t,n,i){return n&&e(t.prototype,n),i&&e(t,i),t}}();!function(){function e(t){i(this,e),this.tile=t,this.$(".navigation-more").on("click",this.moreClick.bind(this))}r(e,[{key:"$",value:function(e){function t(t){return e.apply(this,arguments)}return t.toString=function(){return e.toString()},t}(function(e){return $(e,this.tile)})},{key:"moreClick",value:function(e){e.preventDefault(),this.$(".navigation-more").toggleClass("open"),this.$(".navigation-more-items").toggleClass("open")}}])}()},/*!**********************************!*\
  !*** ./app/js/tiles/photoday.js ***!
  \**********************************/
/*! exports provided: default */
/*! exports used: default */
function(e,t,n){"use strict";function i(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}var r=function(){function e(e,t){for(var n=0;n<t.length;n++){var i=t[n];i.enumerable=i.enumerable||!1,i.configurable=!0,"value"in i&&(i.writable=!0),Object.defineProperty(e,i.key,i)}}return function(t,n,i){return n&&e(t.prototype,n),i&&e(t,i),t}}(),a=function(){function e(){i(this,e),this.img=$(".zoom-icon"),this.img.on("click",this.openImage.bind(this.img))}return r(e,[{key:"openImage",value:function(e){e.preventDefault();var t=e.target.href;0===$("#image-overlay").length&&$("body").append('<div id="image-overlay" class="overlay overlay-ajax">\n                <div class="pb-image"><img src="'+t+'"/></div>\n            </div>'),$("#image-overlay").show(),$("#image-overlay").on("click",function(){$("#image-overlay").remove()})}}]),e}();t.a=a},/*!**************************************!*\
  !*** ./app/js/tiles/photogallery.js ***!
  \**************************************/
/*! exports provided: default */
/*! exports used: default */
function(e,t,n){"use strict";function i(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}var r=function(){function e(e,t){for(var n=0;n<t.length;n++){var i=t[n];i.enumerable=i.enumerable||!1,i.configurable=!0,"value"in i&&(i.writable=!0),Object.defineProperty(e,i.key,i)}}return function(t,n,i){return n&&e(t.prototype,n),i&&e(t,i),t}}(),a=function(){function e(t){i(this,e),this.tile=t,this.initSwiper()}return r(e,[{key:"initSwiper",value:function(){this.galleryThumbs=new Swiper("#"+this.tile.id+" .photogallery-container",{navigation:{nextEl:"#"+this.tile.id+" .photogallery-container .swiper-button-next",prevEl:"#"+this.tile.id+" .photogallery-container .swiper-button-prev"}})}}]),e}();t.a=a}])});
//# sourceMappingURL=portalmdh.js.map
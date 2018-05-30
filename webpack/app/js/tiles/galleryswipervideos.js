export default class GallerySwiperVideosTile {
  constructor(tile) {
    this.tile = tile;
    this.initSwiper();
  }
  initSwiper() {
    this.galleryTop = new Swiper(`#${this.tile.id} .gallery-top`, {
      grabCursor: true
    });
    this.galleryThumbs = new Swiper(`#${this.tile.id} .gallery-thumbs`, {
      virtualTranslate: true,
      navigation: {
        nextEl: `#${this.tile.id} .gallery-thumbs-container .swiper-button-next`,
        prevEl: `#${this.tile.id} .gallery-thumbs-container .swiper-button-prev`,
      },
      centeredSlides: true,
      slidesPerView: 'auto',
      touchRatio: 0.2,
      slideToClickedSlide: true,
    });
    this.galleryThumbs.on('slideChange', this.slideChange);
    this.galleryTop.controller.control = this.galleryThumbs;
    this.galleryThumbs.controller.control = this.galleryTop;
  }

  slideChange() {
    let thumbsLeft = this.$el.offset().left -5;
    let thumbsRight = thumbsLeft + this.$el.outerWidth() + 10;

    let $currentSlide = $(this.slides[this.activeIndex]);
    let currentSlideLeft = $currentSlide.offset().left;
    let currentSlideRight = currentSlideLeft + $currentSlide.outerWidth();

    if (currentSlideLeft < thumbsLeft || currentSlideRight > thumbsRight) {
      let wrapperLeft = this.$wrapperEl.offset().left;
      this.$wrapperEl.transform(`translate(${thumbsLeft - currentSlideLeft + wrapperLeft}px)`);
    }
  }
}
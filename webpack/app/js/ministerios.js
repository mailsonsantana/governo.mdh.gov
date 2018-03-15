export default class Ministers {
  constructor(tile) {
    new Swiper(`.ministers-carousel .carousel-thumbs`, {
      navigation: {
        nextEl: `.ministers-carousel .carousel-thumbs .swiper-button-next`,
        prevEl: `.ministers-carousel .carousel-thumbs .swiper-button-prev`,
      },
      pagination: {
        el: `.ministers-carousel .carousel-thumbs .swiper-pagination`,
        clickable: true,
      },
    });
  }
}

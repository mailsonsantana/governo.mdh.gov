export default class ComposicaoTile {
  constructor(tile) {
    new Swiper(`.brasil-composicao-tile .composicao-thumbs`, {
      navigation: {
        nextEl: `.brasil-composicao-tile .composicao-thumbs .swiper-button-next`,
        prevEl: `.brasil-composicao-tile .composicao-thumbs .swiper-button-prev`,
      },
      pagination: {
        el: `.brasil-composicao-tile .composicao-thumbs .swiper-pagination`,
        clickable: true,
      },
    });
  }
}

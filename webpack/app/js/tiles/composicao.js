export default class ComposicaoTile {
  constructor(tile) {
    this.tile = tile;

    this.initSwiper();
    this.initSecondComposicao();
  }
  initSwiper() {
    this.swiper = new Swiper(`#${this.tile.id} .composicao-thumbs`, {
      navigation: {
        nextEl: `#${this.tile.id} .composicao-thumbs .swiper-button-next`,
        prevEl: `#${this.tile.id} .composicao-thumbs .swiper-button-prev`,
      },
      pagination: {
        el: `#${this.tile.id} .composicao-thumbs .swiper-pagination`,
        clickable: true,
      },
    });
  }
  initSecondComposicao() {
    let $column = $(this.tile).parents('.column');
    this.$tiles = $('.brasil-composicao-tile', $column);
    if (this.$tiles.length !== 2) {
      return;
    }
    this.$otherTile = this.$tiles.not(this.tile);
    this.hideSecondComposicao();
    this.initSwitComposicao();
  }
  hideSecondComposicao() {
    if ($('body.template-compose').length > 0) {
      return;
    }
    let $lastTile = this.$tiles.last();
    if (this.tile === $lastTile[0]) {
      $lastTile.hide();
    }
  }
  initSwitComposicao() {
    let $ul = $('<ul>');
    for (let tile of this.$tiles) {
      let text = $('.switch-composicao', tile).attr('data-text');
      if (typeof(text) === 'undefined') {
        return;
      }
      let $li = $(`<li>${text}</li>`)
      if (this.tile === tile) {
        $li.addClass('active');
      } else {
        $li.on('click', function(e) {
          e.preventDefault();
          $(this.tile).hide();
          this.$otherTile.show();
        }.bind(this));
      }
      $ul.append($li);
    }
    $('.switch-composicao', this.tile).append($ul);
  }
}

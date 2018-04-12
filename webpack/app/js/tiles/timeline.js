export default class TimeLineTile {
  constructor(tile) {
    this.tile = tile;

    this.initSwiper();
    this.initSecondTimeLine();
  }
  initSwiper() {
    var months = [];
    $('.swiper-container .swiper-slide').each(function(i) {
      months.push($(this).find('.month').attr('data-swiper-month'))
    });

    this.swiper = new Swiper(`#${this.tile.id} .timeline-thumbs`, {
      navigation: {
        nextEl: `#${this.tile.id} .timeline-thumbs .swiper-button-next`,
        prevEl: `#${this.tile.id} .timeline-thumbs .swiper-button-prev`,
      },
      pagination: {
        el: `#${this.tile.id} .timeline-thumbs .swiper-pagination`,
        clickable: true,
        renderBullet: function (index, className) {
          return '<div class="swiper-month ' + className + '"><p>' + months[index] + '</p></div>';
        },
      },
    });
  }
  initSecondTimeLine() {
    let $column = $(this.tile).parents('.column');
    this.$tiles = $('.brasil-timeline-tile', $column);
    if (this.$tiles.length !== 2) {
      return;
    }
    this.$otherTile = this.$tiles.not(this.tile);
    this.hideSecondTimeLine();
    this.initSwitTimeLine();
  }
  hideSecondTimeLine() {
    if ($('body.template-compose').length > 0) {
      return;
    }
    let $lastTile = this.$tiles.last();
    if (this.tile === $lastTile[0]) {
      $lastTile.hide();
    }
  }
  initSwitCarousel() {
    let $ul = $('<ul>');
    for (let tile of this.$tiles) {
      let text = $('.switch-timeline', tile).attr('data-text');
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
    $('.switch-timeline', this.tile).append($ul);
  }
}

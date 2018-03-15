export default class SocialLike {
  constructor(tile) {
    this.$tile = $(tile);
    for (let link of this.$('a')) {
      if (link.host !== location.host) {
        continue;
      }
      if (this.$('.likes').lenght > 0) {
        continue;
      }
      this.$tile.append(this.template(link.href, link.innerText.trim()));
    }
    this.$('.likes-more').on('click', this.moreClick.bind(this));
  }
  $(selector) {
    return $(selector, this.$tile);
  }
  fb(url) {
    let appId = $('meta[property="fb:app_id"]').attr('content');
    if (typeof(appId) === 'undefined') {
      return '';
    }
    let params = {
      app_id: appId,
      display: 'popup',
      href: url,
      redirect_uri: location.href
    };
    let html = `<li class="likes-item likes-fb likes-pinned">
      <a class="slPrivacy"
         title="Share on Facebook (open in new window)"
         href="https://www.facebook.com/dialog/share?${$.param(params)}"
         onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=600,width=600');return false;">
         Facebook
      </a>
    </li>`;
    return html;
  }
  twitter(url, title) {
    let params = {
      text: title,
      url: url
    };
    let html = `<li class="likes-item likes-twitter likes-pinned">
      <a class="slPrivacy"
          title="Tweet (opens in new window)"
          href="https://twitter.com/intent/tweet?${$.param(params)}"
          onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=600,width=600');return false;">
          Twitter
      </a>
    </li>`;
    return html;
  }
  linkedin(url, title) {
    let params = {
      mini: 'true',
      url: url,
      title: title,
    };
    let html = `<li class="likes-item likes-linkedin">
      <a class="slPrivacy"
         title="Share on Linkedin (open in new window)"
         href="https://www.linkedin.com/shareArticle?${$.param(params)}"
         onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=600,width=600');return false;">
        Linkedin
      </a>
    </li>`;
    return html;
  }
  gplus(url) {
    let language = $('meta[property="og:locale"]').attr('content');
    if (typeof(language) === 'undefined') {
      return '';
    }
    let params = {
      url: url,
      hl: language.replace('_', '-')
    };
    let html = `<li class="likes-item likes-gplus">
      <a class="slPrivacy"
         title="Share on Google+ (open in new window)"
         href="https://plus.google.com/share?${$.param(params)}"
         onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=600,width=600');return false;">
         Google Plus
      </a>
    </li>`;
    return html;
  }
  template(url, title) {
    let $ul = $('<ul class="likes">');
    $ul.append(this.fb(url));
    $ul.append(this.twitter(url, title));
    $ul.append(this.linkedin(url, title));
    $ul.append(this.gplus(url));
    $ul.append(`
      <li class="likes-item likes-link">
        <a href="${url}">Link</a>
      </li>
      <li class="likes-more likes-pinned">
        <a href="#">...</a>
      </li>
    `);
    return $ul;
  }
  moreToggle($el) {
    if ($el.hasClass('likes-open')) {
      $el.removeClass('likes-open');
      this.$('.likes-more').removeClass('likes-open');
      this.$('.likes-more > a').html('...');
    } else {
      $el.addClass('likes-open');
      this.$('.likes-more').addClass('likes-open');
      this.$('.likes-more > a').html('x');
    }
  }
  moreClick(e) {
    e.preventDefault();
    this.moreToggle(this.$('.likes-item:not(.likes-pinned)'));
  }
}


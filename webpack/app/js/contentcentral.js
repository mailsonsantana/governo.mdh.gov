export default class ContentCentral {
  constructor() {
    $('#filter-toggle').on('click', this.hideFilter.bind(this));
  }
  hideFilter(e) {
    e.preventDefault();
    $('#filter-toggle').toggleClass('closed');
    $('#results-bar dd.actionMenuContent').toggleClass('closed');
  }
}

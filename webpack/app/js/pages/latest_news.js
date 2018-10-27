export default class Library {
  constructor() {
    $('#filter-toggle').on('click', this.toggleFilter.bind(this));
    // No search parameters -- start closed
    if (location.search === '') {
      sessionStorage.latestNewsOpen = false;
    }
    // The filter box is open between searches
    if (sessionStorage.latestNewsOpen === 'true') {
      this.toggleFilter();
    }
  }
  toggleFilter(e) {
    if (typeof e !== 'undefined') {
      e.preventDefault();
      sessionStorage.latestNewsOpen = (sessionStorage.latestNewsOpen === 'false');
    }
    $('#filter-toggle').toggleClass('closed');
    $('#results-bar dd.actionMenuContent').toggleClass('closed');
  }
}
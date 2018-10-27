export default class Library {
  constructor() {
    $('#filter-toggle').on('click', this.toggleFilter.bind(this));
    // No search parameters -- start closed
    if (location.search === '') {
      sessionStorage.libraryOpen = false;
    }
    // The filter box is open between searches
    if (sessionStorage.libraryOpen === 'true') {
      this.toggleFilter();
    }
  }
  toggleFilter(e) {
    if (typeof e !== 'undefined') {
      e.preventDefault();
      sessionStorage.libraryOpen = (sessionStorage.libraryOpen === 'false');
    }
    $('#filter-toggle').toggleClass('closed');
    $('#results-bar dd.actionMenuContent').toggleClass('closed');
  }
}
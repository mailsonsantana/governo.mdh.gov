import Library from './js/pages/library.js';
import LatestNews from './js/pages/latest_news.js';


$(() => {  
  if ($('.template-search-library')[0] != null) {
    new Library();
  }
  if ($('.template-latest-news')[0] != null) {
    new LatestNews();
  }
});

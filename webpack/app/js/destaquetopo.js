export default class DestaqueTopo {
  constructor() {
  	if ($('.section-navegue-por-temas').length < 1){
	    $('#portal-description').css('filter','invert(100)');
	    $('#portal-title').css('filter','invert(100)');
	    $('.link-contraste').css('filter','invert(100)').css('border-right', '1px solid #000');
	    $('.links-destaque').css('filter','invert(100)')
	    $('.link-vlibras').css('filter','invert(100)');
	    $('#breadcrumbs-home').css('filter','invert(100)');
	}
  }
}
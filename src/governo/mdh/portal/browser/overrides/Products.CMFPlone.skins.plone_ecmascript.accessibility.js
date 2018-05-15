var setFontSize = function(direction, step) {
  var font_size = $('body').attr('data-fontsize');
  if (typeof font_size === 'undefined' || direction === 0) {
    font_size = 1.0;
  } else {
    font_size = parseFloat(font_size);
    font_size += (step * direction);
  }
  createCookie("selectedfontsize", font_size.toString(), 365);
  $('body').attr('data-fontsize', font_size);
  $('body').css('font-size', font_size + 'rem');
};
$(document).ready(function(){
  var selectedfontsize = readCookie("selectedfontsize");
  if (selectedfontsize) {
    $('body').attr('data-fontsize', selectedfontsize);
    setFontSize(1, 0); // reset to old font size
  }

  $('#siteaction-contraste a').on('click', function(e) {
    e.preventDefault();
    var contraste = readCookie('contraste');
    if(typeof contraste === 'undefined') {
      createCookie('contraste', 'on', 365);
      $('body').addClass('contraste');
    } else {
      if (contraste === 'on') {
        createCookie('contraste', 'off', 365);
        $('body').removeClass('contraste');
      } else {
        createCookie('contraste', 'on', 365);
        $('body').addClass('contraste');
      }
    }
  });
  var contraste = readCookie('contraste');
  if (contraste === 'on'){
    $('body').addClass('contraste');
  }
});

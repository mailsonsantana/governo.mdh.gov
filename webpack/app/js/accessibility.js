export default class ResizeFont {
  constructor() {
    $('#viewlet-texttospeech').before(`<ul class="resize-font">
      <li><a class="bigger" href="javascript:setFontSize(+1, 0.25);">A+</a></li>
      <li><a class="normal" href="javascript:setFontSize(0, 0.25);">A</a></li>
      <li><a class="lower" href="javascript:setFontSize(-1, 0.25);">A-</a></li>
    <ul>`);
  }
}

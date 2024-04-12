/* -------------------------------------------------------------------------- */
/*                                    Utils                                   */
/* -------------------------------------------------------------------------- */
var docReady = function docReady(fn) {
  // see if DOM is already available
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', fn);
  } else {
    setTimeout(fn, 1);
  }
};

/*-----------------------------------------------
|  Scroll To Top
-----------------------------------------------*/

var scrollToTopInit = function scrollToTopInit() {
  var btn = document.querySelector('[data-scroll-top]');
  if (btn) {
    btn.style.display = 'none';
    // eslint-disable-next-line func-names
    window.onscroll = function () {
      if (window.scrollY > 550) {
        btn.style.display = 'block';
      } else {
        btn.style.display = 'none';
      }
    };
    btn.addEventListener('click', function () {
      window.scrollTo(0, 0);
    });
  }
};


docReady(scrollToTopInit);


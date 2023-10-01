(function setProgress() {
  var progressbar = document.getElementById("progressbar");
  var now_page = js_vars.page;
  var max_page = progressbar.getAttribute("aria-valuemax");
  var percent = (100 * now_page) / max_page;
  progressbar.setAttribute("aria-valuenow", now_page);
  progressbar.setAttribute("style", "width: " + percent + "%");
  progressbar.innerHTML = Math.round(percent) + "%";
})();

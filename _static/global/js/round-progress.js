(function setProgress() {
  var progressbar = document.getElementById("progressbar");
  var now = js_vars.current;
  var max = js_vars.max;
  var percent = (100 * now) / max;
  progressbar.setAttribute("aria-valuenow", now);
  progressbar.setAttribute("aria-valuemax", max);
  progressbar.setAttribute("style", "width: " + percent + "%");
  progressbar.innerHTML = now + "/" + max + "ラウンド";
})();

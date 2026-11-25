// A sale notice that shows only on the sale's dates. The notice is in the page, hidden; this
// script shows it from the start of the sale to its end, by this device's clock, and hides it
// again at the end if the page is still open. It sets no cookie, stores nothing and sends
// nothing. Without JavaScript the notice stays hidden.
(function () {
  var sale = {
    // Black Friday 2026: midnight Pacific at the start of Friday, November 27, to midnight
    // Pacific at the start of Tuesday, December 1.
    start: Date.UTC(2026, 10, 27, 8, 0, 0),
    end: Date.UTC(2026, 11, 1, 8, 0, 0),
    isOn: function (now) { return now >= sale.start && now < sale.end; }
  };
  if (typeof module !== "undefined") module.exports = sale;  // for the date test in Node
  if (typeof document === "undefined") return;

  var root = document.documentElement;
  function show(isShown) {
    // The class shows the notice before the first paint (assets/style.css); the attribute follows.
    root.classList.toggle("sale-on", isShown);
    document.querySelectorAll(".sale").forEach(function (notice) { notice.hidden = !isShown; });
  }
  var now = Date.now();
  if (!sale.isOn(now)) return;
  root.classList.add("sale-on");
  document.addEventListener("DOMContentLoaded", function () { show(sale.isOn(Date.now())); });
  setTimeout(function () { show(false); }, sale.end - now);
})();

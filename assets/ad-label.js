// A visitor who comes from an ad (utm_medium=cpc in the address): put a label for that ad on this
// page's App Store links, so App Store Connect can count the downloads each ad brings. This sets
// no cookie, stores nothing and sends nothing.
(function () {
  var query = new URLSearchParams(location.search);
  if (query.get("utm_medium") !== "cpc") return;
  var label = [query.get("utm_source") || "ad", query.get("utm_content") || "all"].join("-")
    .toLowerCase().replace(/[^a-z0-9-]/g, "").slice(0, 40);
  document.querySelectorAll('a[href^="https://apps.apple.com/"]').forEach(function (link) {
    var url = new URL(link.href);
    url.searchParams.set("ct", label);
    link.href = url.toString();
  });
})();

<?php
header('Content-Type: text/javascript');
# generate heat maps for hot zone

echo "
window.onload = function() { var heatmapData = [
  new google.maps.LatLng(37.7749, -122.4194)
  ];
  var heatmap = new google.maps.visualization.HeatmapLayer({
     data: heatmapData
  });
heatmap.setMap(map);
}
";
?>

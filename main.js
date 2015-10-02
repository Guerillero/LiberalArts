  var map = L.map('map', {minZoom: 4, zoom: 4, center: L.latLng(38, -102)});
  
  L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {attribution: 'Map data: &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'}).addTo(map);
  
  // Now that the basemap is done, add data
  
  var cluster = L.markerClusterGroup();
  

$.getJSON("/LiberalArts/LA.json", function(data){
      var pts = L.geoJson(data, {
        pointToLayer: function(feature, cords){
          var Marker = L.marker(cords);
          Marker.bindPopup('<center>' + feature.properties.title + '<br/>' + '<b>Rank:</b> ' + feature.properties.type + '<br><a href="http://en.wikipedia.org/wiki/' + feature.properties.title + '" target="_blank">Link</a></center>');
          return Marker;
        }
      });
      
      cluster.addLayer(pts);
      map.addLayer(cluster);
    });

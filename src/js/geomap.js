var backend;
var layer_group = L.layerGroup().addTo(map);

new QWebChannel(qt.webChannelTransport, function (channel) {
            backend = channel.objects.handler;
        });


function move_to(lat, lon) {
    map.flyTo(L.latLng(lat, lon))
}


function add_marker(lat, lon, popup_message) {
    let marker = L.marker(
        [lat, lon],
        {}
    ).addTo(layer_group);

    let icon = L.AwesomeMarkers.icon(
        {
            "extraClasses": "fa-rotate-0",
            "icon": "info-sign",
            "iconColor": "white",
            "markerColor": "gray",
            "prefix": "glyphicon"
        }
    );
    marker.setIcon(icon);

    let popup = L.popup({"maxWidth": "100%"});

    let html = eval(popup_message);
    popup.setContent(html);

    marker.bindPopup(popup);

    marker.on('mouseover', function (e) {
        this.openPopup();
    });
    marker.on('mouseout', function (e) {
        this.closePopup();
    });


}


function clear_markers() {
    layer_group.clearLayers()
}

function map_clicked(e) {
    // alert("You clicked the map at " + e.latlng);
    backend.locate(e.latlng.lat, e.latlng.lng)
}

map.on('click', map_clicked);

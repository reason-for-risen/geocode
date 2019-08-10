function move_to(lat, lon) {
    map.flyTo(L.latLng(lat, lon))
}


function add_marker(lat, lon, popup_message) {
    let marker = L.marker(
        [lat, lon],
        {}
    ).addTo(map);

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

}


function map_clicked(e) {
    alert("You clicked the map at " + e.latlng);

}

map.on('click', map_clicked);

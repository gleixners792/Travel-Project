// Create the tile layer that will be the background of our map
// var API_KEY = "pk.eyJ1IjoiYXJ0cGVya2l0bnkiLCJhIjoiY2pvbHhicWppMDd6ODNyczgwajgxOTh1eiJ9.Tp-0nrsAJdOY0SPSfyuzqg";

// console.log(API_KEY);
var queryFile = "/data/Facilities_API_v1.csv";

var lightmap = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
  attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
  maxZoom: 8,
  id: 'mapbox/streets-v11',
  tileSize: 512,
  zoomOffset: -1,
  accessToken: API_KEY
});

// Initialize all of the LayerGroups we'll be using
var layers = {
  ARCHIVES: new L.LayerGroup(),
  CAMPGROUND: new L.LayerGroup(),
  CEMETERY: new L.LayerGroup(),
  LIBRARY: new L.LayerGroup(),
  MUSEUM: new L.LayerGroup(),
  HATCHERY: new L.LayerGroup(),
  VISTOR: new L.LayerGroup()
};

// Create the map with our layers
var map = L.map("map-id", {
  center: [39.8283, -98.5795],
  zoom: 5,
  layers: [
    layers.ARCHIVES,
    layers.CAMPGROUND,
    layers.CEMETERY,
    layers.LIBRARY,
    layers.MUSEUM,
    layers.HATCHERY,
    layers.VISTOR
  ]
});


// Add our 'lightmap' tile layer to the map
lightmap.addTo(map);

// Create an overlays object to add to the layer control
var overlays = {
  "Archives": layers.ARCHIVES,
  "Campground": layers.CAMPGROUND,
  "Cemetery": layers.CEMETERY,
  "Library": layers.LIBRARY,
  "Museum": layers.MUSEUM,
  "National Fish Hatchery": layers.HATCHERY,
  "Visitor Center": layers.VISTOR,
};

// Create a control for our layers, add our overlay layers to it
L.control.layers(null, overlays, {
  collapsed: false
}).addTo(map);

// Create a legend to display information about our map
var info = L.control({
  position: "bottomright"
});

// When the layer control is added, insert a div with the class of "legend"
info.onAdd = function () {
  var div = L.DomUtil.create("div", "legend");
  return div;
};
// Add the info legend to the map
info.addTo(map);

// Initialize an object containing icons for each layer group
var icons = {
  ARCHIVES: L.ExtraMarkers.icon({
    icon: "ion-briefcase",
    iconColor: "white",
    markerColor: "yellow",
    shape: "star"
  }),
  CAMPGROUND: L.ExtraMarkers.icon({
    icon: "ion-bonfire",
    iconColor: "white",
    markerColor: "red",
    shape: "circle"
  }),
  CEMETERY: L.ExtraMarkers.icon({
    icon: "ion-android-alert",
    iconColor: "white",
    markerColor: "blue-dark",
    shape: "penta"
  }),
  LIBRARY: L.ExtraMarkers.icon({
    icon: "ion-ios-book",
    iconColor: "white",
    markerColor: "orange",
    shape: "circle"
  }),
  MUSEUM: L.ExtraMarkers.icon({
    icon: "ion-android-globe",
    iconColor: "white",
    markerColor: "green",
    shape: "circle"
  }),
  HATCHERY: L.ExtraMarkers.icon({
    icon: "ion-earth",
    iconColor: "white",
    markerColor: "rose",
    shape: "circle"
  }),
  VISTOR: L.ExtraMarkers.icon({
    icon: "ion-android-people",
    iconColor: "white",
    markerColor: "black",
    shape: "circle"
  })
};

// Perform an API call to the Citi Bike Station Information endpoint

// When the first API call is complete, perform another call to the Citi Bike Station Status endpoint
console.log(queryFile);

d3.csv(queryFile).then(function (data) {
  console.log(data);


  //var updatedAt = infoRes.last_updated;
  //var stationStatus = statusRes.data.stations;
  //var stationInfo = infoRes.data.stations;

  // Create an object to keep of the number of markers in each layer
  var agencyCount = {
    ARCHIVES: 0,
    CAMPGROUND: 0,
    CEMETERY: 0,
    LIBRARY: 0,
    MUSEUM: 0,
    HATCHERY: 0,
    VISTOR: 0
  };

  // Initialize a stationStatusCode, which will be used as a key to access the appropriate layers, icons, and station count for layer group
  var governAgency;

  // Loop through the stations (they're the same size and have partially matching data)
  for (var i = 0; i < data.length; i++) {

    //console.log(data[i].FacilityID);

    // Create a new station object with properties of both station objects
    var agency = Object.assign({}, data[i].FacilityID, data[i].FacilityName);
    // If a station is listed but not installed, it's coming soon
    if (data[i].FacilityTypeDescription == "Archives") {
      governAgency = "ARCHIVES";
    }
    else if (data[i].FacilityTypeDescription == "Campground") {
      governAgency = "CAMPGROUND";
    }
    else if (data[i].FacilityTypeDescription == "Cemetery and Memorial") {
      governAgency = "CEMETERY";
    }
    else if (data[i].FacilityTypeDescription == "Library") {
      governAgency = "LIBRARY";
    }
    else if (data[i].FacilityTypeDescription == "Museum") {
      governAgency = "MUSEUM";
    }
    else if (data[i].FacilityTypeDescription == "National Fish Hatchery") {
      governAgency = "HATCHERY";
    }
    else {
      governAgency = "VISTOR";
    }

    // Update the agency count
    agencyCount[governAgency]++;
    // Create a new marker with the appropriate icon and coordinates
    var newMarker = L.marker([data[i].FacilityLatitude, data[i].FacilityLongitude], {
      icon: icons[governAgency]
    });

    // Add the new marker to the appropriate layer
    newMarker.addTo(layers[governAgency]);

    // Bind a popup to the marker that will  display on click. This will be rendered as HTML
    newMarker.bindPopup("Facility ID>> " + data[i].FacilityID + "<br>" + "Facility Name>> " + data[i].FacilityName + "<br>" + "Facility Phone>> " + data[i].FacilityPhone);
  }

  // Call the updateLegend function, which will... update the legend if you want to add.
  //updateLegend(agencyCount);
  //});

});
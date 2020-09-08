import React from "react";
import ReactDOM from "react-dom";
import Sidebar from "./components/Sidebar";

// setting up mapbox
mapboxgl.accessToken =
  "pk.eyJ1IjoibWR3YWxkbWFuMjIiLCJhIjoiY2puajJoYnN0MHY0aDNyb2pld2YyZjNhZyJ9.5FLtyOmoKXAJLSkegNvrbg";

var map = new mapboxgl.Map({
  container: "map",
  style: "mapbox://styles/mapbox/streets-v11",
  center: [-104.9903, 39.7392],
  zoom: 12,
});

ReactDOM.render(<Sidebar map={map} />, document.getElementById("sidebar"));

function formatHTMLforMarker(props) {
  var { city, state, address } = props;
  var html =
    '<div class="marker-title">' +
    address +
    "</div>" +
    "<h4>Address</h4>" +
    "<span>" +
    city +
    "</span>" +
    "<h4>City</h4>" +
    "<span>" +
    state +
    "</span>";
  return html;
}

// setup popup display on the marker



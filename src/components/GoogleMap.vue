<template>
  <div class="q-pa-md map-box">
    <div class="title">Geo View</div>

    <div
      class="google-map"
      style="border: 2px solid black"
      ref="mapContainer"
    ></div>
    <div class="map-slider">
      <q-badge color="info">
        #Orgs: {{ sliderValue }} (1 to {{ markerTempData.length }})
      </q-badge>
      <q-slider
        v-model="sliderValue"
        @change="dataSlice"
        :min="1"
        :max="markerTempData.length"
        label
        color="info"
        
        
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";

export default {
  name: "GoogleMap",
  props: ["customFilter", "stateFilter", "terrFilter", "isStateSelected"],
  setup() {
    return {
      sliderValue: ref(10),
    };
  },

  data() {
    return {
      map: null,

      styles:[
    {
      featureType: "all",
      elementType: "labels",
      stylers: [{ visibility: "off" }],
    },
    {
      featureType: "administrative.country",
      elementType: "all",
      stylers: [{ visibility: "off" }],
    },
    {
      featureType: "water",
      elementType: "all",
      stylers: [{ color: "#D2E9E9" }],
    },
    {
      featureType: "administrative.country",
      elementType: "labels",
      stylers: [{ visibility: "off" }],
    },
    {
      featureType: "administrative",
      elementType: "labels.text.fill",
      stylers: [{ color: "#444444", visibility: "off" }, { zIndex: 99999 }],
    },
    {
      featureType: "landscape",
      elementType: "all",
      stylers: [{ color: "#D2E9E9" }],
    },
    {
      featureType: "administrative",
      elementType: "all",
      stylers: [{ visibility: "off" }],
    },
    {
      featureType: "road",
      elementType: "all",
      stylers: [
        { saturation: -100 },
        { lightness: 45 },
        { visibility: "off" },
        { zIndex: 0 }, // Decrease the zIndex for filled color
      ],
    },
  ],
      markerTempData: [],
      markerData: [],
    };
  },
  mounted() {
    this.initMap();
    this.customRender();
  },

  methods: {
    initMap() {
      const usaBounds = {
        north: 49.3457868,
        south: 22.7433195,
        east: -66.9513812,
        west: -124.7844079,
      };
      console.log(usaBounds);

      this.map = new window.google.maps.Map(this.$refs.mapContainer, {
        zoom: 4,
        center: { lat: 39.116386, lng: -104.26425 },
        disableDefaultUI: true,
        zoomControl: true,
        scrollwheel: true,
        disableDoubleClickZoom: false,
        draggable: true,
        styles: this.styles, // Apply the styles
      });

      this.sliderValue = this.markerData.length;
      this.loadGeoJson();
      this.usaLabels();

      this.addMarkers();
    },

    customRender() {
      //changing label of chart based on metrix selected(potential,diag.....)
      //   this.model=val

      // converting filter data to JSON to pass in the server
      //  console.log('State-jSON',JSON.stringify(this.stateFilter))
      //  console.log('territory-jSON',JSON.stringify(this.terrFilter))

      let path = "http://127.0.0.1:5000/map";

      //sending post request to the server with the state and territory filter
      //getting chart data

      this.error = null; //initializing the error with the null value again
      fetch(path, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          state: this.stateFilter,
          terr: this.terrFilter,
          isstateselected: this.isStateSelected,
        }),
      })
        .then((response) => {
          //Handling errors if the server is not generating the output properly
          if (response.ok) {
            return response.json();
          } else {
            throw new Error("Something went wrong");
          }
        })
        .then((data) => {
          // console.log(data.output);
          const map_coords = [];
          data.output.forEach((x) => {
            map_coords.push({ org_geo_coord_x: x[0], org_geo_coord_y: x[1] });
          });

          this.markerData = map_coords;
          this.markerTempData = map_coords;
          this.initMap();
        })
        .catch((err) => {
          this.error = true;
          console.log(err, "Failed to fetch data");
        });
    },

    loadGeoJson() {
      this.map.data.loadGeoJson(
        "https://storage.googleapis.com/mapsdevsite/json/states.js",
        { idPropertyName: "STATE" }
      );

      this.map.data.setStyle({
        strokeColor: "black",
        strokeOpacity: 0.5,
        strokeWeight: 1,
        fillColor: "white",
        fillOpacity: 1,
        strokeDasharray: "4 4", // dashed stroke
        zIndex: 1,
        label: {
          color: "black",
          fontWeight: "bold",
          textProperty: "STATE_NAME",
          zIndex: 9999,
        },
      });

      const plainMapType = new window.google.maps.StyledMapType(this.styles, {
        name: "Plain Map",
      });

      this.map.mapTypes.set("plain_map", plainMapType);
      this.map.setMapTypeId("plain_map");
    },
    dataSlice() {
      // console.log(this.sliderValue);
      this.markerData = this.markerTempData.slice(0, this.sliderValue + 1);
      this.initMap();
    },

    addMarkers() {
      var markerIcons = {
        url: "https://chart.googleapis.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|e28743",
        size: new window.google.maps.Size(21, 34),
        origin: new window.google.maps.Point(0, 0),
        anchor: new window.google.maps.Point(10, 34),
      };

      if (this.markerData.length != 0) {
        this.markerData.forEach((x) => {
          const lng = parseFloat(x.org_geo_coord_x);
          const lat = parseFloat(x.org_geo_coord_y);

          const marker = new window.google.maps.Marker({
            position: { lat: lat, lng: lng },
            map: this.map,
            icon: markerIcons,
          });

          const contentString = `
            <div class="map-card">
              <!-- Your content here -->
            </div>
          `;

          const infowindow = new window.google.maps.InfoWindow({
            content: contentString,
          });

          marker.addListener("click", function () {
            infowindow.open(this.map, marker);
          });
        });
      }
    },

    usaLabels() {
      const coords_label = this.stateLabels;

      coords_label.forEach((x) => {
        const lat = parseFloat(x.coords.lat);
        const long = parseFloat(x.coords.lon);

        const marker = new window.google.maps.Marker({
          position: { lat: lat, lng: long },
          map: this.map,

          label: x.code,
          icon: {
            path: "M 0 0", // Hide the default marker icon
          },
          zIndex: 9999,
        });
        console.log(marker);
      });
    },

    getDataFromFlask() {
      // console.log(this.selectedOption);
      axios
        .get(`http://127.0.0.1:5000/states`) // Replace with the actual Flask endpoint URL
        .then((response) => {
          this.stateNames = response.data;
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });
      axios
        .get(`http://127.0.0.1:5000/${this.selectedOption}`) // Replace with the actual Flask endpoint URL
        .then((response) => {
          this.markerTempData = response.data;
          this.markerData = response.data; // Update markerData with the received data
          // console.log(this.markerData);
          this.sliderValue = this.markerTempData.length;
          this.initMap();
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });
    },
  },

  computed: {
    stateLabels() {
      return [
        {
          code: "AL",
          label: "Alabama",
          coords: { lat: 32.806671, lon: -86.79113 },
        },
        {
          code: "AK",
          label: "Alaska",
          coords: { lat: 61.370716, lon: -152.404419 },
        },
        {
          code: "AZ",
          label: "Arizona",
          coords: { lat: 33.729759, lon: -111.431221 },
        },
        {
          code: "AR",
          label: "Arkansas",
          coords: { lat: 34.969704, lon: -92.373123 },
        },
        {
          code: "CA",
          label: "California",
          coords: { lat: 36.116203, lon: -119.681564 },
        },
        {
          code: "CO",
          label: "Colorado",
          coords: { lat: 39.059811, lon: -105.311104 },
        },
        {
          code: "CT",
          label: "Connecticut",
          coords: { lat: 41.597782, lon: -72.755371 },
        },
        {
          code: "DE",
          label: "Delaware",
          coords: { lat: 39.318523, lon: -75.507141 },
        },
        {
          code: "FL",
          label: "Florida",
          coords: { lat: 27.766279, lon: -81.686783 },
        },
        {
          code: "GA",
          label: "Georgia",
          coords: { lat: 33.040619, lon: -83.643074 },
        },
        {
          code: "HI",
          label: "Hawaii",
          coords: { lat: 21.094318, lon: -157.498337 },
        },
        {
          code: "ID",
          label: "Idaho",
          coords: { lat: 44.240459, lon: -114.478828 },
        },
        {
          code: "IL",
          label: "Illinois",
          coords: { lat: 40.349457, lon: -88.986137 },
        },
        {
          code: "IN",
          label: "Indiana",
          coords: { lat: 39.849426, lon: -86.258278 },
        },
        {
          code: "IA",
          label: "Iowa",
          coords: { lat: 42.011539, lon: -93.210526 },
        },
        {
          code: "KS",
          label: "Kansas",
          coords: { lat: 38.5266, lon: -96.726486 },
        },
        {
          code: "KY",
          label: "Kentucky",
          coords: { lat: 37.66814, lon: -84.670067 },
        },
        {
          code: "LA",
          label: "Louisiana",
          coords: { lat: 31.169546, lon: -91.867805 },
        },
        {
          code: "ME",
          label: "Maine",
          coords: { lat: 44.693947, lon: -69.381927 },
        },
        {
          code: "MD",
          label: "Maryland",
          coords: { lat: 39.063946, lon: -76.802101 },
        },
        {
          code: "MA",
          label: "Massachusetts",
          coords: { lat: 42.230171, lon: -71.530106 },
        },
        {
          code: "MI",
          label: "Michigan",
          coords: { lat: 43.326618, lon: -84.536095 },
        },
        {
          code: "MN",
          label: "Minnesota",
          coords: { lat: 45.694454, lon: -93.900192 },
        },
        {
          code: "MS",
          label: "Mississippi",
          coords: { lat: 32.741646, lon: -89.678696 },
        },
        {
          code: "MO",
          label: "Missouri",
          coords: { lat: 38.456085, lon: -92.288368 },
        },
        {
          code: "MT",
          label: "Montana",
          coords: { lat: 46.921925, lon: -110.454353 },
        },
        {
          code: "NE",
          label: "Nebraska",
          coords: { lat: 41.12537, lon: -98.268082 },
        },
        {
          code: "NV",
          label: "Nevada",
          coords: { lat: 38.313515, lon: -117.055374 },
        },
        {
          code: "NH",
          label: "New Hampshire",
          coords: { lat: 43.452492, lon: -71.563896 },
        },
        {
          code: "NJ",
          label: "New Jersey",
          coords: { lat: 40.298904, lon: -74.521011 },
        },
        {
          code: "NM",
          label: "New Mexico",
          coords: { lat: 34.840515, lon: -106.248482 },
        },
        {
          code: "NY",
          label: "New York",
          coords: { lat: 42.165726, lon: -74.948051 },
        },
        {
          code: "NC",
          label: "North Carolina",
          coords: { lat: 35.630066, lon: -79.806419 },
        },
        {
          code: "ND",
          label: "North Dakota",
          coords: { lat: 47.528912, lon: -99.784012 },
        },
        {
          code: "OH",
          label: "Ohio",
          coords: { lat: 40.388783, lon: -82.764915 },
        },
        {
          code: "OK",
          label: "Oklahoma",
          coords: { lat: 35.565342, lon: -96.928917 },
        },
        {
          code: "OR",
          label: "Oregon",
          coords: { lat: 44.572021, lon: -122.070938 },
        },
        {
          code: "PA",
          label: "Pennsylvania",
          coords: { lat: 40.590752, lon: -77.209755 },
        },
        {
          code: "RI",
          label: "Rhode Island",
          coords: { lat: 41.680893, lon: -71.51178 },
        },
        {
          code: "SC",
          label: "South Carolina",
          coords: { lat: 33.856892, lon: -80.945007 },
        },
        {
          code: "SD",
          label: "South Dakota",
          coords: { lat: 44.299782, lon: -99.438828 },
        },
        {
          code: "TN",
          label: "Tennessee",
          coords: { lat: 35.747845, lon: -86.692345 },
        },
        {
          code: "TX",
          label: "Texas",
          coords: { lat: 31.054487, lon: -97.563461 },
        },
        {
          code: "UT",
          label: "Utah",
          coords: { lat: 40.150032, lon: -111.862434 },
        },
        {
          code: "VT",
          label: "Vermont",
          coords: { lat: 44.045876, lon: -72.710686 },
        },
        {
          code: "VA",
          label: "Virginia",
          coords: { lat: 37.769337, lon: -78.169968 },
        },

        {
          code: "WA",
          label: "Washington",
          coords: { lat: 47.400902, lon: -121.490494 },
        },
        {
          code: "WV",
          label: "West Virginia",
          coords: { lat: 38.491226, lon: -80.95455 },
        },
        {
          code: "WI",
          label: "Wisconsin",
          coords: { lat: 44.268543, lon: -89.616508 },
        },
      ];
    },

    coords() {
      // Your coords data
      return [
        {
          ORG_GEO_COORD_X: "-77.23406999999999",
          ORG_GEO_COORD_Y: "38.867416",
        },
        {
          ORG_GEO_COORD_X: "-111.89846999999999",
          ORG_GEO_COORD_Y: "33.55579",
        },
        {
          ORG_GEO_COORD_X: "-83.90628000000001",
          ORG_GEO_COORD_Y: "35.968666999999996",
        },
        {
          ORG_GEO_COORD_X: "-86.80643",
          ORG_GEO_COORD_Y: "35.976434000000005",
        },
        { ORG_GEO_COORD_X: "-73.95585", ORG_GEO_COORD_Y: "40.763992" },
        { ORG_GEO_COORD_X: "-75.15856", ORG_GEO_COORD_Y: "39.949733" },
        { ORG_GEO_COORD_X: "-92.37214", ORG_GEO_COORD_Y: "34.743148" },
        { ORG_GEO_COORD_X: "-80.04183", ORG_GEO_COORD_Y: "32.810561" },
        {
          ORG_GEO_COORD_X: "-118.28038000000001",
          ORG_GEO_COORD_Y: "34.021306",
        },
        {
          ORG_GEO_COORD_X: "-78.86674000000001",
          ORG_GEO_COORD_Y: "42.892862",
        },
        {
          ORG_GEO_COORD_X: "-71.12276999999999",
          ORG_GEO_COORD_Y: "42.371790000000004",
        },
        { ORG_GEO_COORD_X: "-74.42194", ORG_GEO_COORD_Y: "40.411126" },
      ];
    },
  },
  watch: {
    stateFilter(newValue, oldValue) {
      if (JSON.stringify(newValue)!== JSON.stringify(oldValue)) {
        this.customRender();
      }
    },

    terrFilter(newValue, oldValue) {
      if (!this.isStateSelected && JSON.stringify(newValue)!== JSON.stringify(oldValue)) {
        this.customRender();
      }
    },
  },
};
</script>

<style scoped>
.map-box {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}
.google-map {
  width: 100%;
  height: 400px;
}
.map-slider {
  width: 30vw;
  background-color: transparent;
  padding: 0.5vh 2vh;
}
.title {
  width: 100%;
  height: 5vh;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1vw;
  font-weight: 600;
  background-color: #e6e6e6;
  margin: 1vh 0;
}
.slider-btn {
  background-color: turquoise;
}
.q-slider .q-slider__track{
  color: black !important;
}
</style>

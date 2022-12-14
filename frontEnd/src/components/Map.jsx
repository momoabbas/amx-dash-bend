// import { Wrapper, Status } from "@googlemaps/react-wrapper";
import { GoogleMap, useJsApiLoader, Marker } from "@react-google-maps/api";
import React from "react";
import { Box, Typography } from "@mui/material";
const containerStyle = {
  width: "400px",
  height: "400px",
};

const map_data = [
  {
    id: 1,
    modelId: "qq123",
    lat: 12.972442,
    lng: 77.580643,
    isActive: true,
  },
  {
    id: 2,
    modelId: "qq456",
    lat: 12.772442,
    lng: 77.540643,
    isActive: false,
  },
  {
    id: 3,
    modelId: "qq456",
    lat: 11.772442,
    lng: 77.440843,
    isActive: false,
  },
  {
    id: 4,
    modelId: "qq456",
    lat: 12.772432,
    lng: 78.540643,
    isActive: true,
  },
];

const center = {
  lat: 12.772442,
  lng: 77.540643,
};

export default function Map(props) {
  var dron_state_icon = {
    red: "./images/tag-red-md.png",
    green: "./images/tag-green-md.png",
  };

  const { isLoaded } = useJsApiLoader({
    id: "google-map-script",
    googleMapsApiKey: process.env.REACTA_APP_GOOGLE_MAP_API_KEY,
  });

  if (!isLoaded) {
    return <Box>loading...</Box>;
  }
  const handleMarkerClick = (prop) => {
    alert(prop);
  };
  return (
    <Box sx={{ width: "100%", height: "100%" }}>
      <GoogleMap
        center={center}
        zoom={props.zoom}
        mapContainerStyle={{ width: "100%", height: "100%" }}
      >
        {map_data.map((data, id) => {
          return (
            <Marker
              position={data}
              icon={data.isActive ? dron_state_icon.green : dron_state_icon.red}
              onClick={() => handleMarkerClick(data.modelId)}
            />
          );
        })}
      </GoogleMap>
    </Box>
  );
}

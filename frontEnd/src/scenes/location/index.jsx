import React from "react";
import Map from "../../components/Map";
import { Box, Typography } from "@mui/material";

export default function Location() {
  return (
    <Box
      sx={{
        width: "calc(100% - 250px)",
        height: "calc(100% - 40px)",
        position: "absolute",
        top: "40px",
        left: "250px",
      }}
    >
      <Map zoom={10} />
    </Box>
  );
}

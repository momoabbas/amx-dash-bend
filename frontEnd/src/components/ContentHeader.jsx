import React from "react";
import { Box, Typography } from "@mui/material";

export default function ContentHeader({ pageTilte }) {
  return (
    <Box
      sx={{
        marginBottom: "1rem",
      }}
    >
      <Typography
        sx={{
          fontSize: "1.5rem",
          fontWeight: "700",
          color: "primary.main",
          textTransform: "uppercase",
        }}
      >
        {pageTilte}
      </Typography>
    </Box>
  );
}

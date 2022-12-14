import React from "react";
import { Box, Button } from "@mui/material";
import DataTable from "../../components/DataTable";
const columns = [
  { id: "name", label: "File Name", minWidth: 170 },
  { id: "date", label: "date", minWidth: 100 },
  {
    id: "download",
    label: "",
    minWidth: 10,
  },
];

const rows = [
  {
    name: "QQ123",
    date: "12.13.2022",
    status: "dd/mm/yyyy",
  },
  {
    name: "QQ456",
    date: "12.13.2022",
    status: "dd/mm/yyyy",
  },
  {
    name: "QQ789",
    date: "12.13.2022",
    status: "dd/mm/yyyy",
  },
];

export default function LogReview() {
  return (
    <Box sx={{ width: "95%", height: "95%" }}>
      <Box
        sx={{
          width: "100%",
          height: "20%",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <Button
          variant="contained"
          component="label"
          sx={{
            width: "100%",
            height: "50%",
            backgroundColor: "primary.light",
            boxShadow: "none",
            border: "1px dashed black",
            color: "black",
            fontSize: "1rem",
            "&:hover": {
              backgroundColor: "primary.main",
              color: "white",
            },
          }}
        >
          Upload
          <input hidden accept="image/*" multiple type="file" />
        </Button>
      </Box>
      <Box sx={{ width: "100%", height: "80%" }}>
        <DataTable columns={columns} rows={rows} />
      </Box>
    </Box>
  );
}

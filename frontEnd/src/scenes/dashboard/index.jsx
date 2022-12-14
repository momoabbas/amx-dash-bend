import { Box, IconButton, useTheme, Typography } from "@mui/material";
import React from "react";
// import { tokens } from "../../theme";
import DataCircle from "../../components/DataCircle";
import MyResponsiveLine from "../../components/LineChart";
import { styles } from "./styles";
export default function Dashboard() {
  return (
    <Box className="main" sx={styles.main_container}>
      <Box sx={styles.top_main_wrap}>
        <Box sx={styles.header_wrap}>
          <Typography sx={styles.header_title}>
            flight data of the month
          </Typography>
        </Box>
        <Box sx={styles.count_wrap}>
          <DataCircle count="121" dataTitle="total flights for the month" />
          <DataCircle count="5" dataTitle="drone counts" />
          <DataCircle
            count="12"
            periods="years"
            dataTitle="average age of drones"
          />
          <DataCircle count="10" dataTitle="total annotation" />
        </Box>
      </Box>

      {/* graph  */}
      <Box sx={styles.bottom_main_wrap}>
        <Box sx={styles.header_wrap}>
          <Typography sx={styles.header_title}>
            per day flights of the month
          </Typography>
        </Box>
        <Box sx={styles.line_char_wrap}>
          <MyResponsiveLine />
        </Box>
      </Box>
    </Box>
  );
}

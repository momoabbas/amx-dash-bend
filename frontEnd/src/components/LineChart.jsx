import React from "react";
import { Box, IconButton, useTheme, Typography } from "@mui/material";
import { ResponsiveLine } from "@nivo/line";
import { mockLineData as data } from "../data/mockData";

const MyResponsiveLine = () => (
  <ResponsiveLine
    data={data}
    margin={{ top: 50, right: 110, bottom: 50, left: 60 }}
    xScale={{ type: "point" }}
    yScale={{
      type: "linear",
      min: "auto",
      max: "auto",
      stacked: true,
      reverse: false,
    }}
    yFormat=" >-.2f"
    axisTop={null}
    axisRight={null}
    axisBottom={{
      orient: "bottom",
      tickSize: 6,
      tickPadding: 7,
      tickRotation: 0,
      legend: "Day",
      legendOffset: 36,
      legendPosition: "middle",
    }}
    axisLeft={{
      orient: "left",
      tickSize: 6,
      tickPadding: 5,
      tickRotation: 0,
      legend: "Flights",
      legendOffset: -44,
      legendPosition: "middle",
    }}
    colors={{ scheme: "category10" }}
    lineWidth={5}
    pointSize={10}
    pointColor={{ from: "color", modifiers: [] }}
    pointBorderWidth={2}
    pointBorderColor="#006385"
    enablePointLabel={true}
    pointLabelYOffset={-10}
    useMesh={true}
    legends={[]}
  />
);
export default MyResponsiveLine;

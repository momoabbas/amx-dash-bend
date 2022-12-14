import { useState } from "react";
import { Box, IconButton, useTheme, Typography } from "@mui/material";
import {
  Sidebar as ProSideBar,
  Menu,
  MenuItem,
  SubMenu,
} from "react-pro-sidebar";
import DashboardIcon from "@mui/icons-material/Dashboard";
import AnalyticsIcon from "@mui/icons-material/Analytics";
import ListAltIcon from "@mui/icons-material/ListAlt";
import ShareLocationIcon from "@mui/icons-material/ShareLocation";
import LoupeIcon from "@mui/icons-material/Loupe";
import RateReviewIcon from "@mui/icons-material/RateReview";
import VideoLibraryIcon from "@mui/icons-material/VideoLibrary";
import RocketIcon from "@mui/icons-material/Rocket";
import ExtensionIcon from "@mui/icons-material/Extension";
import "../../styles/global.css";
import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <ProSideBar className="sidebar-container">
      <Menu
        className="menu-wrapper"
        menuItemStyles={{
          button: ({ level, active, disabled }) => {
            if (level === 0)
              return {
                color: disabled ? "#000" : "#ffffff",
                backgroundColor: active ? "#3CA9CA" : "unset",
              };
          },
        }}
      >
        <Box className="logo-wrapper">
          <img
            style={{ width: "100px", height: "100px" }}
            src="./images/logo.svg"
          />
        </Box>
        <Box className="sidebar-top-items">
          <MenuItem
            className="menu-item"
            icon={<DashboardIcon />}
            routerLink={<Link to="/" />}
          >
            Dashboard
          </MenuItem>
          <MenuItem
            className="menu-item"
            icon={<AnalyticsIcon />}
            routerLink={<Link to="/live-analytics" />}
          >
            live analytics
          </MenuItem>
          <MenuItem
            className="menu-item"
            icon={<ListAltIcon />}
            routerLink={<Link to="/drone-listed" />}
          >
            Drones Listed
          </MenuItem>
          <MenuItem
            className="menu-item"
            icon={<ShareLocationIcon />}
            routerLink={<Link to="/location" />}
          >
            Drone Locations
          </MenuItem>
          <MenuItem
            className="menu-item"
            icon={<LoupeIcon />}
            routerLink={<Link to="/add-drone" />}
          >
            Add Drones
          </MenuItem>
          <MenuItem
            className="menu-item"
            icon={<ExtensionIcon />}
            routerLink={<Link to="/plugin" />}
          >
            Pay for Plugin
          </MenuItem>
        </Box>
        <Box className="sidebar-bottom-items">
          <MenuItem
            className="menu-item"
            icon={<RateReviewIcon />}
            routerLink={<Link to="/log-review" />}
          >
            Log Review
          </MenuItem>
          <MenuItem
            className="menu-item"
            icon={<VideoLibraryIcon />}
            routerLink={<Link to="/video-list" />}
          >
            Video
          </MenuItem>
          <MenuItem
            className="menu-item"
            icon={<RocketIcon />}
            routerLink={<Link to="/mission" />}
          >
            Mission
          </MenuItem>
        </Box>
      </Menu>
    </ProSideBar>
  );
}

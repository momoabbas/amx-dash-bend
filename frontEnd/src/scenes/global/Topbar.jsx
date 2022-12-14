import React, { useContext } from "react";
import { Box, IconButton, useTheme, Typography } from "@mui/material";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import LogoutIcon from "@mui/icons-material/Logout";
import { useNavigate, useLocation } from "react-router-dom";
import { AuthContext } from "../../components/UserInfo";
export default function Topbar() {
  const { setUserState } = useContext(AuthContext);
  const navigate = useNavigate();
  const location = useLocation();
  let user = JSON.parse(localStorage.getItem("userInfo"));
  function logOut() {
    localStorage.clear();
    setUserState(false);
    navigate(location.state ? location.state.from.pathname : "/login");
  }
  return (
    <Box className="topbar">
      <Box display="flex">
        <IconButton type="button" className="topbar-icon-wrapper">
          <AccountCircleIcon className="topbar-icon" />
          <Typography className="topbar-text">PROFILE</Typography>
        </IconButton>
        <IconButton
          type="button"
          className="topbar-icon-wrapper"
          onClick={logOut}
        >
          <LogoutIcon className="topbar-icon" />
          <Typography className="topbar-text">LOG OUT</Typography>
        </IconButton>
      </Box>
    </Box>
  );
}

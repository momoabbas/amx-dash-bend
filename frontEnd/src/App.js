import "./styles/app.css";
import { ProSidebarProvider } from "react-pro-sidebar";
import { ThemeProvider, Typography } from "@mui/material";
import Topbar from "./scenes/global/Topbar";
import Sidebar from "./scenes/global/Sidebar";
import { theme } from "./theme";
import { Routes, Route } from "react-router-dom";
import Dashboard from "./scenes/dashboard";
import DronListed from "./scenes/drone-listed";
import AddDrone from "./scenes/add-drone";
import LogReview from "./scenes/log-review";
import Plugin from "./scenes/plugin";
import Login from "./scenes/login";
import Location from "./scenes/location";
import React, { useContext } from "react";
import PrivateRoutes from "./protectedRoutes";
import { AuthContext } from "./components/UserInfo";
import LiveAnalytics from "./scenes/live-anly";
function App() {
  const { userState } = useContext(AuthContext);

  return (
    <ThemeProvider theme={theme}>
      <ProSidebarProvider>
        <div className="app">
          {userState ? <Sidebar /> : null}
          <main className="content">
            {userState ? <Topbar /> : null}
            <Routes>
              <Route element={<PrivateRoutes />}>
                <Route path="/" element={<Dashboard />} />
                <Route path="/drone-listed" element={<DronListed />} />
                <Route path="/add-drone" element={<AddDrone />} />
                <Route path="/plugin" element={<Plugin />} />
                <Route path="/log-review" element={<LogReview />} />
                {/* <Route path="/video-list" element={<VideoList />} /> */}
                {/* <Route path="/mission" element={<Mission />} /> */}
                <Route path="/location" element={<Location />} />
                <Route path="/live-analytics" element={<LiveAnalytics />} />
              </Route>
              <Route path="/login" element={<Login />} />
            </Routes>
          </main>
        </div>
      </ProSidebarProvider>
    </ThemeProvider>
  );
}

export default App;

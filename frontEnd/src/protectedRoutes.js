import React, { useContext } from "react";
import { Navigate, Outlet, useLocation } from "react-router-dom";
import { AuthContext } from "./components/UserInfo";
const PrivateRoutes = () => {
  const { name, userState } = useContext(AuthContext);
  const location = useLocation();
  return userState ? (
    <Outlet />
  ) : (
    <Navigate to="/login" state={{ from: location }} />
  );
};
export default PrivateRoutes;

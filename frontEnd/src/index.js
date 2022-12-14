import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { BrowserRouter } from "react-router-dom";
import UserInfo from "./components/UserInfo";
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <UserInfo>
        <App />
      </UserInfo>
    </BrowserRouter>
  </React.StrictMode>
);

import React, { useState, createContext } from "react";
export const AuthContext = createContext();
const UserInfo = ({ children }) => {
  const [name, setName] = useState(null);
  const [userState, setUserState] = useState(false);
  const user = {
    name,
    setName,
    userState,
    setUserState,
  };
  return <AuthContext.Provider value={user}>{children}</AuthContext.Provider>;
};
export default UserInfo;

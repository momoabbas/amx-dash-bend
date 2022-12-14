import React, { useContext } from "react";
import {
  Box,
  FormControl,
  Button,
  IconButton,
  FormHelperText,
} from "@mui/material";
import { AuthContext } from "../../components/UserInfo";
import { useNavigate, useLocation } from "react-router-dom";
import OutlinedInput from "@mui/material/OutlinedInput";
import InputLabel from "@mui/material/InputLabel";
import InputAdornment from "@mui/material/InputAdornment";
import Visibility from "@mui/icons-material/Visibility";
import VisibilityOff from "@mui/icons-material/VisibilityOff";

export default function Login() {
  // const [userId, setUserId] = useState("");
  // const [userPassword, setUserPassword] = useState("");
  const { setUserState } = useContext(AuthContext);
  const navigate = useNavigate();
  const location = useLocation();
  const handleLogin = () => {
    setUserState(true);
    navigate(location.state ? location.state.from.pathname : "/");
  };
  // async function Login() {
  //   let result = await fetch("/login", {
  //     method: "POST",
  //     header: {
  //       "Content-Type": "application/json",
  //       Accept: "application/json",
  //     },
  //     body: JSON.stringify(userData),
  //   });
  //   result = await result.json();
  //   localStorage.setItem("userInfo", JSON.stringify(result));
  //   setUserState(true);
  //   navigate(location.state ? location.state.from.pathname : "/");
  // }
  const [values, setValues] = React.useState({
    userid: "",
    password: "",
    showPassword: false,
  });

  const handleChange = (prop) => (event) => {
    setValues({ ...values, [prop]: event.target.value });
  };

  const handleClickShowPassword = () => {
    setValues({
      ...values,
      showPassword: !values.showPassword,
    });
  };

  const handleMouseDownPassword = (event) => {
    event.preventDefault();
  };
  return (
    <Box
      sx={{
        width: "100vw",
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
        backgroundColor: "primary.main",
        backgroundImage: "linear-gradient(116deg, #0a556c 0%, #22667a 100%);",
        position: "absolute",
        top: "0",
        left: "0",
      }}
    >
      <Box
        sx={{
          width: "300px",
          height: "300px",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
          backgroundColor: "#efefef",
          borderRadius: "5px",
        }}
      >
        <Box sx={{ color: "primary.main", m: 1 }}>
          <img src="./images/logo-dark.svg" style={{ color: "black" }} />
        </Box>
        <FormControl sx={{ m: 1, width: "80%" }} variant="outlined">
          <InputLabel htmlFor="outlined-adornment-userid">
            Company Id
          </InputLabel>
          <OutlinedInput
            sx={{ height: "45px" }}
            id="outlined-adornment-userid"
            type={values.showPassword ? "text" : "userid"}
            value={values.userid}
            onChange={handleChange("userid")}
            endAdornment={<InputAdornment position="end"></InputAdornment>}
            label="Company Id"
          />
        </FormControl>
        <FormControl sx={{ m: 1, width: "80%" }} variant="outlined">
          <InputLabel htmlFor="outlined-adornment-password">
            Password
          </InputLabel>
          <OutlinedInput
            sx={{ height: "45px" }}
            id="outlined-adornment-password"
            type={values.showPassword ? "text" : "password"}
            value={values.password}
            onChange={handleChange("password")}
            endAdornment={
              <InputAdornment position="end">
                <IconButton
                  aria-label="toggle password visibility"
                  onClick={handleClickShowPassword}
                  onMouseDown={handleMouseDownPassword}
                  edge="end"
                >
                  {values.showPassword ? <VisibilityOff /> : <Visibility />}
                </IconButton>
              </InputAdornment>
            }
            label="Password"
          />
        </FormControl>
        <Button
          variant="contained"
          sx={{ m: 1, width: "80%", padding: "10px 16px" }}
          onClick={handleLogin}
        >
          Log in
        </Button>
        {/* <FormHelperText>Forgot your password?</FormHelperText> */}
      </Box>
    </Box>
  );
}

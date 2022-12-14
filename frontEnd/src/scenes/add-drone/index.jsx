import * as React from "react";
import {
  Box,
  Button,
  OutlinedInput,
  FormControl,
  Typography,
} from "@mui/material";
import { styles } from "./styles";
import ContentHeader from "../../components/ContentHeader";

export default function AddDrone() {
  const [values, setValues] = React.useState({
    type: "",
    uin: "",
    cid: "",
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
    <div className="main">
      <ContentHeader pageTilte="Add Drone" />
      <Box sx={styles.main_container}>
        <FormControl fullWidth sx={styles.main_wrap} variant="filled">
          <Box sx={styles.input_wrap}>
            <Typography sx={styles.input_label}>Aircraft Type:</Typography>
            <OutlinedInput
              id="outlined-adornment-weight"
              value={values.weight}
              onChange={handleChange("type")}
              aria-describedby="outlined-weight-helper-text"
              inputProps={{
                "aria-label": "aircraft type",
              }}
              sx={styles.input_field}
            />
          </Box>
          <Box sx={styles.input_wrap}>
            <Typography sx={styles.input_label}>UIN No:</Typography>
            <OutlinedInput
              id="outlined-adornment-weight"
              value={values.weight}
              onChange={handleChange("uin")}
              aria-describedby="outlined-weight-helper-text"
              inputProps={{
                "aria-label": "uin",
              }}
              sx={styles.input_field}
            />
          </Box>
          <Box sx={styles.input_wrap}>
            <Typography sx={styles.input_label}>Connection ID:</Typography>
            <OutlinedInput
              id="outlined-adornment-weight"
              value={values.weight}
              onChange={handleChange("cid")}
              aria-describedby="outlined-weight-helper-text"
              inputProps={{
                "aria-label": "cid",
              }}
              sx={styles.input_field}
            />
          </Box>
          <Button variant="contained" disableElevation sx={styles.con_btn}>
            CONNECT
          </Button>
        </FormControl>
      </Box>
    </div>
  );
}

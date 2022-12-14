import * as React from "react";
import {
  Box,
  Button,
  OutlinedInput,
  FormControl,
  Typography,
} from "@mui/material";
import Map from "../../components/Map";
// add drone css
export const styles = {
  plug_main_container: {
    width: "100%",
    height: "100%",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    flexDirection: "column",
    flexWrap: "wrap",
    backgroundColor: "primary.main",
    borderRadius: "5px",
    padding: "1rem 1rem",
  },
  plug_main_wrap: {
    width: "100%",
    display: "flex",
    justifyContent: "center",
    alignItems: "flex-start",
  },
  input_wrap: { width: "100%", marginBottom: "10px" },
  input_label: {
    color: "white",
    fontSize: "1.2rem",
    marginBottom: "10px",
  },
  input_field: { backgroundColor: "white", width: "100%" },
  add_btn: {
    backgroundColor: "primary.light",
    width: "100%",
    color: "black",
    fontSize: "1.2rem",
    marginTop: "6px",
    "&:hover": {
      backgroundColor: "secondary.main",
      color: "white",
    },
  },
  annot_wrap: {
    width: "100%",
    marginTop: "1rem",
    display: "flex",
    justifyContent: "flex-start",
    alignItems: "flex-start",
    flexDirection: "column",
  },
  annot_list_wrap: {
    width: "100%",
    height: "400px",
    display: "flex",
    justifyContent: "flex-start",
    alignItems: "flex-start",
    backgroundColor: "white",
    borderRadius: "5px",
  },
};

export default function LiveAnalytics() {
  const [pipMode, setPipMode] = React.useState({
    width: "300px",
    height: "200px",
  });
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
  const handlePipMode = () => {
    setPipMode({
      width: "300px",
      height: "200px",
    });
  };
  return (
    <Box
      sx={{
        width: "100%",
        height: "100%",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Box sx={{ width: "100%", height: "100%", padding: "1rem" }}>
        <Box
          sx={{
            width: "100%",
            height: "100%",
            backgroundColor: "black",
            position: "relative",
          }}
        >
          {/* pip map */}
          <Box
            sx={{
              position: "absolute",
              bottom: "10px",
              right: "10px",
              borderRadius: "10px",
            }}
            style={pipMode}
            onClick={handlePipMode}
          >
            <Map zoom={6} />
          </Box>
        </Box>
      </Box>
      <Box
        sx={{
          width: "332px",
          height: "100%",
          paddingTop: "1rem",
          paddingRight: "1rem",
          paddingBottom: "1rem",
        }}
      >
        <Box sx={styles.plug_main_container}>
          <FormControl fullWidth sx={styles.plug_main_wrap} variant="filled">
            <Box sx={styles.input_wrap}>
              <Typography sx={styles.input_label}>Plug-In</Typography>
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

            <Button variant="contained" disableElevation sx={styles.add_btn}>
              Add
            </Button>
          </FormControl>
          <Box sx={styles.annot_wrap}>
            <Typography sx={styles.input_label}>Annotation List:</Typography>
            <Box sx={styles.annot_list_wrap}></Box>
          </Box>
        </Box>
      </Box>
    </Box>
  );
}

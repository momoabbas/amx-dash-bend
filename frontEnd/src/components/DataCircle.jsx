import { Box, Typography } from "@mui/material";
const styles = {
  main_con: {
    width: "100%",
    height: "100%",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    flexDirection: "column",
    gap: "10px",

  },
  circle_wrap: {
    width: "152px",
    height: "152px",
    border: "10px solid",
    borderColor: "primary.main",
    borderRadius: "50%",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    flexDirection: "column",
  },
  count_txt: {
    fontSize: "4rem",
    color: "primary.main",
    fontWeight: "500",
    lineHeight: "64px",
    fontFamily: "inherit",
  },
  period_txt: {
    fontSize: "1.2rem",
    color: "primary.main",
    fontWeight: "bold",
  },
  bttm_wrap: {
    display: "flex",
    justifyContent: "flex-start",
    alignItems: "flex-start",
    flexDirection: "column",
    gap: "10px",
    flex: "1",
  },
  bttm_txt: {
    fontSize: "1rem",
    fontWeight: "500",
    color: "primary.main",
    textTransform: "uppercase",
    width: "100%",
    textAlign: "center",
  },
};
export default function DataCircle(props) {
  return (
    <Box sx={styles.main_con}>
      <Box sx={styles.circle_wrap}>
        <Typography sx={styles.count_txt}>{props.count}</Typography>
        <Typography sx={styles.period_txt}>{props.period}</Typography>
      </Box>
      <Box sx={styles.bttm_wrap}>
        <Typography sx={styles.bttm_txt}>{props.dataTitle}</Typography>
      </Box>
    </Box>
  );
}

// add drone css
export const styles = {
  main_container: {
    width: "100%",
    minHeight: "25%",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    flexWrap: "wrap",
    backgroundColor: "primary.main",
    borderRadius: "5px",
  },
  main_wrap: {
    width: "90%",
    padding: "5rem",
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
  con_btn: {
    backgroundColor: "primary.light",
    width: "200px",
    color: "black",
    fontSize: "1.2rem",
    marginTop: "2rem",
    "&:hover": {
      backgroundColor: "secondary.main",
      color: "white",
    },
  },
};

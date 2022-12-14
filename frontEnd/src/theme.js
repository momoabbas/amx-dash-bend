import { createTheme } from "@mui/material/styles";

export const tokens = () => ({
  primary: {
    100: "#cedde2",
    200: "#9dbbc4",
    300: "#6c99a7",
    400: "#3b7789",
    500: "#0a556c",
    600: "#084456",
    700: "#063341",
    800: "#04222b",
    900: "#021116",
  },
  grey: {
    100: "#f9f9f9",
    200: "#f3f3f3",
    300: "#ececec",
    400: "#e6e6e6",
    500: "#e0e0e0",
    600: "#b3b3b3",
    700: "#868686",
    800: "#5a5a5a",
    900: "#2d2d2d",
  },
  highlighter: {
    100: "#d5eaf0",
    200: "#acd4e1",
    300: "#82bfd2",
    400: "#59a9c3",
    500: "#2f94b4",
    600: "#267690",
    700: "#1c596c",
    800: "#133b48",
    900: "#091e24",
  },
});
// mui theme settings

export const themeSettings = () => {
  const colors = tokens();
  return {
    palette: {
      primary: {
        main: colors.primary[500],
        light: colors.primary[100],
      },
      secondary: {
        main: colors.highlighter[500],
      },
      background: {
        default: colors.grey[100],
      },
    },
    typography: {
      fontFamily: ["Source Sans Pro", "san-serif"].join(","),
      fontSize: 12,
      h1: {
        fontFamily: ["Source Sans Pro", "san-serif"].join(","),
        fontSize: 40,
      },
      h2: {
        fontFamily: ["Source Sans Pro", "san-serif"].join(","),
        fontSize: 32,
      },
      h3: {
        fontFamily: ["Source Sans Pro", "san-serif"].join(","),
        fontSize: 24,
      },
      h4: {
        fontFamily: ["Source Sans Pro", "san-serif"].join(","),
        fontSize: 20,
      },
      h5: {
        fontFamily: ["Source Sans Pro", "san-serif"].join(","),
        fontSize: 16,
      },
      h6: {
        fontFamily: ["Source Sans Pro", "san-serif"].join(","),
        fontSize: 14,
      },
    },
  };
};

export const theme = createTheme(themeSettings());

import { createTheme } from "@mui/material/styles"

const theme = createTheme({
  palette: {
    primary: {
    },
  },
  components: {
    MuiCssBaseline: {
      styleOverrides: {
        html: {
          direction: "rtl",
          scrollBehavior: "smooth",
        },
      },
    },
  },
})

export default theme

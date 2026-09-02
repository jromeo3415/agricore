import { createTheme } from "@mui/material";

const theme = createTheme({
    palette: {
        mode: 'light',
        primary: {
            main: '#367C2B'
        },
        secondary: {
            main: '#ff7308'
        },
        background: {
            default: '#193714'
        }
    },
    shape: {
        borderRadius: 8, 
    },
});

export default theme;
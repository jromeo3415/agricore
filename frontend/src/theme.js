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
            default: '#F7F9F6',
            paper: '#FFFFFF',
        },
    },
    shape: {
        borderRadius: 8, 
    },
});

export default theme;
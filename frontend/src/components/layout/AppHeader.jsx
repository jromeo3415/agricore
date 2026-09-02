import { AppBar, Toolbar, Typography, Box, Button } from "@mui/material";
import CompostIcon from '@mui/icons-material/Agriculture';

function AppHeader() {
    return (
        <AppBar position="static">
            <Toolbar>

                <CompostIcon sx={{ mr: 2 }} />
                <Typography variant="h6">Agricore Operations Command Center</Typography>

            </Toolbar>
        </AppBar>

    )
}

export default AppHeader;
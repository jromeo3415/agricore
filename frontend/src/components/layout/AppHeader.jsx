import { AppBar, Toolbar, Typography, Box, Button } from "@mui/material";
import CompostIcon from '@mui/icons-material/Agriculture';

function AppHeader({username, role, onLogout}) {
    return (
        <AppBar position="static">
            <Toolbar>

                <CompostIcon sx={{ mr: 2 }} />
                <Typography variant="h6">Agricore Operations Command Center</Typography>

                {username && (
                        <Box sx={{ display: 'flex', alignItems: 'center', justifyItems: 'right', gap: 2}}>
                        
                        <Typography variant="body2">{username} ({role})</Typography>

                        <Button color="inherit" onClick={onLogout}>Log Out</Button>
                    </Box>
                )}

            </Toolbar>
        </AppBar>

    )
}

export default AppHeader;
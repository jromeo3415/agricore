import { DataGrid } from "@mui/x-data-grid";
import { Alert, Box, CircularProgress } from "@mui/material";
import { useState, useEffect } from "react";
import apiClient from "../../api/client";

const columns = [
    {field: 'id', headerName: 'Farm ID', width: 100},
    {field: 'name', headerName: 'Name', width: 120},
    {field: 'count', headerName: '# of Equipment', width: 100},
    {field: 'maintenance_count', headerName: '# w/ Maintenance Status', width: 120},
    {field: 'maintenance_percent', headerName: '% Maintenance Equipment', width: 120},
]

function FarmMaintenanceDataGrid() {
    const [farms, setFarms] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        let isMounted = true;
        setLoading(true);

        async function fetchFarms() {
            try {
                const response = await apiClient.get('/farms/maintenance_flags');
                if (isMounted) setFarms(response.data);
            } catch {
                if (isMounted) setError('Unable to retrieve maintenance flagged farms');
            } finally {
                if (isMounted) setLoading(false);
            }
        }
        
        fetchFarms();
        return(() => isMounted = false);
    }, []);

    return(
        <Box>
            {loading && <CircularProgress/>}
            {error && <Alert severity="error">{error}</Alert>}
            {!loading && !error && <DataGrid rows={farms} columns={columns} getRowId={(row) => row.id} /> }
        </Box>
    );
}

export default FarmMaintenanceDataGrid;
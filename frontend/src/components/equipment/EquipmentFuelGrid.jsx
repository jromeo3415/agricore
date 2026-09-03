import { DataGrid } from "@mui/x-data-grid";
import { Alert, Box, CircularProgress } from "@mui/material";
import { useState, useEffect } from "react";
import apiClient from "../../api/client";

const columns = [
    {field: 'id', headerName: 'Equipment ID', width: 120},
    {field: 'model', headerName: 'Model', width: 100},
    {field: 'status', headerName: 'Status', width: 70},
    {field: 'fuel_level', headerName: 'Fuel Level', width: 100},
    {field: 'facility_id', headerName: 'Farm ID', width: 70},
]

function EquipmentFueldGrid() {
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [equipment, setEquipment] = useState([]);

    useEffect(() => {
        let isMounted=true;
        async function fetchMissions() {
            setLoading(true);

            try {
                const response = await apiClient.get('/equipments?fuel_threshold=30')
                if (isMounted) setEquipment(response.data);
                setError(null);
            } catch {
                if (isMounted) setError('Unable to retrieve reliability metrics');
            } finally {
                if (isMounted) {setLoading(false);
            }
            }
        
            isMounted = false;
        }

        fetchMissions();
}, []);


    return (
        <Box>
            {loading && <CircularProgress />}
            {error && <Alert severity="error">{error}</Alert>}
            {!loading && !error && <DataGrid rows={equipment} columns={columns} getRowId={(row) => row.id}/>}
        </Box>
    )
};

export default EquipmentFueldGrid
import { DataGrid } from "@mui/x-data-grid";
import apiClient from "../../api/client";
import { useState, useEffect } from "react";
import { CircularProgress, Box, Alert } from "@mui/material";

const columns = [
    {field: 'id', headerName: 'Job ID', width: 70},
    {field: 'title', headerName: 'Title', width: 100},
    {field: 'equipment_farm_id', headerName: 'Equipment Farm ID', width: 150},
    {field: 'operator_farm_id', headerName: 'Operator Farm ID', width: 150},
];

function DiscrepancyDataGrid() {
    const [loading, setLoading] = useState(true);
    const [discrepancies, setDiscrepancies] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        let isMounted = true;
        setLoading(true);

        async function fetchDiscrepancies() {
            try {
                const response = await apiClient.get('/field_jobs/discrepancies');
                if (isMounted) setDiscrepancies(response.data)
            } catch {
                if (isMounted) setError('Could not load mission discrepancies');
            } finally {
                if (isMounted) setLoading(false);
            }
        }

        fetchDiscrepancies();
        return() => {
            isMounted=false;
        }
    }, []);

    return (
        <Box>
            {loading && <CircularProgress/>}
            {error && <Alert severity="error">{error}</Alert>}

            {!loading && !error && (
                <Box sx={{width: '%100'}}>
                    <DataGrid rows={discrepancies} columns={columns} getRowId={(row) => row.id} />
                </Box>
            )}
        </Box>
    );
}

export default DiscrepancyDataGrid;
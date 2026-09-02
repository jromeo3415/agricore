import { DataGrid } from "@mui/x-data-grid";
import { useState, useEffect } from "react";
import apiClient from "../../api/client";
import { Alert, Box, CircularProgress } from "@mui/material";

const columns = [
    {field: 'equipment_model', headerName: 'Equipment Model', width: 100},
    {field: 'completed', headerName: 'Completed', width: 80},
    {field: 'failed', headerName: 'Failed', width: 80},
    {field: 'completed_to_failed', headerName: 'C - F Ratio', width: 120},
]

function ReliabilityMetricsDataGrid() {
    const [loading, setLoading] = useState(true);
    const [metrics, setMetrics] = useState([])
    const [error, setError] = useState(null);

    useEffect(() => {
        let isMounted = true;
        async function fetchMetrics() {
            try {
                const response = await apiClient.get('/field_jobs/reliability_metrics')
                if (isMounted) setMetrics(response.data);
            } catch {
                if (isMounted) setError('Unable to retrieve maintenance flagged farms');
            } finally {
                if (isMounted) setLoading(false)
            }
            isMounted = false;
        }

        fetchMetrics();
    }, []);

    return (
        <Box>
            {loading && <CircularProgress />}
            {error && <Alert severity="error" />}
            {!error && !loading && <DataGrid rows={metrics} columns={columns} getRowId={(row) => row.equipment_model} />}
        </Box>
    );
}

export default ReliabilityMetricsDataGrid;
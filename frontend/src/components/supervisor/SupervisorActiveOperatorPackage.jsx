
import { useState } from "react";
import { Box, Typography, TextField, Stack, Button, CircularProgress, Alert, Card, CardContent } from "@mui/material";
import apiClient from "../../api/client";

function SupervisorActiveOperatorPackage() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [supervisorData, setSupervisorData] = useState(null);
  const [supervisorID, setSupervisorID] = useState("");

  async function buttonSubmit() {
    setError(null);
    setSupervisorData(null);

    if (!supervisorID.trim()) {
      setError("Please enter a supervisor ID");
      return;
    }

    setLoading(true);

    try {
      const response = await apiClient.get(
        `/supervisors/${supervisorID}/active_operators`
      );

      setSupervisorData(response.data);
    } catch (err) {
      if (err.response?.status === 404) {
        setError("Supervisor not found or has no active operators.");
      } else {
        setError("Unable to query supervisor data.");
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        gap: 2,
        alignItems: "center",
      }}
    >
      <Typography variant="h6">
        Find the number of active operators for a supervisor
      </Typography>

      <Stack direction="row" spacing={2}>
        <TextField
          label="Supervisor ID"
          type="number"
          value={supervisorID}
          onChange={(e) => setSupervisorID(e.target.value)}
          size="small"
        />

        <Button
          variant="contained"
          onClick={buttonSubmit}
          disabled={loading}
        >
          Search
        </Button>
      </Stack>

      {loading && <CircularProgress />}

      {error && (
        <Alert severity="error" sx={{ width: "100%", maxWidth: 500 }}>
          {error}
        </Alert>
      )}

      {supervisorData && (
        <Card sx={{ width: "100%", maxWidth: 500 }}>
          <CardContent>
            <Typography variant="h6">
              {supervisorData.name}
            </Typography>

            <Typography color="text.secondary">
              Supervisor ID: {supervisorData.id}
            </Typography>

            <Typography sx={{ mt: 2 }}>
              Active Operators:{" "}
              <strong>
                {supervisorData.farmhands_active_jobs}
              </strong>
            </Typography>
          </CardContent>
        </Card>
      )}
    </Box>
  );
}

export default SupervisorActiveOperatorPackage;
import { Typography, Container } from "@mui/material";
import AppHeader from "./components/layout/AppHeader"
import DiscrepancyDataGrid from "./components/field_job/DiscrepancyDataGrid"
import EquipmentFueldGrid from "./components/equipment/EquipmentFuelGrid";
import FarmMaintenanceDataGrid from "./components/farm/FarmMaintenanceDataGrid";
import ReliabilityMetricsDataGrid from "./components/field_job/ReliabilityMetricsDataGrid";

function Dashboard() {
  return (
    <>
      <AppHeader />
      
      <Container maxWidth="lg" sx={{mt: 4}}>

        <Typography>
          Low Fuel Equipment
        </Typography>
        <EquipmentFueldGrid />

        <Typography>
          Colocation Discrepancies
        </Typography>
        <DiscrepancyDataGrid/>

        <Typography>
          Farms with lots of maintenance equipment
        </Typography>
        <FarmMaintenanceDataGrid />

        <Typography>
          Equipment Reliability Metrics
        </Typography>
        <ReliabilityMetricsDataGrid />

        </Container>
    </>
  )
}

export default Dashboard;
import { Typography, Container } from "@mui/material";
import AppHeader from "./components/layout/AppHeader"
import { AuthProvider, useAuth } from "./context/AuthContext";
import LoginForm from "./components/auth/LoginForm";
import DiscrepancyDataGrid from "./components/field_job/DiscrepancyDataGrid"
import EquipmentFueldGrid from "./components/equipment/EquipmentFuelGrid";
import FarmMaintenanceDataGrid from "./components/farm/FarmMaintenanceDataGrid";
import ReliabilityMetricsDataGrid from "./components/field_job/ReliabilityMetricsDataGrid";
import SupervisorActiveOperatorPackage from "./components/supervisor/SupervisorActiveOperatorPackage";

function Dashboard() {
  const{user, logout} = useAuth()
  
  return (
    <>
      <AppHeader username={user?.sub} role={user?.role} onLogout={logout}/>
      
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

        <SupervisorActiveOperatorPackage />

        </Container>
    </>
  )
}

function AppContent() {
    const{isAuthenticated} = useAuth();
    return isAuthenticated ? <Dashboard /> : <LoginForm />
}

function App(){
  return (
    <AuthProvider>
      <AppContent />
    </AuthProvider>
  )
}

export default App;
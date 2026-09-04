import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import theme from './theme.js'
import { ThemeProvider, CssBaseline } from '@mui/material'
import { AuthProvider } from './context/AuthContext.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <ThemeProvider theme={theme}>
      <AuthProvider>
        <CssBaseline />
        <App />
      </AuthProvider>
    </ThemeProvider>
  </StrictMode>
)

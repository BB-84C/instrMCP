@echo off
REM InstrMCP Jupyter Lab Startup Script
REM This script starts Jupyter Lab with instrMCP configured

echo.
echo ================================================================================
echo Starting Jupyter Lab with instrMCP
echo ================================================================================
echo.

REM Set environment variables
set instrMCP_PATH=D:\instrMCP
set PYTHONPATH=D:\instrMCP

REM Create startup notebook
python start_jupyter_mcp.py

pause

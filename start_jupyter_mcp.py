"""
Helper script to start Jupyter Lab with instrMCP server.

This script:
1. Creates a startup notebook if needed
2. Launches Jupyter Lab
3. Instructions to load and start the MCP server
"""

import subprocess
import os
import sys
from pathlib import Path

def create_startup_notebook():
    """Create a minimal startup notebook for instrMCP."""
    notebook_content = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# InstrMCP Server Startup\n",
                    "\n",
                    "This notebook initializes the instrMCP server for use with Claude Code and other AI assistants."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "source": [
                    "# Load the instrMCP extension\n",
                    "%load_ext instrmcp.extensions"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "source": [
                    "# Start the MCP server on port 8123 (default)\n",
                    "%mcp_start"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "source": [
                    "# Check server status\n",
                    "%mcp_status"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "source": [
                    "# Enable unsafe mode (allows code execution, parameter setting, measurements)\n",
                    "# WARNING: Only enable this if you trust the AI assistant\n",
                    "%mcp_unsafe"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "source": [
                    "# Optional: Enable additional features\n",
                    "# %mcp_option add measureit database\n",
                    "# %mcp_restart"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Server is Ready!\n",
                    "\n",
                    "The instrMCP server is now running and ready to accept connections from Claude Code.\n",
                    "\n",
                    "You can now use Claude Code to interact with instruments and run measurements."
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.11.5"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    import json
    notebook_path = Path("D:/instrMCP/instrMCP_startup.ipynb")
    with open(notebook_path, 'w') as f:
        json.dump(notebook_content, f, indent=2)
    
    print(f"Created startup notebook: {notebook_path}")
    return notebook_path

def main():
    """Start Jupyter Lab with instrMCP."""
    # Create startup notebook
    notebook_path = create_startup_notebook()
    
    print("\n" + "="*80)
    print("Starting Jupyter Lab with instrMCP")
    print("="*80)
    print("\nNext steps:")
    print("1. Jupyter Lab will open in your browser")
    print(f"2. Open the notebook: {notebook_path.name}")
    print("3. Run each cell to:")
    print("   - Load the instrMCP extension")
    print("   - Start the MCP server")
    print("   - Enable unsafe mode (for full functionality)")
    print("4. Once running, Claude Code can connect to the server")
    print("\n" + "="*80 + "\n")
    
    # Set environment variables
    os.environ['instrMCP_PATH'] = 'D:/instrMCP'
    os.environ['PYTHONPATH'] = 'D:/instrMCP'
    
    # Start Jupyter Lab
    subprocess.run(['jupyter', 'lab', '--notebook-dir=D:/instrMCP'], cwd='D:/instrMCP')

if __name__ == "__main__":
    main()

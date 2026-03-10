# InstrMCP Configuration for qdevBot

## ✅ Installation Complete

InstrMCP has been successfully installed and configured for use with Claude Code (qdevBot).

### Configuration Files Created

1. **MCP Server Config**: `C:/Users/Administrator/.qdevbot/config/instrmcp.json`
2. **MCP Config**: `C:/Users/Administrator/.qdevbot/config/mcp.json`
3. **Startup Helper**: `D:/instrMCP/start_jupyter_mcp.py`

## 🚀 Quick Start

### Option 1: Automatic Startup (Recommended)

```bash
cd D:/instrMCP
python start_jupyter_mcp.py
```

This will:
- Create a startup notebook (`instrMCP_startup.ipynb`)
- Launch Jupyter Lab
- Provide step-by-step instructions

### Option 2: Manual Startup

1. **Start Jupyter Lab**:
   ```bash
   cd D:/instrMCP
   jupyter lab
   ```

2. **Create a new notebook and run these cells**:

   ```python
   # Cell 1: Load instrMCP extension
   %load_ext instrmcp.extensions
   ```

   ```python
   # Cell 2: Start MCP server
   %mcp_start
   ```

   ```python
   # Cell 3: Check status
   %mcp_status
   ```

   ```python
   # Cell 4: Enable unsafe mode (for full functionality)
   %mcp_unsafe
   ```

   ```python
   # Cell 5 (Optional): Enable additional features
   # %mcp_option add measureit database
   # %mcp_restart
   ```

## 🔧 Configuration Details

### MCP Server Settings

- **Host**: `127.0.0.1`
- **Port**: `8123` (default)
- **Transport**: STDIO proxy (for Claude Code compatibility)
- **Launcher**: `D:/instrMCP/agentsetting/claudedesktopsetting/claude_launcher.py`

### Environment Variables

The following are automatically set:
- `instrMCP_PATH=D:/instrMCP`
- `PYTHONPATH=D:/instrMCP`

## 📋 Verification Checklist

- [x] InstrMCP installed (`pip install -e .`)
- [x] Configuration files created
- [x] Startup script created
- [ ] Jupyter Lab started
- [ ] MCP server running
- [ ] Claude Code connected

## 🧪 Testing the Connection

### 1. Check if Jupyter MCP server is running

```bash
curl http://127.0.0.1:8123/health
```

Expected output: `{"status":"ok"}`

### 2. Test MCP connection from Claude Code

In Claude Code, type:
```
/mcp
```

You should see `instrMCP` listed as an available server.

### 3. Test a simple command

Ask Claude Code:
```
What MCP tools are available?
```

## 🛠️ Troubleshooting

### Issue: "instrMCP not configured"

**Cause**: Jupyter server with instrMCP extension is not running.

**Solution**: 
1. Start Jupyter Lab
2. Load the extension with `%load_ext instrmcp.extensions`
3. Start the server with `%mcp_start`

### Issue: "Connection refused"

**Cause**: MCP server not listening on port 8123.

**Solution**:
1. Check Jupyter Lab is running
2. Verify `%mcp_status` shows "Server running"
3. Check firewall isn't blocking port 8123

### Issue: "Module not found: instrmcp"

**Cause**: InstrMCP not installed in the current Python environment.

**Solution**:
```bash
cd D:/instrMCP
pip install -e .
```

## 📚 Next Steps

Once the server is running, you can:

1. **Explore instruments**: 
   - Ask Claude Code: "What instruments are available?"

2. **Run measurements**:
   - Ask Claude Code: "Show me how to do a 1D sweep"

3. **Access database**:
   - Enable with: `%mcp_option add database`
   - Ask Claude Code: "What experiments are in the database?"

4. **Use MeasureIt templates**:
   - Enable with: `%mcp_option add measureit`
   - Ask Claude Code: "Show me MeasureIt measurement templates"

## 🔒 Security Notes

- **Safe Mode** (default): Read-only access, no code execution
- **Unsafe Mode** (`%mcp_unsafe`): Allows code execution, parameter setting, measurements
  - ⚠️ Only enable if you trust the AI assistant
  - User consent required for cell modifications

## 📖 Documentation

- **InstrMCP Docs**: https://instrmcp.readthedocs.io
- **QCoDeS Docs**: https://qcodes.github.io/Qcodes/
- **MCP Protocol**: https://github.com/anthropics/mcp

---

**Status**: Configuration complete ✅  
**Next Step**: Start Jupyter Lab and run the MCP server

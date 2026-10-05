### Check the virtual environment
If you are unsure which Python interpreter is running, check its path:

```powershell
python -c "import sys; print(sys.executable)"
```

For this project, the path should end with `.venv\Scripts\python.exe`.

If a different environment is being used, activate this project's environment:

```powershell
.\.venv\Scripts\Activate.ps1
```
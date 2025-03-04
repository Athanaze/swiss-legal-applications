# build_portable_vectorizer.ps1
# Script to build a portable .exe for Vectorizer on Windows using PyInstaller
# Assumes only vectorizer.py is present in the current directory

# Exit on error
$ErrorActionPreference = "Stop"

# Define variables
$ProjectDir = Get-Location
$ScriptName = "vectorizer.py"
$OutputDir = Join-Path $ProjectDir "dist"
$ExeName = "Vectorizer.exe"
$ModelName = "BAAI/bge-m3"
$ModelDestDir = Join-Path $ProjectDir "models" $ModelName
$BuildSpec = "vectorizer.spec"
$PythonVersion = "3.10.13"
$PythonInstaller = "python-$PythonVersion.exe"
$PythonUrl = "https://www.python.org/ftp/python/$PythonVersion/python-$PythonVersion.exe"

# Check if running on Windows
if ($env:OS -ne "Windows_NT") {
    Write-Host "This script is designed for Windows. Use the Linux version on non-Windows systems."
    exit 1
}

# Ensure vectorizer.py exists
if (-not (Test-Path $ScriptName)) {
    Write-Host "Error: $ScriptName not found in the current directory ($ProjectDir)."
    exit 1
}

# Install Python if not already installed
$PythonPath = "C:\Python310\python.exe"
if (-not (Test-Path $PythonPath)) {
    Write-Host "Python not found. Downloading and installing Python $PythonVersion..."
    Invoke-WebRequest -Uri $PythonUrl -OutFile $PythonInstaller
    Start-Process -FilePath $PythonInstaller -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait -NoNewWindow
    Remove-Item $PythonInstaller
    # Update PATH for this session
    $env:Path = "C:\Python310;C:\Python310\Scripts;" + $env:Path
}

# Verify Python is installed
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Error: Python installation failed or not added to PATH."
    exit 1
}
Write-Host "Python version:"
python --version

# Install pip if not present
if (-not (python -m pip --version 2>$null)) {
    Write-Host "Installing pip..."
    Invoke-WebRequest -Uri "https://bootstrap.pypa.io/get-pip.py" -OutFile "get-pip.py"
    python get-pip.py
    Remove-Item "get-pip.py"
}

# Install required Python packages
Write-Host "Installing required Python packages..."
python -m pip install pyinstaller PyQt6 PyPDF2 sentence-transformers openai torch psutil matplotlib plyer pynvml huggingface_hub

# Check if the model already exists and skip download if it does
if ((Test-Path $ModelDestDir) -and (Test-Path (Join-Path $ModelDestDir "pytorch_model.bin"))) {
    Write-Host "Model '$ModelName' already exists at $ModelDestDir, skipping download."
} else {
    Write-Host "Downloading the BAAI/bge-m3 model to local directory..."
    $downloadScript = @"
from huggingface_hub import snapshot_download
import os

MODEL_NAME = "BAAI/bge-m3"
MODEL_DEST_DIR = os.path.join(os.getcwd(), "models", MODEL_NAME)

# Create the models directory if it doesn't exist
os.makedirs(os.path.dirname(MODEL_DEST_DIR), exist_ok=True)

# Download the model
snapshot_download(repo_id=MODEL_NAME, local_dir=MODEL_DEST_DIR, force_download=True)
print(f"Model '{MODEL_NAME}' downloaded to {MODEL_DEST_DIR}")
"@
    $downloadScript | Out-File -FilePath "download_model.py" -Encoding utf8
    python download_model.py
    Remove-Item "download_model.py"
}

# Verify the model directory exists and has the required file
if (-not (Test-Path $ModelDestDir) -or -not (Test-Path (Join-Path $ModelDestDir "pytorch_model.bin"))) {
    Write-Host "Error: Model directory or pytorch_model.bin not found. Check permissions or network."
    exit 1
}

# Create a PyInstaller spec file if it doesn’t exist
if (-not (Test-Path $BuildSpec)) {
    Write-Host "Generating PyInstaller spec file..."
    pyi-makespec --onefile `
                 --add-data "$ModelDestDir;models/$ModelName" `
                 --add-data "$ScriptName;." `
                 --icon=$null `
                 --name "$($ExeName -replace '.exe','')" "$ScriptName"
}

# Modify the spec file to include additional data files and hidden imports
$specContent = @"
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['$ScriptName'],
             pathex=['$ProjectDir'],
             binaries=[],
             datas=[('$ModelDestDir', 'models/$ModelName')],
             hiddenimports=['PyQt6.QtWidgets', 'PyQt6.QtCore', 'PyQt6.QtGui', 'torch', 'sentence_transformers', 'openai', 'psutil', 'matplotlib', 'plyer', 'pynvml', 'huggingface_hub'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='$($ExeName -replace '.exe','')',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          icon=None)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='$($ExeName -replace '.exe','')')
"@
$specContent | Out-File -FilePath $BuildSpec -Encoding utf8

# Build the executable using PyInstaller
Write-Host "Building portable .exe file..."
pyinstaller --noconfirm --clean $BuildSpec

# Debug: List contents of dist/ to diagnose
Write-Host "Listing contents of dist/ after build:"
Get-ChildItem -Path $OutputDir -Recurse | Format-Table -AutoSize

# Move the .exe to a convenient location and clean up
Write-Host "Moving .exe to $OutputDir..."
if (-not (Test-Path $OutputDir)) { New-Item -ItemType Directory -Path $OutputDir | Out-Null }
$exePath = Join-Path $OutputDir "Vectorizer" $ExeName
if (Test-Path $exePath) {
    Move-Item -Path $exePath -Destination $OutputDir
    Write-Host "Moved $ExeName to $OutputDir/"
} elseif (Test-Path (Join-Path $OutputDir $ExeName)) {
    Write-Host "$ExeName already in $OutputDir (unexpected location)"
} else {
    Write-Host "Warning: Could not find $ExeName in expected locations. Checking for alternative files..."
    $execFile = Get-ChildItem -Path $OutputDir -Filter "Vectorizer*" -Recurse | Select-Object -First 1
    if ($execFile) {
        Move-Item -Path $execFile.FullName -Destination (Join-Path $OutputDir $ExeName)
        Write-Host "Found and moved $($execFile.FullName) to $OutputDir/$ExeName"
    } else {
        Write-Host "Error: No .exe file found in dist/. Check PyInstaller output for errors."
        exit 1
    }
}

# Clean up temporary files
Write-Host "Cleaning up..."
Remove-Item -Path "build" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path (Join-Path $OutputDir "Vectorizer") -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path $BuildSpec -Force -ErrorAction SilentlyContinue

Write-Host "Build complete! Portable .exe is located at $OutputDir/$ExeName"
Write-Host "You can run it directly: $OutputDir/$ExeName"

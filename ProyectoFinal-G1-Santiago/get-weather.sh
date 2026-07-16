#!/bin/bash
# Activar Conda
source /home/emilioalbanfs/miniforge3/etc/profile.d/conda.sh
eval "$(conda shell.bash hook)"
conda activate iccd332
# Ir al directorio del proyecto
cd "$(dirname "$0")"
export OPENWEATHER_API_KEY="2879a8a960c30d3235371fa96f1e579b"
python3 main.py >> output.log 2>&1

"""
Herramientas (tools) del agente Strands para vsCode-AI.

Cada módulo expone funciones decoradas con @tool que el agente puede invocar
autónomamente durante la generación de proyectos firmware.
"""

from agent.tools.catalog_tools import load_board, load_peripheral, list_catalog
from agent.tools.guide_tools import read_guide, list_guides
from agent.tools.file_tools import write_file, read_project_file, list_project_files
from agent.tools.analysis_tools import analyze_code, detect_board, detect_peripherals

# Lista completa de tools para pasarle al agente
ALL_TOOLS = [
    load_board,
    load_peripheral,
    list_catalog,
    read_guide,
    list_guides,
    write_file,
    read_project_file,
    list_project_files,
    analyze_code,
    detect_board,
    detect_peripherals,
]

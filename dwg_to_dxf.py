import aspose.cad as cad
from aspose.cad.imageoptions import DxfOptions, CadRasterizationOptions
from aspose.cad import Color  # Correct Color import
import os
import time
from tqdm import tqdm  # Progress bar
import argparse  # For command-line arguments
# local
import support


#  Main function to handle both command-line and VSCode front-end execution
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert DWG files to DXF format.")
    parser.add_argument("--directory", help="Path to the directory containing DWG files")
    args = parser.parse_args()

    if args.directory:
        # Command-line mode
        input_directory = args.directory
        if not os.path.isdir(input_directory):
            print(f"Error: The directory '{input_directory}' does not exist.")
        else:
            support.convert_dwg_to_dxf(input_directory)
    else:
        # VSCode Interactive Mode
        # 👇 Set this manually when running from VSCode
        input_directory = './dwg_files'
        # input_directory = r"C:\Users\bradley.eylander\OneDrive - LMI Consulting\CUI-PSNS SIOP CADS\DoD SAFE-jeshUoUp36YSF8YC"
        layers_only = False

        # Validate and run
        if not os.path.isdir(input_directory):
            print(f"Error: The directory '{input_directory}' does not exist.")
        else:
            print(f"Running in VSCode Interactive Mode using directory: {input_directory}")
            support.convert_dwg_to_dxf(input_directory, layers_only=layers_only)

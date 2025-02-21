import aspose.cad as cad
from aspose.cad.imageoptions import DxfOptions, CadRasterizationOptions
from aspose.cad import Color  # Correct Color import
import os
import time
from tqdm import tqdm  # Progress bar
import argparse  # For command-line arguments
# local
import support

# Function to handle DWG to DXF conversion
def convert_dwg_to_dxf(fdir):
    # Create an output directory for DXF files
    output_dir = os.path.join(fdir, "DXF_Converted")
    os.makedirs(output_dir, exist_ok=True)

    # Get all DWG files in the directory
    dwg_files = [f for f in os.listdir(fdir) if f.lower().endswith('.dwg')]
    total_files = len(dwg_files)
    print(f"Found {total_files} DWG files for conversion.")

    # Start processing with a progress bar
    for i, dwg_file in enumerate(tqdm(dwg_files, desc="Converting DWG to DXF", unit="file")):
        dwg_path = os.path.join(fdir, dwg_file)
        dxf_file = os.path.splitext(dwg_file)[0] + ".dxf"
        dxf_path = os.path.join(output_dir, dxf_file)

        start_time = time.time()  # Track time for each file

        try:
            support.dxf_options(dwg_path, dwg_file, dxf_path, dxf_file, start_time, total_files, i)
        except Exception as e:
            print(f"\nError converting {dwg_file}: {e}")

        try:
            support.print_dxf_file(dxf_path)
        except Exception as e:
            print(f"\nError getting layers from DXF file {dxf_file}: {e}")

    print("Batch conversion completed successfully!")

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
            convert_dwg_to_dxf(input_directory)
    else:
        # VSCode Interactive Mode
        # 👇 Set this manually when running from VSCode
        input_directory = './dwg_files'

        # Validate and run
        if not os.path.isdir(input_directory):
            print(f"Error: The directory '{input_directory}' does not exist.")
        else:
            print(f"Running in VSCode Interactive Mode using directory: {input_directory}")
            convert_dwg_to_dxf(input_directory)

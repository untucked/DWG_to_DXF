import aspose.cad as cad
from aspose.cad.imageoptions import DxfOptions, CadRasterizationOptions
from aspose.cad import Color  # Correct Color import
import os
import time
from tqdm import tqdm  # Progress bar

# Specify the directory containing the DWG files
fdir = './dwg_files'

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
        # Load DWG file
        image = cad.Image.load(dwg_path)

        # Specify DXF options
        # cadRasterizationOptions =  cad.imageoptions.CadRasterizationOptions()
        # Specify DXF options
        #  # Specify DXF options
        # cadRasterizationOptions.page_height = 800.5
        # cadRasterizationOptions.page_width = 800.5
        # cadRasterizationOptions.zoom = 1.5
        # cadRasterizationOptions.layers = "Layer"
        # cadRasterizationOptions.background_color = Color.green

        options =  cad.imageoptions.DxfOptions()
        options.version = cad.imageoptions.DxfOutputVersion.R12

        # Save as DXF
        image.save(dxf_path, options)

        # Calculate time taken for this file
        time_taken = time.time() - start_time
        estimated_time_remaining = time_taken * (total_files - (i + 1))

        print(f"\n{dwg_file} converted to {dxf_file} ({time_taken:.2f} sec)")
        print(f"Estimated time remaining: {estimated_time_remaining / 60:.2f} minutes")
    
    except Exception as e:
        print(f"\nError converting {dwg_file}: {e}")
    break

print("Batch conversion completed successfully!")

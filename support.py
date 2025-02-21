import aspose.cad as cad
from aspose.cad.imageoptions import DxfOptions, CadRasterizationOptions
from aspose.cad import Color  # Correct Color import
import time
from aspose.cad import Image
from aspose.cad.fileformats.cad import CadImage
import ezdxf
import os

def dxf_options(dwg_path, dwg_file, dxf_path, dxf_file,
                start_time, total_files, idx):
    # Load DWG file
    image = cad.Image.load(dwg_path)

    # Specify DXF options
    options = DxfOptions()
    options.version = cad.imageoptions.DxfOutputVersion.R12  # Most compatible version

    # Rasterization options for better resolution
    raster_options = CadRasterizationOptions()
    raster_options.page_height = 1200.0  # Increased resolution height
    raster_options.page_width = 1200.0   # Increased resolution width
    raster_options.zoom = 2.0  # Higher zoom for better detail
    # raster_options.layers = ["Model"]  # Convert only the "Model" layout
    raster_options.background_color = Color.green  # White background for clarity

    # Attach rasterization options to DXF options
    options.vector_rasterization_options = raster_options

    # Save as DXF
    image.save(dxf_path, options)

    # Calculate time taken for this file
    time_taken = time.time() - start_time
    estimated_time_remaining = time_taken * (total_files - (idx + 1))

    print(f"\n{dwg_file} converted to {dxf_file} ({time_taken:.2f} sec)")
    print(f"Estimated time remaining: {estimated_time_remaining / 60:.2f} minutes")

def print_dxf_file(dxf_file):
    try:
        doc = ezdxf.readfile(dxf_file)
        layers = doc.layers

        print("Available layers:")
        for i, layer in enumerate(layers, start=1):
            print(f"{i}. {layer.dxf.name}")

        return [layer.dxf.name for layer in layers]

    except IOError:
        print(f"Cannot open DXF file: {dxf_file}")
    except ezdxf.DXFStructureError:
        print("Invalid or corrupted DXF file.")


if __name__ == "__main__":
    dxf_file = './dwg_files/DXF_Converted/civil_example-imperial.dxf'
    print_dxf_file(dxf_file)
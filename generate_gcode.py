import os
import subprocess

def generate_gcode(stl_file, prusa_slicer_path="prusa-slicer", config_file=None):
    """
    Generate a G-code file from an STL using PrusaSlicer.
    
    Args:
        stl_file (str): Path to the STL file.
        prusa_slicer_path (str): Path to the PrusaSlicer executable. Default assumes it's in the PATH.
        config_file (str): Optional path to a PrusaSlicer configuration file (.ini).
    
    Returns:
        str: Path to the generated G-code file, or error message if the process fails.
    """
    # Check whether stl file exists
    if not os.path.isfile(stl_file):
        return f"Error: STL file '{stl_file}' does not exist."
        
    # Generate output filename from stl filename
    stl_filename = os.path.basename(stl_file)
    gcode_filename = os.path.splitext(stl_filename)[0] + ".gcode"
    gcode_path = gcode_filename


    # Build the command for the prusa slicer subprocess
    command = [
        prusa_slicer_path,
        "--export-gcode",       # Flag to export G-code
        stl_filename,               # Input STL file
        "--output", gcode_path # Output G-code file path
    ]
    
    # Add configuration file if provided
    if config_file:
        if not os.path.isfile(config_file):
            return f"Error: Config file '{config_file}' does not exist."
        command.extend(["--load", config_file])

    try:
        # Run the PrusaSlicer command
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            return f"G-code generated successfully: {gcode_path}"
        else:
            return f"Error during slicing: {result.stderr}"
    except FileNotFoundError:
        return f"Error: PrusaSlicer executable not found at '{prusa_slicer_path}'."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


# If this script is started directly, execute the function generate_gcode
if __name__ == "__main__":
    
    # Inputs
    stl_file = "flowerpot.stl"  # Path to your STL file
    prusa_slicer_path = "C:\\Program Files\\Prusa3D\\PrusaSlicer\\prusa-slicer-console.exe" # Prusa Standard Slicer Path for Windows Console use
    config_file = "flower_pot_config.ini"  # Path to my custom config file, can be exported from Prusa Slicer under File ->  Export --> Export Configuration

    # Generate G-code
    result = generate_gcode(stl_file, prusa_slicer_path, config_file)
    print(result)
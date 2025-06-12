import datetime
import os
import argparse
from typing import Optional

print("Script started")  # Debug output

def get_user_input(prompt: str, default: Optional[str] = None) -> str:
    """Get user input with an optional default value."""
    if default:
        user_input = input(f"{prompt} [{default}]: ").strip()
        return user_input if user_input else default
    return input(f"{prompt}: ").strip()

def generate_filepath(
    institution: str,
    work_package: str,
    location: str,
    sensor_type: str,
    sensor_number: int,
    data_type: str,
    date: datetime.datetime,
    extension: str = "jpg"
) -> tuple[str, str]:
    """
    Generate a standardized filepath and filename from metadata.
    
    Args:
        institution (str): Institution code (e.g., 'uu')
        work_package (str): Work package identifier (e.g., 'WP3')
        location (str): Location name (e.g., 'zandmotor')
        sensor_type (str): Type of sensor (e.g., 'camera')
        sensor_number (int): Sensor identifier number (e.g., 1)
        data_type (str): Type of data (e.g., 'raw-data')
        date (datetime.datetime): Date of the data collection
        extension (str): File extension (default: 'jpg')
    
    Returns:
        tuple[str, str]: (filepath, filename)
    """
    # Generate filename components
    filename_parts = [
        date.strftime('%b.%d.%Y'),
        location,
        f'{sensor_type}{sensor_number}',
        data_type,
        extension
    ]
    filename = '.'.join(filename_parts)
    
    # Generate path components
    path_parts = [
        'Research',
        f'research-{institution}',
        work_package,
        location,
        data_type,
        sensor_type,
        f'{sensor_type}{sensor_number}',
        date.strftime('%Y'),
        date.strftime('%b.%d')
    ]
    
    # Join path and filename
    return os.path.join(*path_parts), filename

def main():
    print("Entering main function")  # Debug output
    parser = argparse.ArgumentParser(description='Generate standardized file paths for Delta Enigma data')
    parser.add_argument('--interactive', action='store_true', help='Run in interactive mode')
    args = parser.parse_args()
    print(f"Arguments parsed: {args}")  # Debug output

    if args.interactive:
        print("\n=== Delta Enigma Path Generator ===\n")
        print("Enter the following information (press Enter to use defaults):\n")

        # Get user input with sensible defaults
        institution = get_user_input("Institution code", "uu")
        work_package = get_user_input("Work package", "WP3")
        location = get_user_input("Location", "zandmotor")
        sensor_type = get_user_input("Sensor type", "camera")
        sensor_number = int(get_user_input("Sensor number", "1"))
        data_type = get_user_input("Data type", "raw-data")
        extension = get_user_input("File extension", "jpg")
        
        # Get date input
        while True:
            try:
                date_str = get_user_input("Date (YYYY-MM-DD)", datetime.datetime.now().strftime("%Y-%m-%d"))
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD")

        # Generate and display results
        filepath, filename = generate_filepath(
            institution=institution,
            work_package=work_package,
            location=location,
            sensor_type=sensor_type,
            sensor_number=sensor_number,
            data_type=data_type,
            date=date,
            extension=extension
        )

        print("\n=== Generated Path Information ===")
        print(f"Full path: {filepath}")
        print(f"Filename: {filename}")
        print(f"Complete path: {os.path.join(filepath, filename)}")
        
        # Create directory structure
        create_dirs = input("\nWould you like to create this directory structure? (y/n): ").lower()
        if create_dirs == 'y':
            try:
                os.makedirs(filepath, exist_ok=True)
                print(f"\nDirectory structure created at: {filepath}")
            except Exception as e:
                print(f"\nError creating directory structure: {e}")
    else:
        # Example usage
        date = datetime.datetime(2024, 5, 26)  # May 26, 2024
        filepath, filename = generate_filepath(
            institution='uu',
            work_package='WP3',
            location='zandmotor',
            sensor_type='camera',
            sensor_number=1,
            data_type='raw-data',
            date=date
        )
        print(f"Generated filepath:\n{filepath}\nFilename:\n{filename}")

if __name__ == "__main__":
    main() 
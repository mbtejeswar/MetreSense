import pandas as pd
import os

def create_dataset_csv(image_folder_path):
    # Ensure the 'images/' directory exists
    os.makedirs('images', exist_ok=True)
    
    # Create DataFrame structure
    dataset = {
        'image_name': [],
        'meter_reading': []
    }
    
    df = pd.DataFrame(dataset)
    
    # Save empty CSV template
    csv_path = 'data/images/meter_readings.csv'
    df.to_csv(csv_path, index=False)
    print(f"Created empty CSV at: {csv_path}")
    
    # Print example of how to add entries
    print("\nExample format:")
    print("image_name,meter_reading")
    print("meter1.jpg,00822976")
    print("meter2.jpg,00823001")

# Example usage
image_folder = "images"
create_dataset_csv(image_folder)


def add_meter_reading(image_name, reading):
    csv_path = 'data/images/meter_readings.csv'
    
    # Check if the CSV file exists
    if not os.path.exists(csv_path):
        print(f"CSV file not found at {csv_path}. Please create it first.")
        return
    
    # Read the existing CSV file
    df = pd.read_csv(csv_path)
    
    # Add the new row
    new_row = {'image_name': image_name, 'meter_reading': reading}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    
    # Save the updated CSV
    df.to_csv(csv_path, index=False)
    print(f"Added reading for {image_name}")

# Example: add_meter_reading("meter1.jpg", "00822976")


def add_images_to_csv(image_folder, csv_path='data/images/meter_readings.csv'):
    # Ensure the CSV file exists
    if not os.path.exists(csv_path):
        # Create an empty CSV if it doesn't exist
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        df = pd.DataFrame(columns=['image_name', 'meter_reading'])
        df.to_csv(csv_path, index=False)
        print(f"Created new CSV file at {csv_path}")
    else:
        # Load the existing CSV
        df = pd.read_csv(csv_path)

    # Get all image names from the folder
    image_names = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Add new images to the CSV if they are not already present
    existing_images = set(df['image_name']) if not df.empty else set()
    new_images = [img for img in image_names if img not in existing_images]

    if new_images:
        # Create rows for new images with empty meter_reading
        new_rows = [{'image_name': img, 'meter_reading': ''} for img in new_images]
        df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)
        df.to_csv(csv_path, index=False)
        print(f"Added {len(new_images)} new images to the CSV.")
    else:
        print("No new images to add. All images are already in the CSV.")

    print(f"CSV updated at: {csv_path}")

# Example usage
image_folder = "data/images/meters"  # Replace with the path to your folder containing images
add_images_to_csv(image_folder)
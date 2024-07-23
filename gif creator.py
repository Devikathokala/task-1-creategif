import imageio
import os

def create_gif(image_folder, output_gif, duration):
    images = []
    # Get all image files in the given folder
    for filename in os.listdir(image_folder):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            file_path = os.path.join(image_folder, filename)
            images.append(imageio.imread(file_path))
    
    # Save images as GIF
    imageio.mimsave(output_gif, images, duration=duration)

if __name__ == "__main__":
    image_folder = 'path/to/your/images'  # Folder containing images
    output_gif = 'output.gif'  # Output file name
    duration = 0.5  # Duration of each frame in seconds

    create_gif(image_folder, output_gif, duration)
    print(f"GIF saved as {output_gif}")

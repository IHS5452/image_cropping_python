from PIL import Image

def crop_image():
    image_path = input("Enter the image path: ")
    image = Image.open(image_path)

    current_width, current_height = image.size
    print("Current image dimensions:")
    print("Width:", current_width)
    print("Height:", current_height)

    new_width = int(input("Enter the new width: "))
    new_height = int(input("Enter the new height: "))

    save_location = input("Enter the save location: ")
    output_filename = input("Enter the output file name: ")
    output_filepath = f"{save_location}/{output_filename}"

    try:
        cropped_image = image.crop((0, 0, new_width, new_height))
        cropped_image.save(output_filepath)
        print("Image cropped and saved successfully:", output_filepath)
    except Exception as e:
        print("Error:", str(e))

crop_image()

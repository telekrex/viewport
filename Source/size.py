def resize_image(original_size, limit_x, limit_y):
    # Unpack original size
    original_x, original_y = original_size

    # Calculate new size while maintaining aspect ratio
    if original_x <= limit_x and original_y <= limit_y:
        # Image already within limits
        new_size = (original_x, original_y)
    else:
        # Calculate new size with the same aspect ratio
        ratio = min(limit_x / original_x, limit_y / original_y)
        new_size = (int(original_x * ratio), int(original_y * ratio))

    return new_size

# Example usage
if __name__ == "__main__":
    # Replace these values with your image size and limits
    image_size = (2500, 5400)
    limit_x = 500
    limit_y = 400

    new_size = resize_image(image_size, limit_x, limit_y)
    print(f"Original Size: {image_size}")
    print(f"Resized Size: {new_size}")
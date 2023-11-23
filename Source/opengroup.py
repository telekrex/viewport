import os

x = "C:/Users/nitro/Documents/GitHub/image-viewer/Test Images/msedge_S70Jw7RAVq.png"

def grab_files(from_path):
    head, tail = os.path.split(from_path)
    folder = str(head)
    files = []
    for item in os.listdir(folder):
        for format in ['.png', '.jpg', '.jpeg', '.bmp', '.tif', '.gif', '.webp']:
            if item.endswith(format):
                item_path = folder + '/' + item
                files.append(item_path)
    return files, files.index(from_path)


def neat_name(file_path):
    head, tail = os.path.split(file_path)
    for format in ['.png', '.jpg', '.jpeg', '.bmp', '.tif', '.gif', '.webp']:
        tail = str(tail.replace(format, ''))
    return tail


all_images, current_file = grab_files(x)

print(all_images)
print(current_file)
print(neat_name(all_images[current_file]))
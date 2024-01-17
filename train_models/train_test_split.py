import os
import shutil
from sklearn.model_selection import train_test_split


def get_files_in_current_folder(folder_path="."):
    # 获取当前文件夹下所有文件的路径
    files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if
             os.path.isfile(os.path.join(folder_path, file))]
    return files


def delete_folder_contents(folder_path):
    shutil.rmtree(folder_path)
    print(f"All contents of {folder_path} have been deleted.")


if __name__ == "__main__":
    delete_folder_contents("/home/yy/data/wildfire/flames2/flames2_output")
    '''
    label_root_path = "/home/yy/data/wildfire/data_enhance/labels/"
    image_paths = get_files_in_current_folder("/home/yy/data/wildfire/data_enhance/images")
    # train_images, test_images = train_test_split(image_paths, test_size=0.15, random_state=42)
    train_images, val_images = train_test_split(image_paths, test_size=0.1, random_state=42)
    train_dir = '/home/yy/data/wildfire/D-Fire-001/train/'
    # test_dir = '/home/yy/data/wildfire/D-Fire-001/test/'
    val_dir = '/home/yy/data/wildfire/D-Fire-001/val/'
    
    train_img = train_dir + "images"
    train_labels = train_dir + "labels"
    # test_img = test_dir + "images"
    # test_labels = test_dir + "labels"
    val_img = val_dir + "images"
    val_labels = val_dir + "labels"
    
    os.makedirs(train_img, exist_ok=True)
    os.makedirs(train_labels, exist_ok=True)
    # os.makedirs(test_img, exist_ok=True)
    # os.makedirs(test_labels, exist_ok=True)
    os.makedirs(val_img, exist_ok=True)
    os.makedirs(val_labels, exist_ok=True)
    
    for train_path in train_images:
        shutil.copy(train_path, train_img)
        txt_path = label_root_path + train_path.split("/")[-1].split(".")[0] + ".txt"
        shutil.copy(txt_path, train_labels)
    
    print("train update OK")
    # for test_path in test_images:
    #     shutil.copy(test_path, test_img)
    #     txt_path = label_root_path + test_path.split("/")[-1].split(".")[0] + ".txt"
    #     shutil.copy(txt_path, test_labels)
    # print("test update OK")
    for val_path in val_images:
        shutil.move(val_path, val_img)
        txt_path = label_root_path + val_path.split("/")[-1].split(".")[0] + ".txt"
        shutil.move(txt_path, val_labels)
    # 将图片和标签信息移动到相应的文件夹
    # def move_files(image_paths, labels, destination_dir):
    #     for image, label in zip(image_paths, labels):
    #         shutil.copy(image, os.path.join(destination_dir, os.path.basename(image)))
    #         shutil.copy(os.path.join(labels_dir, label), os.path.join(destination_dir, os.path.splitext(os.path.basename(image))[0] + '.txt'))
    #
    # move_files(train_images, train_labels, train_dir)
    # move_files(test_images, test_labels, test_dir)
    '''


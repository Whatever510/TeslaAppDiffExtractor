import os
import json
import zipfile



def setup():
    if not os.path.exists("results"):
        os.mkdir("result")

    if not os.path.exists("unzipped"):
        os.mkdir("unzipped")

    print("[INFO] Result Folder is setup")

"""
Unzips the APK file and stores it in the folder unzipped with the fitting version Number
@param zip_file_old: The name of the old file
@param zip_file_new: The name of the new file
"""
def unzip(zip_file_old, zip_file_new, version_number_old, version_number_new):


    # Specify the folders where the unzipped files will be placed
    directory_to_extract_to_old = "unzipped/" + version_number_old
    directory_to_extract_to_new = "unzipped/" + version_number_new

    # If the folders do not exist yet, create them and unzip
    if not os.path.exists(directory_to_extract_to_old):
        os.mkdir(directory_to_extract_to_old)
        with zipfile.ZipFile(zip_file_old, 'r') as zip_ref:
            zip_ref.extractall(directory_to_extract_to_old)

    if not os.path.exists(directory_to_extract_to_new):
        os.mkdir(directory_to_extract_to_new)
        with zipfile.ZipFile(zip_file_new, 'r') as zip_ref:
            zip_ref.extractall(directory_to_extract_to_new)

    print("[INFO] The files have been extracted")


"""
Method to display images. Not currently in use
"""
def show_images(path1, path2, added, deleted):
    index = 0
    for file in deleted:
        path = os.path.join(path1,file)
        image = cv2.imread(path)
        cv2.imshow("Deleted{}".format(index), image)
        index+=1
        cv2.waitKey(0)

    index = 0
    for file in added:
        path = os.path.join(path2,file)
        image = cv2.imread(path)
        cv2.imshow("Added{}".format(index), image)
        index+=1
        cv2.waitKey(0)


"""
Find the differences between the two versions.
@param old_files: A list containing all the files of the old version.
@param new_files: A list containing all the files of the new version.
@param path1: the base path of the old version.
@param path2: the base path of the new version.
@return: List containing the deleted and added files.
"""
def get_differences(old_files, new_files, path1, path2):
    deleted = []
    added = []

    old_files_stripped = list({x.replace('\\','/').replace(path1, '') for x in old_files})
    new_files_stripped = list({x.replace('\\','/').replace(path2, '') for x in new_files})

    for name in old_files_stripped:
        if not name in new_files_stripped:
            deleted.append(name)

    for name in new_files_stripped:
        if not name in old_files_stripped:
            added.append(name)

    return deleted, added

"""
Extract all the files in a given directory.
@param dir_name: The base dir for the search directory.
@return: a list containing the paths to all the files in the given directory
"""
def get_list_of_files(dir_name):

    list_of_files = os.listdir(dir_name)
    all_files = list()

    for entry in list_of_files:
        fullPath = os.path.join(dir_name, entry)

        if (os.path.isdir(fullPath)):
            all_files = all_files + get_list_of_files(fullPath)
        else:
            all_files.append(fullPath)

    return all_files

"""
Create the output file containing the paths to all the added and deleted files
@param deleted: a list containing all the deleted files.
@param added: a list containing all the added files.
"""
def create_output_file(deleted, added):

    with open("result/PathDifferences.txt","w") as out_file:
        out_file.write("This File contains the added and deleted Files entrys\n\n")
        out_file.write("DELETED\n")
        for filename in deleted:
            out_file.write("- " + filename+'\n')
        out_file.write(100*'#'+'\n\n')
        out_file.write("ADDED\n")
        for filename in added:
            out_file.write("+ " + filename+'\n')

"""
Extract the differences in the locales String file
@param locales_file_old: path to the old locales file.
@param locales_file_new: path to the new locales file.
@return: Two lists containing the deleted and added files
"""
def get_locales_differneces(locales_file_old, locales_file_new):
    deleted_strings = []
    added_strings = []

    with open(locales_file_old, "r") as file_old:
        locales_old = file_old.readlines()

    with open(locales_file_new, "r") as file_new:
        locales_new = file_new.readlines()

    for line in locales_old:
        if not line in locales_new:
            deleted_strings.append(line)
            #print("Deleted"+line)
    for line in locales_new:
        if not line in locales_old:
            added_strings.append(line)
            #print("Added"+line)

    return deleted_strings, added_strings

"""
Save the added and deleted string ressources to a txt file.
@param deleted_strings: the list of deleted string resources.
@param added_strings: the list of added string resources.
"""
def save_strings(deleted_strings, added_strings):

    with open("result/StringDifferences.txt","w") as result_file:
        result_file.write("This File contains the added and deleted String entrys\n\n")
        result_file.write("DELETED\n")
        for line in deleted_strings:
            result_file.write("-" +line+'\n')

        result_file.write(100*('#') + '\n\n')
        result_file.write("ADDED\n")
        for line in added_strings:
            result_file.write("+" +line + '\n')

"""
Get the difference in the API files
@param api_old: the path to the old api file
@param api_new: the path to the new api file
"""
def get_api_differences(api_old, api_new):
    api_list_old = []
    api_list_new = []

    with open(api_old) as old_api_file:
        api_list_old = json.load(old_api_file)

    with open(api_new) as new_api_file:
        api_list_new = json.load(new_api_file)

    keys_old = api_list_old.keys()
    keys_new = api_list_new.keys()

    with open("result/ApiDifferences.txt","w") as api_file:
        api_file.write("This File contains the added and deleted API entrys\n\n")
        api_file.write("DELETED\n")
        for name in keys_old:
            if not name in keys_new:
                api_file.write("- " +name+'\n')

        api_file.write(100*('#') + '\n\n')
        api_file.write("ADDED\n")
        for name in keys_new:
            if not name in keys_old:
                api_file.write("+ " +name+'\n')

"""
Finds a certain file in the given directory.
@param name: The name of the file to be found.
@param path: The base directory for the search.
"""
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def main(zip_file_old = "", zip_file_new = ""):
    working_dir = os.getcwd().replace('\\','/')

    setup()

    #zip_file_old = "ZipFiles\com.teslamotors.tesla_4.2.3-742-742_minAPI23(arm64-v8a,armeabi-v7a,x86_64)(nodpi)_apkmirror.com.apk"
    #zip_file_new = "ZipFiles\com.teslamotors.tesla_4.3.0-766-766_minAPI23(arm64-v8a,armeabi-v7a,x86_64)(nodpi)_apkmirror.com.apk"
    if not os.path.exists(zip_file_old) or not os.path.exists(zip_file_new):
        print("[ERROR] One or both files can´t be opened. Please try again")
        return
    # Get the path ending, which is the name of the APK
    zip_file_name_old = os.path.basename(os.path.normpath(zip_file_old))
    zip_file_name_new = os.path.basename(os.path.normpath(zip_file_new))

    # Extract the version number from the APK name
    version_number_old = zip_file_name_old.split("_")[1].split("-")[0]
    version_number_new = zip_file_name_new.split("_")[1].split("-")[0]

    print("[INFO] Unzipping files...")
    unzip(zip_file_old, zip_file_new,version_number_old, version_number_new)

    base_dir_old = working_dir + "/unzipped/" + version_number_old
    base_dir_new = working_dir + "/unzipped/" + version_number_new

    print(base_dir_old)

    locales_file_old = find("app_i18n_locales_en.json", base_dir_old).replace('\\','/')
    locales_file_new = find("app_i18n_locales_en.json", base_dir_new).replace('\\','/')

    owners_api_file_old = find("env_ownerapi_endpoints.json", base_dir_old).replace('\\','/')
    owners_api_file_new = find("env_ownerapi_endpoints.json", base_dir_new).replace('\\','/')


    #path1 = "D:/Programming/TeslaApp/4.2.3/Android/"
    #path2 = "D:/Programming/TeslaApp/4.3.0/Android/"

    #locales_file_old = "D:/Programming/TeslaApp/4.2.3/Android/res/raw/app_i18n_locales_en.json"
    #locales_file_new = "D:/Programming/TeslaApp/4.3.0/Android/res/raw/app_i18n_locales_en.json"


    #path_to_owner_api_old = "D:/Programming/TeslaApp/4.2.3/Android/res/raw/env_ownerapi_endpoints.json"
    #path_to_owner_api_new = "D:/Programming/TeslaApp/4.3.0/Android/res/raw/env_ownerapi_endpoints.json"
    print("[INFO] Extracting all the files of the old and new version")
    old_files = get_list_of_files(base_dir_old)
    new_files = get_list_of_files(base_dir_new)
    print("[INFO] Calculating differences...")

    deleted, added = get_differences(old_files, new_files, base_dir_old, base_dir_new)

    create_output_file(deleted, added)
    print("[INFO] Differences saved to PathDifferences.txt")

    print("[INFO] Extracting String differences")
    deleted_strings, added_strings = get_locales_differneces(locales_file_old, locales_file_new)

    save_strings(deleted_strings, added_strings)
    print("[INFO] Saved String differences to StringDifferences.txt")

    print("[INFO] Extracting API differences")
    get_api_differences(owners_api_file_old, owners_api_file_new)
    print("[INFO] Saved API Differences to ApiDifferences.txt")

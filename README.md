# Tesla App Update Differences Extractor

Python program that finds the differences between two versions of the Tesla App.
When Tesla updates the app a lot of changes happen unnoticed. This program finds all the added and deleted files, API endpoints as well as the added and deleted text resources.

## Requirements
To use this program, please install the required packages with the following commands:

```
pip install tk
```

## Usage
Download the APK File (not the Bundle File) from [APK Mirror](https://www.apkmirror.com/) and save it on your PC. The tesla apk can be found here: [Tesla APK](https://www.apkmirror.com/apk/tesla-motors-inc/tesla-motors/). Do not unpack the file.

Then start the GUI and select the APK File of the older and newer version by running:

```
python gui.py
```

## Output
The program will create two directories.
- The **unzipped/** directory contains the unzipped apk data. This directory can be deleted after the program finishes. To inspect the added files follow the paths specified in **PathDifferences.txt**

- The **result** directory contains three txt files:
    - **ApiDifferences.txt** contains all changes to the api calls.+
    - **StringDifferences.txt** contains all the added and deleted String resources between the two versions
    - **PathDifferences** contains the paths to all added and deleted files. To inspect a certain element follow the path mentioned in the file. The unzipped apks can be found in the **unzipped/** directory. To see deleted files check in the older version, to see newly added file check the newer version.

# Tesla App Update Differences Extractor

Python program that finds the differences between two versions of the Tesla App.
When Tesla updates the app a lot of changes happen unnoticed. This program finds all the added and deleted files, API endpoints as well as the added and deleted text resources.

## Requirements
To use this program, please install the required packages with the following commands:

```
pip install tk
```

## Usage

The program works with android and iOS files. Please make sure to check the checkbox if the provided file is an iOS app. If an android apk file is used do **NOT** check the box, otherwise the program will crash.

To start the gui run:



```
python gui.py
```

### For Android
Download the APK File (not the Bundle File) from [APK Mirror](https://www.apkmirror.com/) and save it on your PC. The tesla apk can be found here: [Tesla APK](https://www.apkmirror.com/apk/tesla-motors-inc/tesla-motors/). Do not unpack the file.




### For iOS
Download the app file and convert it to a .zip file. This can be done by unzipping the file with [WinRAR](https://www.win-rar.com/start.html?&L=1) and zipping it again.
Select the iOS Checkbox at the bottom.

### Starting the Program
After the files have been selected and the checkbox was set according to the used app files press "Start" to initiate the program.

## Output
The program will create two directories.
- The **unzipped/** directory contains the unzipped apk data. This directory can be deleted after the program finishes. To inspect the added files follow the paths specified in **PathDifferences.txt**

- The **result** directory contains three txt files:
    - **ApiDifferences.txt** contains all changes to the api calls.+
    - **StringDifferences.txt** contains all the added and deleted String resources between the two versions
    - **PathDifferences** contains the paths to all added and deleted files. To inspect a certain element follow the path mentioned in the file. The unzipped apks can be found in the **unzipped/** directory. To see deleted files check in the older version, to see newly added file check the newer version.

# google-drive-orphans
Scans local Google Drive folders for any files that have not synced with Google Drive.

I noticed some files I copied to local Google Drive folders were not being synced to the cloud.  And the non-synced files (orphans) lacked the following extended attribute:  `com.google.drivefs.item-id#S`.  So this python script looks for such orphans in a folder by printing filenames for all files that lack that extended attribute.

Usage:

`python orphans.py [-h] folder_path`

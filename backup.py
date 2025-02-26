import os
import time
import subprocess

# Configuration
DIRECTORY_TO_ARCHIVE = "/path/to/directory"  # Change this
ARCHIVE_NAME = f"backup_{time.strftime('%Y-%m-%d_%H-%M-%S')}.tar.gz"
ARCHIVE_PATH = f"/tmp/{ARCHIVE_NAME}"
RCLONE_REMOTE = "rclonename:directory"  # Replace 'myremote' with your rclone remote name
BACKUPS_AGE = "10d"

# Create a compressed archive
print(f"Creating archive: {ARCHIVE_PATH}")
subprocess.run(["tar", "-czf", ARCHIVE_PATH, DIRECTORY_TO_ARCHIVE], check=True)

# Upload to cloud using rclone
print(f"Uploading {ARCHIVE_NAME} to {RCLONE_REMOTE}")
subprocess.run(["rclone", "copy", ARCHIVE_PATH, RCLONE_REMOTE], check=True)

# Remove local archive
print("Cleaning up...")
os.remove(ARCHIVE_PATH)

# Delete files older than 10 days in backup folder
print("Deleting old backups...")
subprocess.run(["rclone", "delete", RCLONE_REMOTE, "--min-age", BACKUPS_AGE], check=True)

print("Backup completed successfully.")
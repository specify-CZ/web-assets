import os

# Sample Specify web asset server settings.

# Turns on bottle.py debugging, module reloading and printing some
# information to console.
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 'yes')

# This secret key is used to generate authentication tokens for requests.
# The same key must be set in the Web Store Attachment Preferences in Specify.
# A good source for key value is: https://www.grc.com/passwords.htm
# Set KEY to None to disable security. This is NOT recommended since doing so
# will allow anyone on the internet to use the attachment server to store
# arbitrary files.
# Can be set via the KEY environment variable for Kubernetes deployments.
KEY = os.getenv('KEY', 'test_attachment_key')

# Auth token timestamp must be within this many seconds of server time
# in order to be considered valid. This prevents replay attacks.
# Set to None to disable time tolerance.
# Can be set via the TIME_TOLERANCE environment variable.
TIME_TOLERANCE = int(os.getenv('TIME_TOLERANCE', '150'))

# Set this to True to require authentication for downloads in addition
# to uploads and deletes.  Static file access, if enabled, is not
# affected by this setting.
REQUIRE_KEY_FOR_GET = os.getenv('REQUIRE_KEY_FOR_GET', 'True').lower() in ('true', '1', 'yes')

# This is required for use with the Web Portal.
# Enables the 'getfileref' and '/static/...' URLs.
ALLOW_STATIC_FILE_ACCESS = os.getenv('ALLOW_STATIC_FILE_ACCESS', 'True').lower() in ('true', '1', 'yes')

# These values are interpolated into the web_asset_store.xml resource
# so the client knows how to talk to the server.
HOST = os.getenv('HOST', 'localhost')
PORT = int(os.getenv('PORT', '8080'))

SERVER_NAME = HOST
SERVER_PORT = PORT

# Port the development test server should listen on.
DEVELOPMENT_PORT = PORT

# Map collection names to directories.  Set to None to store
# everything in the same originals and thumbnail directories.  This is
# recommended unless some provision is made to allow attachments for
# items scoped above collections to be found.

# COLLECTION_DIRS = {
#     # 'COLLECTION_NAME': 'DIRECTORY_NAME',
#     'KUFishvoucher': 'Ichthyology',
#     'KUFishtissue': 'Ichthyology',
# }

COLLECTION_DIRS = None

# Base directory for all attachments.
BASE_DIR = os.getenv('BASE_DIR', '/home/specify/attachments/')

# Originals and thumbnails are stored in separate directories.
THUMB_DIR = os.getenv('THUMB_DIR', 'thumbnails')
ORIG_DIR = os.getenv('ORIG_DIR', 'originals')

# Set of mime types that the server will try to thumbnail.
CAN_THUMBNAIL = {'image/jpeg', 'image/gif', 'image/png', 'image/tiff', 'application/pdf', 'image/heic', 'image/heif'}

# What HTTP server to use for stand-alone operation.
SERVER = os.getenv('SERVER', 'paste') # Requires python-paste package. Fast, and seems to work good.
# SERVER = 'wsgiref'  # For testing. Requires no extra packages.


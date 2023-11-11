# Basic login system
> *All logins are hashed in sha256*

This is a simple login system similar to my previous one except this is much stronger.
It contains sha256 hashing which is the gold standard for hashing algorithms in the 
modern day.

It saves all data in the format username:password in the database in custom file type
called `.hannahs_login_system` in the database folder.

The test file login credentials are test123 pass123
## Info
To install the requirements run `pip install -r requirements.txt`
User info is stored in `./database`
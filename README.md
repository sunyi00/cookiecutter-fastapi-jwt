### To run this app:

1. cd into the new directory:
   - `cd <what you chose for app_slug>/`
2. Install the required packages:
   - `pip install -r requirements.txt`
3. Run the API with hypercorn:
   - `hypercorn app.api:api --reload`

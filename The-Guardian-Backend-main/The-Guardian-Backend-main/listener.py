import firebase_admin
from firebase_admin import credentials, db
import time

# load service account key
cred = credentials.Certificate("serviceAccountKey.json")

# start app with firebase url
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://guardian-home-security-system-default-rtdb.firebaseio.com/"
})

# references to database
command_ref = db.reference("command")
status_ref = db.reference("status")


def capture_face():
    print("📸 Simulating face capture...")
    time.sleep(2)  # pretend the camera is doing work
    print("✅ Face saved.")


def main():
    print("👂 Listening for commands...")
    last_action = None

    while True:
        command = command_ref.get()

        if command:
            action = command.get("action")

            if action != last_action:
                print(f"🆕 New command: {action}")
                last_action = action

                if action == "save_face":
                    capture_face()

                    status_ref.set({"message": "face_saved"})

                    command_ref.set({"action": "idle"})

        time.sleep(1)


if __name__ == "__main__":
    main()

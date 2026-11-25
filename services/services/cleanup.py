
import os
import time

def cleanup_old_files(folders, retention_seconds=3600):
    now = time.time()

    for folder in folders:
        if not os.path.exists(folder):
            continue

        for filename in os.listdir(folder):
            path = os.path.join(folder, filename)

            try:
                if os.path.isfile(path):
                    age = now - os.path.getmtime(path)

                    if age > retention_seconds:
                        os.remove(path)
            except OSError:
                pass

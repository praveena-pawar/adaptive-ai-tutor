from pathlib import Path
from tempfile import NamedTemporaryFile

from backend.app.services.file_storage import save_temp_file


# Create a small test file with some content.
with NamedTemporaryFile(
    mode="wb",
    suffix=".pdf",
    delete=False,
) as test_file:
    test_file.write(b"PDF storage test")
    test_file_path = Path(test_file.name)

try:
    # Open the test file and copy it to temporary storage.
    with test_file_path.open("rb") as file:
        temp_path = save_temp_file(file)

    print(f"Temporary file exists: {temp_path.exists()}")
    print(f"Temporary file path: {temp_path}")
    print(f"File size: {temp_path.stat().st_size} bytes")

    # Verify that the content was copied correctly.
    print(f"Content copied: {temp_path.read_bytes() == b'PDF storage test'}")

finally:
    # Remove both temporary test files.
    test_file_path.unlink(missing_ok=True)

    if "temp_path" in locals():
        temp_path.unlink(missing_ok=True)
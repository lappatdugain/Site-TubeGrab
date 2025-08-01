from datetime import datetime
import os

def get_file_date(file_path):
    """Return the last modification date of the file as a YYYY-MM-DD string."""
    datestamp = os.path.getmtime(file_path)
    modified_date = datetime.fromtimestamp(datestamp).strftime('%Y-%m-%d')
    return modified_date

def get_today_date():
    """Return today's date as a YYYY-MM-DD string."""
    return datetime.now().strftime('%Y-%m-%d')

def delete_old_files(directory_path):
    """Check and print the modification date of files in a directory compared to today."""
    today_date = get_today_date()
    
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if not os.path.isfile(file_path):
            continue
        try:
            file_date = get_file_date(file_path)
            if file_date != today_date:
                os.remove(file_path)
        except Exception as e:
            print(f"Error processing {filename}: {e}")


if __name__=='__main__':
    delete_old_files("/tmp/tubegrab/")






import zipfile
import os

class APKExtractor:
    def __init__(self, apk_path):
        self.apk_path = apk_path
        self.extract_to = self.get_folder_name(apk_path)

    @staticmethod
    def get_folder_name(apk_path):
        apk_name = os.path.basename(apk_path)
        folder_name = os.path.splitext(apk_name)[0]
        return folder_name

    def extract(self):
        if not zipfile.is_zipfile(self.apk_path):
            print(f"File {self.apk_path} bukan file ZIP yang valid.")
            return

        with zipfile.ZipFile(self.apk_path, 'r') as apk:
            file_list = apk.namelist()
            total_files = len(file_list)

            for i, file in enumerate(file_list, start=1):
                print(f"Mengekstrak {file} ({i}/{total_files})")
                apk.extract(file, self.extract_to)

        print(f"File {self.apk_path} diekstrak ke folder '{self.extract_to}'.")

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python apk_extractor.py <path_to_apk>")
        return

    apk_path = sys.argv[1]
    extractor = APKExtractor(apk_path)
    extractor.extract()

if __name__ == '__main__':
    main()
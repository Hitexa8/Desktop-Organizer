from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
from datetime import datetime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 0
            print(filename)
            if filename != 'newDesktop':
                new_name = filename # f1.jpg and f2.jpg
                extension = 'noname' # noname
                # print(new_name,extension)
                try:
                    extension = str(os.path.splitext(folder_to_track + '/' + filename)[1]) # .jpg
                    path = extensions_folders[extension] # C:/Users/ingle/OneDrive/Desktop/Destination/Media/Images path of newDesktop where file is to be sent
                    # print(extension,path)
                except Exception:
                    extension = 'noname'
                dir_present = extensions_folders[extension].split("/")
                main = "C:/Users/ingle/OneDrive/Desktop/Destination"
                for i in range(len(dir_present) - 6):
                    if not os.path.exists(extensions_folders[extension]):
                        os.makedirs(extensions_folders[extension])
                        main += "/" + dir_present[6+i]
                now = datetime.now() # date + time
                year = now.strftime("%Y") # year in 200x format
                month = now.strftime("%m") # month in 01 to 12
                # print(now,year,month)
                folder_destination_path = extensions_folders[extension] # C:/Users/ingle/OneDrive/Desktop/Destination/Media/Images

                year_exists = False
                month_exists = False
                for folder_name in os.listdir(extensions_folders[extension]): # returns directories in newDesktop of extension type and check for year and month
                    if folder_name == year:
                        folder_destination_path = extensions_folders[extension] + "/" + year
                        year_exists = True
                        for folder_month in os.listdir(folder_destination_path):
                            if month == folder_month:
                                folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                month_exists = True
                if not year_exists: # if folders of year nd month are not present than it will create months and years folders
                    os.mkdir(extensions_folders[extension] + "/" + year)
                    folder_destination_path = extensions_folders[extension] + "/" + year
                    # print("Made folder",year)
                if not month_exists:
                    os.mkdir(folder_destination_path + "/" + month)
                    folder_destination_path = folder_destination_path + "/" + month
                    # print("Made folder",month)
                file_exists = os.path.isfile(folder_destination_path + "/" + new_name) # false if files are not present in newDesktop
                # print(new_name,file_exists) 
                while file_exists:
                    i += 1
                    # splitext splits the path into filename + extension of it
                    # splitext[0] = path + filename and splitext[1] = extension of file
                    new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + ("("+str(i)+")") + os.path.splitext(folder_to_track + '/' + filename)[1]
                    new_name = new_name.split("/")[4]
                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    print(new_name,file_exists)
                src = folder_to_track + "/" + filename
                new_name = folder_destination_path + "/" + new_name
                print(src,new_name)
                # os.rename(src, new_name)
extensions_folders = {
# noname or other type of files
    'noname': "C:/Users/ingle/OneDrive/Desktop/Destination/Other",
# Audio
    '.aif' : "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Audio",
    '.cda' : "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Audio",
    '.mid' : "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Audio",
    '.midi' : "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Audio",
    '.mp3' : "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Audio",
    '.mpa' : "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Audio",
    '.ogg' : "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Audio",
    '.wav' : "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Audio",
    '.wma' : "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Audio",
    '.wpl' : "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Audio",
    '.m3u' : "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Audio",
#Text
    '.txt' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/TextFiles",
    '.doc' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Microsoft/Word",
    '.docx' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Microsoft/Word",
    '.odt ' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/TextFiles",
    '.pdf': "C:/Users/ingle/OneDrive/Desktop/Destination/Text/PDF",
    '.rtf': "C:/Users/ingle/OneDrive/Desktop/Destination/Text/TextFiles",
    '.tex': "C:/Users/ingle/OneDrive/Desktop/Destination/Text/TextFiles",
    '.wks ': "C:/Users/ingle/OneDrive/Desktop/Destination/Text/TextFiles",
    '.wps': "C:/Users/ingle/OneDrive/Desktop/Destination/Text/TextFiles",
    '.wpd': "C:/Users/ingle/OneDrive/Desktop/Destination/Text/TextFiles",
#Video
    '.3g2': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Video",
    '.3gp': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Video",
    '.avi': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Video",
    '.flv': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Video",
    '.h264': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Video",
    '.m4v': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Video",
    '.mkv': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Video",
    '.mov': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Video",
    '.mp4': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Video",
    '.mpg': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Video",
    '.mpeg': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Video",
    '.rm': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Video",
    '.swf': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Video",
    '.vob': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Video",
    '.wmv': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Video",
#Images
    '.ai': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Images",
    '.bmp': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Images",
    '.gif': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Images",
    '.ico': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Images",
    '.jpg': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Images",
    '.jpeg': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Images",
    '.png': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Images",
    '.ps': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Images",
    '.psd': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Images",
    '.svg': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Images",
    '.tif': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Images",
    '.tiff': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Images",
    '.CR2': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Images",
    '.webp': "C:/Users/ingle/OneDrive/Desktop/Destination/Media/Images",
# Internet
    '.asp': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Internet",
    '.aspx': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Internet",
    '.cer': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Internet",
    '.cfm': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Internet",
    '.cgi': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Internet",
    '.pl': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Internet",
    '.css': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Internet",
    '.htm': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Internet",
    '.js': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Internet",
    '.jsp': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Internet",
    '.part': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Internet",
    '.php': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Internet",
    '.rss': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Internet",
    '.xhtml': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Internet",
# Compressed
    '.7z': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Compressed",
    '.arj': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Compressed",
    '.deb': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Compressed",
    '.pkg': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Compressed",
    '.rar': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Compressed",
    '.rpm': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Compressed",
    '.tar.gz': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Compressed",
    '.z': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Compressed",
    '.zip': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Compressed",
# Disc
    '.bin': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Disc",
    '.dmg': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Disc",
    '.iso': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Disc",
    '.toast': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Disc",
    '.vcd': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Disc",
# Data
    '.csv': "C:/Users/ingle/OneDrive/Desktop/Destination/Programming/Database",
    '.dat': "C:/Users/ingle/OneDrive/Desktop/Destination/Programming/Database",
    '.db': "C:/Users/ingle/OneDrive/Desktop/Destination/Programming/Database",
    '.dbf': "C:/Users/ingle/OneDrive/Desktop/Destination/Programming/Database",
    '.log': "C:/Users/ingle/OneDrive/Desktop/Destination/Programming/Database",
    '.mdb': "C:/Users/ingle/OneDrive/Desktop/Destination/Programming/Database",
    '.sav': "C:/Users/ingle/OneDrive/Desktop/Destination/Programming/Database",
    '.sql': "C:/Users/ingle/OneDrive/Desktop/Destination/Programming/Database",
    '.tar': "C:/Users/ingle/OneDrive/Desktop/Destination/Programming/Database",
    '.xml': "C:/Users/ingle/OneDrive/Desktop/Destination/Programming/Database",
    '.json': "C:/Users/ingle/OneDrive/Desktop/Destination/Programming/Database",
# Executables
    '.apk': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Executables",
    '.bat': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Executables",
    '.com': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Executables",
    '.exe': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Executables",
    '.gadget': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Executables",
    '.jar': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Executables",
    '.wsf': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Executables",
# Fonts
    '.fnt': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Fonts",
    '.fon': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Fonts",
    '.otf': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Fonts",
    '.ttf': "C:/Users/ingle/OneDrive/Desktop/Destination/Other/Fonts",
# Presentations
    '.key': "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Presentations",
    '.odp': "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Presentations",
    '.pps': "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Presentations",
    '.ppt': "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Presentations",
    '.pptx': "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Presentations",
# Programming
    '.c': "C:/Users/ingle/OneDrive/Desktop/Destination/Programming/C&C++",
    '.class': "C:/Users/ingle/OneDrive/Desktop/Destination/Programming/Java",
    '.dart': "C:/Users/ingle/OneDrive/Desktop/Destination/Programming/Dart",
    '.py': "C:/Users/ingle/OneDrive/Desktop/Destination/Programming/Python",
    '.sh': "C:/Users/ingle/OneDrive/Desktop/Destination/Programming/Shell",
    '.swift': "C:/Users/ingle/OneDrive/Desktop/Destination/Programming/Swift",
    '.html': "C:/Users/ingle/OneDrive/Desktop/Destination/Programming/html",
    '.h': "C:/Users/ingle/OneDrive/Desktop/Destination/Programming/html",
# Spreadsheets
    '.ods' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Microsoft/Excel",
    '.xlr' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Microsoft/Excel",
    '.xls' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Microsoft/Excel",
    '.xlsx' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Microsoft/Excel",
    '.csv' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Microsoft/Excel",
# System
    '.bak' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Other/System",
    '.cab' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Other/System",
    '.cfg' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Other/System",
    '.cpl' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Other/System",
    '.cur' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Other/System",
    '.dll' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Other/System",
    '.dmp' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Other/System",
    '.drv' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Other/System",
    '.icns' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Other/System",
    '.ico' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Other/System",
    '.ini' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Other/System",
    '.lnk' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Other/System",
    '.msi' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Other/System",
    '.sys' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Other/System",
    '.tmp' : "C:/Users/ingle/OneDrive/Desktop/Destination/Text/Other/System",
}
folder_to_track = "C:/Users/ingle/OneDrive/Desktop/Track"
folder_destination = "C:/Users/ingle/OneDrive/Desktop/Destination"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
try:
	while True:
		time.sleep(10)
except KeyboardInterrupt:
	observer.stop()
observer.join()
import os 
lst=os.listdir()
print(lst)
lst.remove("main.py")
def ifnotexist(folder):
    if not os.path.exists(folder):
        os.makedirs("Images")
        os.makedirs("Media")
        os.makedirs("Docs")
        os.makedirs("Others")

def movefile(foldername,lst):
    for file in lst:
        os.replace(file,f"{foldername}/{file}")
docext=[".txt",".pdf",".ppt",".doc",".docx"]
docs=[file for file in lst if os.path.splitext(file)[1].lower() in docext]
print(docs)
imgext=[".png",".jpg",".jpeg"]
image=[file for file in lst if os.path.splitext(file)[1].lower() in imgext]
print(image)
mediaext=[".mp4",".mp3"]
media=[file for file in lst if os.path.splitext(file)[1].lower() in mediaext]
print(media)
others=[]
for file in lst:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in docext) and (ext not in imgext) and (ext not in mediaext) and os.path.isfile(file):
        others.append(file)
print(others)

ifnotexist("Images")
ifnotexist("Media")
ifnotexist("Docs")
ifnotexist("Others")

movefile("Media",media)
movefile("docs",docs)
movefile("others",others)
movefile("images",image)
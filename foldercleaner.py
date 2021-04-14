import os
file= os.listdir()
#print(file)
def main(folders):
    if not os.path.exists(folders):
        os.makedirs(folders)
main("images")
main("documents")
main("media")


imagextentions= [".jpg",".JPG",".JPEG",".jpeg",".png",".PNG"]
img= [i for i in file if os.path.splitext(i)[1] in imagextentions]

docextensions= [".pptx",".pdf",".xlsx",".docx",".txt"]
doc= [i for i in file if os.path.splitext(i)[1] in docextensions]

mediaextensions= [".mp3",".mp4"]
media = [i for i in file if os.path.splitext(i)[1] in mediaextensions ]


other= []
for files in file:
    ext = os.path.splitext(files)[1]
    if (ext not in imagextentions) and (ext not in docextensions) and (ext not in mediaextensions):
        other.append(files)
print(other)
#print(media)
for i in img:
    os.replace(i,f"images/{i}" )
for i in doc:
    os.replace(i,f"documents/{i}")
for i in media:
    os.replace(i,f"media/{i}")
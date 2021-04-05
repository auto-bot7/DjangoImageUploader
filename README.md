# DjangoImageUploader
An Image Uploader using Django that allows user to upload and view images on a webpage.
Start a django project [ImageUploader]
Create an application [api]
Register api in settings.INSTALLED APPS
Create models -
  photo - for storing images
  date - for generating/storing date of upload
Register models in admin.py
Upload an image.[using admin panel]
Check for auto-generated folder "my image" inside the project directory, your media_file/image will be stored over here.
Make changes in urls.py to view the static files/image through the link in the admin module.
To save images in the BASE directory configured in settings.py append MEDIA_ROOT=BASE_DIR/'folder_name/media'. The images now will be saved as media(path defined in settings.py)/myimage(path defined in models.py)
To provide a url to the media_files you may also use MEDIA_URL(refer django's documentation) in settings.py
Created a folder for templates inside application folder
Create a template foe home page.
Create a form.
Write views for home page, data submission and viewing images on home page.

NOTE-> The document/code is well indented and commented and is ready to be used.

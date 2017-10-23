# SimpleCloudFileServer
A very simple image file server, written in python. RAM-only storage, serves only JPEG and JSON. Defaults to running on localhost port 8000

Once this is running, upload a file with, e.g.:
`curl -H "Content-Type: image/jpeg" -X POST http://localhost:8000 --data-binary "@/Users/benwheatley/Desktop/img.jpg"`

The server _generates_ an image name when an image is uploaded, and returns that name (as JSON) in response to the upload.

Any image (there are no access restrictions) may be accessed with the URL `http://<servername>/<imagename>`. By way of example: `http://localhost:8000/1`

To find all images on the server, load the URL `http://localhost:8000/index.json`, which returns a JSON array of all file names.

Files are *never* stored. Filesystem is *never* accessed. Image filenames are generated server-side, *never* client-side, to minimise the attack surface of the server.

If you can see this message, it's only been manually tested — this project was for me to learn the Python way to do unit testing, and I've not had time yet.

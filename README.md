# Link Extractor
 
Extract links from Directory listing based on the extension.

## Docker

```bash
mkdir -p $(pwd)/files;
docker pull ghcr.io/jadia/link-extractor:latest && \
docker run -d --restart unless-stopped \
--name link-extractor \
-p 80:80 \
-v $(pwd)/files:/app/files \
ghcr.io/jadia/link-extractor:latest
```

## Screenshots

### Home Page

![Home Page](images/2021-05-29-18-27-06.png)

### Results Page

![Results Page](images/2021-05-29-18-28-46.png)

### Copy or Download the list of URLs

![Download URI list](images/2021-05-29-18-30-37.png)
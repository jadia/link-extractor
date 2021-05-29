# Link Extractor
 
Extract links from Directory listing based on the extension.

## Docker

```bash
docker run -d --restart unless-stopped \
--name link-extractor \
-p 80:80 \
-v $(pwd)/files:/app/files \
ghcr.io/jadia/link-extractor:latest
```

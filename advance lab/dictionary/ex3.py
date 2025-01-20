#Q.3) Create list of urls and you need to filter out only those that start with 'https' for Example: urls = [ "http://example.com", "https://secure-site.com", "ftp://files.example.org", "https://another-secure-site.com" ]

urls = [ "http://example.com", "https://secure-site.com", "ftp://files.example.org", "https://another-secure-site.com" ]
secure_urls = [url for url in urls if url.startswith("https")]
http_url=[url for url in urls if "https" in url]
print(secure_urls)
print(http_url)

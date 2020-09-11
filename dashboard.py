# Personal Dashboard
# Headlines from the best newspapers: BBC, NYtimes, ABC, HN
# Weather for today

import requests 
import http.server
import socketserver

API_KEY = "1aabcf84f880499295073d5b77ae6b9a"
SOURCES = ["bbc-news", "abc-news-au", "hacker-news"]

# News API
def get_news(src):
    """Get top news stories from news API for a given news source.
    
    Makes get request for top stories and decodes JSON data.
    """
    url = ("https://newsapi.org/v2/top-headlines"
          f"?sources={src}"
          f"&apiKey={API_KEY}")

    response = requests.get(url)
    return response.json()

def gather_news():
    """Generates list of objects containing articles from sources found in global list
    
    Makes separate GET request for each
    """
    news_data = []
    for s in SOURCES:
        source_data = get_news(s)
        articles = source_data["articles"]
        news_data.append(articles)
    return news_data

def generate_html_list(articles):
    """Generates header and list containing headlines from one source.
    
    Takes list of articles as argument.
    """
    source = articles[0]["source"]["name"]
    headlines = ""
    
    for a in articles:
        headlines = headlines + f"<li><a href={a['url']}>{a['title']}</a></li>"

    html = f"<h2>{source}</h1><ul>{headlines}</ul>"
    return html

def generate_all_news(sources):
    """Iterates through data  in list and generates HTML for each.
    
    Takes list of news objects and returns list of HTML strings.
    """
    news_html = ""
    for s in sources:
        news_html = news_html + generate_html_list(s)
    return news_html

# Local webserver
class Handler(http.server.SimpleHTTPRequestHandler):
    """Prints HTML to body of response to GET requests"""
    def do_HEAD(self):
        self.send_response(200)
        seld.send_header("Content-type", "text/html")
        self.end_headers()
    def do_GET(self):
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Writes response body
        self.wfile.write("<html><head><title>Dashboard</title></head>"
                         "<body><h1>Dashboard</h1>".encode("utf8"))
        # Generates HTML for BBC articles
        news_data = gather_news()
        news_html = generate_all_news(news_data)        
        self.wfile.write(bytes(news_html, "utf8"))
        # finish HTML file
        self.wfile.write(bytes("</body></html>", "utf8"))
        return

handler_object = Handler

PORT = 8000

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()





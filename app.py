from flask import Flask, redirect, request, jsonify
from url_shortner import main, get_original_url, add_click, get_stat

app = Flask(__name__)


@app.route("/<short_code>", methods=['GET'])
def url_redirect(short_code):
    url_data = get_original_url(short_code)
    print(f"ADD CLICK {url_data}, \n {type(url_data)}")

    if url_data :
        add_click(short_code, json_file="default.json")
        return redirect(url_data['url'], code=301)

    return "No data found...", 404  # Return a 404 if the URL is not found

@app.route("/stat/<short_code>", methods=['GET'])
def stat(short_code):
    url_data = get_stat(short_code)
    return str(url_data.get('clicks'))

@app.route("/", methods=['POST'])
def home():
    base_domain = request.host + '/'
    # BASE_DOMAIN = request.host_url

    data = request.get_json()
    if data:
        original_url = data.get('url')
    else:
        original_url = 'https://www.geeksforgeeks.org/system-design-url-shortening-service/#how-would-you-design-a-url-shortener-service-like-tinyurl'
    short_code = main(original_url)

    return base_domain + short_code


if __name__ == '__main__':
    app.run(debug=True)


import aiohttp


APOD_URL = "https://api.nasa.gov/planetary/apod/"

API_KEY = "DEMO_KEY"

# DEMO_KEY limits
#   30 requests per IP address per hour
#   50 requests per IP address per day
# Go to https://api.nasa.gov/index.html#signUp to get a personal API key

# API_KEY = "your-API-key-goes-here"



async def fetch_apod_async(date):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"{APOD_URL}?api_key={API_KEY}&date={date}"
        ) as response:
            if response.status == 200:
                data = await response.json()
                print(f"{data = }")
                print(f"{type(data) = }")
                
                if data['media_type'] != 'image':  # onlyl d/l images
                    return
                
                if "hdurl" in data:  # attempt to get HD version of image
                    image_url = data["hdurl"]
                else:  # fall back to std definition
                    image_url = data["url"]
                
                image_title = data['title']
                image_filename = f"{image_title.replace(' ', '_')}.jpg"

                async with session.get(image_url) as response:
                    if response.status == 200:
                        with open(image_filename, 'wb') as image_out:
                            image_out.write(await response.read())
                    else:
                        display_error(response, f"Bad image fetch for {image_url}")
            else:
                display_error(response, f"Bad date request for {date}")

    return response.status == 200

def display_error(response, message):
    print(f"Response error code: {response.status}")
    print(message)
    print(response.text())
    print("*" * 60)

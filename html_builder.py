from helpers import convert_nones
from pytube_wrapper import Status


class Site:
    def __init__(
        self,
        status: Status,
        lda_vis=None,
        wordcloud_path: str = None,
        url: str = "site.html",
        **info,
    ):
        if info:
            info["Rating"] = convert_nones(info["Rating"])
            info["Tags"] = convert_nones(info["Tags"])
            self.SITE_TITLE = f"{info['Author']} | {info['Title']}"
        else:
            self.SITE_TITLE = "Error."

        self.HEAD = f"""
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@100..900&display=swap" rel="stylesheet">
                <link href="fontawesome-free-6.5.1-web/css/all.css" rel="stylesheet">
                <link rel="stylesheet" href="styles.css">
                <title>{self.SITE_TITLE}</title>
            </head> """
        self.BODY_CONTENT = (
            f"""
            <div id="info">
                <a href="{info['URL']}" target="_blank">
                    <img class="thumbnail" src="{info['Thumbnail']}"/>
                </a>
                <span class="title">{info['Title']}</span>
                <span class="stat">
                    <i class="fa-brands fa-youtube fa-xl" style="color: red;"></i>
                    <span class="author">{info['Author']}</span>
                </span>
                
                <span id="stats">
                    <span class="stat">
                        <i class="fa-solid fa-clock fa-lg"></i>
                        <p>{info['Length']}</p>
                    </span>
                    <span class="stat">
                        <i class="fa-solid fa-eye fa-lg"></i>
                        <p>{info['Views']:,}</p>
                    </span>
                    <span class="stat">
                        <i class="fa-solid fa-thumbs-up fa-lg"></i>
                        <p>{info['Rating']}</p>
                    </span>
                    <span class="stat">
                        <i class="fa-solid fa-hashtag fa-lg"></i>
                        <p>{info['Tags']}</p>   
                    </span>
                </span>   
            </div>

            <div id="output">
                <div id="wordcloud">
                    <img src="{wordcloud_path}"/>
                </div>
                {lda_vis}
            </div> """
            if status.name == "POSITIVE"
            else f"<div#error>{status.value}</div>"
        )

        self.BODY = f"""
            <body>
                <div id="content">
                    {self.BODY_CONTENT}
                </div>    
            </body>"""

        self.HTML = f"""
            <!DOCTYPE html>
                <html lang="en">
                {self.HEAD}
                {self.BODY}
            </html> """

        self.URL = url


def generate_site(status: Status, lda_vis=None, wordcloud_path: str = None, **info):
    for key, value in info.items():
        if isinstance(value, str):
            info[key] = value.encode("utf-8", "ignore").decode("utf-8")

    site = Site(
        url="result.html",
        status=status,
        lda_vis=lda_vis,
        wordcloud_path=wordcloud_path,
        **info,
    )

    with open(site.URL, "w", encoding="utf-8") as file:
        file.write(site.HTML)

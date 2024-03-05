from helpers import convert_nones
from wordcloud import WordCloud
import os


def results_to_html(lda_vis, lda_topics, wordcloud_path: str, **info) -> None:
    output_file_name = f"{info['Author']}.html"
    file_path = os.path.join(os.getcwd(), output_file_name)

    info["Rating"] = convert_nones(info["Rating"])
    info["Tags"] = convert_nones(info["Tags"])
    content = f"""
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@100..900&display=swap" rel="stylesheet">
            <link href="fontawesome-free-6.5.1-web/css/all.css" rel="stylesheet">
            <link rel="stylesheet" href="styles.css">

            <title>{info['Author']} | "{info['Title']}"</title>
        </head>
        <body>
            <div id="content">
                <div id="info">
                    <a href="{info['URL']}" target="_blank">
                        <img class="thumbnail" src="{info['Thumbnail']}"/>
                    </a>
                    <h1>{info['Title']}</h1>
                    <span class="stat">
                        <i class="fa-brands fa-youtube fa-xl" style="color: red;"></i>
                        <h2>{info['Author']}</h2>
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
                            <i class="fa-regular fa-thumbs-up fa-lg"></i>
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
                </div>     
            </div>
        </body>
    </html>"""

    with open(file_path, "w") as file:
        file.write(content)

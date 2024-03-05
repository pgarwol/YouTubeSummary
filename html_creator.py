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
            <link rel="stylesheet" href="styles.css">
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@100..900&display=swap" rel="stylesheet">
            <title>{info['Author']} | "{info['Title']}"</title>
        </head>
        <body>
            <div id="content">
                <div id="info">
                    <img class="thumbnail" src="{info['Thumbnail']}"/>
                    <h1>{info['Title']}</h1>
                    <h2>{info['Author']}</h2>  
                    <p class="stat">Length: {info['Length']}</p>
                    <p class="stat">Views count: {info['Views']:,}</p>
                    <p class="stat">Rating: {info['Rating']}</p>
                    <p class="stat">Tags: {info['Tags']}</p>             
                </div>
                <div id="wordcloud">
                    <img src="{wordcloud_path}"/>
                </div>
                {lda_vis}
                  
            </div>
        </body>
    </html>"""

    with open(file_path, "w") as file:
        file.write(content)

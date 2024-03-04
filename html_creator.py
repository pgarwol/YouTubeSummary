import os


def results_to_html(lda_vis, lda_topics, **info):
    print(info)
    content = f'''
            <div id="content">
                <div id="info">
                    <img src="{info['Thumbnail']}"/>
                    <h1>{info['Title']}</h1>
                    <h2>{info['Author']}</h2>
                    <span id="stats"> 
                        <p class="stat">Length: {info['Length']}</p>
                        <p class="stat">Views count: {info['Views']}</p>
                    </span>
                </div>
                <div id="lda">
                    <span id="lda-content"> {lda_vis} </span>
                </div>     
            </div>
        </body>
    </html>'''


    output_file_name = "results.html"
    file_path = os.path.join(os.getcwd(), output_file_name)
    with open(file_path, "a") as file:
        file.write(content)
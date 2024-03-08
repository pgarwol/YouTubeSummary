from lda import LDA
from pytube_wrapper import Movie
from wordcloud_wrapper import create_wordcloud, save_wordcloud
from html_builder import generate_site


def run() -> None:
    movie = Movie(url="https://www.youtube.com/watch?v=gMvr826M7Xg")
    if movie.status.name == "POSITIVE":
        lda = LDA(content=movie.captions, lang=movie.language)
        word_cloud = create_wordcloud(words=lda.tokens, lang=movie.language)
        word_cloud_path = save_wordcloud(wordcloud=word_cloud, ext="jpg")
        generate_site(
            status=movie.status,
            lda_vis=lda.html,
            wordcloud_path=word_cloud_path,
            **movie.info
        )
        print("Process finished with success.")
    else:
        generate_site(status=movie.status)
        print("Process failed.")


if __name__ == "__main__":
    run()

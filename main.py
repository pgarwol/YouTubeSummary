from lda import LDA
from pytube_wrapper import Movie
from wordcloud import WordCloud
from wordcloud_wrapper import create_wordcloud, save_wordcloud
from html_creator import results_to_html


def run() -> None:
    movie = Movie(url="https://www.youtube.com/watch?v=J-ahbMeH8nE")
    if movie.caption is None:
        return None  # TODO: change handling
    print(movie)
    lda = LDA(content=movie.caption, lang="pl")
    word_cloud = create_wordcloud(words=lda.tokens)
    word_cloud_path = save_wordcloud(wordcloud=word_cloud, ext="jpg")
    results_to_html(lda_vis=lda.html, wordcloud_path=word_cloud_path, **movie.info)

    print("Process finished.")


if __name__ == "__main__":
    run()

from lda import LDA
from yt_wrapper import YT
from wordcloud import WordCloud
from wordcloud_wrapper import create_wordcloud, save_wordcloud
from html_creator import results_to_html


def run() -> None:
    movie = YT(url="https://www.youtube.com/watch?v=FmRm--vRHCg", caption_lang="a.en")
    if movie.caption is None:
        return None  # TODO: change handling
    print(movie)
    lda = LDA(content=movie.caption, lang="en")
    word_cloud = create_wordcloud(words=lda.tokens)
    wc_path = save_wordcloud(wc=word_cloud, name=movie.title, ext="jpg")
    results_to_html(
        lda_vis=lda.html, lda_topics=lda.topics, wordcloud_path=wc_path, **movie.info
    )


if __name__ == "__main__":
    run()

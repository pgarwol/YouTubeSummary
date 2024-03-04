from lda import LDA
from yt_wrapper import YT
from wordcloud import WordCloud
from wordcloud_wrapper import create_wordcloud, save_wordcloud


def run() -> None:
    movie = YT(url="https://www.youtube.com/watch?v=vP3rYUNmrgU", caption_lang="a.en")
    if movie.caption is None:
        return None  # TODO: change handling
    print(movie)
    lda = LDA(content=movie.caption, lang="en")
    word_cloud = create_wordcloud(words=lda.tokens)
    save_wordcloud(wc=word_cloud, name=movie.title, ext="jpg")


if __name__ == "__main__":
    run()

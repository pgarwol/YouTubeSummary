from movie import Movie
from lda import LDA
from wordcloud import WordCloud
from yt_wrapper import YT
from wordcloud_wrapper import create_wordcloud, save_wordcloud


def run() -> None:
    yt = YT(url="https://www.youtube.com/watch?v=mvqPWay9ABI", caption_lang="a.en")

    movie = Movie(url=yt.url, title=yt.title, caption=yt.caption)
    print(movie)
    lda = LDA(content=movie.caption, lang="en")
    word_cloud = create_wordcloud(words=lda.tokens)
    save_wordcloud(wc=word_cloud, name=movie.title, ext="jpg")


if __name__ == "__main__":
    run()

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"
SENTENCES_COUNT = 1


if __name__ == "__main__":
    # url = "https://en.wikipedia.org/wiki/Automatic_summarization"
    # parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    parser = PlaintextParser.from_string("""As early as 1944, the expression "Polish death camp" appeared as the title of a Collier's magazine article, "Polish Death Camp". This was an excerpt from the Polish resistance fighter Jan Karski's 1944 memoir, Courier from Poland: The Story of a Secret State (reprinted in 2010 as Story of a Secret State: My Report to the World). Karski himself, in both the book and the article, had used the expression "Jewish death camp", not "Polish death camp".[40][41] As shown in 2019, the Collier's editor changed the title of Karski's article typescript, "In the Belzec Death Camp", to "Polish Death Camp".[42][43]

Other early-postwar, 1945 uses of the expression "Polish death camp" occurred in the periodicals Contemporary Jewish Record,[44] The Jewish Veteran,[45] and The Palestine Yearbook and Israeli Annual,[46] as well as in a 1947 book, Beyond the Last Path, by Hungarian-born Jew and Belgian resistance fighter Eugene Weinstock[47] and in Polish writer Zofia Nałkowska's 1947 book, Medallions.[48]

A 2016 article by Matt Lebovic stated that West Germany's Agency 114, which during the Cold War recruited former Nazis to West Germany's intelligence service, worked to popularize the term "Polish death camps" in order to minimize German responsibility for, and implicate Poles in, the atrocities.[49]

Mass media
On 30 April 2004 a Canadian Television (CTV) Network News report referred to "the Polish camp in Treblinka". The Polish embassy in Canada lodged a complaint with CTV. Robert Hurst of CTV, however, argued that the term "Polish" was used throughout North America in a geographical sense, and declined to issue a correction.[50] The Polish Ambassador to Ottawa then complained to the National Specialty Services Panel of the Canadian Broadcast Standards Council. The Council rejected Hurst's argument, ruling that the word "'Polish'—similarly to such adjectives as 'English', 'French' and 'German'—had connotations that clearly extended beyond geographic context. Its use with reference to Nazi extermination camps was misleading and improper."[30]

In 2009 Zbigniew Osewski, grandson of a Stutthof concentration camp prisoner, announced that he was suing Axel Springer AG for calling Majdanek concentration camp a "former Polish concentration camp" in a November 2008 article in the German newspaper Die Welt.[51] The case started in 2012.[52]

On 23 December 2009, historian Timothy Garton Ash wrote in The Guardian: "Watching a German television news report on the trial of John Demjanjuk a few weeks ago, I was amazed to hear the announcer describe him as a guard in 'the Polish extermination camp Sobibor'. What times are these, when one of the main German TV channels thinks it can describe Nazi camps as 'Polish'? In my experience, the automatic equation of Poland with Catholicism, nationalism and antisemitism – and thence a slide to guilt by association with the Holocaust – is still widespread. This collective stereotyping does no justice to the historical record."[53]

In 2010 the Polish-American Kosciuszko Foundation launched a petition demanding that four major U.S. news organizations endorse use of the expression "German concentration camps in Nazi-occupied Poland".[54][55]

Canada's Globe and Mail reported on 23 September 2011 about "Polish concentration camps". Canadian Member of Parliament Ted Opitz and Minister of Citizenship and Immigration Jason Kenney supported Polish protests.[56]

In 2013 Karol Tendera, who had been a prisoner at Auschwitz-Birkenau and is secretary of an association of former prisoners of German concentration camps, sued the German television network ZDF, demanding a formal apology and 50,000 zlotys, to be donated to charitable causes, for ZDF's use of the expression "Polish concentration camps".[57] ZDF was ordered by the court to make a public apology.[58] Some Poles felt the apology to be inadequate and protested with a truck bearing a banner that read "Death camps were Nazi German - ZDF apologize!" They planned to take their protest against the expression "Polish concentration camps" 1,600 kilometers across Europe, from Wrocław in Poland to Cambridge, England, via Belgium and Germany, with a stop in front of ZDF headquarters in Mainz.[59]

The New York Times Manual of Style and Usage recommends against using the expression,[60][61] as does the AP Stylebook,[62] and that of The Washington Post.[35] However, the 2018 Polish bill has been condemned by the editorial boards of The Washington Post[35] and The New York Times.[36]""", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)

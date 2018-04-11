# Web-Novel-Editor

## The Problem

The typical simplified path for an author is usually to; write the book, edit it, then publish it. While this is still a tried and true method, and although e-books have shortened the gap, in this era of internet connectivity there is a new format for authors to have readers access their works.  They are called Web Novels.  In China, many fiction books especially sci-fi, fantasy, martial arts, and romance novels are now being published directly to the web.  Instead of compiling a whole book to be released, authors instead write and release a single chapter, usually fairly short, on some sort of daily or weekly release schedule.  In my opinion this is, by far, a better way.  It's like comparing Night of the Living Dead to The Walking Dead.

There is one problem that faces many web novel enthusiasts.  Someone who does not speak the language of origin has to wait for chapters to be translated.  One would think, 'Why not just use Google Translate'.  Machine Translation is a path that many readers have tried.  The problem is; machine translators currently available on the internet are purposed. Whether for conversational translations that will focus on day to day language use, or for business translations that will focus on trade; there is no machine translator that can capture the nuance and flow of a novel.  It would be like running the Lord of the Rings through Google Translate, you'll get a translation but it wont have that special something that turns words into a story.

As an avid web novel enthusiast and a data scientist, I decided it was time to put a stop to this.  I decided to make a new form of machine translator that will not only take web novels from their language of origin to English, but also edit and stylize the output to make the robotic descriptive.

|<img src="https://images.gr-assets.com/books/1460555353l/29909306.jpg" alt="Chaotic Sword God" style="width: 175px;"/>|<img src="http://avatar.manganelo.com/avatar/362-shen_yin_wang_zuo.jpg" alt="Shen Ying Wang Zuo" width= '175px' height= '265px'/>|<img src='https://www.wuxiaworld.com/images/covers/mga.png' alt = 'Martial God Asura' width= '175px' height= '265px'/>|<img src='https://lnmtl.com/assets/images/novel/2-200.jpg' alt = 'Tales of Demons and Gods' width= '175px' height= '265px'/>|<img src='https://f01.mrcdn.info/file/mrportal/h/9/5/b/QU.2NpMOHZc.png' alt = 'Panlong' width='175px' height= '265px'/>|


## The Data

Luckily there is a large amount of data available on the open web.  There are many websites that offer chapters translated and edited by fans.

I used two such website [Gravity Tales](https://www.gravitytales.com) and [Wuxiaworld](https://www.wuxiaworld.com) due to their hosting some of my favorite novels and also being permissive of web scraping and use of their content.

I compiled 200 chapters for 5 different novels.

##### * Chatoic Sword God:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CSG Novel Page](http://gravitytales.com/novel/chaotic-sword-god)
##### * Shen Ying Wang Zuo:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SYWZ Novel Page](http://gravitytales.com/novel/shen-ying-wang-zuo)
##### * Martial God Asura:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MGA Novel Page](https://www.wuxiaworld.com/novel/martial-god-asura)
##### * Tales of Demons and Gods:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TDG Novel Page](https://www.wuxiaworld.com/novel/tales-of-demons-and-gods)
##### * Coiling Dragon:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CD Novel Page](https://www.wuxiaworld.com/novel/coiling-dragon)

I picked these novels because they have a multitude of similarities while being very different.  The genres, time periods and story lines and vocabulary of the author vary greatly.

I then found the original Chinese versions of these 1000 chapters. From their various hosting sites in China.

##### [Web Scraping Code](https://github.com/Jeff-Saler/Web-Novel-Editor/tree/master/src/web_scrape)

## Example of Data
### Opening Paragraph of Chaotic Sword God Chapter 1:


> #### Original Text (Raw):
>
在一片连绵不绝的广阔山脉之中，两座足有千丈高的剑型山峰相隔百米的距离矗立在茫茫云海之下。这两座剑型的山峰非常陡峭，看上去仿佛是两把放大版的神剑插在天地间似地，没有任何可攀岩的地方。

>-----------------------

> #### Google Translated Text:
>
In a vast and endless range of mountains, two sword-shaped peaks with a thousand feet high stand 100 meters apart under a sea of clouds. The two sword-shaped peaks are very steep, and they look like two enlarged versions of the Excalibur inserted between heaven and earth. There is no place for rock climbing.

>------------------------

> #### Human Translated and Edited (Target):
>
Within a seemingly endless chain of mountain ranges, there were two sword-shaped mountain peaks well over a thousand feet tall and a hundred meters apart from each other as it towered under the vast ocean of clouds. Both of these sword-shaped mountains were extremely precipitous and looked as if two gods had once stabbed their swords into the world. No matter where one looked, there was no way to climb up these mountains.

## The Model

The most effective model for translation or editing is a sequence to sequence (seq2seq) recursive neural network (RNN).  I created my RNN with Keras using the Tensorflow backend. I decided to use character prediction rather than word prediction so that it would be better suited to learning new words and better able to generalize.

The model is structured as an embedding layer, an encoding layer with a Long Short Term Memory (LSTM) layer, a hidden dense layer, and a decoding layer with another LSTM.

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import telebot
from telebot import types

TOKEN = 'YOUR TOKEN' # محل توکن شما 
bot = telebot.TeleBot(TOKEN)

@bot.inline_handler(lambda query: len(query.query.split()) == 0)
@bot.inline_handler(lambda query: len(query.query.split()) == 1)
@bot.inline_handler(lambda query: len(query.query.split()) == 2)
@bot.inline_handler(lambda query: len(query.query.split()) == 3)
@bot.inline_handler(lambda query: len(query.query.split()) == 4)
@bot.inline_handler(lambda query: len(query.query.split()) == 5)
@bot.inline_handler(lambda query: len(query.query.split()) == 6)
@bot.inline_handler(lambda query: len(query.query.split()) == 7)
@bot.inline_handler(lambda query: len(query.query.split()) == 8)
@bot.inline_handler(lambda query: len(query.query.split()) == 9)
@bot.inline_handler(lambda query: len(query.query.split()) == 10)
@bot.inline_handler(lambda query: len(query.query.split()) == 11)
@bot.inline_handler(lambda query: len(query.query.split()) == 12)
@bot.inline_handler(lambda query: len(query.query.split()) == 13)
@bot.inline_handler(lambda query: len(query.query.split()) == 14)
@bot.inline_handler(lambda query: len(query.query.split()) == 15)
@bot.inline_handler(lambda query: len(query.query.split()) == 16)
@bot.inline_handler(lambda query: len(query.query.split()) == 18)
@bot.inline_handler(lambda query: len(query.query.split()) == 19)
@bot.inline_handler(lambda query: len(query.query.split()) == 20)
def qq(q):
    text = q.query
    thumbb = 'http://lettergenerator.net/alphabetletters/bold/printable-letter-asap-b.jpg'
    thumbc = 'http://lettergenerator.net/alphabetletters/bold/printable-letter-forque-c.jpg'
    thumbi = 'http://lettergenerator.net/alphabetletters/bold/printable-letter-newtown-i.jpg'
    git = 'https://cdn4.iconfinder.com/data/icons/iconsimple-logotypes/512/github-512.png'
    dehpic = 'https://s.cafebazaar.ir/1/upload/icons/com.efossa.dehkhoda.png'
    git_rp = 'http://www.escope.cz/images/gr200.png'
    googlepic = 'http://cdn.geekwire.com/wp-content/uploads/2015/09/Screen-Shot-2015-09-01-at-9.03.40-AM.png'
    bold = types.InlineQueryResultArticle('1', 'Bold', types.InputTextMessageContent('<b>{}</b>'.format(text), parse_mode="HTML"), description='{}'.format(text), thumb_url=thumbb, thumb_width=20, thumb_height=20)
    code = types.InlineQueryResultArticle('2', 'Code', types.InputTextMessageContent('<code>{}</code>'.format(text), parse_mode="HTML"), description='{}'.format(text), thumb_url=thumbc, thumb_width=20, thumb_height=20)
    italic = types.InlineQueryResultArticle('3', 'Italic', types.InputTextMessageContent('<i>{}</i>'.format(text), parse_mode="HTML"), description='{}'.format(text), thumb_url=thumbi, thumb_width=20, thumb_height=20)
    github = types.InlineQueryResultArticle('4', 'Search Github User', types.InputTextMessageContent('[found User](https://github.com/{})'.format(text), parse_mode="Markdown"), description='Search Github', thumb_url=git, thumb_width=20, thumb_height=20)
    githubrepo = types.InlineQueryResultArticle('5', 'Github Search repository', types.InputTextMessageContent('[Found repository](https://github.com/search?=&q={})'.format(text), parse_mode="Markdown"), thumb_url=git_rp)
    deh = types.InlineQueryResultArticle('6', 'Search Dictionary Dehkhoda', types.InputTextMessageContent('[Meaning :   {}](http://api.vajehyab.com/dehkhoda/{})'.format(text,text), parse_mode="Markdown"), thumb_url=dehpic)
    google = types.InlineQueryResultArticle('7', 'Google Search', types.InputTextMessageContent('[{}](https://www.google.com/search?q={})'.format(text,text), parse_mode='Markdown'), description='Search : {}'.format(text), thumb_url=googlepic)
    bot.answer_inline_query(q.id, [bold, code, italic, github, githubrepo, deh, google], cache_time=1)

    
    
bot.polling(True)

#new Update Soon

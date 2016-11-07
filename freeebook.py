import bs4 as bs
import urllib.request
import yagmail

url = 'https://bit.ly/Free-Tech-Learning'

source = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(source, 'lxml')

titul = soup.h2.text.strip

yag = yagmail.STMP('nalevanko.data@gmail.com')
to = 'michal.nalevanko@gmail.com'
subject = 'Daily eBook Update'
body = "Hello,\nhere is today's free e-book: {}.\n\nHave a nice day!".format(titul)

yag.send(to=to, subject=subject, contents=body)

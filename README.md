# Text Mask Zero            
A free and open-source webpage that masks a message under another message. Runs entirely on the front end and is built with Brython!

### Where Am I? 
Welcome! This is the GitHub repo for **Text Mask Zero**, a website that allows you to "encode" and hide any `ascii` text under some other text by using zero-width characters.


### Why Text Mask Zero? 
You probably have some messages that you want to send to your friend and don't want other people to see, even if they have a hand on your friend's phone or somehow hack into and see their messages. 
Zero-width characters are interesting! They cannot be seen normally but are still `UTF-8` characters. This means that they can be sent through most text messaging apps. Given that both you and your friend know __the tool__, you can probably use it to send a "secret" message to each other. The masking text might be anything casual and unimportant, but the actual message that lies beneath can be __anything__!

### Is It Safe? 
Yes! Since all of the processes are done on the client side, __no data is ever sent to either any server or other parties__. (That's the magic of `Brython`. It allows Python code to run on a webpage without a server.)

### Sounds Great! How do I Use It?
Just follow the link <https://rawcdn.githack.com/thaitri2005/Text-Mask-Zero/d229cb8e8693e08ddd65ce2ecb24dce3ff7c268d/index.html> and start typing away. Yes, it is that easy.

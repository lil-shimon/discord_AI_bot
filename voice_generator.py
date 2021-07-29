import subprocess
import re

# remove_custom_emoji
def remove_custom_emoji(text):
    pattern = r'<:[a-zA-Z0-9_]+:[0-9]+>'
    return re.sub(pattern,'',text)   

# urlAbb
def urlAbb(text):
    pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
    return re.sub(pattern,'plz remove url',text)

# creat_WAV
def creat_WAV(inputText):

    inputText = remove_custom_emoji(inputText)
    inputText = urlAbb(inputText)
    input_file = 'input.txt'

    with open(input_file,'w',encoding='shift_jis') as file:
        file.write(inputText)

    open_jtalk = ['open_jtalk']
    mech = ['-x', '/usr/local/Cellar/open-jtalk/1.11/dic']
    htsvoice = ['-m', '/usr/local/Cellar/open-jtalk/1.11/voice/mei/mei_normal.htsvoice']
    speed = ['-r', '1.0']
    outwav = ['-ow', 'out.wav']
    cmd = open_jtalk + mech + htsvoice + speed + outwav
    print(cmd)

    subprocess.run(cmd)
    return True

if __name__ == '__main__':
    creat_WAV('???')

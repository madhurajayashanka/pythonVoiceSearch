import speech_recognition as sr;
import webbrowser as wb;

r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()
r4=sr.Recognizer()

with sr.Microphone() as source:
    print('Listening... (to stop say "Stop")')
    audio=r3.listen(source)
    run=True
    if 'stop' in r3.recognize_google(audio):
        print('stopped')
        run=False
while(run):
    if 'search on google' in r1.recognize_google(audio):
        url='www.google.com/search?q='
        with sr.Microphone() as source:
            print('search your query in google')
            print('Listening... (to stop say "Stop")')
            audio=r1.listen(source)
            
            try:
                text=r1.recognize_google(audio)
                print("I thinks you said '" + r1.recognize_google(audio) + "'")
                f_text=url + text
                print(f_text)
                wb.get().open(f_text)
            except sr.UnknownValueError as e:
                print('error')
            except sr.RequestError as e:
                print('failed'.format(e))
            finally:
                print('done')
                
                
            
    if 'search on youtube' in r2.recognize_google(audio):
        r2=sr.Recognizer()
        url='www.youtube.com/results?search_query='
        with sr.Microphone() as source:
            print('search your query in youtube')
            print('Listening... (to stop say "Stop")')
            audio=r2.listen(source)
            
            try:
                text=r2.recognize_google(audio)
                print("I thinks you said '" + r2.recognize_google(audio) + "'")
                f_text=url + text
                print(f_text)
                wb.get().open(f_text)
            except sr.UnknownValueError as e:
                print('error')
            except sr.RequestError as e:
                print('failed'.format(e))
            finally:
                print('done')
                
    
    
    print('Listening... (to stop say "Stop")')
    r4=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r4.listen(source)
        if 'stop' in r4.recognize_google(audio):
            print('stopped')
            run=False
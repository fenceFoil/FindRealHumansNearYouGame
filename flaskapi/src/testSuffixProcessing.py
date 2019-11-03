import requests
GPT2_URL = "http://ec2-18-221-77-224.us-east-2.compute.amazonaws.com:465/"


def generateSuffixForPrompt(prompt):
    global GPT2_URL
    response = requests.post(GPT2_URL+'gpt2', json={"prompt":prompt})
    if response.status_code != 200:
        import random
        print ("Not 200 from gpt2 server")
        return random.choice(['and you had better believe it!', 'woo hoo!', '<<excited beep boop>>', 'praise Shrek.'])
    else:
        # TODO: Process GPT2
        suffix = response.text
        accepted = ""
        #suffix = suffix.replace ('"', "")
        #suffix = suffix.replace ("'", "" )
        suffix = suffix.replace ("\n", " ")
        suffix = suffix.replace ("\r", " ")
        suffix = suffix.replace ('..', ".")
        suffix = suffix.replace ('...', ".")
        suffix = suffix.replace ('.....', ".")

        notFirstLoop = False
        thisSentenceEnds = False
        for token in suffix.split(" "):
            accepted += (" " if notFirstLoop else "") + token
            notFirstLoop = True
            #print (token)
            killloop = False
            for endchar in [".", "!", ":", "?", "<|endoftext|>"]:
                if endchar in token:
                    killloop = True
                    thisSentenceEnds = True
            if killloop:
                #print ('breaking')
                break
        if not thisSentenceEnds:
            accepted = accepted[:75]+"..."
        accepted = accepted.replace("<|endoftext|>", ".")

        return accepted

prmt = "I am a sports star."
suffix = generateSuffixForPrompt(prmt)
print(prmt+suffix)
import openai
openai.api_key="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"

def generate_response(myprompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=myprompt,
        temperature=.3,                 # recommended: 0.3 to 0.7
        max_tokens=1024
    )
    print (response.choices)
    # return response.choices[0].text.strip()
    return response

def main ():
    myprompt = input("How can I help you? \n")
    print(generate_response(myprompt))

if __name__ == "__main__":
    main()
from openai import OpenAI

client = OpenAI(
    api_key = "KEY"
)

while True:
    messageNum = input("How many messages do you want?")

    system_data = [
        {"role": "system", "content": "You are a bot that simulates messages that would be posted to a university's group chat app by students that attend the university. Among other things, you can comment on how well you're doing in your classes, the state of campus, different buildings on campus, study group requests, etc. They can be up to 3 sentences in length. Feel free to use slightly mature language. Use a maximum of one emoji per response. Depending on the number inputted, send that number of unique messages, separated by newline characters. Do not number the responses or do anything to separate them other than the newline characters."},
        {"role": "user", "content": messageNum}
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=system_data
    )
    res = response.choices[0].message.content
    system_data.append({"role": "assistant", "content": res})
    print(res)
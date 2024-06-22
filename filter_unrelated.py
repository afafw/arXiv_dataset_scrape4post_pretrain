import pandas as pd
from dotenv import load_dotenv
from openai import AsyncOpenAI
import asyncio
import os

load_dotenv() 

client = AsyncOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE"),
)

MODEL_NAME = os.environ.get("USE_THIS_MODEL")

async def create_chat_completion(messages, model=MODEL_NAME):
    while True:
        try:
            completion = await client.chat.completions.create(
                messages=messages,
                model=model,
            )
            return completion.choices[0].message.content
        except Exception:
            await asyncio.sleep(10)  # Non-blocking sleep

def append_new_message(messages, new_message, role="user"):
    messages.append({"role": role, "content": new_message})
    return messages

def create_message_wth_system_role(content, role="system"):
    return [{"role": role, "content": content}]

async def relavant(title):  # return True if title is relevant
    messages = create_message_wth_system_role("You are a perfect classifier for classifying articles regarding whether they are relevant to autism/autism spectrum disorder. The user will provide you with the title of an article and you will return True if the article is relevant to autism/autism spectrum disorder by saying \"TRUE\" or \"FALSE\".", role="system")
    messages = append_new_message(messages, title + " Now argue whether TRUE or FALSE", role="user")
    response = await create_chat_completion(messages)
    # print(response)
    return response.strip() == "TRUE"

# create empty pd dataframe
df_filtered = pd.DataFrame(columns=['Title', 'Entry_ID'])

async def process_row(row, df_filtered):
    print("processing:" + row['Title'])
    if await relavant(row['Title']):
        # put this row into df_filtered
        print(row['Title'] + " is relevant")
        df_filtered = pd.concat([df_filtered, pd.DataFrame([row])], ignore_index=True)
    else:
        print(row['Title'] + " is not relevant")
    return df_filtered

async def main():
    #Not yet multithreaded.
    df = pd.read_csv("target_titles.csv")
    df_filtered = pd.DataFrame(columns=['Title', 'Entry_ID'])
    for index, row in df.iterrows():
        df_filtered = await process_row(row, df_filtered)
        
    df_filtered.to_csv("filtered.csv", index=False)
    
asyncio.run(main())

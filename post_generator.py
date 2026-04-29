from llm_helper import llm

def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"


def generate_post(length, language, tag, retrieved_posts, tone="Professional", use_emoji="On"):
    prompt = get_prompt(length, language, tag, retrieved_posts, tone, use_emoji)
    response = llm.invoke(prompt)
    return response.content


def get_prompt(length, language, tag, retrieved_posts, tone="Professional", use_emoji="On"):
    length_str = get_length_str(length)

    emoji_instruction = {
        "On": "Feel free to use relevant emojis throughout the post.",
        "Off": "Do NOT use any emojis.",
        "Minimal": "Use at most 1-2 emojis, only if very relevant.",
    }.get(use_emoji, "")

    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    4) Tone: {tone}
    5) Emoji Usage: {emoji_instruction}

    If Language is Hinglish then it means it is a mix of Hindi and English.
    The script for the generated post should always be English.
    '''

    if retrieved_posts:
        prompt += "\n6) Here are examples of user's writing style:\n"
        for i, post in enumerate(retrieved_posts):
            post_text = post.get('text', '')
            prompt += f'\n Example {i+1}: \n {post_text}\n'
            
        prompt += "\nGenerate a new post in a similar style to the examples above."

    return prompt


if __name__ == "__main__":
    print(generate_post("Medium", "English", "Mental Health", []))
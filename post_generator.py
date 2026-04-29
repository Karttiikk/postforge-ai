from llm_helper import llm

def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"


def generate_post(length, language, tag, retrieved_posts, tone="Professional", use_emoji="On", user_prompt=""):
    prompt = get_prompt(length, language, tag, retrieved_posts, tone, use_emoji, user_prompt)
    response = llm.invoke(prompt)
    return response.content


def get_prompt(length, language, tag, retrieved_posts, tone="Professional", use_emoji="On", user_prompt=""):
    length_str = get_length_str(length)

    emoji_instruction = {
        "On": "Feel free to use relevant emojis throughout the post.",
        "Off": "Do NOT use any emojis.",
        "Minimal": "Use at most 1-2 emojis, only if very relevant.",
    }.get(use_emoji, "")

    prompt = f'''
    Craft a highly engaging, insightful, and meaningful LinkedIn post based on the parameters below.
    Ensure the content is well-structured, thought-provoking, and naturally drives engagement.
    Crucially, incorporate relevant quantitative data, statistics, or real-world metrics where applicable to justify your points and add authority.
    
    Do NOT include any preamble, concluding remarks like "Here is your post", or meta-commentary. Output ONLY the final post content.

    Parameters:
    1) Topic/Core Theme: {tag}
    2) Target Length: {length_str}
    3) Language: {language} (If Hinglish, use a natural conversational blend of Hindi and English written in the English alphabet)
    4) Tone: {tone}
    5) Emoji Guidelines: {emoji_instruction}
    '''

    if user_prompt.strip():
        prompt += f"\n    Additional instructions from user:\n    {user_prompt}\n"

    if retrieved_posts:
        prompt += "\n6) Here are examples of user's writing style:\n"
        for i, post in enumerate(retrieved_posts):
            post_text = post.get('text', '')
            prompt += f'\n Example {i+1}: \n {post_text}\n'
            
        prompt += "\nGenerate a new post in a similar style to the examples above."

    return prompt


if __name__ == "__main__":
    print(generate_post("Medium", "English", "Mental Health", []))
def build_prompt(context, question):

    prompt = f"""
    You are an AI Knowledge Assistant.
    Answer ONLY from the supplied context.
    If answer not available say
    "I don't know."

    Context: {context}
    Question:{question}
    """

    return prompt
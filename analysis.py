import os
import openai
from settings import OPEN_AI_KEY
from list_youtube_comments import comment_workflow, extract_data
import sys

openai.api_key = OPEN_AI_KEY

def call_davinci_003(prompt, 
                     temperature = 0.7, 
                     max_tokens = 312, 
                     top_p = 1.0, 
                     frequency_penalty = 0.0, 
                     presence_penalty = 1, 
                     prefix = '',
                     suffix = ''):
    prompt += prefix + "\n\n" + prompt + "\n\n" + suffix

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )
    return response

def summarize_comments(comments):
    full_summary = _batch_llm_calls(comments, 
                                    suffix="Tl;dr", 
                                    max_tokens=275)
    return full_summary

def semantic_analysis(full_summary):
    semantics = _batch_llm_calls([''.join(full_summary)], 
                                 prefix="Decide whether the following text's sentiment is positive, neutral, or negative", 
                                 max_tokens=500, 
                                 top_p=1.0,
                                 frequency_penalty=0.5, 
                                 temperature=0, 
                                 presence_penalty=0.0)
    return semantics[0]

def keywords_extraction(full_summary):
    all_keywords = _batch_llm_calls([''.join(full_summary)], 
                                    prefix="Extract the keywords from the following text", 
                                    max_tokens=60, 
                                    temperature=0.4, 
                                    frequency_penalty=0.9, 
                                    presence_penalty=0.0)
    return all_keywords

def _batch_llm_calls(comment_chunks,
                     temperature = 0.7, 
                     max_tokens = 312,
                     top_p = 1.0, 
                     frequency_penalty = 0.0, 
                     presence_penalty = 1, 
                     prefix = '',
                     suffix = ''):
    
    full_result = []
    for chunk in comment_chunks:
        part_result = call_davinci_003(prompt = f"""
                                        {chunk}
                                    """, 
                                    temperature = temperature, 
                                    max_tokens=max_tokens,
                                    top_p=top_p,
                                    frequency_penalty = frequency_penalty,
                                    presence_penalty = presence_penalty,
                                    prefix = prefix,
                                    suffix = suffix)

    
    full_result.append(part_result["choices"][0]["text"].strip())
    return full_result

if __name__== "__main__":
    comments = comment_workflow(video_id = sys.argv[1])
    summary = summarize_comments(comments)
    print('-------------SUMMARY-------------')
    print(''.join(summary))


    print('-------------SEMANTICS-------------')
    semnatics = semantic_analysis(summary)
    print(semnatics)

    print('-------------KEYWORDS-------------')
    keywords = keywords_extraction(summary)
    print(keywords)
 
    
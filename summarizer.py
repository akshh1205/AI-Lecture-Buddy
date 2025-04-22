import torch
torch.classes 


from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_chunk=1000):
    
    text = text.replace('\n', ' ')
    chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
    summary = ""
  
    for chunk in chunks:
        result = summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]
        summary += result['summary_text'] + "\n\n"
    return summary

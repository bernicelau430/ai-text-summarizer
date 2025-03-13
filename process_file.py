import sys
import pymupdf
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import AutoTokenizer

def process_file(file_path):

    # getting string content of file
    if file_path.endswith('.txt'):
        with open(file_path, 'r') as file:
            content = file.read()
    elif file_path.endswith('.pdf'):
        # Process PDF
        doc = pymupdf.open(file_path)
        content = ""
        for page in doc:
            output = page.get_text("blocks")
            previous_block_id = 0
            for block in output:
                # check if block is text
                if block[6] == 0:
                    # check if block is a repeat
                    if previous_block_id != block[5]:
                        previous_block_id = block[5]
                        content += block[4]
    else :
        content = "Error: Cannot process files that are not `.pdf`s or `.txt`s"
        return content

    # TODO: incorporate the bart model and summarize import content
    file_path = "./model.pth"

    device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

    model_ckpt = "facebook/bart-base"
    model2 = AutoModelForSeq2SeqLM.from_pretrained(model_ckpt).to(device)
    state_dict = torch.load(file_path, map_location = device)

    #return state_dict.keys()

    model2.load_state_dict(state_dict)

    # Tokenize input text
    tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
    inputs = tokenizer(content, return_tensors="pt", max_length=2048, truncation=True).to(device)

    # Generate summary
    summary_ids = model2.generate(
    inputs['input_ids'],
    num_beams=8,
    max_length=200,
    min_length=100,
    early_stopping=True,
    temperature=0.8
    )

    # Decode the summary
    bullets = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    ########################### Bullet summary version:

    # formatted = "".join(["\n- " + sentence.strip() for sentence in bullets.split("-") if sentence.encode('ascii', errors='ignore').decode().strip()])

    ##########################

    ########################## Regular summary version:

    sentences = bullets.split(".")
    sentences = ["\n- " + sentence.strip() + "." for sentence in sentences if sentence.encode('ascii', errors='ignore').decode().strip()]
    formatted = ""
    for sen in sentences:
        formatted = formatted + sen

    ##########################


    output = "Input Text: \n\n"
    output += content
    output += "\n\nBullet Point Summary from BART: \n\n"
    output += formatted
    return output


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        result = process_file(file_path)
        print(result)  # This will be captured by Node.js

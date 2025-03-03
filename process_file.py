import sys
import pandas as pd
# Import any other libraries you need
import pymupdf 

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
    
    # TODO: incorporate the bart model and summarize import content 
    return content 


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        result = process_file(file_path)
        print(result)  # This will be captured by Node.js
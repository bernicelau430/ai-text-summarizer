# AI Text Summarizer
- [Bernice Lau](https://www.linkedin.com/in/lau-bernice/)
- [Brandon Howell](https://www.linkedin.com/in/bbrandonhowell/)
- [Cece Hildreth](https://www.linkedin.com/in/cece-h-a59a8b200/)
- [Daiwik Swaminathan](https://www.linkedin.com/in/daiwik-swaminathan-6433391a4/)
- [Luke Yium](https://www.linkedin.com/in/lukeyium/)

## Project Overview

### Project Description
Our project will take in plaintext as input and output a bullet point list summary of the input text using an AI model trained on Facebook’s BART (Bidirectional and Auto-Regressive Transformers) sequence-to-sequence model. This project’s overall task is natural language processing.

### Data
Our project will take in the BBC News Summary dataset from Kaggle, which contains 2225 extractive summarizations of BBC news articles from 2004-2005 in the following categories: business, entertainment, politics, sport, and tech. Each category contains the text from an article within that category in a text file. If we find the dataset to not have enough breadth of information to cover our use cases like we want, we may also generate text-summary pairs using an LLM, though this is more likely a task for future expansion.

### Platform
We are planning to use the pytorch deep learning library. The BART model will be utilized and fine-tuned for our purposes. Further, we would like to use ROUGE (or a similar metric), which serves as a way to evaluate how good the generated summaries are compared to a reference (which could be a human written summary). In the interest of time and scope, we aim to have a version of our project working in the terminal on our local machines. However, if time permits, we can upgrade to a simple frontend where a user may enter their text to summarize (still on local machines but could explore options to publicize this).

### Implementation plan
We will verify the implementation from this source, Kaggle, works. Then modify the input data (by finding a different data set) and expanding on the existing source code to create the output data we want. Interaction with this model will be mainly through an IDE and using Python. If we have extra time, we will look into creating input summaries from an LLM to minimize noise that human-created summaries create.

### Testing plan
For testing, our current plan is to use ROUGE (Recall-Oriented Understudy for Gisting Evaluation). This is an evaluation metric that compares an automatically generated summary against a provided human-produced reference summary, giving a score based on similarity and overlap.

### Future expansion
For future expansion, we could adapt the program to take in multiple forms of input, such as pdf uploads. This would make the summarization process more efficient for users by eliminating the time spent copying and pasting their inputs. We could also implement a web interface to improve user experience and make our program more accessible to the general public. Finally, we could expand the scope of the summarizer to input multiple related texts and synthesize them as a whole.

## Running the program
1. Installing Python and pip

To run the program, make sure you have Python installed (3.12 recommended). You can find that [here](https://https://www.python.org/downloads/).
After installing, be sure you have pip, which you can download by running `python -m ensurepip --upgrade`
You can install the required python libraries with pip: `pip install -r requirements.txt`

2. Installing NodeJS and dependencies

Next, to run the self hosted server, ensure you have NodeJS installed. You can find that [here](https://nodejs.org/en/download).
After installing, install node dependencies with `npm install express multer cors`

3. Setting Python path

Finally, edit `server.js` and follow the instructions on lines 1-3 to set the path of your python installation from step 1.

4. Running the program

To run, in your terminal, run `node server.js`. Then in a browser, navigate to [localhost:3000](http://localhost:3000). From there, you can upload `.txt` or `.pdf` files, such as the provided `example.pdf` file about the Amazon rainforest to get a bullet point summary!

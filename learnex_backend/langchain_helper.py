#from langchain.llms import OpenAI
#import secret_key
import os
from langchain.chat_models import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

llm = AzureChatOpenAI(
    api_version = os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_key = os.getenv("AZURE_OPENAI_API_KEY"),
    model = os.getenv("AZURE_OPENAI_MODEL"),
    temperature=0.8
)


def generate_subject_help_links(subject):

    prompt_template_items = PromptTemplate(
        input_variables=['subject'],
        template="""Suggest some good links for CBSE class XI student for subjcect {subject}. Return it as a comma separated string"""
    )

    helpful_links_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="helpful_links")

    chain = SequentialChain(
        chains=[helpful_links_chain],
        input_variables=['subject'],
        output_variables=["helpful_links"]
    )

    response = chain({'subject': subject})

    return response

if __name__ == "__main__":
    print(generate_subject_help_links("physics"))

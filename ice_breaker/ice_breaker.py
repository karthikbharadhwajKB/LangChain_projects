from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedIn import scrape_linkedIn_profile, data_preprocessing

if __name__ == "__main__":
    load_dotenv()

    ## scraping linkedin profile
    linked_data = scrape_linkedIn_profile(linkedin_profile=None, use_api=False)

    ## data preprocessing
    data = data_preprocessing(linked_data)

    ## Prompt
    summary_template = """
    Given the LinkedIn {information} about a person I want you to create:
    1. A Short Summary.
    2. two interesting facts about them.
    """

    ## Prompt Template
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    ## llm model
    chat_llm = ChatOpenAI(temperature=0.2, model="gpt-3.5-turbo")

    ## chain
    chain = LLMChain(llm=chat_llm, prompt=summary_prompt_template)

    ## response
    response = chain.invoke(input={"information": data})

    print(response["text"])

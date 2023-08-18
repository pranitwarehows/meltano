import jwt
from langchain.document_loaders import CubeSemanticLoader
from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain


# Construct the connection string using the parameters
connection_string = "postgresql://cube:6728e90c7094149d49f53c0977f7e7be@tan-squid.sql.aws-eu-central-1.cubecloudapp.dev:5432/tan-squid"
db = SQLDatabase.from_uri(connection_string)

llm= OpenAI(openai_api_keys="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",temperature=0, verbose= True)
db_chain= SQLDatabaseChain.from_llm(llm,db,verbose=True)


response = db_chain.run("How many products are present in store")

print (response)
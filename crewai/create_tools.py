from langchain_community.tools.sql_database.tool import (
    InfoSQLDatabaseTool,
    ListSQLDatabaseTool,
    QuerySQLCheckerTool,
    QuerySQLDataBaseTool,
)
from langchain_community.utilities.sql_database import SQLDatabase
from crewai_tools import tool
from langchain_community.llms import Ollama

# Load the database
db = SQLDatabase.from_uri("sqlite:///players.db")

# Define the tools
@tool("list_tables")
def list_tables() -> str:
    """
    List all tables in the database.
    
    Returns:
        str: A string containing the names of all tables in the database.
    """
    return ListSQLDatabaseTool(db=db).invoke("")

@tool("tables_schema")
def tables_schema(tables: str) -> str:
    """
    List all schemas in the database.
    
    Returns:
        str: A string containing the names of all schemas in the database.
    """    
    tool = InfoSQLDatabaseTool(db=db)
    return tool.invoke(tables)

@tool("execute_sql")
def execute_sql(sql_query: str) -> str:
    """
    Execute sql query in the database.
    
    Returns:
        str: A string containing the result of the query.
    """
    return QuerySQLDataBaseTool(db=db).invoke(sql_query)

@tool("check_sql")
def check_sql(sql_query: str) -> str:
    """
    Check sql query in the database.
    
    Returns:
        str: A string containing the result of the query.
    """    
    return QuerySQLCheckerTool(db=db, llm=llm).invoke({"query": sql_query})
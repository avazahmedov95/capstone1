import json
import sqlite3
from semantic_kernel.functions import kernel_function, KernelArguments
from .agent_logger import AgentLogger

DB_PATH = "db/sales"
SCHEMA_FILE = "db/schema.json"

# Load schema once
try:
    with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
        SCHEMA = json.load(f)
except Exception:
    SCHEMA = {}


def is_query_safe(query: str) -> bool:
    """
    Check if query contains dangerous SQL operations.
    Returns False if query is unsafe.
    """
    if not query:
        return False

    # Convert to lowercase for easier checking
    q = query.lower()

    # Forbidden SQL commands (can destroy or modify structure/data)
    forbidden_keywords = [
        "drop ",
        "delete ",
        "replace ",
    ]

    # Block if any forbidden keyword found
    for word in forbidden_keywords:
        if word in q:
            return False

    return True


class DatabasePlugin:
    @kernel_function(name="SelectQuery", description="Execute a SELECT SQL query and return results.")
    async def select_query(self, query: str, arguments: KernelArguments) -> str:
        AgentLogger.log_action("Database", "SELECT", query)

        if not is_query_safe(query):
            AgentLogger.log_error("Database", f"Unsafe query detected: {query}")
            return json.dumps({"error": "Unsafe query detected. Operation blocked for security reasons."})

        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            conn.close()

            AgentLogger.log_action("Database", "RESULT", f"{len(results)} rows fetched")
            return json.dumps(results)
        except Exception as e:
            AgentLogger.log_error("Database", str(e))
            return json.dumps({"error": str(e)})

    @kernel_function(name="ExecuteNonQuery", description="Execute INSERT, UPDATE query.")
    async def execute_non_query(self, query: str, arguments: KernelArguments) -> str:
        AgentLogger.log_action("Database", "WRITE", query)

        # Safety check for dangerous commands
        if not is_query_safe(query):
            AgentLogger.log_error("Database", f"Unsafe or restricted query blocked: {query}")
            return json.dumps({"error": "This type of query is not allowed for safety reasons."})

        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            conn.close()

            AgentLogger.log_action("Database", "STATUS", "Success")
            return json.dumps({"status": "success"})
        except Exception as e:
            AgentLogger.log_error("Database", str(e))
            return json.dumps({"error": str(e)})

    @kernel_function(name="GetSchema", description="Return schema info or description for a specific table.")
    async def get_schema(self, query: str = "", arguments: KernelArguments = None) -> str:
        AgentLogger.log_action("Database", "SCHEMA_REQUEST", query or "all tables")
        try:
            if not SCHEMA:
                return "Schema is empty or could not be loaded."

            query_lower = (query or "").lower()
            found_table = next((t for t in SCHEMA.keys() if t in query_lower), None)

            if found_table:
                table = SCHEMA[found_table]
                result = f"Table: {found_table}\nDescription: {table['description']}\n\nColumns:\n"
                for col, desc in table["columns"].items():
                    result += f"  - {col}: {desc}\n"
                return result

            # Return full schema
            full_result = "Database schema: 'sales'\n\n"
            for name, table in SCHEMA.items():
                full_result += f"Table: {name}\nDescription: {table['description']}\nColumns:\n"
                for col, desc in table["columns"].items():
                    full_result += f"  - {col}: {desc}\n"
                full_result += "\n"
            return full_result

        except Exception as e:
            AgentLogger.log_error("Database", str(e))
            return f"Error while generating schema info: {str(e)}"

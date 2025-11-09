import os
import requests
from semantic_kernel.functions import kernel_function, KernelArguments
from .agent_logger import AgentLogger

GITHUB_API = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPO")


class GitHubPlugin:
    """Plugin to manage GitHub Issues."""

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"token {GITHUB_TOKEN}" if GITHUB_TOKEN else "",
    }

    @kernel_function(name="CreateIssue", description="Create a new GitHub issue.")
    async def create_issue(self, title: str, body: str = "", arguments: KernelArguments = None) -> str:
        AgentLogger.log_action("GitHub", "CREATE_ISSUE", title)
        try:
            if not GITHUB_TOKEN or not GITHUB_REPO:
                return "GitHub token or repository not configured."

            url = f"{GITHUB_API}/repos/{GITHUB_REPO}/issues"
            data = {"title": title, "body": body}
            response = requests.post(url, headers=self.headers, json=data)

            if response.status_code == 201:
                issue = response.json()
                AgentLogger.log_action("GitHub", "SUCCESS", f"Issue #{issue['number']} created")
                return f"Issue created: #{issue['number']} - {issue['html_url']}"
            else:
                AgentLogger.log_error("GitHub", f"Failed to create issue: {response.status_code}")
                return f"Failed to create issue: {response.status_code}, {response.text}"
        except Exception as e:
            AgentLogger.log_error("GitHub", str(e))
            return f"Error while creating issue: {str(e)}"

    @kernel_function(name="EditIssue", description="Edit an existing GitHub issue.")
    async def edit_issue(self, issue_number: int, title: str = None, body: str = None, arguments: KernelArguments = None) -> str:
        AgentLogger.log_action("GitHub", "EDIT_ISSUE", f"#{issue_number}")
        try:
            if not GITHUB_TOKEN or not GITHUB_REPO:
                return "GitHub token or repository not configured."

            url = f"{GITHUB_API}/repos/{GITHUB_REPO}/issues/{issue_number}"
            data = {}
            if title:
                data["title"] = title
            if body:
                data["body"] = body

            response = requests.patch(url, headers=self.headers, json=data)
            if response.status_code == 200:
                issue = response.json()
                AgentLogger.log_action("GitHub", "SUCCESS", f"Issue #{issue['number']} updated")
                return f"Issue #{issue['number']} updated successfully."
            else:
                AgentLogger.log_error("GitHub", f"Failed to update: {response.status_code}")
                return f"Failed to update: {response.status_code}, {response.text}"

        except Exception as e:
            AgentLogger.log_error("GitHub", str(e))
            return f"Error while editing issue: {str(e)}"

    @kernel_function(name="CloseIssue", description="Close a GitHub issue.")
    async def close_issue(self, issue_number: int, arguments: KernelArguments = None) -> str:
        AgentLogger.log_action("GitHub", "CLOSE_ISSUE", f"#{issue_number}")
        try:
            if not GITHUB_TOKEN or not GITHUB_REPO:
                return "GitHub token or repository not configured."
            url = f"{GITHUB_API}/repos/{GITHUB_REPO}/issues/{issue_number}"
            response = requests.patch(url, headers=self.headers, json={"state": "closed"})
            if response.status_code == 200:
                AgentLogger.log_action("GitHub", "SUCCESS", f"Issue #{issue_number} closed")
                return f"Issue #{issue_number} closed successfully."
            elif response.status_code == 403:
                AgentLogger.log_error("GitHub", "Permission denied to close issue.")
                return "Permission denied to close issue."
            else:
                AgentLogger.log_error("GitHub", f"Failed: {response.status_code}")
                return f"Failed: {response.status_code}, {response.text}"
        except Exception as e:
            AgentLogger.log_error("GitHub", str(e))
            return f"Error while closing issue: {str(e)}"


    @kernel_function(name="ListIssues", description="List all open issues in the GitHub repository.")
    async def list_issues(self, arguments: KernelArguments = None) -> str:
        """List open GitHub issues."""
        try:
            if not GITHUB_TOKEN or not GITHUB_REPO:
                return "GitHub token or repository not configured."

            url = f"{GITHUB_API}/repos/{GITHUB_REPO}/issues"
            response = requests.get(url, headers=self.headers)

            if response.status_code == 200:
                issues = response.json()
                if not issues:
                    return "No open issues found."
                formatted = "\n".join([f"#{i['number']} - {i['title']}" for i in issues])
                return "Open issues:\n" + formatted
            else:
                return f"Failed to fetch issues: {response.status_code}, {response.text}"

        except Exception as e:
            return f"Error while listing issues: {str(e)}"
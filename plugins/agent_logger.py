import os
import logging
from datetime import datetime, timedelta

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "agent.log")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    handlers=[logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8")],
)
logger = logging.getLogger("Agent")


class AgentLogger:
    """Centralized logger used by all plugins."""

    @staticmethod
    def log_action(source: str, action: str, detail: str):
        msg = f"[{source}] {action}: {detail}"
        logger.info(msg)

    @staticmethod
    def log_error(source: str, error: str):
        msg = f"[{source}] ❌ ERROR: {error}"
        logger.error(msg)

    @staticmethod
    def read_logs_for_period(minutes: int = 10):
        """Return logs from the last N minutes."""
        if not os.path.exists(LOG_FILE):
            return "No log file found."

        cutoff = datetime.now() - timedelta(minutes=minutes)
        lines = []
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    ts_str = line.split(" | ")[0]
                    ts = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S,%f")
                    if ts >= cutoff:
                        lines.append(line.strip())
                except Exception:
                    continue
        return "\n".join(lines) if lines else f"No logs found in the last {minutes} minutes."

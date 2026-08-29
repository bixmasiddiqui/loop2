from pathlib import Path
from datetime import datetime
import subprocess


PROGRESS_FILE = Path("progress.md")
SUMMARY_FILE = Path("summary.md")


def run_git_command(command):
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return ""

    return result.stdout.strip()


def read_progress():
    return PROGRESS_FILE.read_text(encoding="utf-8")


def get_latest_commit():
    return run_git_command(
        ["git", "log", "-1", "--format=%H"]
    )


def get_latest_commit_message():
    return run_git_command(
        ["git", "log", "-1", "--format=%s"]
    )


def get_recent_commits():
    return run_git_command(
        ["git", "log", "-5", "--pretty=format:%h - %s"]
    )


def write_summary(timestamp, commit_hash, commit_message, recent_commits):
    summary = f"""# Repository Progress Summary

## Run

{timestamp}

## Latest Commit

**Commit:** `{commit_hash}`

**Message:** {commit_message}

## Recent Commits

{recent_commits}

---

This summary was generated automatically.
"""

    SUMMARY_FILE.write_text(summary, encoding="utf-8")


def update_progress(timestamp, commit_hash, commit_message):
    progress = f"""# Scheduled Loop Progress

## Loop State

- Last Run: {timestamp}
- Last Commit: {commit_hash}
- Last Commit Message: {commit_message}

## Recorded Progress

The loop has processed repository progress up to:

`{commit_hash}`

Last recorded change:

{commit_message}
"""

    PROGRESS_FILE.write_text(progress, encoding="utf-8")


def main():

    print("=================================")
    print("   Scheduled Memory Loop")
    print("=================================")

    # 1. Read the persistent memory
    progress = read_progress()

    # 2. Gather current repository information
    latest_commit = get_latest_commit()
    latest_message = get_latest_commit_message()
    recent_commits = get_recent_commits()

    if not latest_commit:
        print("No Git commits found.")
        return

    # 3. Check whether this commit was already processed
    if latest_commit in progress:
        print("No new progress found.")
        print("This commit has already been recorded.")
        return

    # 4. Create timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 5. Write summary
    write_summary(
        timestamp,
        latest_commit,
        latest_message,
        recent_commits
    )

    # 6. Update the persistent memory
    update_progress(
        timestamp,
        latest_commit,
        latest_message
    )

    print("New progress recorded.")
    print(f"Commit: {latest_commit}")
    print(f"Message: {latest_message}")
    print("Progress memory updated.")


if __name__ == "__main__":
    main()
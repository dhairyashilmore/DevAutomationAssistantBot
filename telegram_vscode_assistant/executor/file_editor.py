"""Intelligent file editing and code insertion."""
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


def find_target_file(prompt: str, project_root: Path) -> Path:
    """Find the best target file for code insertion based on the prompt."""
    # Look for specific filenames mentioned in prompt
    extensions = [".js", ".jsx", ".ts", ".tsx", ".py", ".java", ".cpp"]
    words = prompt.split()
    
    for word in words:
        for ext in extensions:
            if word.lower().endswith(ext):
                for path in project_root.rglob(word):
                    return path
    
    # Fallback: find first source file
    for ext in extensions:
        found = list(project_root.rglob(f"*{ext}"))
        if found:
            return found[0]
    
    # Default output file
    return project_root / "generated_code.txt"


def insert_code_into_file(file_path: Path, code: str, position: str = "end") -> None:
    """Insert generated code into a file at the specified position.
    
    Args:
        file_path: File to modify
        code: Code to insert
        position: 'end', 'start', or 'after_imports' (for .py/.js files)
    """
    logger.info("Inserting code into %s at position '%s'", file_path, position)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    if not file_path.exists():
        # Create new file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)
        return
    
    # Read existing content
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Determine insertion point
    if position == "after_imports":
        # For Python/JS: insert after import statements
        lines = content.split("\n")
        insert_idx = 0
        for i, line in enumerate(lines):
            if line.strip().startswith(("import ", "from ", "require(")):
                insert_idx = i + 1
        new_content = "\n".join(lines[:insert_idx]) + "\n" + code + "\n" + "\n".join(lines[insert_idx:])
    elif position == "start":
        new_content = code + "\n" + content
    else:  # end
        new_content = content + "\n" + code
    
    # Write back
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    logger.info("Code successfully inserted")


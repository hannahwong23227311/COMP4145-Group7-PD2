# COMP4145 Project Development 2 — Idea 1

Stock trading strategy and portfolio analysis prototype.

## Local setup (Windows)

1. Open this repository folder in VS Code.
2. Select the workspace interpreter: `Ctrl+Shift+P` → **Python: Select Interpreter** → `.venv`.
3. In the VS Code terminal, install the project dependencies:

   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

4. When the Streamlit app is added, run it with:

   ```powershell
   .\.venv\Scripts\python.exe -m streamlit run app.py
   ```

Keep API keys and other secrets out of source control. The local
`.streamlit/secrets.toml` file is ignored by Git.
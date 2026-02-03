## MKDocs

MkDocs is a static site generator specifically geared toward creating project documentation. It’s written in Python and uses Markdown files for content. As someone who isn't strongly geared towards software or web development, it saved my life for this project. 

![MkDocs](https://saportfoliodev.blob.core.windows.net/images/Screenshot 2026-02-03 004929.png){ width="450" }

Above is a code snippet of a markdown file that mkdocs would use. I love how simple it is to format. 

**pip install mkdocs mkdocs-material**<br>
First command, ran using Bash in VSCode. This installs MkDocs. This is also included in the requirements.txt file for the AppService.

**mkdocs new .**<br>
Also ran using Bash in VSCode. This creates the mkdocs.yml file and docs folder in the same location.

**mkdocs.yml**: *Your configuration file (where you'll set the site name, theme, and nav)*<br>
**docs/**: *The folder where all your .md files (like index.md) will live.*

**mkdocs serve**<br>
MkDocs will give you a local URL (usually http://127.0.0.1:8000/) to present your webpage. 





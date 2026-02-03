# Storage Strategy

I used Azure Blob Storage to host high-resolution images and diagrams for the site. I didn't care for folder hierarchy, so I didnt opt into Data Lake or even Files. 

## Creating the storage account

* **Basics:** To start, I named the storage account "saportfoliodev" to follow the format of: 1.storage account, 2. project name, and 3. dev or prod. This is the best way im able to cope with no alphanumeric characters. 

For this project, cost is one of my priorities, so it's no question I would select Standard performance and LRS Redundancy. 

![Basics](https://saportfoliodev.blob.core.windows.net/images/Screenshot 2026-02-01 123317.png)

* **Isolation:** This container is isolated from any private or sensitive data to prevent accidental exposure.

In the future, I plan to migrate this to a fully private storage account fronted by an **Azure Front Door** or CDN to eliminate anonymous access entirely.
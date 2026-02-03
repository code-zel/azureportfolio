# Storage Strategy

I used Azure Blob Storage to host high-resolution images and diagrams for the site. I didn't care for folder hierarchy, so I didnt opt into Data Lake or even Files. 

## Creating the storage account

* **Basics:** 
To start, the storage account was named "**saportfoliodev**" to follow the format of: 1.storage account, 2. project name, and 3. dev or prod. This is the best way im able to cope with no alphanumeric characters. 

For this project, cost is one of my priorities, so it's no question I would select **Standard** performance and **LRS Redundancy**. 

![Basics](https://saportfoliodev.blob.core.windows.net/$web/Screenshot 2026-02-01 123317.png)

* **Advanced:** 
It's important that **secure transfer for REST API operations** is enabled, as all connections will be forced to use HTTPS and therefore all data will be encyrpted in transit. 

Let's talk about **Allow enabling anonymous access on individual containers**. In the screenshot, it's disabled, but in order to have images load for website visitors, I had to enable it. 
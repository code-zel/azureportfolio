# Storage Strategy

I used Azure Blob Storage to host high-resolution images and diagrams for the site. I didn't care for folder hierarchy, so I didnt opt into Data Lake or even Files. 

## Basics

To start, the storage account was named "**saportfoliodev**" to follow the format of: 1.storage account, 2. project name, and 3. dev or prod. This is the best way im able to cope with no alphanumeric characters. 

For this project, cost is one of my priorities, so it's no question I would select **Standard** performance and **LRS Redundancy**. 

![Basics](https://saportfoliodev.blob.core.windows.net/images/Screenshot 2026-02-01 123317.png){ width="450" }

## Advanced
It's important that **secure transfer for REST API operations** is enabled, as all connections will be forced to use HTTPS and therefore all data will be encyrpted in transit. 

Let's talk about **Allow enabling anonymous access on individual containers**. Disabling this option (or leaving it unchecked) stops site visitors from seeing files presented on the site. The only way around this is by using a CDN or Front Door, which starts at ~$30/month. In my case, I enabled the anonymous access for the storage account. When doing this, it's important to note that if your site is to contain any sensitive info such as passwords, PII, or backups, that you create a separate, private storage account(with anonymous access disabled). 

**Storage account key access** is disabled/unchecked. These keys are risky because they never expire. We want a more modern auth where permissiosn are granted to users or apps. This also ties in with having **Default to Microsoft Entra authorization in the Azure portal** enabled/checked.

**TLS** is set to a 1.2 minimum, as older versions are known to have vulnerabilities. 

**Permitted scope copy** was set to the highest security level. It mandates that the source account must be on the same private network as itself.

![Advanced-Security](https://saportfoliodev.blob.core.windows.net/images/Screenshot 2026-02-01 130042.png){ width="450" }

Because we are interested in just a Blob storage, we have **hierachical namespace** disabled/unchecked, which leads to SFTP and network file system v3 being unavailable. 

**Cross tenant replication** is disabled. I have no interest in other tenants at this moment. 

![Advanced-Security](https://saportfoliodev.blob.core.windows.net/images/Screenshot 2026-02-01 130051.png){ width="450" }

My chosen blob access tier for this project was **Hot**. I believe that the files on the website will be accessed frequently. Since I'm dumping all of my screenshots I've taken into the blob, I probably won't use a lot of them. Therefore, it may be smart to introduce lifecycle management to make those unused images turn cold.  

The settings for Azure Files have been left alone since Files will not be used for this project. 

![Advanced-Security](https://saportfoliodev.blob.core.windows.net/images/Screenshot 2026-02-01 130100.png){ width="450" }






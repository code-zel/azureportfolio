# Custom Domain Goal 

Have visitors see the front page of my App Service when they navigate to "**wetzelwisdom.com**"

## GoDaddy

For this project, GoDaddy.com was used to affordably purchase and manage the DNS records the wetzelwisdom.com domain. I chose the most basic plan, for they tried to sell me a m365 domain(lol) and protection against domain theft/unwanted charges. 

## Configuration

The first step is to visit your AppService on Azure and view the **Custom Domain** settings. We have to grab both the **IP Address** and **Custom Domain Verification ID**

![Config](https://saportfoliodev.blob.core.windows.net/images/Screenshot 2026-02-03 001728.png){ width="450" }

In the DNS settings of the GoDaddy domain, an **A** record is to be created using the IP address, and a **TXT** using the Custom Domain Verification ID. 

Once the records are created in GoDaddy, we can navigate back to the AppService's custom domain page to add the wetzelwisdom.com domain. Once the domain is validated and added, a binding must also be created using SNI SSL. 

![Config](https://saportfoliodev.blob.core.windows.net/images/Screenshot 2026-02-02 175227.png){ width="450" }
![Config](https://saportfoliodev.blob.core.windows.net/images/Screenshot 2026-02-02 175859.png){ width="450" }

*And now, we can reach our mkdocs webpage through wetzelwisdom.com! Woohoo!*
![Config](https://saportfoliodev.blob.core.windows.net/images/Screenshot 2026-02-02 175922.png){ width="450" }
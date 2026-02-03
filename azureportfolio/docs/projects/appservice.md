## App Service

The goal is to create an app service that has a low base mothly cost and can integrate with Github for CI/CD

## Basics

For the app, the setup was more straightforward that other services. My language and OS of choice was **Python 3.14** and **Linux** running on a **Basic B1** located in East US2. Out of avialable programming languages, I'm most familiar with Python. As an effect of choosing such, Linux is the forced OS. Linux is the only supported operating system for running Python. The only time Windows would be needed for python code is when I'm working with Windows COM objects. 

I chose the basic pricing plan with the intention of cost reduction. **Zone redundancy** is available only on Premium pricing plans. 

![Basics](https://saportfoliodev.blob.core.windows.net/images/Screenshot 2026-02-01 120118.png){ width="450" }

As one of the goals is to connect this app to a storage account, I opted out of making a databse. 

## Continuous Deployment

As of this moment, my github repo was already created, and I didn't even catch I had spelled the name of the repo incorrectly. This caused some fixing-to-do down the line.

![CD](https://saportfoliodev.blob.core.windows.net/images/Screenshot 2026-02-01 120653.png){ width="450" }

**Basic authentication** was left disabled. It's actually more secure to do so. Disabling this option forces Entra for authentication rather than a hard-coded password. This is also disabled with the intent of configuring Github actions and OIDC later down the road. 

![CD](https://saportfoliodev.blob.core.windows.net/images/Screenshot 2026-02-01 120714.png){ width="300" }




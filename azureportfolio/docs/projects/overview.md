## What is this?

This is a cloud portfolio application created to demonstrate competency in Microsoft Azure architecture and modern DevOps practices. The frontend is built using MkDocs, a static site generator powered by Python, utilizing the Material theme for a responsive, professional user interface. The application is hosted on an Azure App Service and is continuously deployed via a custom GitHub Actions pipeline. This automated workflow triggers immediately upon code commits, building the static site artifacts and deploying them to the Azure container. The entire solution is accessible via the custom domain wetzelwisdom.com, which is fully secured with an Azure App Service Managed Certificate (SSL/TLS) for end-to-end encryption.

The App Service architecture is anchored by a zero-trust networking model that uses Azure Private Link to cut off public internet exposure. By routing traffic through a Private Endpoint, the App Service talks to the storage backend using a private IP within the VNet. This communication is strictly moderated by Network Security Groups, which act as a granular firewall to ensure only authorized traffic flows between resources. When you pair this with OIDC for passwordless GitHub deployments and SOC 2 data classification, you get a hardened, enterprise-grade setup that keeps the infrastructure locked down.

# Services used

!(https://az-icons.com/export/icons/675ad8e4daebee40114a4fe36033257c.svg)
!(https://az-icons.com/export/icons/ce8c231e0aac956666abed4c3e6963a2.svg)
!(https://az-icons.com/export/icons/c60ec5d6c1d7f2a0d38687db0ab1f40a.svg)
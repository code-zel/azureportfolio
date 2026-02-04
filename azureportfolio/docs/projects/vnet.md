# Network Strategy

The storage account and app service must exist in their own subnets. <br>
The storage account must be able to talk to the app service using a Private Endpoint. <br>
The storage account must not be accessible from the internet <br>
Network security groups must exist for each subnet and filter traffic under least-access principles. <br>
Do this ALL without caving in and buying a FrontDoor, NAT Gateway, or any paid service.

## It all begins with the VNET

First, we can create our subnets through a **virtual network**. 

For our vnet, we're using the default **/16** address space. The subnets will both use a **/24** address space. What differs between them is that the App Service subnet (SNET-Portfolio-App) is **public** while the Storage Account subnet (SNET-Portfolio-PE) is **private.** PE actually stands for **Private Endpoint**. This subnet will use a Private Endpoint in order to talk to the App Service. 

(screenshot 02-01 201507)

## Private Endpoint

In the creation of the Private Endpoint, PE-Portfolio-Storage, we set up several network tasks:<br>
    - Creating the PE subnet <br>
    - Linking the PE to the blob <br>
    - Integreating the blob with a private DNS zone <br>
    - Creating the PE-Portfolio-Storage-nic<br>

(screenshot 02-01 202721)

This establishes the private endpoint and gives the blob an ip of 10.0.1.4. 

(screenshot 02-03 200334)

## Network security groups

The first group, **NSG-Portfolio-Data**, is the group for the PE subnet. The logic for these rules is that we want to allow traffic from the app. Only the app. The storage account's private endpoint is not to initiate any outbound connections. 

(screenshot 02-03 201433)

The second group, **NSG-Portfolio-App**, is designed with a "Deny by Default" security posture. It explicitly allows only specific outbound traffic while blocking all non-standard inbound traffic.

(screenshot 02 03 201607)

## Verifying above configurations

+  Let's verify the Private Endpoint Connection. We need to make sure it's **Approved** and tied to the correct subnet. Looking at the overview of our Private Endpoint, we can see it's Approved! Clicking into **PE-Portfolio-Storage-nic**, we can see it's IP address is 10.0.1.4, which matches the PE subnet. 

(screenshot 02-03 203055)
(screenshot 02-03 203111)

+  Let's verify the app is connected to our vnet so that it can reach the private IP. We can do that by going into the Networking section of our App Service. **Outbound internet traffic** is enabled and we can see the **Subent name** shows the App subnet. Good!

(screenshot 02-03 203241)

+ Let's verify DNS resolution. If my app service resolves the storage URL to a public IP, it will try to go over the internet (and likely be blocked). We can verify by going to the App Service page and accessing **Advanced Tools**. From there, we can open a bash terminal and run "nslookup saportfoliodev.blob.core.windows.net". 

Success! It's showing the IP of **10.0.1.4**, proving the app is successfully communicating with storage over the Microsoft backbone.

(screenshot 02-03 191354)

## A fatal mistake

Remember how I said I want to do this without using a CDN, Front Door, or any service that costs money?

I set this all up, verified connections, then disabled **Public network access** for my storage account. Here's what happened:

(screenshot 02-03 191832)

After some research, I gathered the understanding that this is because **the client** (aka your device, not the app) is is trying to fetch those images directly from the storage URL when the site is accessed. Not good. 


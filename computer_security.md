# Security

## Stuxnet

- [Stuxnet wikipedia article](https://en.wikipedia.org/wiki/Stuxnet)
- [Broadcom - Exploring Stuxnet’s PLC Infection Process](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=ad4b3d10-b808-414c-b4c3-ae4a2ed85560&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)
- Targetted gas centrifuges used in nuclear fuel enrichment

### Further reading

- [Zippe-type centrifuge](https://en.wikipedia.org/wiki/Zippe-type_centrifuge#:~:text=From%20Wikipedia%2C%20the%20free%20encyclopedia,in%20naturally%20occurring%20uranium%20compounds)
- [Cross-Platform / Modular Glupteba Malware Uses ManageX](https://www.trendmicro.com/en_us/research/20/i/cross-platform-modular-glupteba-malware-uses-managex.html)

## Darknet diaries

### Episode 86: The LinkedIn Incident

- Companies affected by hack: LinkedIn, Dropbox and one other company
- Culprit fingerprinted using IP address and user agent
- Mistakes done by people hacked
  - Using home computer to access work and using the private keys to login to VPN
  - Password reuse in mutliple systems
  - Sharing clues about production env publicly.
- Mistakes done by attacker
  - Accessing everything with the same IP and same user agent info(sputnik). That allowed people to figerprint him.
  - Using American services like gmail, vimeo, etc that allowed american law enforcement to get access to logs pertaining to him.
- Mistakes done by company
  - Allowing access to production env from corp net
  - Not salting passwords
  - Not checking for access anamolies. In this case the hacker was accessing from Russia.

#### Questions

- How to retain logs for post-mortem investigations?

### Episode 89: Cybereason - Molerats in the cloud

- Cybereason - an Israeli company that creates the endpoint protection solution
- Founder from Unit 8200 (Israels equivalent of NSA)
- user behavior analytics/anamoly detection based on a in-memory graph based rules/execution engine
- An agent needs to be intalled on every machine
- Phishing mails with malicious attachments - exe masking itself as doc or pdf file
- Talks about a hack where the malware checked if arabic was installed before doing its thing. This greatly reduced the possbility of the malware triggerring alarms in sandboxes
- VirusTotal was used by the team but it did not detect the uploaded file as virus (probably because of the above mentioned trick used by the virus)

#### Follow-up tasks

- Create an exe that looks like a doc file to figure out how easy it is to do and figure out if Windows or anyother major OS provides any kind-of protections or indications

## Random points

- Modular composition of malware
- Dropper, packer (UPX packer)

### Gloassary

- Malware
- Virus
- Worm
- Rootkit

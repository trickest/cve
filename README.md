<h1 align="center">CVE PoC <a href="https://twitter.com/intent/tweet?text=CVE%20PoC%20-%20Find%20almost%20every%20publicly%20available%20CVE%20Proof-of-Concept%2E%0Aby%20%40trick3st%0Ahttps%3A%2F%2Fgithub%2Ecom%2Ftrickest%2Fcve%0A&hashtags=cve,poc,vulnerability,vulnerabilities,exploit,infosec,cybersecurity"><img src="https://img.shields.io/badge/Tweet--lightgrey?logo=twitter&style=social" alt="Tweet" height="20"/></a></h1>
<h3 align="center">Almost every publicly available CVE PoC.</h3>

## Current hottest CVEs
| Title      | URL |  
| ----------- | ----------- |  
| CVE-2022-0001      | [/trickest/cve/blob/main/2022/CVE-2022-0001.md](https://github.com/trickest/cve/blob/main/2022/CVE-2022-0001.md) |  
| CVE-2022-25297      | [/trickest/cve/blob/main/2022/CVE-2022-25297.md](https://github.com/trickest/cve/blob/main/2022/CVE-2022-25297.md) |  
| CVE-2022-1388      | [/trickest/cve/blob/main/2022/CVE-2022-1388.md](https://github.com/trickest/cve/blob/main/2022/CVE-2022-1388.md) |  
| CVE-2022-25451      | [/trickest/cve/blob/main/2022/CVE-2022-25451.md](https://github.com/trickest/cve/blob/main/2022/CVE-2022-25451.md) |  

To see the complete history go [here](hot_cves.csv)

[<img src="./banner.png" />](https://trickest-access.paperform.co/)

## How it works
### [Trickest](https://trickest.com) Workflow Architecture

![Trickest Workflow - PoC](workflow.png "Trickest Workflow - PoC")

### TB; DZ (Too big; didn't zoom):
- Collect CVE details from [cvelist](https://github.com/CVEProject/cvelist) (Shout out to [CVE Project](https://github.com/CVEProject)!)
- Split CVEs up by year.
- Find PoCs for each CVE using 2 techniques:
    1. References
        - Gather each CVE's `References`.
        - Check if any of them points to a PoC using [ffuf](https://github.com/ffuf/ffuf) and a list of keywords

         Regex:
         ```(?i)[^a-z0-9]+(poc|proof of concept|proof[-_]of[-_]concept)[^a-z0-9]+```

         (Thanks [@joohoi](https://github.com/joohoi)!)
         
         **Note**: [ffuf](https://github.com/ffuf/ffuf) is awesome for more purposes than just content discovery.

         Get CVE referenced in HackerOne Reports - [AllVideoPocsFromHackerOne](https://github.com/zeroc00I/AllVideoPocsFromHackerOne) (Thanks [@zeroc00I](https://github.com/zeroc00I)!)


    2. Github
        
        Search GitHub for repositories with [find-gh-poc](https://github.com/trickest/find-gh-poc) that mention the CVE ID.
- Merge the fresh results into the repository without overwriting the data that was committed manually.
- Filter false positives using `blacklist.txt`.
- Merge all of the found PoCs.
- Generate GitHub badges for each affected software version using [shields.io](https://shields.io).
- Write everything into easy-to-read markdown files.



> **As described, almost everything in this repository is generated automatically. We carefully designed the workflow (and continue to develop it) to ensure the results are as accurate as possible.**



## Use cases 
- Browse around, find a nice PoC, and test away!
- `Watch` the repository to receive notifications about new PoCs as soon as they go public.
- Search for a specific product(s) (and possibly version) to find all public exploits related to it.
- Monitor the [atom feed](https://github.com/trickest/cve/commits/main.atom) for a specific product(s).
- Create a searchable HTML table using the template and script in [summary_html](summary_html)
    - Example: https://www.andrewmohawk.com/cve_summary (Thanks [@AndrewMohawk](https://github.com/AndrewMohawk)!)

## Contribution
All contribtutions/ideas/suggestions are welcome! Create a new ticket via [GitHub issues](https://github.com/trickest/cve/issues) or tweet at us [@trick3st](https://twitter.com/trick3st).

## Build your own workflows

We believe in the value of tinkering; cookie-cutter solutions rarely cut it. Sign up for a [Trickest](https://trickest.com) demo to customize this workflow to your use case, get access to many more workflows, or build your own workflows from scratch!

[<img src="./banner.png" />](https://trickest-access.paperform.co/)

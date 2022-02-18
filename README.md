<h1 align="center">CVE PoC <a href="https://twitter.com/intent/tweet?text=CVE%20PoC%20-%20Find%20almost%20every%20publicly%20available%20CVE%20Proof-of-Concept%2E%0Ahttps%3A%2F%2Fgithub%2Ecom%2Ftrickest%2Fcve%0A&hashtags=cve,poc,vulnerability,vulnerabilities,exploit,infosec,cybersecurity"><img src="https://img.shields.io/badge/Tweet--lightgrey?logo=twitter&style=social" alt="Tweet" height="20"/></a></h1>
<h3 align="center">Almost every publicly available CVE PoC.</h3>


## How it works
### [Trickest](https://trickest.com) Workflow Architecture

```mermaid
graph LR
generate-years-with-seq:::trickest ---> split-years:::trickest
split-years:::trickest ---> print-single-year:::trickest
cve-list-clone:::trickest ---> json-per-year:::trickest
print-single-year:::trickest ---> json-per-year:::trickest
json-per-year:::trickest ---> year-references:::trickest
year-references:::trickest ---> current-year-references:::trickest
ffuf:::trickest ---> jq:::trickest
jq:::trickest ---> grep-found-references:::trickest
current-year-references:::trickest ---> grep-found-references:::trickest
json-per-year:::trickest ---> generate-product-names:::trickest
generate-product-names:::trickest ---> get-all-product-names:::trickest
json-per-year:::trickest ---> generate-vulnerability-names:::trickest
generate-vulnerability-names:::trickest ---> merge-all-vulnerability-names:::trickest
json-per-year:::trickest ---> generate-version-names:::trickest
generate-version-names:::trickest ---> merge-all-version-names:::trickest
json-per-year:::trickest ---> generate-descriptions:::trickest
generate-descriptions:::trickest ---> merge-all-descriptions:::trickest
print-single-year:::trickest ---> create-regex-query:::trickest
create-regex-query:::trickest ---> find-gh-poc:::trickest
find-gh-poc:::trickest ---> merge-all-poc-github:::trickest
get-previous-github-pocs:::trickest ---> merge-all-poc-github:::trickest
merge-all-poc-github:::trickest ---> get-all-data:::trickest
merge-all-version-names:::trickest ---> get-all-data:::trickest
merge-all-descriptions:::trickest ---> get-all-data:::trickest
merge-all-vulnerability-names:::trickest ---> get-all-data:::trickest
get-all-product-names:::trickest ---> get-all-data:::trickest
year-references:::trickest ---> ffuf:::trickest
merge-poc-references:::trickest ---> get-all-data:::trickest
get-all-data:::trickest ---> generate-readmes-and-push:::trickest
grep-found-references:::trickest ---> merge-valid-poc-references:::trickest
merge-valid-poc-references:::trickest ---> merge-poc-references:::trickest
previous-executions-references:::trickest ---> merge-valid-poc-references:::trickest
readme.sh:::trickest ---> generate-readmes-and-push:::trickest
grep-found-references:::trickest ---> store-all-valid-poc-references:::trickest
classDef trickest background:black,fill: #0A2741,border: 1px solid #105F7B,border-radius: 2px,color:#17B0D0,font-size:15px
```

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
    2. Github
        
        Search GitHub for repositories with [find-gh-poc](https://github.com/trickest/find-gh-poc) (release soon!) that mention the CVE ID.
- Get manually added CVEs with their PoCs.
- Get all previous results and deduplicate.
- ```grep -v``` bad results by using ```blacklist.txt```
- Merge all of the found PoCs.
- Generate GitHub badges for each affected software version using [shields.io](https://shields.io).
- Write everything into easy-to-read markdown files.



> **As described, almost everything in this repository is generated automatically. We carefully designed the workflow (and continue to develop it) to ensure the results are as accurate as possible.**



## Use cases 
- Browse around, find a nice PoC, and test away!
- `Watch` the repository to receive notifications about new PoCs as soon as they go public.
- Search for a specific product(s) (and possibly version) to find all public exploits related to it.
- Monitor the [atom feed](https://github.com/trickest/cve/commits/main.atom) for a specific product(s).

## Contribution
All contribtutions/ideas/suggestions are welcome! Create a new ticket via [GitHub issues](https://github.com/trickest/cve/issues) or tweet at us [@trick3st](https://twitter.com/trick3st).

## Build your own workflows

We believe in the value of tinkering; cookie-cutter solutions rarely cut it. Sign up for a demo on [trickest.com](https://trickest.com) to customize this workflow to your use case, get access to many more workflows, or build your own from scratch!

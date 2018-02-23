Title: Web Scraping with Firefox
Date: 2018-01-06
Modified: 2017-12-14 21:10
Category: Code
Tags: code, javascript, scraping
Slug: scraper-firefox-greasemonkey
Authors: Nicolás Bohórquez
Summary: An alterna(t)ive way to extract data from the web, i'm going to use Firefox and greasemonkey to scrape some data from Twitter.
Series: small_chunks_of_code
Status: published

Ok, scraping, a super tool to get data from the web, companies try to get info from the users using small rewards and monetizing their data after some sort of "anonymization", while newcomers try to get the data to compete and break the walled gardens, recently Linkedin [lost](https://thenextweb.com/artificial-intelligence/2017/08/15/linkedin-loses-legal-right-to-protect-user-data-from-ai-scraping/) a battle in that sense against HiQ, the technique of gather that data from websites is called scraping.

Companies tries to detect automated browsers with some standard behaviour analysis techniques and devs just try to make a living, have fun or kill the system. This time i am going to show a simple crawler that scrapes data from twitter simulating a user that scrolls down the page ad infinitum.

Twitter loads data in chunks and offers an free API with some restrictions, but what if i want to search for the followers of a famous Colombian ~~[criminal]~~ former president? 5M followers with the [API](https://developer.twitter.com/en/docs/basics/rate-limits) would take something like:

t = 5000000 / (15 * 200 * 4)

fifteen calls 4 times per hour with 200 results per call, about 416 hours or 17 days approx., can we do better? i don't know, that's the subject for the next post, but for know we are going to try a different approach.

## Greasemonkey

An important tool for devs are Firefox addons, in concretetly Greasemonkey and co. which allows you to execute javascript code directly on the browser when you open a page. For this small example i am going to use [Tampermonkey](https://tampermonkey.net/) since i like the dashboard that it gives you to manage the scripts:

![Tampermonkey scripts]({filename}/images/code/tampermonkey_script_overview.png)

After you familiarize with this tool you can checkout this code as a new script:

```
// ==UserScript==
// @name         twitter-scraper
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @require     http://code.jquery.com/jquery-2.1.1.min.js
// @require  https://gist.github.com/raw/2625891/waitForKeyElements.js
// @author       You
// @include      https://twitter.com/AlvaroUribeVel/followers
// @grant        GM_addStyle
// ==/UserScript==

(function() {
    'use strict';
    var loops = 0;
    var found = 0;

    function isElementInViewport (el) {
        //special bonus for those using jQuery
        if (typeof jQuery === "function" && el instanceof jQuery) {
            el = el[0];
        }

        var rect = el.getBoundingClientRect();

        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) && /*or $(window).height() */
            rect.right <= (window.innerWidth || document.documentElement.clientWidth) /*or $(window).width() */
        );
    }

    //this is the important one!
    function addCustomSearchResult (follower) {
        var txt = follower[0].textContent.replace('\n',' ').trim().toLowerCase();
        if(txt.indexOf("uribist") == -1){
            follower[0].parentNode.parentNode.parentNode.parentNode.parentNode.remove();
        } else {
            found++;
            console.log("Found! ",found, " loops: "+loops);
            document.getElementsByClassName("ProfileCard-bg")[0].remove();
            document.getElementsByClassName("ProfileCard-avatarLink")[0].remove();
            document.getElementsByClassName("ProfileCard-actions")[0].remove();
        }
        window.scrollTo(0,0);
    }

    function isElementVisible(el) {
        var rect     = el.getBoundingClientRect(),
            vWidth   = window.innerWidth || doc.documentElement.clientWidth,
            vHeight  = window.innerHeight || doc.documentElement.clientHeight,
            efp      = function (x, y) { return document.elementFromPoint(x, y) };

        // Return false if it's not in the viewport
        if (rect.right < 0 || rect.bottom < 0
            || rect.left > vWidth || rect.top > vHeight)
            return false;

        // Return true if any of its four corners are visible
        return (
            el.contains(efp(rect.left,  rect.top))
            ||  el.contains(efp(rect.right, rect.top))
            ||  el.contains(efp(rect.right, rect.bottom))
            ||  el.contains(efp(rect.left,  rect.bottom))
        );
    }

    setInterval(function() {
        var el = document.getElementsByClassName("ProfileAvatar-image")[0];
        if( isElementVisible(el) == false){
            el.scrollIntoView();
        }
        var height = document.body.scrollHeight;
        loops++;
        window.scrollTo(0,height);

    }, 30000);

    waitForKeyElements (".ProfileCard-bio", addCustomSearchResult);


})();
```

The script basically:

- **Line 9**: Can be activated for a specific page
- **Line 35**: Defines a function that process each node of the class 'ProfileCard-bio' deleting those that don't meet a certain condition
- **Line 69**: Defines a function that scrolls up and down the page each 30 seconds to activate Twitter's calls for more results
- **Line 80**: Waits for new elements with the class 'ProfileCard-bio' and calls the function defined in line 35 for those elements

You can process the results in a variety of ways, enhance, save,etc. Next time i am going to compare this approach with the traditional API access.

**Disclaimer**: Use this _only_ for teaching purposes, i am not taking any kind of responsability for the missuse of this type of technique.

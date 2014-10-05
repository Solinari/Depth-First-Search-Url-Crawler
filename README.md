Depth-First-Search-Url-Crawler
==============================
I had a lot of fun getting this to work. 

Right now all it does is:
1) start at the passed url
2) find all url's on that url
3) go to each of those url's
4) find all url's on each of those url's...
5) ad infinitum...

Since I'm not storing these right now, it'l crash out python
due to hitting the maximum recursion depth. 

Next steps is to think about saving these url's or viewing data on each page
Or perhaps using a stored value of data to compare against and save it for future mining/analysis purposes.

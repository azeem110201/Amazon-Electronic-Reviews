# Amazon Electronic Items Reviews

[![N|Solid](https://miro.medium.com/max/1200/1*YJNS0JVl7RsVDTmORGZ6xA.png)](https://scrapy.org/)

This Repositories contains code along with the dataset for more than 400k+ amazon electronics items reviews


## Installation

Amazon Electronic Items Reviews requires [Scrapy](https://scrapy.org/) v1+ to run.

Install the dependencies and devDependencies and start the server.

```sh
pip install scrapy
```

Then clone this repo and 

```sh
scrapy crawl amazon
```

and if you want to save this record into csv then run the below command

```sh
scrapy crawl amazon -o results.csv
```

##### Note:

      Please uncomment the BASE_URL variable for scraping either positive or negative reviews, because positive and negative reviews were scraped separately to get maximum reviews. 
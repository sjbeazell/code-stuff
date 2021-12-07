#!/usr/bin/env python	
import time
from zapv2 import ZAPv2

# the URL of the application to be tested
target = 'changeMe'

# change to match the API key set in ZAP, or use None if the API key is disabled
apiKey = 'changeMe'

# by default ZAP API client will connect to port 8080
zap = ZAPv2(apikey=apiKey)

# use the line below if ZAP is not listening on port 8080, for example, if listening on port 8090
# zap = ZAPv2(apikey=apiKey, proxies={'http': 'http://127.0.0.1:8090', 'https': 'https://127.0.0.1:8090}) 

print('Spidering target {}'.format(target))

# the scan returns a scan id to support concurrent scanning
scanID = zap.spider.scan(target)
while int(zap.spider.status(scanID)) < 100:
	# poll the status until it completes
	print('Spidering porgress %: {}'.format(zap.spider.status(scanID)))
	time.sleep(1)
	
print('Spider has completed!')

# prints the URLs the spider has crawled

print('\n'.join(map(str, zap.spider.results(scanID))))

# if required post process the spider results

#! /usr/bin/python

import xively
import datetime
import sys

if len (sys.argv) < 5:
    print 'USAGE: ' + sys.argv[0] + ' API_KEY FEED_ID channelName data'
    sys.exit (1)

API_KEY = sys.argv[1]
FEED_ID = sys.argv[2]
channelName = sys.argv[3]
data = sys.argv[4]

now = datetime.datetime.utcnow()

try:
    api = xively.XivelyAPIClient(API_KEY)
    print 'API call OK'

	try:
		feed = api.feeds.get(FEED_ID)
		print 'feed call OK'

		try:
			stream = feed.datastreams.get (channelName)
			print 'stream call OK'

			stream.current_value = data
			stream.at = now

			try:
				stream.update()
				print 'update call OK'
			except Exception as e:
				print 'update call FAILED' + e
				sys.exit (1)

		except Exception as e:
			print 'stream call FAILED ' + e
			sys.exit (1)

	except Exception as e:
		print 'feed call FAILED ' + e
		sys.exit (1)
except Exception as e:
	print 'API call FAILED ' + e
	sys.exit (1)

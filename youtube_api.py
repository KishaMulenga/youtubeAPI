import json
from pyyoutube import Api 
api = Api(api_key="YOUR_API_KEY")

channel_by_id = api.get_channel_info(channel_id="UC_x5XG1OV2P6uZZ5FSM9Ttw")
channel_statistics = channel_by_id.items[0].statistics 
channel_viewCount = channel_by_id.items[0].statistics.viewCount
print("This is channel statistics: {}".format(channel_statistics))
print("This is channel viewCount: {}".format(channel_viewCount))
#print(channel_by_id.items[0].to_dict())

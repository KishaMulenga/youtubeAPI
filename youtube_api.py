from pyyoutube import Api 
api = Api(api_key="YOUR_API_KEY")

channel_by_id = api.get_channel_info(channel_id="UC_x5XG1OV2P6uZZ5FSM9Ttw")
print(channel_by_id.items[0].to_dict())

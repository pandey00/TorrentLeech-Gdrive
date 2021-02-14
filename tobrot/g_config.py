from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1631083376:AAEB4z5GY3mF7bf7mvK4Pxw3wg8_oQsvTiU"
    APP_ID = 1712179
    API_HASH = "35507b2597b41a609e613ade393effe8"
    OWNER_ID = 777252565
    AUTH_CHANNEL = [-1001452962072]
    DESTINATION_FOLDER = "TorrentLeech-Gdrive" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    RCLONE_CONFIG = """
[DRIVE]
type = drive
client_id = 982931265312-n776nj3pev49ln6918cksfk6dqhe4m92.apps.googleusercontent.com
client_secret = Z-HDMGAPvViFGxllmYrrxXS4
scope = drive
root_folder_id =1VCBM1JfPogW_ekkZMnnj__f0WiO-026v
token = {"access_token":"ya29.a-fill-your-details-af4ychuHswBt8X0nf2oWmczsHg6MYPSE6hXo-PJ-fill-your-details-s06KAecfw_H-tYThBtbs:20:25.430920315Z"}
team_drive = 0AB0q-fill-your-details-sdrgsgsdUk9PVA
"""

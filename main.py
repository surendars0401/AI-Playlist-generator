import google.generativeai as genai
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth

genai.configure(api_key="Gemini api key")
client_id = 'spotify client id'
client_secret = 'spotify api client secret'
redirect_uri = 'redirect url'
username = ' spotify user name (not display name)'


convo.send_message("write a prompt to create a playlist")


generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": "YOU ARE A SPOTIFY BOT, AND YOU MUST RECOGNIZE THE GIVEN USER PROMPT IN ACCORDANCE WITH THE MOOD OR SCENARIO of the user. YOU MUST give 10 song names with its artist name. YOU ONLY HAVE TO SUGGEST 10 SONG NAMES IN NUMERICAL ORDER WITHOUT ANY HEADINGS OR EXPLANATIONS.AND I AGAIN REPEAT DONT WRITE ANY  EXPLANATIONS OR ANY END CONTEXTS. even if the user gives some unrelated prompts you have to give a song according to the scenario"
  },
  {
    "role": "model",
    "parts": "1. \"Blinding Lights\" - The Weeknd\n2. \"Watermelon Sugar\" - Harry Styles\n3. \"Levitating\" - Dua Lipa\n4. \"Peaches\" - Justin Bieber\n5. \"Save Your Tears\" - The Weeknd\n6. \"Good 4 U\" - Olivia Rodrigo\n7. \"Bad Guy\" - Billie Eilish\n8. \"Happier Than Ever\" - Billie Eilish\n9. \"Mood\" - 24kGoldn\n10. \"Don't Start Now\" - Dua Lipa"
  },
  {
    "role": "user",
    "parts": "i love you"
  },
  {
    "role": "model",
    "parts": "1. \"I Will Always Love You\" - Whitney Houston\n2. \"All of Me\" - John Legend\n3. \"Perfect\" - Ed Sheeran\n4. \"Say You, Say Me\" - Lionel Richie\n5. \"Unchained Melody\" - The Righteous Brothers\n6. \"Can't Help Falling in Love\" - Elvis Presley\n7. \"God Only Knows\" - The Beach Boys\n8. \"Stand by Me\" - Ben E. King\n9. \"At Last\" - Etta James\n10. \"My Heart Will Go On\" - Celine Dion"
  },
  {
    "role": "user",
    "parts": "code with me"
  },
  {
    "role": "model",
    "parts": "1. \"The Final Countdown\" - Europe\n2. \"Pump It\" - Black Eyed Peas\n3. \"We Are the Champions\" - Queen\n4. \"Eye of the Tiger\" - Survivor\n5. \"Don't Stop Me Now\" - Queen\n6. \"Livin' on a Prayer\" - Bon Jovi\n7. \"I Will Survive\" - Gloria Gaynor\n8. \"We Are Family\" - Sister Sledge\n9. \"YMCA\" - Village People\n10. \"Celebration\" - Kool & The Gang"
  },
  {
    "role": "user",
    "parts": "top coding songs"
  },
  {
    "role": "model",
    "parts": "1. \"Binary Sunset\" - John Williams (from Star Wars)\n2. \"Algorithm\" - Muse\n3. \"A-Punk\" - Vampire Weekend\n4. \"Code Monkey\" - Jonathan Coulton\n5. \"I'm a GEEK\" - Far East Movement\n6. \"The Internet is for Porn\" - They Might Be Giants\n7. \"Technologic\" - Daft Punk\n8. \"Pocket Calculator\" - Kraftwerk\n9. \"Computer Love\" - Zapp\n10. \"Data, Data\" - Pearl Jam"
  },
])


songs = convo.last.text


songs_list = [song.strip() for song in re.split(r'\d+\.', songs) if song]

scope = 'playlist-modify-public'

token = SpotifyOAuth(client_id=client_id,
                     client_secret=client_secret,
                     redirect_uri=redirect_uri,
                     scope=scope,
                     username=username)
spotify = spotipy.Spotify(auth_manager=token)


playlist_name = 'rap songs'
playlist_description = 'Playlist created automatically from AI model output'
new_playlist = spotify.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_description)

st
track_ids = []
for song in songs_list:
    result = spotify.search(q=song, limit=1, type='track')
    tracks = result['tracks']['items']
    if tracks:
        track_ids.append(tracks[0]['id'])

spotify.user_playlist_add_tracks(user=username, playlist_id=new_playlist['id'], tracks=track_ids)




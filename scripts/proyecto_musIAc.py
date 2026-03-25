import google.generativeai as genai
from pythonosc import udp_client
import argparse
import os

# 1. Setup Gemini
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    print("Key found successfully!")
else:
    print("Key not found. Check your Path variables.")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-3-flash-preview')

# 2. Setup Sonic Pi OSC Bridge
# Sonic Pi listens on port 4560 by default
ip = "127.0.0.1"
port = 4560
client = udp_client.SimpleUDPClient(ip, port)

def generate_and_play():
    painting = input("Enter Painting Name: ")
    author = input("Enter Author: ")

    prompt = f"""
    Act as an algorithmic music composer for Sonic Pi (Ruby-based).
    Create a short musical sketch inspired by the painting '{painting}' by {author}.

    Constraints:
    - Use Ruby syntax compatible with Sonic Pi.
    - Focus on 'programmer happiness': clean, readable code.
    - Use comments to explain the visual-to-musical mapping.
    - Return ONLY the code. No conversational text. No markdown backticks.

    STRICT SYNTAX RULES:
    1. Only use these verified Sonic Pi synths: :sine, :saw, :prophet, :hollow, :pluck, :piano, :blade, :pretty_bell, :chipbass.
    2. Do not use :plucked or :string.
    3. Use 'live_loop' for continuous patterns.
    4. Return ONLY the Ruby code block.
    """

    print(f"\n🎨 Consulting the Muse for '{painting}'...")

    # Call Gemini
    response = model.generate_content(prompt)
    ruby_code = response.text.strip()

    # Clean up markdown if Gemini accidentally includes it
    ruby_code = ruby_code.replace("```ruby", "").replace("```", "")

    print("🎹 Sending code to Sonic Pi...")
    print("-" * 30)
    print(ruby_code)
    print("-" * 30)

    # 3. The "Magic" Command
    # We send the code to the /run-code address which Sonic Pi understands
    client.send_message("/run-code", ruby_code)

if __name__ == "__main__":
    try:
        while True:
            generate_and_play()
            print("\nListening... (Ctrl+C to stop)")
    except KeyboardInterrupt:
        print("\nSilent night.")


# The Dispatcher: This loop listens for our Python script
# live_loop :art_code_runner do
#   use_real_time
#   # This waits for any OSC message ending in /run-code
#   res = sync "/osc*/run-code"

#   # The code arrives as a list; we take the first element and 'eval' it
#   code_string = res[0]

#   puts "🎨 Painting received! Executing code..."
#   eval code_string
# end
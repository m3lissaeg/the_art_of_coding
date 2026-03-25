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
      You are a Sonic Pi Code Generator.
      Task: Generate a Ruby script for the painting '{painting}' by {author}.

      STRICT RULES:
      1. Output MUST be RAW Ruby code only.
      2. NO markdown formatting, NO backticks, NO "Here is your code" text.
      3. Use ONLY # for comments. Ensure every comment is on its own new line.
      4. Use 'get(:vol, 0.5)' for all amp: values.
      5. Avoid complex one-liners; keep logic simple to prevent syntax errors.
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


# The Hardened Dispatcher
# live_loop :art_code_runner do
#   use_real_time
#   res = sync "/osc*/run-code"

#   # 1. Extract and Clean the String
#   raw_code = res[0].to_s

#   # 2. Safety Scrubbing
#   # Removes markdown ticks if they escaped the Python filter
#   clean_code = raw_code.gsub("```ruby", "").gsub("```", "")

#   # Fixes common AI chord/synth naming hallucinations
#   clean_code = clean_code.gsub(':major9', ':maj9')
#   .gsub(':plucked', ':pluck')
#   .gsub('\"', '"') # Fixes escaped quotes

#   puts "🎨 Painting received! Executing sanitized code..."

#   begin
#     # We clear previous loops to prevent "ghost" sounds overlapping
#     stop if look > 0
#     eval clean_code
#   rescue Exception => e
#     # This will now give you a much clearer explanation of exactly which line failed
#     puts "❌ Code Error: #{e.message}"
#     puts "Full code received was: #{clean_code}"
#   end
# end
import streamlit as st
import time
import datetime
from datetime import date, timedelta
import random
import math
import os
from PIL import Image



# Page configuration
st.set_page_config(
    page_title="💕 Happy 22nd Birthday My Love! 💕",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="expanded"
)
# --- Big "I ❤️ U" made of small hearts ---
love_art = """
<div style="text-align: center; font-size: 18px; line-height: 1.1; font-family: monospace;">

<!-- I -->
❤️❤️❤️       
  ❤️
  ❤️
  ❤️
❤️❤️❤️      

<br>

<!-- Heart -->
   ❤️❤️   ❤️❤️   
 ❤️❤️❤️❤️❤️❤️❤️ 
 ❤️❤️❤️❤️❤️❤️❤️ 
  ❤️❤️❤️❤️❤️❤️  
    ❤️❤️❤️❤️    
      ❤️❤️      
       ❤️       

<br>

<!-- U -->
❤️       ❤️
❤️       ❤️
❤️       ❤️
❤️       ❤️
 ❤️❤️❤️❤️ 

</div>
"""

st.markdown(love_art, unsafe_allow_html=True)
# Animated sparkles row
sparkle_cols = st.columns(7)
sparkles = ["✨", "💫", "⭐", "🌟", "✨", "💫", "⭐"]
for i, col in enumerate(sparkle_cols):
    with col:
        st.markdown(f'<div class="sparkle" style="text-align: center; font-size: 1.5rem;">{sparkles[i]}</div>', unsafe_allow_html=True)


# --- Background Music Player ---
st.markdown("### 🎵 Background Music")
music_folder = 'music'
if os.path.exists(music_folder):
    music_files = [f"{music_folder}/{mus}" for mus in os.listdir(music_folder) if mus.lower().endswith(("mp3", "wav", "ogg"))]
    if music_files:
        selected_song = st.selectbox("Choose a song to play", music_files)
        audio_file = open(selected_song, "rb").read()
        st.audio(audio_file, format='audio/mp3')
    else:
        st.info("No music files found in the 'music' folder.")
else:
    st.warning("Music folder not found. Please add audio files here.")
# Enhanced floating hearts
heart_cols = st.columns(9)
heart_emojis = ["💖", "💕", "💗", "💝", "💖", "💕", "💗", "💝", "💖"]
for i, col in enumerate(heart_cols):
    with col:
        st.markdown(f'<div class="heart" style="animation-delay: {i*0.2}s;">💖</div>', unsafe_allow_html=True)


#--- Messages from Heaven Section ---
st.markdown("---")
st.markdown("### 💌 Messages from Those Watching Over You ❤️✨")
messages_from_heaven = {
    "Mom": "My dearest child, even from heaven, I am so proud and love you endlessly. Shine bright always.",
    "Grandmother": "Sweetheart, your smile lights up the world. I'm always beside you in spirit, sending love.",
    "Grandfather": "To my beloved granddaughter, your heart is pure and kind. Remember, I’m always watching and cheering you on."
}
# Soft visual style for heavenly messages
st.markdown(
    """
    <div style="
        background: #fff0f5;
        border-left: 6px solid #ff69b4;
        padding: 15px;
        border-radius: 10px;
        font-style: italic;
        color: #7b2a3a;">
    """, unsafe_allow_html=True)
for sender, message in messages_from_heaven.items():
    st.markdown(f"**From {sender}:**  \n*\"{message}\"*")
st.markdown("</div>", unsafe_allow_html=True)

# --- Celebration Enhancements ---
col1, col2 = st.columns(2)
with col1:
    if st.button("🎉 Celebrate with Balloons!"):
        st.balloons()
with col2:
    if st.button("❄️ Remember with Snowflake Magic"):
        st.snow()



# Advanced CSS with more animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&family=Poppins:wght@300;400;600;700&display=swap');

    .main {
        background: linear-gradient(45deg, #ff6b9d, #c44569, #f8b500, #ff6b9d, #a8e6cf, #ff6b9d);
        background-size: 600% 600%;
        animation: gradientShift 10s ease infinite;
        font-family: 'Poppins', sans-serif;
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        25% { background-position: 100% 0%; }
        50% { background-position: 100% 100%; }
        75% { background-position: 0% 100%; }
        100% { background-position: 0% 50%; }
    }

    .love-header {
        text-align: center;
        color: #fff;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.7);
        font-size: 3.5rem;
        margin-bottom: 2rem;
        animation: titlePulse 3s ease-in-out infinite;
        font-family: 'Dancing Script', cursive;
        font-weight: 700;
    }

    @keyframes titlePulse {
        0%, 100% { transform: scale(1) rotate(0deg); }
        25% { transform: scale(1.05) rotate(1deg); }
        50% { transform: scale(1.1) rotate(0deg); }
        75% { transform: scale(1.05) rotate(-1deg); }
    }

    .heart {
        color: #ff1744;
        font-size: 2.5rem;
        animation: heartbeat 1.8s ease-in-out infinite;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    @keyframes heartbeat {
        0% { transform: scale(1) rotate(0deg); }
        14% { transform: scale(1.4) rotate(5deg); }
        28% { transform: scale(1) rotate(-2deg); }
        42% { transform: scale(1.4) rotate(3deg); }
        70% { transform: scale(1) rotate(0deg); }
    }

    .wish-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(255, 255, 255, 0.85));
        border-radius: 25px;
        padding: 2.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 15px 35px rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(8px);
        border: 2px solid rgba(255, 255, 255, 0.25);
        position: relative;
        overflow: hidden;
    }

    .wish-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        animation: shimmer 3s infinite;
    }

    @keyframes shimmer {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    }

    .countdown-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 1.5rem 0;
        box-shadow: 0 10px 30px rgba(118, 75, 162, 0.3);
        animation: countdownGlow 2s ease-in-out infinite alternate;
    }

    @keyframes countdownGlow {
        from { box-shadow: 0 10px 30px rgba(118, 75, 162, 0.3); }
        to { box-shadow: 0 15px 40px rgba(118, 75, 162, 0.6); }
    }

    .memory-card {
        background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 50%, #fd79a8 100%);
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        animation: cardFloat 4s ease-in-out infinite;
    }

    @keyframes cardFloat {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        25% { transform: translateY(-5px) rotate(0.5deg); }
        50% { transform: translateY(-10px) rotate(0deg); }
        75% { transform: translateY(-5px) rotate(-0.5deg); }
    }

    .stButton > button {
        background: linear-gradient(45deg, #ff6b9d, #c44569, #ff6b9d);
        background-size: 200% 200%;
        color: white;
        border: none;
        border-radius: 30px;
        padding: 1rem 2.5rem;
        font-size: 1.2rem;
        font-weight: bold;
        transition: all 0.4s ease;
        box-shadow: 0 5px 15px rgba(255, 107, 157, 0.3);
        animation: buttonGradient 3s ease infinite;
    }

    @keyframes buttonGradient {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }

    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 25px rgba(255, 107, 157, 0.5);
    }

    .balloon-animation {
        animation: balloonFloat 4s ease-in-out infinite;
        font-size: 5rem;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.2);
    }

    @keyframes balloonFloat {
        0%, 100% { transform: translateY(0px) rotate(-2deg); }
        25% { transform: translateY(-15px) rotate(1deg); }
        50% { transform: translateY(-30px) rotate(0deg); }
        75% { transform: translateY(-15px) rotate(-1deg); }
    }

    .sparkle {
        animation: sparkle 1.5s ease-in-out infinite;
    }

    @keyframes sparkle {
        0%, 100% { opacity: 1; transform: scale(1) rotate(0deg); }
        50% { opacity: 0.3; transform: scale(1.2) rotate(180deg); }
    }

    .love-meter {
        background: linear-gradient(90deg, #ff6b9d 0%, #ff1744 100%);
        height: 20px;
        border-radius: 10px;
        animation: lovePulse 2s ease-in-out infinite;
    }

    @keyframes lovePulse {
        0%, 100% { box-shadow: 0 0 20px rgba(255, 107, 157, 0.5); }
        50% { box-shadow: 0 0 30px rgba(255, 107, 157, 0.8); }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state with more features
if 'wishes_shown' not in st.session_state:
    st.session_state.wishes_shown = []
if 'current_wish' not in st.session_state:
    st.session_state.current_wish = 0
if 'celebration_started' not in st.session_state:
    st.session_state.celebration_started = False
if 'love_level' not in st.session_state:
    st.session_state.love_level = 100
if 'gifts_opened' not in st.session_state:
    st.session_state.gifts_opened = 0
if 'memories_shared' not in st.session_state:
    st.session_state.memories_shared = 0

# Enhanced romantic wishes
romantic_wishes = [
    "Happy 22nd Birthday to the most beautiful soul I know! 💕 Every day with you feels like a celebration of love.",
    "My dearest love, you've turned 22 and you're more radiant than ever! 🌟 Thank you for lighting up my world.",
    "22 years of your amazing existence, and I'm grateful for every heartbeat that brought you to me! 💖",
    "To my gorgeous girlfriend - you're not just a year older, you're a year more wonderful, more lovely, more perfect! 🎂✨",
    "Happy Birthday, my love! You're my favorite person, my best friend, and my greatest adventure rolled into one! 💕",
    "On your 22nd birthday, I promise to love you more intensely than the day before, every single day! 💝",
    "You light up my life brighter than all the candles on your birthday cake combined! 🕯️💕",
    "My sweet angel, you deserve all the happiness in the universe today and always! Happy 22nd Birthday! 🎈💖",
    "At 22, you're like fine wine - getting better, more beautiful, and more intoxicating with time! 🍷💕",
    "Happy Birthday to the girl who makes my heart skip beats and my soul sing with joy! 🎵💖"
]

# Enhanced love reasons
love_reasons = [
    "Your infectious laugh that makes my heart dance with joy ✨",
    "The way you scrunch your nose when you're thinking deeply 😄",
    "How you transform ordinary moments into magical memories 💫",
    "Your compassionate heart that loves everyone unconditionally ❤️",
    "The way you read my mind and heart without me saying a word 💕",
    "Your brilliant sense of humor that lights up every room 😊",
    "How you inspire me to become the best version of myself 🌟",
    "Your mesmerizing eyes that hold entire galaxies within them 👀",
    "The way your hugs heal every wound in my soul 🤗",
    "Your incredible wisdom that guides us through life's adventures 💪",
    "How you sing off-key but with such passion that it's perfect 🎵",
    "The way you believe in dreams and make them feel possible ✨",
    "Your morning hair that looks like a beautiful, adorable mess 😴",
    "How you make the simplest moments feel like fairy tales 🧚‍♀️",
    "Your determination that moves mountains and my heart 💪"
]

# Fun activities and surprises
birthday_activities = [
    "🎨 Virtual Art Gallery Tour Together",
    "🍰 Baking a Virtual Birthday Cake",
    "🌟 Stargazing from Your Window",
    "📚 Reading Love Poetry Aloud",
    "🎭 Creating Silly Dance Moves",
    "🧩 Solving Puzzles Together",
    "🎪 Having an Indoor Picnic",
    "🎬 Planning Our Dream Movie Marathon"
]

# Header with enhanced animation
st.markdown('<h1 class="love-header">💕 Happy 22nd Birthday My Extraordinary Love! 💕</h1>', unsafe_allow_html=True)
# Animated sparkles row
sparkle_cols = st.columns(7)
sparkles = ["✨", "💫", "⭐", "🌟", "✨", "💫", "⭐"]
for i, col in enumerate(sparkle_cols):
    with col:
        st.markdown(f'<div class="sparkle" style="text-align: center; font-size: 1.5rem;">{sparkles[i]}</div>', unsafe_allow_html=True)

# Enhanced floating hearts
heart_cols = st.columns(9)
heart_emojis = ["💖", "💕", "💗", "💝", "💖", "💕", "💗", "💝", "💖"]
for i, col in enumerate(heart_cols):
    with col:
        st.markdown(f'<div class="heart" style="animation-delay: {i*0.2}s;">💖</div>', unsafe_allow_html=True)

# Enhanced birthday countdown
today = date.today()
birthday_2025 = date(2025, 9, 29)  # Change this to actual birthday
next_birthday = date(today.year + 1, birthday_2025.month, birthday_2025.day)

if today < next_birthday:
    days_until = (next_birthday - today).days
    hours_until = (datetime.datetime.combine(next_birthday, datetime.time.min) - datetime.datetime.now()).seconds // 3600
    st.markdown(f"""
    <div class="countdown-box">
        <h2>🎂 Birthday Countdown Timer 🎂</h2>
        <h1>{days_until}</h1>
        <p>Days Until Your Next Birthday!</p>
        <p>Plus {hours_until} hours to go! ⏰</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="countdown-box">
        <h2>🎉 TODAY IS THE DAY! 🎉</h2>
        <h1>IT'S YOUR BIRTHDAY!</h1>
        <p>Let's make this the most amazing day ever! 🎂</p>
    </div>
    """, unsafe_allow_html=True)

# Love meter
st.markdown("### 💕 Love Level Meter")
st.markdown(f"""
<div style="background: #f0f0f0; border-radius: 10px; padding: 5px; margin: 10px 0;">
    <div class="love-meter" style="width: {st.session_state.love_level}%;"></div>
</div>
<p style="text-align: center; font-weight: bold;">Love Level: {st.session_state.love_level}% (INFINITE!) 💕</p>
""", unsafe_allow_html=True)

# Main content with enhanced layout
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown('<div class="wish-card">', unsafe_allow_html=True)

    # Enhanced wish button
    if st.button("💖 Generate Magical Birthday Wish! ✨"):
        st.session_state.celebration_started = True
        if st.session_state.current_wish < len(romantic_wishes):
            wish = romantic_wishes[st.session_state.current_wish]
            st.session_state.current_wish += 1
            st.balloons()
            st.success(wish)

            # Increase love level
            if st.session_state.love_level < 200:
                st.session_state.love_level += 10
        else:
            st.session_state.current_wish = 0
            st.balloons()
            st.success(romantic_wishes[0])

    # Display current wish with enhanced styling
    if st.session_state.celebration_started and st.session_state.current_wish > 0:
        current_wish_index = st.session_state.current_wish - 1
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); 
                    padding: 1.5rem; border-radius: 15px; margin: 1rem 0;
                    box-shadow: 0 5px 15px rgba(255, 154, 158, 0.3);">
            <h3 style="color: #333; text-align: center;">💕 {romantic_wishes[current_wish_index]} 💕</h3>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Enhanced love letter section
    st.markdown('<div class="wish-card">', unsafe_allow_html=True)
    st.markdown("### 💌 A Deep Love Letter From My Heart")

    love_letter = f"""
    **My Dearest, Most Precious Love,**

    Today marks **22 incredible years** of your beautiful, radiant existence on this earth, 
    and I am overwhelmed with gratitude that I get to celebrate this special day with you! 

    You are the **sunshine** that brightens my darkest mornings, the **moonlight** that guides me through 
    uncertain nights, and the **love** that fills every corner of my heart with warmth and joy. 

    Your 22 years have painted this world in more vibrant colors, brought more laughter to countless hearts, 
    and made the universe a infinitely more beautiful place just by your presence in it.

    On this special day, I want you to know that you are:
    - **Loved** beyond the capacity of words to express
    - **Cherished** more than all the stars in the sky
    - **Valued** beyond any treasure on earth
    - **Adored** with every fiber of my being

    As you step into this new year of life, I promise to:
    - Love you more fiercely with each passing day
    - Support your dreams with unwavering dedication
    - Celebrate your victories and comfort you in challenges
    - Create beautiful memories that will last lifetimes

    Here's to another year of incredible adventures together, endless laughter, 
    deeper love, and memories so beautiful they'll make angels weep with joy!

    **Happy 22nd Birthday, my incredible, amazing, beautiful girlfriend!** 💕

    *Forever and always yours,*  
    **Your Devotedly Loving Boyfriend** 💖

    *P.S. - You get more beautiful, more wonderful, and more perfect every single day!*
    """

    st.markdown(love_letter)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # Enhanced birthday cake animation
    st.markdown("""
    <div class="balloon-animation" style="text-align: center;">
        🎂
    </div>
    <p style="text-align: center; font-weight: bold; color: #ff6b9d;">Your Special Birthday Cake!</p>
    """, unsafe_allow_html=True)

    # Enhanced reasons section
    st.markdown('<div class="memory-card">', unsafe_allow_html=True)
    st.markdown("### 💕 Reasons Why I'm Crazy About You")

    if st.button("💝 Tell Me Another Sweet Reason"):
        reason = random.choice(love_reasons)
        st.markdown(f"""
        <div style="background: rgba(255, 255, 255, 0.8); padding: 1rem; 
                    border-radius: 10px; margin: 0.5rem 0; text-align: center;
                    box-shadow: 0 3px 10px rgba(0,0,0,0.1);">
            <strong>💖 {reason}</strong>
        </div>
        """, unsafe_allow_html=True)
        st.session_state.memories_shared += 1

    if st.session_state.memories_shared > 0:
        st.markdown(f"**Reasons shared:** {st.session_state.memories_shared} 💕")

    st.markdown('</div>', unsafe_allow_html=True)

    # Enhanced clock section
    st.markdown('<div class="memory-card">', unsafe_allow_html=True)
    st.markdown("### ⏰ Your Special Day Clock")

    current_time = datetime.datetime.now()
    st.markdown(f"""
    **🕐 Current Time:** {current_time.strftime('%I:%M:%S %p')}  
    **📅 Today's Date:** {current_time.strftime('%A, %B %d, %Y')}  
    **🎂 Birthday Status:** {'🎉 CELEBRATING!' if today.month == 9 and today.day == 29 else '💕 Loving You!'}
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# Enhanced interactive features section
st.markdown("---")
st.markdown("## 🎯 Magical Birthday Experiences")

# Four columns for enhanced features
feat_col1, feat_col2, feat_col3, feat_col4 = st.columns(4)

with feat_col1:
    st.markdown('<div class="wish-card">', unsafe_allow_html=True)
    st.markdown("### 🎵 Love Song Playlist")

    songs = [
        "🎵 'kanmani' by Sachin Siby",
        "💕 'Tuya Saathina' by Gulraj Singh", 
        "🌟 'Odh Tujhi' - Our Song",
       
    ]

    if st.button("🎶 Play Our Love Song"):
        song = random.choice(songs)
        st.success(f"Now Playing: {song}")
        st.balloons()
        st.markdown("🎵 *Music fills the air with love* 🎵")

    st.markdown('</div>', unsafe_allow_html=True)

with feat_col2:
    st.markdown('<div class="wish-card">', unsafe_allow_html=True)
    st.markdown("### 🎁 Surprise Gift Box")

    gifts = [
        "🌹 A Bouquet of Eternal Roses", 
        "💎 Scooter Ride", 
        "🧑‍🍳 The Cooking together ", 
        "🍫 Cheesecake Made with Love",
        "💍 The Meet That Symbolizes Our Bond",
        "📖 Our Love Story with Book",
        "🌟 Calling with Nickname"
    ]

    if st.button("🎁 Open Mystery Gift"):
        gift = random.choice(gifts)
        st.success(f"🎉 You received: {gift}")
        st.session_state.gifts_opened += 1
        if st.session_state.gifts_opened % 3 == 0:
            st.balloons()

    st.markdown(f"**Gifts opened:** {st.session_state.gifts_opened} 🎁")
    st.markdown('</div>', unsafe_allow_html=True)

with feat_col3:
    st.markdown('<div class="wish-card">', unsafe_allow_html=True)
    st.markdown("### 📸 Our Beautiful Memories")

    memories = [
        "💕 The day we first met and time stopped",
        "🌟 Our first 'I love you' ",
        "🎉 All our incredible adventures together", 
        "😊 Every laugh that created our inside jokes",
        "💖 The moment I knew you were 'the one'",
        "🌹 Our first Valentine's Day ",
        "✨ Dancing together in your living room"
    ]

    if st.button("💭 Relive Sweet Memory"):
        memory = random.choice(memories)
        st.success(f"Remembering: {memory}")
        st.markdown("*Hearts are made of memories* 💕")

    st.markdown('</div>', unsafe_allow_html=True)

with feat_col4:
    st.markdown('<div class="wish-card">', unsafe_allow_html=True)
    st.markdown("### 🎪 Birthday Activities")

    if st.button("🎲 Surprise Activity"):
        activity = random.choice(birthday_activities)
        st.success(f"Let's do: {activity}")
        st.markdown("*Adventure awaits!* ✨")

    st.markdown('</div>', unsafe_allow_html=True)

# Enhanced birthday wish form
st.markdown("---")
st.markdown('<div class="wish-card">', unsafe_allow_html=True)
st.markdown("### ✍️ Personalized Birthday Message Creator")

with st.form("enhanced_birthday_wish_form"):
    col_a, col_b = st.columns(2)

    with col_a:
        user_name = st.text_input("Your Name:", value="Your Loving Boyfriend")
        relationship = st.selectbox("Your Relationship:", 
                                  ["Boyfriend", "Partner", "Soulmate", "Best Friend", "Admirer"])

    with col_b:
        wish_type = st.selectbox("Message Type:", 
                               ["Romantic", "Funny", "Heartfelt", "Poetic", "Playful"])
        message_length = st.selectbox("Message Length:", 
                                    ["Short & Sweet", "Medium", "Long & Detailed"])

    birthday_message = st.text_area("Your Special Birthday Message:", 
                                  value="Happy 22nd Birthday, my love! You make every day feel like a celebration. Here's to another year of adventures, laughter, and endless love together! 💕",
                                  height=100)

    if st.form_submit_button("💌 Send This Love Message"):
        st.success(f"💕 Message from {user_name} ({relationship}): {birthday_message}")
        st.balloons()
        st.markdown("*Message delivered straight to the heart!* 💖")

st.markdown('</div>', unsafe_allow_html=True)

# Grand finale with enhanced effects
st.markdown("---")
st.markdown("## 🎊 The Ultimate Birthday Celebration Finale! 🎊")

finale_col1, finale_col2, finale_col3 = st.columns(3)

with finale_col1:
    if st.button("🎆 SPECTACULAR BIRTHDAY SURPRISE! 🎆"):
        st.balloons()
        time.sleep(0.3)
        st.snow()
        time.sleep(0.3)
        st.balloons()

        st.markdown("""
        ## 🎉 ULTIMATE SURPRISE CELEBRATION! 🎉

        ### 🌟 You are absolutely, incredibly, unbelievably AMAZING! 🌟

        #### 💖 Today we celebrate the most wonderful person in the universe - YOU! 💖
        """)

with finale_col2:
    if st.button("💖 LOVE EXPLOSION! 💖"):
        for i in range(3):
            st.balloons()
            time.sleep(0.2)

        st.markdown("""
        ### 💕 INFINITE LOVE ACTIVATION! 💕
        - 💝 22 years of pure awesomeness
        - 🌟 Countless beautiful memories created
        - 💖 Love that grows exponentially every day
        - 🎊 Unlimited birthdays to celebrate together!
        """)

with finale_col3:
    if st.button("🎂 BIRTHDAY MAGIC! 🎂"):
        st.snow()
        time.sleep(0.3)
        st.balloons()

        st.markdown("""
        ### ✨ MAGICAL BIRTHDAY WISHES GRANTED! ✨

        **🧚‍♀️ Your Birthday Fairy Godmother says:**  
        *"All your dreams will come true because you deserve nothing but the absolute best!"*

        **🌟 Birthday Magic Activated! 🌟**
        """)

# Enhanced sidebar
st.sidebar.markdown("## 💕 Birthday Command Center")

# Love statistics
st.sidebar.markdown("### 📊 Love Statistics")
st.sidebar.metric("Current Age", "22 years of pure wonderful! 🎉")
st.sidebar.metric("Days of Amazingness", "8,030+ and counting! ⭐")
st.sidebar.metric("Love Percentage", f"{st.session_state.love_level}% (Infinite!) 💕")
st.sidebar.metric("Wishes Generated", f"{st.session_state.current_wish} 💖")
st.sidebar.metric("Gifts Opened", f"{st.session_state.gifts_opened} 🎁")

# Enhanced controls
st.sidebar.markdown("### 🎛️ Celebration Controls")

if st.sidebar.button("🎈 Launch Love Balloons"):
    st.balloons()
    st.sidebar.success("Balloons of love released! 💕")

if st.sidebar.button("❄️ Create Birthday Magic Snow"):
    st.snow()  
    st.sidebar.success("Magical birthday snow created! ✨")

if st.sidebar.button("💖 Boost Love Level"):
    st.session_state.love_level = min(200, st.session_state.love_level + 25)
    st.sidebar.success(f"Love boosted to {st.session_state.love_level}%! 💕")
st.markdown("### 📸 Gallery of Memories")
photo_folder = 'photos'
if os.path.exists(photo_folder):
    photos = [f"{photo_folder}/{img}" for img in os.listdir(photo_folder) if img.lower().endswith(("jpg", "jpeg", "png"))]
    if photos:
        # Display images in columns for better layout
        cols = st.columns(3)
        for i, photo in enumerate(photos):
            image = Image.open(photo)
            with cols[i % 3]:
                st.image(image, caption=f"Memory: {os.path.basename(photo)}", use_column_width=True)
    else:
        st.info("No photos found in the 'photos' folder.")
else:
    st.warning("Photo folder not found. Please add photos to display here.")

st.markdown("### 🎥 Videos")
video_folder = 'videos'
if os.path.exists(video_folder):
    videos = [f"{video_folder}/{vid}" for vid in os.listdir(video_folder) if vid.lower().endswith(("mp4", "mov"))]
    if videos:
        # Display videos in columns just like photos
        cols = st.columns(2)  # 2 per row (videos need more width than photos)
        for i, video in enumerate(videos):
            with cols[i % 2]:
                st.markdown(
                    f"""
                    <video width="100%" height="250" controls>
                        <source src="{video}" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                    """,
                    unsafe_allow_html=True
                )
    else:
        st.info("No videos found in the 'videos' folder.")
else:
    st.warning("Video folder not found. Please add video files here.")

# --- Background Music Player ---
st.markdown("### 🎵 Background Music")
music_folder = 'music'
if os.path.exists(music_folder):
    music_files = [f"{music_folder}/{mus}" for mus in os.listdir(music_folder) if mus.lower().endswith(("mp3", "wav", "ogg"))]
    if music_files:
        selected_song = st.selectbox("Choose a song to play", music_files)
        audio_file = open(selected_song, "rb").read()
        st.audio(audio_file, format='audio/mp3')
    else:
        st.info("No music files found in the 'music' folder.")
else:
    st.warning("Music folder not found. Please add audio files here.")

# 

# Birthday settings
st.sidebar.markdown("### 📅 Birthday Configuration")
birthday_date = st.sidebar.date_input("Your Actual Birthday:", value=date(2002, 9, 29))
celebration_mode = st.sidebar.selectbox("Celebration Mode:", 
                                       ["Maximum Romance", "Super Fun", "Elegant & Classy", "Wild & Crazy"])

# Music controls
st.sidebar.markdown("### 🎵 Atmosphere Settings") 
mood = st.sidebar.selectbox("Birthday Mood:", 
                          ["Romantic & Dreamy", "Happy & Energetic", "Calm & Peaceful", "Exciting & Adventure"])

# Final enhanced footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); 
            padding: 2rem; border-radius: 20px; margin: 2rem 0;">
    <h2 style="color: #333; font-family: 'Dancing Script', cursive;">💖 Made with Infinite Love & Devotion 💖</h2>
    <h3 style="color: #666;">🎂 For the Most Amazing 22-Year-Old in the Multiverse! 🎂</h3>
    <p style="color: #888; font-style: italic;">Every line of code written with love, every animation crafted with care, 
    every word chosen to make you smile! ✨</p>
    <h4 style="color: #ff6b9d;">Happy 22nd Birthday, Beautiful! You deserve the world! 🌍💕</h4>
</div>
""", unsafe_allow_html=True)

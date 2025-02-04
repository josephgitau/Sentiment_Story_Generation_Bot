import streamlit as st
import google.generativeai as genai
import os

# store api key
api_key = os.getenv("GOOGLE_API_KEY")

# Define app tabs
tab1, tab2 = st.tabs(['Sentiment Analysis', 'Story Generation'])

# get api key from user
with st.sidebar:
    # check if user has provided an api key
    if 'GOOGLE_API_KEY' in st.secrets:
        st.success("API key is already provided!")
        api_key = st.secrets['GOOGLE_API_KEY']
    else: 
        api_key = st.text_input("Enter you Google api key please: ", type='password')
        if not (api_key.startswith('AI')):
            st.warning('Please enter your API key!')
        else:
            st.success("Succesfully added API Key!")

# Model Config
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}


## Code for sentiment analysis
with tab1:
    st.write("Sentiment Analaysis using Gemini 1.5 Pro")
    st.subheader("Generate Sentiment and reasons")

    prompt = st.text_input("Enter a text that you would like analyse sentiment on: ")

    sentiment_model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    )

    chat_session = sentiment_model.start_chat(
    history=[
    {
      "role": "user",
      "parts": [
        "Story Generation Task\n\nTask: Generate a short story given initial seed text and a target length (in words or characters).\n\nInput: A text string (the story seed) and a number (the target length).  Optionally, specify the desired output unit (words or characters).\n\nOutput: A generated story based on the seed, aiming for the specified length.  The output should be one or more paragraphs of coherent text that builds upon the seed.\n\nExamples:\n\nInput:\nSeed: The Three Little Pigs Incident\nLength: 200 words\n\nOutput:\nThe Three Little Pigs Incident: A Building Inspector’s Report\n\nBy B.B. Wolf, Senior Building Inspector, Woodland District Code Enforcement Division\n\nLet me set the record straight. After twenty-seven years with the Woodland Building Department (WBD), I’ve seen every construction shortcut and code violation imaginable. But nothing—and I mean nothing—compares to the infamous Three Pigs incident of 2023. The media had a field day with it, of course. “Big Bad Wolf Terrorizes Innocent Homeowners!” Please. I enforced the International Building Code, 2021 Edition, with local woodland amendments.\n\nIt all started with an anonymous tip to our department’s compliance hotline. The caller, who I would later discover was a rather fastidious beaver from upstream, reported unauthorized construction activities in the Lower Woods district. Three new structures had appeared virtually overnight, with no posted permits, architectural drawings, and highly questionable materials. As the senior inspector for Zone 4, the case landed on my desk.  I looked over our records first, following the protocol. No building permit applications. No site plans. No structural calculations. No soil testing reports. In a designated high-wind zone with seasonal flooding concerns, this was more than just negligent—it was dangerous.  I had to act.\n\nInput:\nSeed: A lone astronaut drifted through space.\nLength: 150 characters\n\nOutput:\nA lone astronaut drifted through space.  His oxygen tanks were low, his comms dead.  Stars blurred into streaks as he tumbled, a tiny speck lost in the vast cosmic ocean.  Hope dwindled with each passing second, replaced by the cold certainty of the void.\n\n\nThe output should not have any code in them and should be a story that is well understood",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Input:\nSeed:  The old lighthouse keeper squinted at the swirling fog.\nLength: 250 words\n\n\nOutput:\n\nThe old lighthouse keeper squinted at the swirling fog. It clung to the craggy cliffs like a damp shroud, obscuring the treacherous rocks below.  The foghorn’s mournful bellow echoed across the churning sea, a lonely sound swallowed by the grey expanse. He’d seen countless storms lash against this lonely outpost, but tonight, a different kind of unease gnawed at him.  The rhythmic pulse of the light, a beacon in the darkness for generations, seemed weaker, almost hesitant.\n\nHe checked the oil levels, the pressure gauge, the intricate workings of the ancient mechanism, but everything appeared normal.  Still, the disquiet remained. He climbed the winding stairs to the lamp room, the cold metal handrail slick beneath his calloused fingers.  As he reached the top, a gust of wind rattled the glass panes, and the fog momentarily parted, revealing a fleeting glimpse of the sea below.  And then he saw it.\n\nA small, dark shape, bobbing gently amidst the waves.  It was too far to distinguish details, but it seemed… unnatural.  The fog closed in again, swallowing the shape and leaving the lighthouse keeper in an oppressive silence, punctuated only by the relentless beat of his own heart.  He gripped the railing, his knuckles white, a cold dread seeping into his bones.  This fog held more than just moisture tonight.  It held a secret, and he had a feeling he was about to find out what it was.\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "once upon 5000 words",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Once upon a time, in the shimmering kingdom of Aethelgard, where magic wove through the very air and the rivers flowed with liquid moonlight, lived a young woman named Elara.  She wasn't a princess, nor a sorceress, nor even particularly remarkable in any way, save for one peculiar trait: she possessed an extraordinary sense of smell.  She could discern the faintest whisper of lilac from a league away, identify the precise age of a vintage wine by its bouquet alone, and even track a lost puppy through a bustling marketplace by its unique scent signature.\n\nElara lived a simple life in the village of Silverstream, nestled at the foot of the Whispering Mountains.  She worked in her family's bakery, filling the air each morning with the warm aroma of freshly baked bread, cinnamon rolls, and her specialty, moonberry tarts, a delicate confection infused with the luminescent berries that grew only on the highest peaks of the mountains.\n\nOne crisp autumn morning, as Elara was arranging her pastries in the shop window, a royal carriage, resplendent in gold and drawn by four magnificent white steeds, clattered to a halt outside.  A herald, adorned in crimson and gold livery, emerged and announced in a booming voice, \"By order of His Royal Majesty, King Theron, all citizens of Silverstream are summoned to the castle this evening for a grand feast!\"\n\nA ripple of excitement, mixed with apprehension, ran through the village. King Theron was known for his lavish celebrations, but this unexpected summons felt… different.  Elara, like the rest of the villagers, felt a prickle of unease beneath the surface of the festive anticipation.\n\nThat evening, Silverstream’s residents, dressed in their finest attire, made their way to the grand castle that loomed over the valley.  Elara, in a simple gown of spun moonlight silk, entered the vast hall, the air thick with the mingled scents of perfume, roasted meats, and a strange, underlying aroma that she couldn't quite place.  It was subtle, almost imperceptible, but to Elara's sensitive nose, it was a discordant note in the symphony of smells.\n\nKing Theron, a tall, imposing figure with a hawk-like gaze, addressed his subjects. He spoke of prosperity and unity, but his words felt hollow to Elara. The strange scent, which she now identified as a rare, exotic orchid known as the \"Nightwhisper,\" grew stronger.  This orchid was rumored to possess mind-altering properties, and its presence in the castle filled Elara with a growing sense of dread.\n\nDuring the feast, a beautiful woman with raven hair and piercing emerald eyes appeared at the king's side.  She introduced herself as Lady Nightshade, the king’s new advisor.  Elara recognized the Nightwhisper orchid’s scent clinging to Lady Nightshade’s clothes, thick and cloying, confirming her suspicions.\n\nOver the following days, a subtle change swept over Aethelgard. The king, once known for his wisdom and fairness, became withdrawn and secretive.  His decrees grew increasingly erratic, favoring Lady Nightshade and her associates while burdening the common folk. Elara noticed that the Nightwhisper’s aroma permeated the castle, the town square, even the very air itself.  The villagers, though seemingly oblivious to the scent, became listless and compliant, their vibrant spirits dulled.\n\nDriven by a growing certainty that Lady Nightshade was using the Nightwhisper orchid to control the king and the kingdom, Elara decided to act.  She knew she had to find a way to break the orchid’s hold, but how?  She sought the wisdom of the village elder, a wizened woman named Maeve who possessed a vast knowledge of herbs and lore.\n\nMaeve listened intently to Elara's concerns, her ancient eyes twinkling with understanding. \"The Nightwhisper is a powerful bloom indeed,\" she said, \"its fragrance can ensnare the mind and bend the will.  But there is one thing that can counteract its influence: the Sunstone, a gem said to hold the very essence of sunlight.\"\n\nMaeve told Elara that the Sunstone was hidden deep within the Whispering Mountains, guarded by mythical creatures and shrouded in ancient magic.  Undeterred, Elara embarked on her perilous quest.  She used her extraordinary sense of smell to navigate the treacherous mountain paths, avoiding dangerous predators and finding hidden trails known only to the mountain folk.\n\nHer journey was fraught with peril. She encountered mischievous sprites who tried to lead her astray with illusions of sweet-smelling flowers, and faced a grumpy mountain troll who demanded riddles in exchange for safe passage.  But Elara persevered, driven by her determination to save her kingdom.\n\nFinally, after days of relentless searching, she reached the Sunstone’s hidden chamber.  The gem, radiating a warm, golden light, pulsed with an energy that seemed to sing to her very soul.  As she reached for it, a shadowy figure emerged from the darkness. It was Lady Nightshade, her eyes burning with a malevolent green light.\n\n“You meddling little baker!” Lady Nightshade hissed.  “You cannot stop me!  The king, the kingdom, all will be mine!”\n\nA fierce battle ensued.  Lady Nightshade, wielding dark magic, conjured illusions of venomous snakes and snarling wolves, but Elara, armed with her wit and her extraordinary sense of smell, was able to discern the illusions from reality.  She used the mountain’s natural scents to her advantage, throwing handfuls of pungent herbs to disrupt Lady Nightshade’s magic and create openings for attack.\n\nFinally, with a swift move, Elara seized the Sunstone.  As its warmth filled her hand, a wave of pure sunlight erupted from the gem, engulfing Lady Nightshade and shattering her illusions.  The Nightwhisper’s cloying scent dissipated, replaced by the fresh, invigorating aroma of pine and mountain air.\n\nReturning to the castle, Elara presented the Sunstone to King Theron.  As the sunlight touched him, the king blinked, as if awakening from a deep sleep.  He looked around, his gaze clear and sharp once more.  He remembered nothing of Lady Nightshade or his strange decrees.  The Nightwhisper’s hold was broken.\n\nLady Nightshade, stripped of her power, fled the kingdom, never to be seen again.  Aethelgard rejoiced, its people freed from the orchid’s insidious influence. King Theron, grateful for Elara's bravery and resourcefulness, rewarded her handsomely, but the true reward for Elara was the knowledge that she had saved her kingdom, not with magic or might, but with her extraordinary sense of smell.  And so, in the shimmering kingdom of Aethelgard, the simple baker girl became a legend, her story whispered on the wind, a testament to the power of even the most unassuming of gifts.\n",
      ],
        },
        ]
    )

    generate_sentiment = st.button("Generate Sentiment", key="generate_sentiment")
    if generate_sentiment and prompt:
        with st.spinner("Generating Sentiment results..."):
            response = chat_session.send_message(prompt)
            st.write(response)
        
    

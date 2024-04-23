# -*- coding: utf-8 -*-
"""AzerExplore.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mX4qEXKzJqr6dYI0MVGVdvyZqyyVGvUN
"""





# Install transformers from source - only needed for versions <= v4.34
!pip install git+https://github.com/huggingface/transformers.git
!pip install accelerate

import torch
from transformers import pipeline

pipe = pipeline("text-generation", model="HuggingFaceH4/zephyr-7b-beta", torch_dtype=torch.bfloat16, device_map="auto")

# We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating

messages_Guba = [
    {
        "role": "Tourist guide",
        "content": "Provide 3 options for different activities in popular places of the city for tourist ",
    },
    {"role": "user", "content": "I want to spend 1 day in Guba, Azerbaijan."},
]
prompt = pipe.tokenizer.apply_chat_template(messages_Guba, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=1024, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])

messages_Guba_3 = [
    {
        "role": "Tourist guide",
        "content": "Provide 3 options for different activities in popular places of the city for tourist ",
    },
    {"role": "user", "content": "I want to spend 3 days in Guba, Azerbaijan."},
]
prompt = pipe.tokenizer.apply_chat_template(messages_Guba, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=1024, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])

messages_Guba_week = [
    {
        "role": "Tourist guide",
        "content": "Provide 3 options for different activities in popular places of the city for tourist ",
    },
    {"role": "user", "content": "I want to spend a week in Guba, Azerbaijan."},
]
prompt = pipe.tokenizer.apply_chat_template(messages_Guba_week, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=1024, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])

messages_Baku_3 = [
    {
        "role": "Tourist guide",
        "content": "Provide 3 options for different activities in popular places of the city for tourist ",
    },
    {"role": "user", "content": "I want to spend 3 days in Baku, Azerbaijan."},
]
prompt = pipe.tokenizer.apply_chat_template(messages_Baku_3, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=1024, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])

messages_Baku_1 = [
    {
        "role": "Tourist guide",
        "content": "Provide 3 options for different activities in popular places of the city for tourist ",
    },
    {"role": "user", "content": "I want to spend 1 days in Baku, Azerbaijan."},
]
prompt = pipe.tokenizer.apply_chat_template(messages_Baku_1, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=1024, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])

messages_Baku_week = [
    {
        "role": "Tourist guide",
        "content": "Provide 3 options for different activities in popular places of the city for tourist ",
    },
    {"role": "user", "content": "I want to spend a week in Baku, Azerbaijan."},
]
prompt = pipe.tokenizer.apply_chat_template(messages_Baku_week, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=1024, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])

messages_Shaki_week = [
    {
        "role": "Tourist guide",
        "content": "Provide 3 options for different activities in popular places of the city for tourist ",
    },
    {"role": "user", "content": "I want to spend a week in Shaki, Azerbaijan."},
]
prompt = pipe.tokenizer.apply_chat_template(messages_Shaki_week, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=1024, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])





messages_Shaki_3 = [
    {
        "role": "Tourist guide",
        "content": "Provide 3 options for different activities in popular places of the city for tourist ",
    },
    {"role": "user", "content": "I want to spend 3 days in Shaki, Azerbaijan."},
]
prompt = pipe.tokenizer.apply_chat_template(messages_Shaki_3, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=1024, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])

# prompt: make a streamlit app to suggest an activity plan in Shaki(for tourists)

import streamlit as st

# Define the application title and layout
st.title("Shaki Activity Planner")
st.write("This application suggests an activity plan for tourists in Shaki, Azerbaijan.")

# Create a form to collect user input
with st.form("user_input"):
    # Get the number of days the user wants to spend in Shaki
    days = st.number_input("How many days do you want to spend in Shaki?", min_value=1, max_value=7)

    # Get the user's interests
    interests = st.multiselect("What are your interests?", ["History", "Culture", "Nature", "Food", "Shopping"])

    # Submit button
    submitted = st.form_submit_button("Submit")

# Generate the activity plan based on user input
if submitted:
    # Create a list of activities based on the user's interests
    activities = []
    if "History" in interests:
        activities.extend(["Visit the Shaki Khan's Palace", "Explore the Old City"])
    if "Culture" in interests:
        activities.extend(["Visit the Shaki Regional Museum", "Attend a traditional music concert"])
    if "Nature" in interests:
        activities.extend(["Hike in the Shaki Mountains", "Visit the Shaki Waterfall"])
    if "Food" in interests:
        activities.extend(["Try traditional Azerbaijani cuisine", "Visit a local market"])
    if "Shopping" in interests:
        activities.extend(["Shop for souvenirs in the Old City", "Visit a local bazaar"])

    # Create a list of suggested itineraries based on the number of days the user wants to spend in Shaki
    itineraries = []
    if days == 1:
        itineraries.append(["Visit the Shaki Khan's Palace", "Explore the Old City", "Try traditional Azerbaijani cuisine"])
    elif days == 3:
        itineraries.append(["Day 1: Visit the Shaki Khan's Palace and explore the Old City", "Day 2: Hike in the Shaki Mountains and visit the Shaki Waterfall", "Day 3: Visit the Shaki Regional Museum and attend a traditional music concert"])
    elif days == 7:
        itineraries.append(["Day 1: Visit the Shaki Khan's Palace and explore the Old City", "Day 2: Hike in the Shaki Mountains and visit the Shaki Waterfall", "Day 3: Visit the Shaki Regional Museum and attend a traditional music concert", "Day 4: Shop for souvenirs in the Old City and visit a local bazaar", "Day 5: Try traditional Azerbaijani cuisine and visit a local market", "Day 6: Relax and enjoy the atmosphere of Shaki", "Day 7: Depart from Shaki"])

    # Display the suggested itineraries to the user
    st.write("Here are some suggested itineraries for your trip to Shaki:")
    for itinerary in itineraries:
        st.write("- " + "\n- ".join(itinerary))



messages_Karabakh = [
    {
        "role": "Tourist guide",
        "content": "Provide 3 options for different activities in popular places of the city for tourist in 2024 ",
    },
    {"role": "user", "content": "I want to spend 1 day in Karabakh, Azerbaijan."},
]
prompt = pipe.tokenizer.apply_chat_template(messages_Karabakh, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=1024, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])

messages = [
    {
        "role": "Storyteller",
        "content": "Provide 1 interesting story and 1 proverb ",
    },
    {"role": "user", "content": "I want to know about Nakchivan."},
]
prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=1024, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])

messages_Karabakh_week = [
    {
        "role": "Tourist guide",
        "content": "Provide 3 options for different activities in popular places of the city for tourist ",
    },
    {"role": "user", "content": "I want to spend a week in Karabakh, Azerbaijan."},
]
prompt = pipe.tokenizer.apply_chat_template(messages_Karabakh_week, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=1024, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])

messages_Karabakh_3 = [
    {
        "role": "Tourist guide",
        "content": "Provide 3 options for different activities in popular places of the city for tourist ",
    },
    {"role": "user", "content": "I want to spend 3 days in Karabakh, Azerbaijan."},
]
prompt = pipe.tokenizer.apply_chat_template(messages_Karabakh_3, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=1024, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])

messages_Nakchivan_3 = [
    {
        "role": "Tourist guide",
        "content": "Provide 3 options for different activities in popular places of the city for tourist ",
    },
    {"role": "user", "content": "I want to spend 3 days in Nakchivan, Azerbaijan."},
]
prompt = pipe.tokenizer.apply_chat_template(messages_Nakchivan_3, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=1024, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])

messages_Nakchivan = [
    {
        "role": "Tourist guide",
        "content": "Provide 3 options for different activities in popular places of the city for tourist ",
    },
    {"role": "user", "content": "I want to spend 1 day in Nakchivan, Azerbaijan."},
]
prompt = pipe.tokenizer.apply_chat_template(messages_Nakchivan, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=1024, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])

messages_Nakchivan_week = [
    {
        "role": "Tourist guide",
        "content": "Provide 3 options for different activities in popular places of the city for tourist ",
    },
    {"role": "user", "content": "I want to spend a week in Nakchivan, Azerbaijan."},
]
prompt = pipe.tokenizer.apply_chat_template(messages_Nakchivan_week, tokenize=False, add_generation_prompt=True)
outputs_Nw = pipe(prompt, max_new_tokens=1024, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs_Nw[0]["generated_text"])

data_Shaki = '''Shaki, an ancient Azerbaijani town featuring a majestic landscape of flora and fauna framed by towering snow-capped peaks, has rich cultural and historical heritage.\n\nAccording to historians, Shaki was founded almost 2,700 years ago and it has experienced ups and downs associated with repeated occupation by stronger nations and empires. Its golden years were during the Shaki Khanate."

Shaki's long and tumultuous history has contributed to the emergence of numerous archaeological and historical sites that can be found there today. It had been a major part of the Silk Road during the ancient times and one of its most famous destinations was the beautiful Caravansarai, which was used as a "hotel" for traders. Today, it is still used as a hotel for travelers.

Shaki, which is located 305 km from the capital Baku, is an attractive place for people with its stone-paved streets, caravanserais, ancient shrines, and hospitality of local residents.

This is the unchanged feature of Shaki from time memorial. Shaki, located at the foot of mountains, is split by Dayirmanarkhi and Gurjana rivers into the northern and southern parts. Alexander Dumas, Thor Heyerdahl and other well-known personalities narrated about the beauty of Shaki in their masterpieces.

Shaki has been one of the major cities along the Silk Road for centuries. The place also boasts the great silk factory that continuously produced silk products for over four centuries.

Every inch, every street of Shaki is ancient. Shaki is like a history museum. There are Gelersen-Gorersen fortress, Shaki Juma mosque, Omar Efendi mosque, Narin Gala and other buildings there...

The ancient Albanian church dating back to 1-2 centuries is one of Shaki's historical monuments. This shrine is considered the first church in the Caucasus. The archaeological finds there included ancient graves, material and cultural samples, and decorations. The church is now a place for Christian worshippers.

Shaki is rich in architectural monuments. The Palace of Shaki Khans is one of the most precious pearls of this place. The maples in the palace's yard are even older than the buildings there. This palace, which is embedded in the memory of tourists, is a unique site embodying the synthesis of people's and palatial architecture. What is attractive is the pictures painted with oil colors, the elegant ornaments all around the windows.

Shaki is home to a number of famous personalities. Founder of the Azerbaijani drama Mirza Fatali Akhundzade was born in Shaki. The house where he grew up is currently a museum.

Today, Shaki, which combines ancient and modern features, has new buildings, a modern park and playgrounds which attract visitors. There are modern healthcare, education, sport and cultural facilities in the town. The landscape also features a plethora of parks and museums that showcase the relics of the city's heydays. With its nearly unspoiled nature, it is a recommended destination for hiking and camping trips.

Shaki is also an industrial town, which rose to prominence with its silk. Shaki silk is famous not only in Azerbaijan but also the whole wide world.

After going through difficulties in the post-Soviet era, Shaki Silk Factory now scaled up its production. The new equipment acquired by the factory rolls out more quality products. The factory exports its products to Iran, Russia and Baltic states.

Shaki is famous for silk carpets as well. These carpets are eye-catching for being hand-made, their colors and quality. Shaki carpets, which stand out for their unique features in the Azerbaijani carpet-weaving art, are sold to local and foreign markets and are precious items in personal collections.

The first thing that comes to mind when we talk about Shaki is elegant decorated kalagayis (kerchiefs). These kalagayis, which became symbols of Shaki, draw one's attention with national ornaments and elegancy.

Shaki wines are known well not only in Azerbaijan but also far beyond.The region produces red and white wines. The products sell locally and are exported to Russia and other countries. Advanced equipment installed at the local factory enables to store products for a long time and improve their quality.

Shaki has unique and rich cuisine. Shaki people are fond of sweets. It seems like local people`s hospitality and joyfulness are associated with thier love for sweets. The smell of Shaki sweets and the popular Shaki halva can be felt all around the town.

There are halva maker shops in every corner of Shaki. Many make these sweets in their own small shops outside their homes. Some families which have made halvas for decades are known by their names. The way the Shaki halva is made is very interesting. Halva is made of rice flour, water, sugar and nuts.

Shaki is famous for its piti. They say that you can hurt Shaki people if you do not taste it. The way of making piti there is peculiar. Piti is made in faience pots. The dish includes peas, lamb, salt, water and onions.

Shaki is also an attractive destination for tourists. Tourists come here throughout the year. Shaki offers modern hotels and resorts. Prices for bungalows and hotel rooms range between 60 and 120 manats.

Ashagi and Yukhari caravanserais built in the 18th century are an exotic place for tourists. It is easy to escape summer heat and city noise there. Yukhari Caravanserai is used as a hotel, which charges 30-80 manats per day.

Shaki is home to a number of ancient arts. There are tinners, potters, hatters and musical instrument makers there.

Shebeke ornament is one of the ancient arts in Shaki and it famed Shaki around the world.

Shebeke takes approximately one to two months. Some shebeke ornaments may take as long as six months to make.

There are some shebeke ornaments in which 15,000 colored items of glass were used.

Shaki is a place where mugham (national folk music) and musical festivals take place. The events held there make Azerbaijan known as a cultural center.

Ancient history, rich cultural heritage, amazing architecture, and colorful art have made Shaki a unique place in Azerbaijan and the world. The present-day modernity has made Shaki even more beautiful as it brought about novelties. Shaki is a town combining the ancient and modern time periods.

Shaki is a land of fairy tales which has boasted its wonderful, witty and easygoing people for 2,700 years. Shaki, which is a cradle of art and culture of Azerbaijan, is currently developing as a result of the government`s firm economic policy.'''

data_Guba='''1. What the weather is like in Guba?
If you're headed north from the beautiful capital towards The Greater Caucasus mountains, at one point you'll come across the Guba District. This truly magical spot is situated more than 600 meters above the sea level, nearby the hills of the Shahdag mountains. Overall, it is comfortable for travelling all around the year. It has temperate continental climate, which allows a nice enjoyable temperature at all times.

Winters are semi-warm with occasional snow days and rains. It can draw away those, who prefer big temperature drops and heavy snowfalls, but the solution is travelling a bit more towards the mountains, to the city of Gusar or the Shahdag mountain, where you can experience the true winter fairytale. The summers on the bright side are not exhaustingly hot, the temperature varying from 17°C to 25 °C.

Arguably, the best time of the year to visit Guba would be either early autumn or the gap between the mid-spring and early summer. Those months can almost guarantee you a good weather full of sunshine and blooming nature around you. Temperatures during these periods nearly drop below 20°C or go above 25°C.

2. Historical heritage of the region
Guba district has been lived in for centuries and centuries. It tracks in the historical records, that on the territory of that region was situated a big city called Khobota during the times of the Caucasian Albania, which traces it back to the century BC.When Azerbaijan started separating into dozens of small khanates, Guba also confirmed their independency, creating their own khanate, which, sadly, was overtook later on by Tsarist Russia in the beginning of 19th century. Rich in all meanings, the city was big and well taken care of. Main percentage of population were and still are azerbaijanis, lezgis and jews. 1. Khinalug village

One of the most breath-taking, must-see spots you can come across in Azerbaijan. It not only holds a historically important meaning as a very ancient human settlement, but Khinalug is considered the highest inhabited settlement in Europe. Situated at the impressive height of 2350 meters above sea level, the village is strategically tucked away between the mountain slopes of the Greater Caucasus. Another captivating aspect of this place, besides the astonishing beauty of its landscapes, is the cultural difference of locals compared to the rest of Azerbaijan. They have their own unique set of rules, traditions, customs. The people of Khinalug have been doing the amazing job of saving their own language for more than 4 thousand years, as well as traditional crafts and folklore. (https://ati.az/blog/khinalug)

2. Juma mosque

Juma mosque is one of the oldest constructions, that are still in use in Guba. The building of it started back in 1792, but it took over 10 years to finish it, so officially it only started functioning as a mosque in 1802. From the decorum and the look of the mosque, it is evident that the architect, a local named Gazi Ismayil was a big professional.

Sadly, as Azerbaijan joined the USSR, the religion faced a lot of pressing coming from the government, therefore in 1933 its madrasah and minaret were destroyed, but the quick thinking of the city's people is what saved the mosque itself. Knowing that the place is soon to be demolished, they started collecting bags of flour inside the building, making it some sort of a stock. Juma mosque has only restored its name after Azerbaijan gained back its independency and now, after so many years and hardships, its functioning as a mosque again.

3. Krasnaya Sloboda Village (Red Village)

Another extremely important in cultural and historical meanings village. Situated right near the main Guba city, it yet couldn't be more different. Krasnaya Sloboda is considered to be the last standing shelter for jews settlement in Azerbaijan. It is quite recognizable, even from afar by the red paint spattered all across the rooftops of the houses. The people of red village usually keep to themselves, holding on to their culture, dialect and traditions. Also, it was homeland for a lot of famous people of Azerbaijan, who were not forgetting their roots, putting in work to better the living conditions of villagers.

4. Chirag gala

Constructed in 5th century, Chirag gala is still an impressive historical monument. Its remains are in the good condition, the huge silhouette of it towering above the lush greenery of Guba Forest. Situated on the huge mountain rock, it started off as a lookout point, basically unreachable and unbeatable. In translation, "chirag" means lamp, which explains the story behind the fortress perfectly, as the country's army's soldiers were warning each other by lightning torches, if the enemy comes close to the castle.

5. Gudialchay Bridge

One of the seven bridges built on the territory of Guba district back in 17 to 19th centuries, but also is considered the last one surviving. The bridge has taken its name from the river, that it helps cross - Gudial. Built in 1894, at the time it was the longest bridge of those existing, reaching the length of 275 meters. As of now, it is the last and only arch bridge in Azerbaijan, so it is under the protection of the country as an architectural monument. Still, the Gudialchay bridge is open for people to walk, significantly easing the trip from the national Nizami Park to the village of Krasnaya Sloboda we discussed earlier. . Afurja waterfall

Afurja waterfall is the highest waterfall on the territory of Azerbaijan. It reaches over 70 meters height, coming down from the mountain Tenge’s slops. Its rapid current and beautiful landscapes around it seem to draw in tourists from every corner of the world at any given time. And it makes a lot of sense with the fascinating natural beauty this place carries. The road lies through no less mesmerizing Tengalty Canyon, that opens up the amazing views to the Greater Caucasus’ Mountain peaks.

2. Gechresh forest and Gudialchay gorge

Two beautiful natural spots, that really showcase the whole beauty this region possesses. Guba is really popular for beautiful lush forests covering the territory of those lands and a Gechresh forest is one of those evident examples. The greenery following you close every step you take. Thick enough to form a natural tunnel above the main road. The fresh air, the ice cold river running between the old trees and the ancient mountains peaking out in the horizon.

No less beautiful is the scenery unfolding before your eyes when you reach gudialchay gorge. The breathtaking beauty of the place going hand in hand with the calmness and safety this place seems to create for everyone who drives or walks through it makes the place even more magical, than possible. The river, running through the gorge fits perfectly into the landscapes, as if adding new depth to the view.

3. The Chenlibel lake

A picture-perfect mesmerizing place, that over the years also became quite popular among tourists. With its crystal clear water, beautiful landscapes and a great overview to the forests surrounding the lake and the sun setting below the horizon level, it becomes a great place to face a nice calm evening with a cup of delicious tea in hand.

In this article we tried to cover mostly everything you need to know before visiting or considering the visit to the gorgeous region of Guba. Overall, Guba district might be a perfect destination point for everyone. But its true, that even experienced travelers might face a variety of difficulties on their way while searching for the ways to explore new countries with a completely different language, set of traditions and culture, in general. We realize, how overwhelming even the best of experiences can be and we have a perfect solution for that.'''

data_Karabakh='''Karabakh is famous in Azerbaijan for its incredibly beautiful nature, ancient history and hospitable people. Liberated in 2020, large-scale reconstruction and restoration works are currently under way in the region, so it's not yet open to tourists. But here's what to look forward to:

One of the main cities is Shusha, a cradle of Azerbaijani national music and literature home to monuments such as Shusha Castle and the once exquisite Yukhari Govhar Agha Mosque. This was the birthplace of key figures in Azerbaijan’s cultural history such as the composer Uzeyir Hajibeyli, who composed the first opera in the Muslim East, and the poetess Khurshidbanu Natavan, daughter of the last Karabakh khan.

Another historic Azerbaijani town is Agdam, which was sadly completely destroyed during the conflict. Prior to this, however, it was famous for its iconic three-storey teahouse, unique Bread Museum and as the home of the Qarabag football team that in recent years has played in the Europa and Champions leagues.

This region is also synonymous with the beautiful Karabakh horse, renowned for its chestnut colour, stamina and strength. In past centuries this breed won prizes at international exhibitions and in 1956 a stallion called Zaman was gifted to British Queen Elizabeth II by the Soviet government. In 2022 President Ilham Aliyev presented the Queen with another Karabakh horse called Shohrat to mark her Platinum Jubilee, along with sculptures of a Karabakh horse named Alkhan and a Dilboz horse (another unique Azerbaijani breed) named Galkhan created by the famous Azerbaijani sculptor Faig Hajiyev.

Several historic churches relate to Caucasian Albania, an ancient Christian state existing across much of today’s Azerbaijan between about 3BC and 8AD. Constructed in the 5th-6th centuries, the Aghoghlan Monastery by the Aghoglan river in the Lachin region is one of Azerbaijan’s finest examples of Albanian architecture. It was built of solid basalt stone and features interior with stone pillars, narrow windows and a curved ceiling.

One of the most beautiful monuments of ancient Albania is the Khudaveng Monastery complex, situated on the left bank of the Terter River in the Kelbajar region. The monastery was constructed from wood, black basalt and baked brick. Its walls are decorated with illustrations and inscriptions made with oil paints, and the roof is covered with tiles.

Located in the Khojavend region, the Amaras Monastery is thought to date back to the 4th century, making this one of the world’s oldest Christian monasteries. The original church, built from white stones, was turned into a monastery in the 13th century and acquired its current appearance in the 19th century. The church is surrounded by well-preserved fortress walls housing monastic cells.

The Khudaferin bridges are two monumental arched bridges across the Aras river between Kumlak and Khudaferin villages, thought to have been built around the 12th century under the Atabeys. The larger one consisting of 15 arches was constructed so well that it’s still in working order today. Three arches are all that remains of the second, though these are still impressive. Together they played an important role in key regional power struggles in the Middle Ages, as well as in facilitating trade and cultural exchange along the Silk Road.

Near the town of Fuzuli in southwestern Azerbaijan is the Azikh Cave, one of the oldest sites of human habitation in the world: it is believed that it may have first been inhabited up to a million years ago. In 1968, Azerbaijani paleontologist Mammadali Huseinov discovered a jawbone of a Neanderthal woman dwelling in the cave between 350,000 and 400,000 years ago. The cave itself is formed from limestone, with an area of about 8,000 square metres and passageways extending up to 600 metres.'''

Karabakh_culture='''The Karabakh region is an area with more ancient history different from most regions of Azerbaijan as well as the world countries. It is Karabakh which is rich in its history, material culture monuments, rich literature, art, and music culture. The beautiful nature, climate, abundance of natural resources have had a great impact on the art of thinking and creativity of Karabakh.  The most important place in the fountain of creativity of Karabakh people belongs to folk arts which are closely related to its mode of life and daily round. It seems natural that Karabakh people’s welfare standards, aesthetic taste, national image, and identity would be seen particularly in this type of art. It’s not in vain that in the most popular museums of the world most admirable samples of folk art were met in the example of Karabakh Folk art. While looking at the rich museum  collections of the Victoria and Albert Museums of London, the Louvre Museum  of Paris, the Metropolitan Museum of Washington, Vienna, Rome, Berlin, Istanbul, Tehran, Cairo art works made by skillful Karabakh masters can be seen everywhere.

The art of nation, which is widely used in the life and daily round of the people of the region and made thanks to Karabakh people’s efforts, has a great and rich history. Kitchen utensils, weapon, and decoration specimen found in Karabakh are not only historical facts, but also valuable resource displaying the craftsmanship of the master who made them. Among the works of art made of metal there are such examples with decorations and descriptions which can deeply inform us about the custom and traditions, religious views, and even clothes of people of that period. The history, ethnographical and artistic features of Karabakh folk art is depicted on clothes. This feature is observed in the garments of certain forms and their decorations as well as art needlework and weaving. The discovery of a great number of ancient material culture samples enabled the study of the history of material culture of Karabakh. It’s not chance that this region which belongs to  Azerbaijan of the ancient and rich history arose the interest of most scientists of the world, at the same time drew the attention of adventurers who wanted to own the history of it spuriously. Every single archeological material; in other words, all large and small examples of material culture- building materials, things for home, kitchen utensils, jewelries discovered in Karabakh are embodiments of characteristic, level, and development features of ancient culture which held a special place in Karabakh people’s life in terms of their production on one hand, and engraving of different glyptic, teorephtic descriptions and decorative patterns on them on the other hand. Different paintings engraved onto the home furnishings and jewelries made of gold, bronze, and copper prove the existence of fine art in Karabakh since ancient times. The carpets woven with their beauty so far. Most of them are protected in popular museums of the world.  The region of Karabakh, which owns a rich cultural heritage, is also famous for its music and mugham.  The music of Karabakh, which enriched the music culture of Azerbaijan with its rare pearls, has the centuries-old traditions. Mughams, popular songs, dances, ashuq work have their specific place in Karabakh music art. It’s mughams which are basis of the Karabakh national music. The works of art of Karabakh representatives of literature take a specific and honorable place in Azerbaijan cultural treasure. The carpets woven in Karabakh , carpet–making schools of Azerbaijan in different periods fascinate people with their beauty so far. Most of them are protected in popular museums of the world. The origins of the art of theatre in Karabakh are connected with the people’s work, mode of life, festival and wedding traditions as well as outlook. The show elements in ceremonies, rites, and games played an important role in the formation of independent folk theatre. Karabakh folk theatre has a realistic feature and was related to the working class. The repertoire of folk theatre was small plays of ethical contents. Folk theatre played an important role in the formation of Karabakh professional theatre.  Thanks to Karabakh folk theatre, professional theatre has been formed first in Shusha, later in Aghdam since XIX century and worked effectively.  The rich iron-ore deposits of Karabakh have played an important role in the formation of blacksmith work on the base of local raw materials since ancient times. Pottery also has kept its importance so far by being one of the most ancient fields of craft production in Karabakh.  The experts ascribe the formation of this field to the Neolithic Age.  The Karabakh cuisine forms the essential part of the Azerbaijan cuisine by being notable for its specific dishes such as Karabakh kyata, Barda nani.

The results of archeological excavations showed that the ancient people who lived in Karabakh created a number of works of art through honorable creative way throughout the history, and one of them is architecture.  Karabakh fine art traditions which date back to the ancient times with its origins held artistic practice of a great many generations. Here include rock paintings in Kalabajar, Aghdam, and Lachin regions, labour tools and home things with rich decorations, the art of carpet weaving which is rare with its beauty and variety, jeweler, etc. It’s also impossible not to remember the architectural monuments distinguished with their grace and elegance- mosques, tombs, palaces, churches, temples, and glazed tile decorative patterns. All these formed the specific “geno stock”of the literary culture of Azerbaijan people and its rich cultural heritage. It was enriched with new tendencies in the middle of XIX century. The main representatives of this period were a talented artist Mir Movsum Navvab, poetess and painter Khurshudbanu Natavan and others.  The Karabakh culture has been and will be a leading and inseparable part of the Azerbaijan culture with its richness and uniqueness.'''

# prompt: generate streamlit app for tourists in Azerbaijan which suggests them a day, 3 days, weekly  activity plans.

import streamlit as st

# Define the data
day_plan =

three_day_plan = """
* Day 1: Visit the Maiden Tower, the Baku Boulevard, and enjoy a traditional Azerbaijani dinner.
* Day 2: Take a day trip to the Gobustan National Park, a UNESCO World Heritage Site that is home to ancient rock carvings and mud volcanoes.
* Day 3: Visit the Ateshgah Fire Temple, a Zoroastrian temple that is one of the most important religious sites in Azerbaijan.
"""

weekly_plan = """
* Day 1: Visit the Maiden Tower, the Baku Boulevard, and enjoy a traditional Azerbaijani dinner.
* Day 2: Take a day trip to the Gobustan National Park.
* Day 3: Visit the Ateshgah Fire Temple.
* Day 4: Take a boat trip to the Caspian Sea.
* Day 5: Visit the Heydar Aliyev Center, a cultural center that is one of the most iconic buildings in Baku.
* Day 6: Visit the Baku Museum of Modern Art.
* Day 7: Relax on the beach or go for a swim in the Caspian Sea.
"""

# Create the Streamlit app
st.title("Tourist Guide for Azerbaijan")

# Get the user input
num_days = st.selectbox("How many days will you be spending in Nakchivan?", ["1", "3", "7"])

# Display the relevant plan
if num_days == "1":
  st.write(day_plan)
elif num_days == "3":
  st.write(three_day_plan)
else:
  st.write(weekly_plan)
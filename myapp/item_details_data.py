# Real, hand-crafted details for the homepage attraction, craft, and festival cards.
# This ensures that clicking any specific card opens a dedicated page containing
# authentic details, real images, and reviews for that specific item.

ITEM_DETAILS = {
    'mahabodhi_temple': {
        'name': "Mahabodhi Temple",
        'type': "attraction",
        'category': "Spiritual & UNESCO Heritage Site",
        'location': "Gaya, Bihar",
        'image': "/static/images/section image1.jpg",
        'description': "The Mahabodhi Temple is a UNESCO World Heritage Site in Bodh Gaya, Bihar. It marks the location where Siddhartha Gautama (Lord Buddha) attained enlightenment under the Bodhi Tree around 589 BCE. The temple features a majestic 50-meter high pyramid-shaped tower, intricate carvings, and the sacred Bodhi Tree. It is the most sacred pilgrimage site for Buddhists worldwide.",
        'highlights': ["The Sacred Bodhi Tree", "Vajrasana (Diamond Throne)", "Lotus Pond", "Meditating Buddha Statues"],
        'parent_city_key': "gaya"
    },
    'anjuna_beach': {
        'name': "Anjuna Beach",
        'type': "attraction",
        'category': "Beach & Nightlife",
        'location': "North Goa, Goa",
        'image': "/static/images/anuja beach.jpg",
        'description': "Anjuna Beach is one of the most popular beaches in Goa, famous for its red-colored rocky shorelines, golden sands, and palm trees. Historically, it was the heart of the hippie culture in the 1960s and 70s. Today, it is famous for hosting the weekly Wednesday Anjuna Flea Market, vibrant beach shacks like Curlies, and its famous psytrance trance music party culture.",
        'highlights': ["Anjuna Flea Market", "Curlies Shack", "Sunset View Points", "Paragliding", "Rocky Formations"],
        'parent_city_key': "goa"
    },
    'gateway_of_india': {
        'name': "Gateway Of India",
        'type': "attraction",
        'category': "Historical Monument",
        'location': "Colaba, Mumbai, Maharashtra",
        'image': "/static/images/section image2.webp",
        'description': "The Gateway of India is an iconic arch-monument built during the early 20th century in Mumbai, Maharashtra. Erected to commemorate the landing of King George V and Queen Mary at Apollo Bunder in 1911, the structure blends Hindu and Muslim architectural styles (Indo-Saracenic). Overlooking the Arabian Sea, it serves as a starting point for ferries to the Elephanta Caves and is the city's most visited landmark.",
        'highlights': ["Indo-Saracenic Archway", "Arabian Sea Views", "Yacht Trips", "Taj Mahal Palace Hotel Backdrop"],
        'parent_city_key': "mumbai"
    },
    'naida_caves': {
        'name': "Naida Caves",
        'type': "attraction",
        'category': "Natural Wonder & Heritage",
        'location': "Diu, Dadra & Nagar Haveli and Daman & Diu",
        'image': "/static/images/section image3.jpg",
        'description': "Naida Caves are a spectacular network of interlinked rock-cut stone caves located near the Diu Fort. Known for their unique geological structures, the caves were carved out by the Portuguese for building stone. Sunlight filters through the natural openings in the cave ceiling, creating an ethereal play of light and shadows, making it a paradise for photographers and nature enthusiasts.",
        'highlights': ["Ethereal Sunlight Patterns", "Labyrinthine Paths", "Photo Opportunities", "Proximity to Diu Fort"],
        'parent_city_key': "diu"
    },
    'phulkari_embroidery': {
        'name': "Phulkari Embroidery",
        'type': "craft",
        'category': "Traditional Textile Craft",
        'location': "Punjab",
        'image': "/static/images/traditional section 1.avif",
        'description': "Phulkari (meaning flower-work) is a traditional embroidery technique from the Punjab region. It is characterized by vibrant, colorful silk threads embroidered in geometric patterns on hand-woven coarse cotton cloth (khaddar). Originally a household craft made by women for family events, Phulkari is now a global heritage craft, representing Punjabi culture and festive joy.",
        'highlights': ["Satin Stitch Embroidery", "Geometric Patterns", "Traditional Bagh Shawls", "Handcrafted Heritage"],
        'parent_city_key': "punjab"
    },
    'bastar_dhokra_art': {
        'name': "Bastar Dhokra Art",
        'type': "craft",
        'category': "Non-Ferrous Metal Casting Craft",
        'location': "Bastar, Chhattisgarh",
        'image': "/static/images/traditional section 2.avif",
        'description': "Dhokra is an ancient non-ferrous metal casting art style that uses the lost-wax casting technique. Practiced by the tribes of Bastar in Chhattisgarh for over 4,000 years, this art form dates back to the Indus Valley Civilization (such as the famous Dancing Girl of Mohenjo-daro). Dhokra artisans create beautiful metal figurines of tribal deities, animals, and decorative items.",
        'highlights': ["Lost-wax Casting Method", "Primitive Bell-metal Figurines", "Tribal Folklore Motifs", "Rustic Aesthetics"],
        'parent_city_key': "chhattisgarh"
    },
    'patan_patola_silk': {
        'name': "Patan Patola Silk",
        'type': "craft",
        'category': "Luxury Double Ikat Weaving",
        'location': "Patan, Gujarat",
        'image': "/static/images/traditional section 3.avif",
        'description': "Patan Patola is a legendary double-ikat silk sari weaving tradition originating in Patan, Gujarat. A single sari can take months or even a year to weave because both warp and weft threads are tie-dyed with absolute mathematical precision before weaving. The colors never fade and the patterns are identical on both sides. Historically worn only by royalty, it is a symbol of ultimate luxury.",
        'highlights': ["Double-ikat Weaving Technique", "Pure Silk with Natural Dyes", "Geometric Patterns", "Lifetime Color Fastness"],
        'parent_city_key': "gujarat"
    },
    'pashmina_shawls': {
        'name': "Pashmina Shawls",
        'type': "craft",
        'category': "Luxury Woolen Craft",
        'location': "Kashmir",
        'image': "/static/images/traditional section 4.avif",
        'description': "Pashmina is a luxury woolen textile crafted from the fine undercoat hair of the Changthangi goat native to the high altitudes of Ladakh. Spun and hand-woven in Kashmir, Pashmina shawls are famous worldwide for their extreme softness, lightweight feel, and warmth. Hand-embroidered Kashmiri Kani and Sozni Pashmina shawls represent centuries of exquisite craftsmanship.",
        'highlights': ["Changthangi Goat Cashmere", "Hand-spinning and Weaving", "Intricate Sozni and Kani Embroidery", "Royal Warmth"],
        'parent_city_key': "kashmir"
    },
    'blue_pottery': {
        'name': "Blue Pottery",
        'type': "craft",
        'category': "Traditional Glazed Pottery",
        'location': "Jaipur, Rajasthan",
        'image': "/static/images/jaipur image2.jpg",
        'description': "Jaipur Blue Pottery is a traditional craft known for its distinctive cobalt-blue dye and glazed finish. Unlike normal pottery, it does not use clay; instead, it is made using a paste of ground quartz, glass, multani mitti (Fuller's Earth), and gum. The craft originated in Persia and was introduced to Jaipur by Maharaja Sawai Ram Singh II in the 19th century.",
        'highlights': ["Clay-free Quartz Paste", "Cobalt-blue & Turquoise Dyes", "Hand-painted Floral Motifs", "Glossy Glaze"],
        'parent_city_key': "jaipur"
    },
    'banarasi_silk': {
        'name': "Banarasi Silk",
        'type': "craft",
        'category': "Royal Brocade Weaving",
        'location': "Varanasi, Uttar Pradesh",
        'image': "/static/images/varanasi image1.jpg",
        'description': "Banarasi saris are made in the holy city of Varanasi and are among the finest saris in India. They are famous for their gold and silver brocade or zari, fine silk, and opulent embroidery. The designs are heavily inspired by Mughal aesthetics, featuring floral foliage motifs (kalga and bel) and net-like patterns. They are a staple of Indian bridal wear.",
        'highlights': ["Gold & Silver Zari Brocades", "Pure Mulberry Silk", "Mughal Floral Motifs", "Traditional Handlooms"],
        'parent_city_key': "varanasi"
    },
    'diwali_festival': {
        'name': "Diwali Festival",
        'type': "festival",
        'category': "Live Cultural Celebration",
        'location': "Jaipur, Rajasthan",
        'image': "/static/images/festival image 1.jpg",
        'description': "Diwali, the Festival of Lights, is celebrated with unparalleled grandeur in Jaipur. The entire 'Pink City' is illuminated with millions of clay lamps (diyas), lanterns, and decorative lights. The city's famous historic gates and bazaars are decorated with unique themes, attracting tourists from across the globe. Families gather for prayers, light firecrackers, and share traditional sweets.",
        'highlights': ["Illuminated Pink City Bazaars", "Sunset Views from Nahargarh Fort", "Traditional Sweets", "Cultural Lighting Displays"],
        'parent_city_key': "jaipur"
    },
    'hornbill_festival': {
        'name': "Hornbill Festival",
        'type': "festival",
        'category': "Tribal Cultural Festival",
        'location': "Kisama near Kohima, Nagaland",
        'image': "/static/images/festival image 2.webp",
        'description': "The Hornbill Festival is a massive 10-day cultural celebration held annually in Nagaland, Northeast India. Organized by the State Tourism Department, it brings together all 17 major Naga tribes at the Kisama Heritage Village near Kohima. The festival showcases traditional Naga dances, folk songs, indigenous games, warrior attire, herbal medicines, food stalls, and the famous chili-eating competition.",
        'highlights': ["Tribal Warrior Dances", "Kisama Heritage Morungs (Huts)", "Naga Folk Music Concerts", "Local Bamboo Crafts & Cuisine"],
        'parent_city_key': "kohima"
    },
    'durga_puja': {
        'name': "Durga Puja",
        'type': "festival",
        'category': "UNESCO Intangible Cultural Heritage",
        'location': "Kolkata, West Bengal",
        'image': "/static/images/festival image 3.webp",
        'description': "Durga Puja in Kolkata is a monumental 5-day carnival celebrating the victory of Goddess Durga over the demon Mahishasura. Recognized by UNESCO as an Intangible Cultural Heritage of Humanity, it turns the entire city of Kolkata into an open-air art gallery. Massive, artistic temporary structures called 'Pandals' house beautifully sculpted clay idols of the Goddess. The air is filled with the rhythmic beats of 'Dhak' drums and the smell of festive delicacies.",
        'highlights': ["Spectacular Themed Pandals", "Clay Idol Crafting in Kumartuli", "Traditional Dhunuchi Dance", "Street Food Tours"],
        'parent_city_key': "kolkata"
    }
}

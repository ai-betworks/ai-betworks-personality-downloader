from models import MasterState

# Used in the demo notebook for one of the demo calls
eliza_generator_demo_input = {
    "public_figure": "Mark Cuban",
    "research": {
        "wikipedia_search_results": [
            '<Document source="https://en.wikipedia.org/wiki/Mark_Cuban" page=""/>\nMark Cuban (born July 31, 1958) is an American businessman and television personality. He is the former principal owner and current minority owner of the Dallas Mavericks of the National Basketball Association (NBA), co-owner of 2929 Entertainment, and was one of the main "sharks" on the ABC reality television series Shark Tank. As of December 2024, Forbes estimates his net worth to be $5.7 billion.\nBorn in Pittsburgh, Pennsylvania, Cuban was involved at a young age in ventures ranging from selling garbage bags to running newspapers during a strike. He graduated from the Kelley School of Business at Indiana University and embarked on a diverse business career that included founding MicroSolutions and Broadcast.com, both of which he sold at substantial profits. Cuban\'s investments span various industries, from technology and media to sports and entertainment. He has been a prominent figure in the NBA, known for his active involvement with the Mavericks (with which he won the 2011 NBA Championship as owner), and disputes with the league\'s management. In his side ventures, Cuban has been involved in philanthropy, political commentary, and reality television.\n\n\n== Early life and education ==\nCuban was born in Pittsburgh, Pennsylvania, on July 31, 1958. His father, Norton Cuban, was an automobile upholsterer. Cuban described his mother, Shirley (née Feldman), as someone with "a different job or different career goal every other week."\nCuban is Jewish, and grew up in Mount Lebanon, a suburb of Pittsburgh, in a working-class family. His paternal grandfather changed the surname from "Chabenisky" to "Cuban" after his family emigrated from Russia through Ellis Island. His maternal grandparents were Romanian Jewish immigrants, according to Mark\'s brother Brian, though Mark has claimed his maternal grandmother was from Lithuania.\nCuban first ventured into business at age 12. He sold garbage bags to pay for a pair of expensive sneakers. A few years later, he earned money by selling stamps and coins. At age 16, Cuban took advantage of a Pittsburgh Post-Gazette strike by running newspapers from Cleveland to Pittsburgh.\nInstead of attending high school for his senior year, he enrolled as a full-time student at the University of Pittsburgh, where he joined the Pi Lambda Phi fraternity. After one year at the University of Pittsburgh, Cuban transferred to Indiana University in Bloomington, Indiana, where he graduated from the Kelley School of Business in 1981 with a Bachelor of Science degree in management. He chose Indiana\'s Kelley School of Business without even visiting the campus because it "had the least expensive tuition of all the business schools on the top 10 list". He had various business ventures during college, including a bar, disco lessons, and a chain letter.\nAfter graduating, Cuban returned to Pittsburgh and took a job with Mellon Bank, where he immersed himself in the study of machines and networking.\n\n\n== Business career ==\nOn July 7, 1982, Cuban moved to Dallas, Texas, where he first found a job as a bartender for a Greenville Avenue bar called Elan and then as a salesperson for Your Business Software, one of the earliest PC software retailers in Dallas. He was fired less than a year later, after meeting with a client to procure new business instead of opening the store.\nCuban co-founded MicroSolutions with support from his previous customers at Your Business Software. Initially, MicroSolutions operated as a systems integrator and software reseller. The company was an early proponent of technologies such as Carbon Copy, Lotus Notes, and CompuServe. One of the company\'s largest clients was Perot Systems. The company grew to more than $30 million in revenue, and in 1990, Cuban sold MicroSolutions to CompuServe—then a subsidiary of H&R Block—for $6 million \n(over $14.7 million  today). He made approximately $2 million after taxes on the deal.\n\n\n=== Audionet and Broadcast.com ===\nIn 1995, Cuban and fellow Indiana University alumnu\n</Document>',
            '<Document source="https://en.wikipedia.org/wiki/Todd_Wagner" page=""/>\nTodd R. Wagner (born August 2, 1960) is an American entrepreneur, co-founder of Broadcast.com and founder and CEO of a company called Charity Network which organizes regular fund raisings. He also co-owns 2929 Entertainment with Mark Cuban, along with other entertainment companies.\n\n\n== Early life ==\nWagner was born in Gary, Indiana. He attended Merrillville High School and then Indiana University, joining Kappa Sigma fraternity Beta Theta chapter.\nHe graduated from Indiana University in 1983. He earned a J.D.  from University of Virginia, then moved to Dallas, Texas, where he became a licensed CPA.  He began a legal career with the national firms Akin, Gump, Strauss, Hauer & Feld and Hopkins & Sutter.\n\n\n== Career ==\n\n\n=== Broadcast.com ===\nIn 1995, Wagner launched AudioNet with Mark Cuban, a platform for broadcasting live sporting events and radio stations over the internet. As CEO, Wagner grew the company and expanded its services to include corporate events and business services.\nIn 1998 Wagner and Cuban changed the name to Broadcast.com and took the company public in the midst of the dot-com boom. The Broadcast.com IPO set an opening-day record, with shares climbing 249% from an offering price of $18 to a closing price of $62.75.\nIn 1999, Wagner and Cuban sold Broadcast.com to Yahoo! for $5.7 billion, making 300 employees millionaires (briefly, on paper) and Wagner and Cuban instant billionaires. Wagner continued to lead the division as Yahoo! Broadcast until May 2000, when he declined an offer to become Yahoo!\'s Chief Operating Officer to focus on other interests.\n\n\n=== 2929 Entertainment ===\nUsing the success of Broadcast.com, Wagner built the Wagner/Cuban Companies including 2929 Productions. Two films the company helped produce received Oscar nominations: (Good Night, and Good Luck and Enron: The Smartest Guys in the Room). Other films include Akeelah and the Bee and The Road. Good Night, directed by and co-starring George Clooney, was nominated for six Academy Awards including Best Picture.\nThrough 2929 Entertainment, Wagner and Mark Cuban have owned a group of vertically integrated entertainment properties including high-definition production company HDNet Films (produced the Academy Award–nominated documentary Enron: The Smartest Guys in the Room); distributor Magnolia Pictures (released Enron and Oscar-nominated Capturing the Friedmans); home video division Magnolia Home Entertainment; the Landmark Theatres art-house chain which was sold in 2018; and high-definition cable channels HDNet and HDNet Movies now AXS TV.\n\n\n=== Other business ventures ===\nWagner also has a stake in the Dallas Mavericks, and he continues to invest in and nurture start-ups. Additionally, Wagner and Mark Cuban were the original investors in Content Partners LLC, a company that invests in the back-end profit participations of Hollywood talent. As of 2019, Wagner remained an equity partner.\nAdditionally Wagner serves on the American Film Institute\'s Board of Trustees.\nIn June 2015, it was announced that Wagner had acquired the celebrity charitable fundraising platform Prizeo for an undisclosed sum.\nTodd’s latest project is FoodFight USA, a nationwide grassroots campaign to clean up America’s tainted food supply. In an early win, Todd\'s influence was behind the passing of the California Food Safety Act in October 2023.\n\n\n=== Charity Network ===\nIn 2014, Wagner launched Chideo, a digital platform designed to raise funds and awareness for causes by connecting fans to celebrities through exclusive video content. Over the next two years, Wagner expanded the concept through the acquisition of online sweepstakes platform Prizeo in June 2015, and online charity auction site Charitybuzz in October 2015.\nIn 2016, Wagner announced the formation of Charity Network, parent company to Charitybuzz, Prizeo and Chideo, with a mission to help charities transition from analog to digital. The company uses celebrities, technology and the media to raise awareness f\n</Document>',
        ],
        "bluesky_profile": {
            "did": "did:plc:y5xyloyy7s4a2bwfeimj7r3b",
            "handle": "mcuban.bsky.social",
            "display_name": None,
            "description": "Entrepreneur \nCostplusdrugs.com",
            "avatar_url": "https://cdn.bsky.app/img/avatar/plain/did:plc:y5xyloyy7s4a2bwfeimj7r3b/bafkreihxddlkbnblytjdbajg5qopawdfcabg5e7ppwja6zmm3lvnedzojm@jpeg",
            "followers_count": 0,
            "follows_count": 0,
            "posts_count": 0,
            "indexed_at": None,
        },
        "bluesky_posts": [
            {
                "uri": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lga3rzunp22l",
                "author_handle": "mcuban.bsky.social",
                "text": "Every morning\n\nEveryone is saying it …\n\nyoutu.be/MiyBJWfvmL8?...",
                "reply_count": 193,
                "repost_count": 1042,
                "like_count": 13182,
                "quote_count": 25,
                "embed": {
                    "record": {
                        "uri": "at://did:plc:bqfjlwiqsqpe26pfeshhragc/app.bsky.feed.post/3lg7uywq2p22q",
                        "cid": "bafyreih5h5pnrk5lyju6aezeyzvusoyx6ir7nmcrchmksjpvdovo7fpnzq",
                        "author_handle": "fishecon.bsky.social",
                        "text": "Oh wow, another bluesky surge, 10 new users per second, app is back in the top 10. Welcome all.  Be nice.",
                    },
                    "media": {
                        "uri": "https://youtu.be/MiyBJWfvmL8?si=o4I2A3xhwmw8MJSW",
                        "title": 'Keith Urban - "BLUE SKY" (Official Audio)',
                        "description": "YouTube video by Keith Urban",
                        "thumb": "https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:y5xyloyy7s4a2bwfeimj7r3b/bafkreif6tjka4cxg2nrc7omum5h3z626uefxn427hwtqe7isnydxlwdjtu@jpeg",
                    },
                },
            },
            {
                "uri": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lg7v7uys4k2r",
                "author_handle": "mcuban.bsky.social",
                "text": "Exactly why @bsky.app is so important.  Engaging on this platform is important.  As is growing this platform. \n\nWhich one of these men joins Tom Anderson and MySoace in the annals of history first ?\n\nTheir greed is our opportunity.",
                "reply_count": 722,
                "repost_count": 3073,
                "like_count": 21550,
                "quote_count": 86,
                "embed": {
                    "uri": "at://did:plc:rrsxo3q3btuw7zxtacgcls7w/app.bsky.feed.post/3lg726ujubc2q",
                    "cid": "bafyreiav35qkum54jvgpv2hjwgnivo5n62ygex7wtyl74e7wsetllyi3re",
                    "author_handle": "aaronblack.bsky.social",
                    "text": "It is not free speech when Trump aligned oligarchs have their thumbs on the algorithms of all the social media apps.",
                    "embeds": [
                        {
                            "alt": "",
                            "fullsize": "https://cdn.bsky.app/img/feed_fullsize/plain/did:plc:rrsxo3q3btuw7zxtacgcls7w/bafkreifaxeqoatd565xpirpbdhb7zz7oax2k3llu4dhgefkia6warfspx4@jpeg",
                            "thumb": "https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:rrsxo3q3btuw7zxtacgcls7w/bafkreifaxeqoatd565xpirpbdhb7zz7oax2k3llu4dhgefkia6warfspx4@jpeg",
                            "aspect_ratio": {"width": 620, "height": 413},
                        }
                    ],
                },
            },
        ],
        "bluesky_replies": [
            {
                "post": {
                    "uri": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lga6kg2kak2q",
                    "author_handle": "mcuban.bsky.social",
                    "text": 'The crypto vertical is still over there.  I oosr over there to bully "up", its where certain people spend their time \n\nand because crypto and pharmacists are still there. \n\nWe will get pharmacists here.  Then Hopefully crypto',
                    "reply_count": 4,
                    "repost_count": 0,
                    "like_count": 9,
                    "quote_count": 0,
                },
                "reply_to_parent": "at://did:plc:66beczfbbbyreeeg6iz33qib/app.bsky.feed.post/3lga45a6a522c",
                "reply_to_root": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lga3rzunp22l",
                "reply_context": [
                    {
                        "uri": "at://did:plc:66beczfbbbyreeeg6iz33qib/app.bsky.feed.post/3lga45a6a522c",
                        "author_handle": "joeyjojoejohnson.bsky.social",
                        "text": "Mark, why do you still post over there? \n\nI can understand viewing? But posting?",
                        "reply_count": 3,
                        "repost_count": 0,
                        "like_count": 10,
                        "quote_count": 0,
                    }
                ],
            },
            {
                "post": {
                    "uri": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lga6cpxr3c2q",
                    "author_handle": "mcuban.bsky.social",
                    "text": "Working on the NBA. Need their permission",
                    "reply_count": 5,
                    "repost_count": 4,
                    "like_count": 51,
                    "quote_count": 1,
                },
                "reply_to_parent": "at://did:plc:zk4o25hzsohzvjb5htadyjht/app.bsky.feed.post/3lga5bbqkwc24",
                "reply_to_root": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lga3rzunp22l",
                "reply_context": [
                    {
                        "uri": "at://did:plc:zk4o25hzsohzvjb5htadyjht/app.bsky.feed.post/3lga5bbqkwc24",
                        "author_handle": "dailyfacts.bsky.social",
                        "text": "Why are Mavericks not on Bluesky?",
                        "reply_count": 1,
                        "repost_count": 2,
                        "like_count": 7,
                        "quote_count": 0,
                    }
                ],
            },
            {
                "post": {
                    "uri": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lg7vd7su2c2r",
                    "author_handle": "mcuban.bsky.social",
                    "text": "Why can't bluesky be the platform for that content ?",
                    "reply_count": 12,
                    "repost_count": 0,
                    "like_count": 122,
                    "quote_count": 0,
                },
                "reply_to_parent": "at://did:plc:tzjk4pzmfh3nzu2zpaxqa7sx/app.bsky.feed.post/3lg7vbn5ah22u",
                "reply_to_root": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lg7v7uys4k2r",
                "reply_context": [
                    {
                        "uri": "at://did:plc:tzjk4pzmfh3nzu2zpaxqa7sx/app.bsky.feed.post/3lg7vbn5ah22u",
                        "author_handle": "steverrobbins.bsky.social",
                        "text": "Mark, we also need someone somewhere to help fund journalistic media. Just sayin’",
                        "reply_count": 5,
                        "repost_count": 1,
                        "like_count": 76,
                        "quote_count": 0,
                    }
                ],
            },
            {
                "post": {
                    "uri": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lg7bypgdlr2c",
                    "author_handle": "mcuban.bsky.social",
                    "text": "Love the comments !!!",
                    "reply_count": 4,
                    "repost_count": 1,
                    "like_count": 235,
                    "quote_count": 0,
                },
                "reply_to_parent": "at://did:plc:4adlzwqtkv4dirxjwq4c3tlm/app.bsky.feed.post/3lg7bvng4hs2t",
                "reply_to_root": "at://did:plc:4adlzwqtkv4dirxjwq4c3tlm/app.bsky.feed.post/3lg7bvng4hs2t",
                "reply_context": [
                    {
                        "uri": "at://did:plc:4adlzwqtkv4dirxjwq4c3tlm/app.bsky.feed.post/3lg7bvng4hs2t",
                        "author_handle": "skylight.social",
                        "text": "Update #9! Let’s gooo!!",
                        "reply_count": 171,
                        "repost_count": 227,
                        "like_count": 2650,
                        "quote_count": 12,
                        "embed": {
                            "alt": None,
                            "thumbnail": "https://video.bsky.app/watch/did%3Aplc%3A4adlzwqtkv4dirxjwq4c3tlm/bafkreia2i7w2octfa66xrjfzcwn2ulogfnz6p2dyo2ellagb2avlm4hdbu/thumbnail.jpg",
                            "playlist": "https://video.bsky.app/watch/did%3Aplc%3A4adlzwqtkv4dirxjwq4c3tlm/bafkreia2i7w2octfa66xrjfzcwn2ulogfnz6p2dyo2ellagb2avlm4hdbu/playlist.m3u8",
                            "aspect_ratio": {"width": 1080, "height": 1920},
                        },
                    }
                ],
            },
            {
                "post": {
                    "uri": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lg7bxuio5i2x",
                    "author_handle": "mcuban.bsky.social",
                    "text": "Get it !",
                    "reply_count": 1,
                    "repost_count": 0,
                    "like_count": 3,
                    "quote_count": 0,
                },
                "reply_to_parent": "at://did:plc:6j4laup5sr5vo6mirdk4hokm/app.bsky.feed.post/3lg6vsxt5us2n",
                "reply_to_root": "at://did:plc:6j4laup5sr5vo6mirdk4hokm/app.bsky.feed.post/3lg6vsxt5us2n",
                "reply_context": [
                    {
                        "uri": "at://did:plc:6j4laup5sr5vo6mirdk4hokm/app.bsky.feed.post/3lg6vsxt5us2n",
                        "author_handle": "shiralazar.bsky.social",
                        "text": "Throwback to a more innocent time when TikTok was filled with cringey lip sync videos and dances!",
                        "reply_count": 1,
                        "repost_count": 0,
                        "like_count": 7,
                        "quote_count": 0,
                        "embed": {
                            "alt": None,
                            "thumbnail": "https://video.bsky.app/watch/did%3Aplc%3A6j4laup5sr5vo6mirdk4hokm/bafkreifti2qepo26ngwysgeir7h26iefzc5ug7x67oho2u4umen4ew7yj4/thumbnail.jpg",
                            "playlist": "https://video.bsky.app/watch/did%3Aplc%3A6j4laup5sr5vo6mirdk4hokm/bafkreifti2qepo26ngwysgeir7h26iefzc5ug7x67oho2u4umen4ew7yj4/playlist.m3u8",
                            "aspect_ratio": {"width": 540, "height": 960},
                        },
                    }
                ],
            },
        ],
        "bluesky_reposts": [
            {
                "repost_author": {
                    "did": "did:plc:h4ynx4kdeljjrfsbpk7p5xst",
                    "handle": "costplusdrugs.com",
                    "display_name": "Mark Cuban Cost Plus Drug Company",
                    "description": None,
                    "avatar_url": "https://cdn.bsky.app/img/avatar/plain/did:plc:h4ynx4kdeljjrfsbpk7p5xst/bafkreiaieepzvpuucoohcq3hsr2voen5liee5azsiwvthdgmbbe5iycyaa@jpeg",
                },
                "reposted_post": {
                    "uri": "at://did:plc:h4ynx4kdeljjrfsbpk7p5xst/app.bsky.feed.post/3lgbk66szxs2j",
                    "author_handle": "costplusdrugs.com",
                    "text": "🎊 3 years of costplusdrugs.com! 🎉\n\nThree years of making prescription pricing what it should be: clear, fair, and for everyone. We’re grateful for the continued support that’s made this journey possible.\n\n📌 We’re not stopping here — keep an eye out for what’s next!",
                    "reply_count": 52,
                    "repost_count": 126,
                    "like_count": 1271,
                    "quote_count": 7,
                    "embed": {
                        "alt": "",
                        "fullsize": "https://cdn.bsky.app/img/feed_fullsize/plain/did:plc:h4ynx4kdeljjrfsbpk7p5xst/bafkreianck5q6qweomh3lwqjxiywthfylkila5uo53onjaxyipemuxf6fy@jpeg",
                        "thumb": "https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:h4ynx4kdeljjrfsbpk7p5xst/bafkreianck5q6qweomh3lwqjxiywthfylkila5uo53onjaxyipemuxf6fy@jpeg",
                        "aspect_ratio": {"width": 1080, "height": 1080},
                    },
                },
            },
            {
                "repost_author": {
                    "did": "did:plc:y5xyloyy7s4a2bwfeimj7r3b",
                    "handle": "mcuban.bsky.social",
                    "display_name": "Mark Cuban",
                    "description": None,
                    "avatar_url": "https://cdn.bsky.app/img/avatar/plain/did:plc:y5xyloyy7s4a2bwfeimj7r3b/bafkreihxddlkbnblytjdbajg5qopawdfcabg5e7ppwja6zmm3lvnedzojm@jpeg",
                },
                "reposted_post": {
                    "uri": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lg7v7uys4k2r",
                    "author_handle": "mcuban.bsky.social",
                    "text": "Exactly why @bsky.app is so important.  Engaging on this platform is important.  As is growing this platform. \n\nWhich one of these men joins Tom Anderson and MySoace in the annals of history first ?\n\nTheir greed is our opportunity.",
                    "reply_count": 722,
                    "repost_count": 3073,
                    "like_count": 21550,
                    "quote_count": 86,
                    "embed": {
                        "uri": "at://did:plc:rrsxo3q3btuw7zxtacgcls7w/app.bsky.feed.post/3lg726ujubc2q",
                        "cid": "bafyreiav35qkum54jvgpv2hjwgnivo5n62ygex7wtyl74e7wsetllyi3re",
                        "author_handle": "aaronblack.bsky.social",
                        "text": "It is not free speech when Trump aligned oligarchs have their thumbs on the algorithms of all the social media apps.",
                        "embeds": [
                            {
                                "alt": "",
                                "fullsize": "https://cdn.bsky.app/img/feed_fullsize/plain/did:plc:rrsxo3q3btuw7zxtacgcls7w/bafkreifaxeqoatd565xpirpbdhb7zz7oax2k3llu4dhgefkia6warfspx4@jpeg",
                                "thumb": "https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:rrsxo3q3btuw7zxtacgcls7w/bafkreifaxeqoatd565xpirpbdhb7zz7oax2k3llu4dhgefkia6warfspx4@jpeg",
                                "aspect_ratio": {"width": 620, "height": 413},
                            }
                        ],
                    },
                },
            },
            {
                "repost_author": {
                    "did": "did:plc:ytc2s54atxb6gwtrgibvqnek",
                    "handle": "raeshandalias.bsky.social",
                    "display_name": "",
                    "description": None,
                    "avatar_url": "https://cdn.bsky.app/img/avatar/plain/did:plc:ytc2s54atxb6gwtrgibvqnek/bafkreig3phlkpnnmizieik3eioub4so45nxotxu2ujhkbiug7drmtgwzo4@jpeg",
                },
                "reposted_post": {
                    "uri": "at://did:plc:ytc2s54atxb6gwtrgibvqnek/app.bsky.feed.post/3lg7krcekd22o",
                    "author_handle": "raeshandalias.bsky.social",
                    "text": "Just in case you were wondering!\nLock in!",
                    "reply_count": 314,
                    "repost_count": 2111,
                    "like_count": 9066,
                    "quote_count": 165,
                    "embed": {
                        "alt": None,
                        "thumbnail": "https://video.bsky.app/watch/did%3Aplc%3Aytc2s54atxb6gwtrgibvqnek/bafkreicyvm4hlrg7t7g55umgq2ndkmv5a6xtsucyv6nhfanx2pifqakgri/thumbnail.jpg",
                        "playlist": "https://video.bsky.app/watch/did%3Aplc%3Aytc2s54atxb6gwtrgibvqnek/bafkreicyvm4hlrg7t7g55umgq2ndkmv5a6xtsucyv6nhfanx2pifqakgri/playlist.m3u8",
                        "aspect_ratio": {"width": 720, "height": 1280},
                    },
                },
            },
        ],
    },
}
eliza_generator_demo_input2 = {
    "public_figure": "Mark Hamill",
    "research": {
        "social_search_results": '<Document href="https://blueskydirectory.com/profiles/markhamillofficial.bsky.social"/>\nMark Hamill on bsky - Profiles - Bluesky Directory Bluesky Directory Browse Profiles Starter Packs Feeds Lists Labelers Clients Metrics Migration Schedulers Utilities Coming soon Press GlossaryMoved to BlueskyRandom Product AboutSubmit Home Browse ProfilesStarter PacksFeedsListsLabelers ClientsMetricsMigrationSchedulers Coming soon PressMoved to BlueskyRandom Product Home Profiles Mark Hamill Mark Hamill @markhamillofficial.bsky.social View on bsky.app Mark Hamill 1,045,236 followers 911 following 363 posts Believe in yourself! Work hard, never give up & anything\'s possible! OR: Kick back, relax & aim low: You\'ll never be disappointed...😜 I IGNORE ALL DMs! Topics Labels Loading data... Entertainment Movies Politics Want news and updates sent to your inbox? Subscribe built by Follow @mubashariqbal.com for updates © 2024 Bluesky Directory. All rights reserved.\n</Document>\n\n---\n\n<Document href="https://bsky.app/profile/did:plc:xyddpg6usmgh2t2jgf4e37yk"/>\nMark Hamill (@markhamillofficial.bsky.social) — Bluesky @markhamillofficial.bsky.social \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c With everything so seemingly terrible these days & no sign of anything remotely hopeful in the near future, I thought you might need this photo of a baby giraffe. \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c go.bsky.app/UeYGL3a Thank you @bill-maxwell.bsky.social \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c 💙 Star Wars was the first movie I saw in a theater and I absolutely ❤️ @markhamillofficial.bsky.social Mar🐫 is in my #MEGABOOST Pack tonight! Everything stated in this post is a provable fact.\n</Document>\n\n---\n\n<Document href="https://blueskydirectory.com/profiles"/>\nBluesky Profiles - Bluesky Directory Bluesky Directory Browse Profiles Starter Packs Feeds Lists Labelers Clients Metrics Migration Schedulers Utilities Coming soon Press GlossaryMoved to BlueskyRandom Product AboutSubmit Home Browse ProfilesStarter PacksFeedsListsLabelers ClientsMetricsMigrationSchedulers PressMoved to BlueskyRandom Product Profiles Profiles A directory of Bluesky profiles organized by topics Add your profile Topics Business and Finance Personal Finance Sensitive Topics Molly Jong-Fast @mollyjongfast.bsky.social George Conway @gtconway.bsky.social The Athletic @theathletic.bsky.social Kelsey Hightower @kelseyhightower.com Anil Dash @anildash.com Wes Bos @wesbos.com Guillermo del Toro @realgdt.bsky.social Al Yankovic @alyankovic.bsky.social Aaron Rupar @atrupar.com Mark Hamill @markhamillofficial.bsky.social Mark Cuban @mcuban.bsky.social Alexandria Ocasio-Cortez @aoc.bsky.social George Takei @georgetakei.bsky.social Jay 🦋 @jay.bsky.team Mubashar “Mubs” Iqbal @mubashariqbal.com Want news and updates sent to your inbox? Follow @mubashariqbal.com for updates © 2024 Bluesky Directory.\n</Document>\n\n---\n\n<Document href="https://bsky.app/profile/markhamillofficial.bsky.social/post/3lbaznck6uk2m"/>\nMark Hamill: "Now that I\'ve fled Leon\'s site for bluer skies, I\'m sure I\'ll be called an #Ex-X, but personally, I\'ll always consider myself a #TwitterQuitter." — Bluesky Mark Hamill Now that I\'ve fled Leon\'s site for bluer skies, I\'m sure I\'ll be called an Ex-X 170.9K likes Fled-X? We know he left that place flying an X-Wing . May the Force be with you.” X-winged it Y fronter company like X Dunno I like "X Luthor" It\'s why I call it Xitter (X=sh) You joined the mass X-odus from X-crement. X-odus I like it! X = Sh I am as well Mark! Whatever you want to call it is fine; we’re just glad you’re here Mark! I\'ll always consider you Red-5\n</Document>\n\n---\n\n<Document href="https://www.msn.com/en-us/money/companies/mark-hamill-says-he-s-leaving-elon-musk-s-x-here-are-all-the-celebrities-migrating-to-bluesky/ar-AA1u2foK"/>\nMark Hamill posted on Bluesky Saturday after joining, then posted on Monday that he\'s a "TwitterQuitter," although his X account is still active and has 4.9 million followers.\n</Document>\n\n---\n\n<Document href="https://www.facebook.com/OfficialQueenpage/about/"/>\nMark Hamill Page is on Facebook. Join Facebook to connect with Mark Hamill Page and others you may know. Facebook gives people the power to share and makes the world more open and connected.\n</Document>\n\n---\n\n<Document href="https://www.facebook.com/itsmarkhamill/"/>\nIt\'s Mark Hamill. 175,817 likes · 72 talking about this. The many faces of Mark Hamill... This is a FAN PAGE dedicated to Mark\'s career!\n</Document>\n\n---\n\n<Document href="https://www.facebook.com/groups/markhamill/"/>\nMark Richard Hamill is an American actor and writer. He is known for his role as Luke Skywalker in the Star Wars film series, beginning with the original 1977 film and subsequently winning three\n</Document>\n\n---\n\n<Document href="https://www.facebook.com/groups/markhamill/members/"/>\nMark Richard Hamill is an American actor and writer. He is known for his role as Luke Skywalker in the Star Wars film series, beginning with the original 1977 film and subsequently winning three\n</Document>\n\n---\n\n<Document href="https://www.facebook.com/groups/895037268198027/"/>\nMark Richard Hamill (born September 25, 1951) is an American actor. He starred as Luke Skywalker in the Star Wars franchise, in the original and sequel trilogies.\n</Document>\n\n---\n\n<Document href="https://www.forbes.com/sites/stephenpastis/2024/11/19/mark-hamill-says-hes-leaving-elon-musks-x-here-are-all-the-celebrities-migrating-to-bluesky/"/>\n“Star Wars” actor Mark Hamill posted Monday about leaving X, formerly known as Twitter, the latest in a trend of accounts with large followings exiting the platform—often for up-and-coming alternative Bluesky—after Donald Trump’s election to a second term, arguing X promotes the far right and raising concerns about owner Elon Musk’s relationship with the president-elect. On Nov. 13, actor Ben Stiller, who is also still on Musk’s platform, posted “Hello BlueSky” to the budding platform and promoted his Bluesky account on X for his 5.3 million followers, later saying “I’m posting on BlueSky…” and “please come there too…”\n</Document>\n\n---\n\n<Document href="https://www.tiktok.com/@hamillhimself"/>\nMark Hamill (@hamillhimself) on TikTok | 7.8M Likes. 2.3M Followers. Kick back, relax & aim low: You\'ll never be disappointed...😜.Watch the latest video from Mark Hamill (@hamillhimself). ... Log in. For You. Following. Explore. LIVE. Log in to follow creators, like videos, and view comments. Log in. Suggested accounts. Create TikTok effects\n</Document>\n\n---\n\n<Document href="https://twitter.com/MarkHamill"/>\nThe latest posts from @MarkHamill\n</Document>\n\n---\n\n<Document href="https://x.com/MarkHamill"/>\nThe latest posts from @MarkHamill\n</Document>\n\n---\n\n<Document href="https://www.instagram.com/MarkHamill/"/>\n6M Followers, 449 Following, 1,877 Posts - Mark Hamill (@MarkHamill) on Instagram: "Believe in Yourself! Work Hard,Never Give Up & Anything\'s Possible! OR Kick Back, Relax & Aim low: You\'ll Never be Disappointed"\n</Document>\n\n---\n\n<Document href="https://www.instagram.com/MarkHamill/"/>\n6M Followers, 449 Following, 1,877 Posts - Mark Hamill (@MarkHamill) on Instagram: "Believe in Yourself! Work Hard,Never Give Up & Anything\'s Possible! OR Kick Back, Relax & Aim low: You\'ll Never be Disappointed" 6M Followers, 449 Following, 1,877 Posts - Mark Hamill (@MarkHamill) on Instagram: "Believe in Yourself! ... Meta Verified. English\n</Document>\n\n---\n\n<Document href="https://www.instagram.com/markhamill/reels/"/>\n6M Followers, 425 Following, 1,841 Posts - Mark Hamill (@markhamill) on Instagram: "Believe in Yourself! Work Hard,Never Give Up & Anything\'s Possible! OR Kick Back, Relax & Aim low: You\'ll Never be Disappointed" 6M Followers, 425 Following, 1,841 Posts - Mark Hamill (@markhamill) on Instagram: "Believe in Yourself! ... Meta Verified. English\n</Document>\n\n---\n\n<Document href="https://www.businessinsider.com/mark-hamill-posting-on-instagram-after-quitting-facebook-2020-1?op=1"/>\nMark Hamill Is Still Posting on Instagram After Quitting Facebook - Business Insider Best Business Credit Cards \'Star Wars\' star Mark Hamill says he quit Facebook over its stance on political ads — but he\'s still posting to Instagram, which Facebook owns "Star Wars" star Mark Hamill may have made a public show of deleting his Facebook account, but it appears he\'s having a tough time letting go of one of the company\'s other apps: Instagram. The actor announced in a tweet on Sunday that he was deleting his Facebook account in protest due to the company\'s stance on fact-checking political ads — specifically, that it won\'t —\xa0and CEO Mark Zuckerberg\'s refusal to amend the policy.\n</Document>\n\n---\n\n<Document href="https://www.facebook.com/itsmarkhamill/videos/4-million-followers-on-instagram/358357661459316/"/>\nCongratulations to Mark Hamill on 4 million followers on Instagram! If you want to follow Mark on Instagram, Twitter or Facebook, search for... | By It\'s Mark Hamill | Facebook It\'s Mark Hamill Congratulations to Mark Hamill on 4 million followers on Instagram! hey mark Hamill this is Jonny goddard you are the best luke skywalker in star wars movie from your star wars fan jonny goddard bend Oregon View more comments It\'s Mark Hamill It\'s Mark Hamill It\'s Mark Hamill It\'s Mark Hamill\'s video It\'s Mark Hamill It\'s Mark Hamill\'s video It\'s Mark Hamill It\'s Mark Hamill\'s video It\'s Mark Hamill It\'s Mark Hamill\'s video It\'s Mark Hamill It\'s Mark Hamill It\'s Mark Hamill It\'s Mark Hamill Forgot password?\n</Document>\n\n---\n\n<Document href="https://www.instagram.com/p/DDa6RzVvh0g/"/>\nmarkhamill on December 10, 2024: "Please stay safe everyone!".\n</Document>\n\n---\n\n<Document href="https://au.linkedin.com/in/hamillmark"/>\n☁️ Mark Hamill ☁️ (He/Him) 🌈\nPeople Leader | Sales Manager | LGBTQI+ advocate | Machine Learning enthusiast at Amazon Web Services (AWS)\nGreater Sydney Area, Australia\n500 connections, 6548 followers\n\n\nAbout:\nI am someone who thrives in rallying passionate people together to drive meaningful business outcomes. Having spent 10 years in sales roles across clinical diagnostics, agency recruitment, and cloud infrastructure, I transitioned to sales and people leadership role at AWS in 2022.\n\nAs a sales and people leader I:\n- lead the business, revenue, and operational performance across 3 business units in Australia\n- coach, develop, and manage a team of 12 AWS sales reps\n\nIf you’re interested in having a conversation with me, shoot me a DM.\n\nOutside of my core leadership role at AWS, I also act as a co-lead for Glamazon Asia Pacific. Glamazon is Amazon\'s LGBTQI+ affinity group\n\n\nExperience:\nSales Manager | Software, Digital, and Enterprise Growth Segments at Amazon Web Services (AWS) (https://www.linkedin.com/company/amazon-web-services/)\nJun 2022 - Present\nSydney, New South Wales, Australia\n\n\nEducation:\nHeriot-Watt University\nInternational Business Management\nJan 2007 - Jan 2011\nGrade: MSc (Hons)\nActivities and societies: N/A\n</Document>\n\n---\n\n<Document href="https://uk.linkedin.com/in/markhamill2"/>\nMark Hamill\nVP Product. Problem Solver.  Finding new ways to use AI to make me look good.\nBelfast Metropolitan Area, United Kingdom\n500 connections, 3600 followers\n\n\nAbout:\nI help product teams create customer value in tech products.  I lead with empathy, and support teams to a build (and fail) safely, using process where it helps - and removing it when it\'s a barrier.\n\nWith over 20 years of experience in product management and a decade specialising in cybersecurity, I\'ve built a career spanning vulnerability scanning, application security, penetration testing, and security awareness training. A lifelong technology enthusiast, I have coded, built computers from scratch, and worked at a range of organisations from global leaders to scrappy startups.\n\n\nExperience:\nVP of Product at MetaCompliance (https://www.linkedin.com/company/metacompliance/)\nNov 2024 - Present\nDerry, Northern Ireland, United Kingdom\n- Supporting Product and Content teams\n- Production vision & strategic planning\n- Thought leadership\n\n\nEducation:\nQueen\'s University Belfast\n2.1 BSc Hons, Computer Science\nJan 2000 - Jan 2004\nGrade: N/A\nActivities and societies: N/A\n</Document>\n\n---\n\n<Document href="https://uk.linkedin.com/in/markhamill"/>\nMark Hamill\nI love leaders and their stories. My relationships are for life. My passions are coffees, conversations and connections. YPO since too long..\nLondon, United Kingdom\nN/A connections, N/A followers\n\n\nAbout:\nMark is who entrepreneurs turn to when they need to hire talent....\n\nBy 2027 Mark is on track to have helped 1000 of the worlds most passionate entrepreneurs worldwide attract the no1 hire they will need to achieve their vision.\n\nWhy connect with Mark?\n1.Are you looking for your next Board role?\n2.Are you searching for your next CEO challenge?\n3.  Are you in need of some tactical Career Transition guidance?\n4. Are you building a Board?\n5. Are you in need of Global Executive Talent?\n6. Interested in Fractional leadership? \n\nI love talking about all of the above, just email or WhatsApp me and we can lock in a call.\n\n25 years accidentally in Executive Search. Passionate about people and their stories. Love connecting CEO’s to Board talent who can help solve their pain. Believer in building your network is the best way to find your next role.\n\n\nExperience:\nChairman & Founder at MyFractionalCEO (https://www.linkedin.com/company/myfractionalceo)\nAug 2024 - Present\nWe have powered up with an amazing CEO and Advisory Board to bring MyFractionalCEO to life. I am super excited by this global platform and look forward to impacting business globally by connecting them to best in class fractional leaders who have sat in their shoes!\n\n\nEducation:\nUniversity College Dublin\nBA Intl\nJan 1991 - Jan 1995\nGrade: N/A\nActivities and societies: N/A\n</Document>\n\n---\n\n<Document href="https://www.linkedin.com/today/author/markhamill?trk=author-info__article-link"/>\nMark Hamill | LinkedIn Join now Sign in Mark Hamill I love leaders and their stories. My relationships are for life. My passions are coffees, conversations and connections. YPO since too long.. View articles by Mark Hamill Career Transition Support July 22, 2023 8 likes Do you want to join our Virtual Board… March 26, 2020 12 likes3 comments A Lonely Transition November 17, 2019 31 likes3 comments CEO SUCCESSION FOR SMBs: TIPS TO ENSURE YOUR… 18 likes1 comment Next stop for company leaders: GenZ 10 likes3 comments Can Artificial Intelligence help your… 32 likes6 comments Privacy Policy Your California Privacy Choices Cookie Policy Copyright Policy Brand Policy Bahasa Indonesia (Indonesian) Bahasa Malaysia (Malay) 简体中文 (Chinese (Simplified)) 正體中文 (Chinese (Traditional))\n</Document>\n\n---\n\n<Document href="https://www.linkedin.com/today/author/markhamill1"/>\nMark Hamill | LinkedIn Join now Sign in Mark Hamill CEO @ ARCET Global | Recognition Programs and Solutions for Customer Experience and AI View articles by Mark Hamill Naila Al Moosawi appointed as Member of the… 12 likes4 comments 16 likes3 comments 10 likes Awards International visit Milan 2015: 10… 19 likes 16 likes1 comment Send Some Good Business Karma Your Way -… 9 likes How positive recognition can lead to long… 11 likes1 comment Quality, Standards and the link to Business… 6 likes1 comment The Perils of Missing the Boat on Business… 3 likes Privacy Policy Your California Privacy Choices Cookie Policy Copyright Policy Brand Policy Bahasa Indonesia (Indonesian) Bahasa Malaysia (Malay) 简体中文 (Chinese (Simplified)) 正體中文 (Chinese (Traditional))\n</Document>\n\n---\n\n<Document href="https://www.cultureslate.com/news/mark-hamill-has-joined-tiktok-and-it-may-not-last-that-long"/>\nMark Hamill Has Joined TikTok, And It May Not Last That Long — CultureSlate Mark Hamill Has Joined TikTok, And It May Not Last That Long Recently, Mark Hamill went on social media and informed fans of a fake TikTok account that was pretending to be him. Hamill then follows a new trend on the app by saying, “Tell me your dog is needy without telling me your dog is needy.” Then he tags the video with “#demandingdoggie” and solidifies that it is him by using the tag “#TheREALHamillHimself.” The video has gotten roughly 3.6 million views and over 841 likes as of the writing of this article. As far as I am concerned, seeing Mark Hamill make adorable videos with his dog on TikTok is one of the best things to come out of 2021 so far, and I hope we get to see even more like it.\n</Document>\n\n---\n\n<Document href="https://www.tiktok.com/@hamillhimself"/>\nMark Hamill (@hamillhimself) on TikTok | 7.8M Likes. 2.3M Followers. Kick back, relax & aim low: You\'ll never be disappointed...😜.Watch the latest video from Mark Hamill (@hamillhimself). ... Upload . Log in. For You. Following. Explore. LIVE. Log in to follow creators, like videos, and view comments. Log in. Suggested accounts. Create\n</Document>\n\n---\n\n<Document href="https://www.tiktok.com/@actormarkhamill"/>\nMark Hamill (@actormarkhamill) on TikTok | 272 Likes. 240 Followers. Believe in yourself! Work hard, never give up & anything\'s possible!Watch the latest video from Mark Hamill (@actormarkhamill).\n</Document>\n\n---\n\n<Document href="https://comicbook.com/starwars/news/star-wars-mark-hamill-shares-his-first-and-probably-last-tiktok/"/>\nStar Wars: Mark Hamill Shares His “First (and Probably Last)” TikTok - ComicBook.com Star Wars: Mark Hamill Shares His “First (and Probably Last)” TikTok Last week, beloved Star Wars legend Mark Hamill took to social media to warn of a fake TikTok […] Last week, beloved Star Wars legend Mark Hamill took to social media to warn of a fake TikTok account that was pretending to be him. he created a Twitter account teaming up with Adam Driver to find a missing dog shares fun content of other people’s dogsIn addition to joining TikTok, Hamill also recently revealed he is in Serbia is to film his upcoming movie The Machine, which he’ll be starring in alongside comedian Bert Kreischer.\n</Document>\n\n---\n\n<Document href="https://itsmarkhamill.tumblr.com/post/651016624380542976/mark-hamill-hamillhimself-is-now-on-tiktok"/>\nIt\'s Mark Hamill Likes More you might like mark hamill its mark hamill hamill himself young mark hamill golden boy handsome mark hamill\'s beard cute smile trendsetter luke skywalker star wars mark hamill it\'s mark hamill hamill himself luke skywalker the mandalorian star wars dave filoni making star wars behind the scenes mandalorian Yes, we have incredible 10.000 Likes on our Mark Hamill fanpage! youtube.com Jimmy Kimmel presents Mark Hamill in the best fake movie of the year! mark hamill marilou york mark and marilou mark hamill awards clipping photoplay male newcomer luke skywalker star wars it\'s mark hamil its-mark-hamill its-mark-hamill mark hamill star wars the force awakens luke skywalker sweet cinnamon roll too pure for this world See this in the app Show more\n</Document>\n\n---\n\n<Document href="https://www.youtube.com/watch?v=dz2UnciOIfI"/>\nMark Hamill channels Luke Skywalker and Darth Vader to surprise Star Wars fans and announce that he\'s offering a BONUS experience: attend a pre-screening of The Last Jedi and get lunch with him in\n</Document>\n\n---\n\n<Document href="https://www.youtube.com/channel/UCmkjK1BAMj5IZSiCrjyUlDQ"/>\nShare your videos with friends, family, and the world\n</Document>\n\n---\n\n<Document href="https://www.youtube.com/watch?v=DiqJe91sYpQ"/>\nMark Hamill, who played Luke Skywalker in the "Star Wars" franchise, made an appearance at the top of the White House press briefing Friday. Hamill praised President Biden\'s legislative\n</Document>\n\n---\n\n<Document href="https://www.youtube.com/watch?v=ur4J15RrAsQ"/>\nThe legend of Luke Skywalker lives on, but Mark Hamill has swapped his droids for a new mechanical companion - Roz the Robot. Off the back of DreamWorks\' Osc\n</Document>\n\n---\n\n<Document href="https://music.youtube.com/channel/UCcHwIExkG6fjj5_CsL-BC2Q"/>\nSign in  Sign in to create & share playlists, get personalized recommendations, and more. MARK HAMILL Share Playlists Playlist • MARK HAMILL • 147 views Playlist • MARK HAMILL • 151 views Playlist • MARK HAMILL • 1 view NEW REST Playlist • MARK HAMILL • 79 views Playlist • MARK HAMILL • 441 views Playlist • MARK HAMILL • 212 views Playlist • MARK HAMILL • 118 views Sleep Playlist • MARK HAMILL • 95 views Playlist • MARK HAMILL • 46 tracks hz sleep Playlist • MARK HAMILL • 46 views New recommendations If playback doesn\'t begin shortly, try restarting your device. Share Include playlist An error occurred while retrieving sharing information. Please try again later. Watch later Share\n</Document>\n\n---\n\n<Document href="https://bsky.app/profile/did:plc:xyddpg6usmgh2t2jgf4e37yk"/>\nMark Hamill (@markhamillofficial.bsky.social) — Bluesky @markhamillofficial.bsky.social \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c With everything so seemingly terrible these days & no sign of anything remotely hopeful in the near future, I thought you might need this photo of a baby giraffe. \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c go.bsky.app/UeYGL3a Thank you @bill-maxwell.bsky.social \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c \u202aMark Hamill\u202c\xa0\u202a@markhamillofficial.bsky.social\u202c 💙 Star Wars was the first movie I saw in a theater and I absolutely ❤️ @markhamillofficial.bsky.social Mar🐫 is in my #MEGABOOST Pack tonight! Everything stated in this post is a provable fact.\n</Document>\n\n---\n\n<Document href="https://www.msn.com/en-us/news/politics/mark-hamill-debuts-hilarious-list-of-donald-trump-s-best-words/ar-BB1kGJZ7"/>\nHe included a screenshot of a recent Trump post on Truth Social, which included the non-words "DISINFORMATES" and "MISINFORMATES." Here\'s some of Hamill\'s list: "Stollen" for stolen\n</Document>\n\n---\n\n<Document href="https://truthsocial.com/"/>\nTruth Social is America\'s "Big Tent" social media platform that encourages an open, free, and honest global conversation without discriminating on the basis of political ideology.\n</Document>\n\n---\n\n<Document href="https://bsky.app/profile/markhamillofficial.bsky.social/post/3ldatvtpnss2d"/>\nMark Hamill: "TONIGHT- Join me along with a FAN-tastic cast for a live radio performance of IT\'S A WONDERFUL LIFE. This rendition of the timeless holiday classic benefits the #EdAsnerFamilyCenter, a truly worthy cause!!! TONIGHT- Join me along with a FAN-tastic cast for a live radio performance of IT\'S A WONDERFUL LIFE. Sounds delightful Thank you for sharing the link 🌵🍀🐞 ▷ It\'s a Wonderful Life 2024 - A Night Benefiting Special Needs Families - Official PPV Live Stream Official PPV Live Stream: ✓ The Ed Asner Family Center ✓ Entertainment, More, Events ✓ LIVE Dec 14, 8PM ET/5PM PT ✓ Garry Marshall Theatre ✓ 4252 W Riverside Dr, Burbank, CA 91505 ✓ The Ed Asner Famil... Truly a great benefit.\n</Document>\n\n---\n\n<Document href="https://www.yahoo.com/entertainment/mark-hamill-torches-trump-over-062019054.html?soc_src=social-sh&soc_trk=fb&tsrc=fb"/>\nMark Hamill Torches Trump Over Moment He ‘Accidentally’ Told The Truth Search query Search the web Search the web New movies, TV, music Mark Hamill Torches Trump Over Moment He ‘Accidentally’ Told The Truth Yahoo is using AI to generate takeaways from this article. Donald Trump on Sunday joked that he didn’t care about his supporters ― but screen icon Mark Hamill and other critics of the former president said there was more than a little truth in the crack. Mark Hamill Strikes Back At Trump\'s Awkward Self-Own With Perfect ‘Star Wars’ Tweak Mark Hamill Has A-Plus Response To Jesse Watters’ ‘C-List’ Ding Mark Hamill Names Favorite Part Of Trump’s ‘Frequent Verbal Catastrophes’ Yahoo! Yahoo Picks © 2025 Yahoo.\n</Document>',
        "wikipedia_search_results": [
            '<Document source="https://en.wikipedia.org/wiki/Luke_Skywalker" page=""/>\nLuke Skywalker is a fictional character in the Star Wars franchise. He was introduced in the original film trilogy as the main protagonist and also appears in the sequel trilogy. Raised as a moisture farmer on the planet Tatooine, Luke joins the Rebel Alliance and becomes a pivotal figure in the struggle against the Galactic Empire. He trains as a Jedi under Obi-Wan Kenobi and Yoda, and eventually confronts his father, the Sith Lord Darth Vader. Years later, Luke trains his nephew Ben Solo and mentors the scavenger Rey. Luke is the twin brother of Leia Organa.\nMark Hamill portrays Luke in all the films of the original trilogy and the sequel trilogy, and in the television series The Mandalorian and The Book of Boba Fett. Hamill won the Saturn Award for Best Actor for his portrayal of Luke in The Empire Strikes Back (1980), Return of the Jedi (1983) and The Last Jedi (2017). He was also nominated for the award for his performance in Star Wars (1977). Luke also appears in novels, comics, and video games.\n\n\n== Creation and development ==\n\n\n=== Star Wars (1977) ===\nGeorge Lucas considered various characterizations for the protagonist of the original Star Wars film. The possibilities included a 60-year-old grizzled war hero, a Jedi Master, a dwarf, and a woman. Luke\'s original surname was "Starkiller", and it remained in the script until a few months into filming. It was dropped due to what Lucas called "unpleasant connotations" with Charles Manson, who became a "star killer" in 1969 when he murdered the well-known actress Sharon Tate. Lucas replaced the problematic name "Starkiller" with "Skywalker".\n\n\n=== Return of the Jedi (1983) ===\nAn alternate ending to the film reportedly featured Luke disappearing into the wilderness "like Clint Eastwood in the spaghetti Westerns."\n\n\n=== The Force Awakens (2015) ===\nLuke\'s lack of screen time in The Force Awakens was due to concerns by screenwriter Michael Arndt that his presence would distract from Rey, leading to an agreement that he be removed from the screen and instead become a plot device. Hamill attended meetings for script readings, and helped conceal Luke\'s role in the film; instead of dialogue, he read stage directions. According to director and co-writer J. J. Abrams, this allowed Hamill to remain involved and his reading helped make a "better experience for everyone."\n\n\n== Portrayal ==\nMark Hamill was originally cast as Luke for Star Wars (1977). Other actors who auditioned for the role include Robby Benson, William Katt, Kurt Russell, and Charles Martin Smith. Hamill was injured in a car accident in January 1977, fracturing his nose and cheekbone. Lucas justified the slight change to Hamill\'s likeness this would impose upon the sequel film, The Empire Strikes Back (1980), by asserting that in the interim between the two films, Luke had been fighting for the Rebel Alliance. It was speculated that the wampa attack at the beginning of The Empire Strikes Back was written in to explain his facial injuries, but Lucas disputed this in the DVD commentary of the film.\n\n\n== Appearances ==\n\n\n=== Original trilogy ===\n\n\n==== Star Wars ====\nLuke was introduced in Star Wars (1977), the first film of the original trilogy. He is portrayed by Mark Hamill in all three films of the trilogy. At the beginning of the film, Luke is living on a moisture farm on the desert planet Tatooine with his uncle Owen and aunt Beru. After his uncle purchases the droids C-3PO and R2-D2, Luke finds a message from Princess Leia of Alderaan inside R2-D2. When R2-D2 goes missing, Luke goes out to search for the droid, and is saved from Tusken Raiders by Obi-Wan Kenobi, an elderly hermit. R2-D2 plays the message from Leia, in which she asks Obi-Wan to help her defeat the Galactic Empire. Obi-Wan says that he and Luke\'s father were once Jedi Knights, and that Luke\'s father was murdered by a traitorous Jedi named Darth Vader. Obi-Wan presents Luke with his father\'s lightsaber and offers to take him to Alderaan and train h\n</Document>',
            '<Document source="https://en.wikipedia.org/wiki/Mark_Hamill_filmography" page=""/>\nMark Hamill is an American actor with a career spanning over fifty years in the entertainment industry. His breakout role of Luke Skywalker in the Star Wars franchise propelled him to popularity in film. To avoid being typecast, Hamill also acted in Broadway plays (mostly in the 1980s) and as a voice actor in several television series and films. The most popular among these is his portrayal of the Joker in multiple Batman films and television shows. This has led him to voice act for other supervillains in animated and live action works.\n\n\n== Live-action roles ==\n\n\n=== Films ===\n\n\n=== Television ===\n\n\n=== Video games ===\n\n\n== Voice roles ==\n\n\n=== Films ===\n\n\n=== Television ===\n\n\n=== Video games ===\n\n\n=== Applications ===\n\n\n== Stage ==\n\n\n== Audio books ==\n\n\n== See also ==\nMark Hamill awards and nominations\n\n\n== References ==\n</Document>',
        ],
        "socials": {
            "bluesky_page": "https://bsky.app/profile/markhamillofficial.bsky.social",
            "bluesky_handle": "markhamillofficial.bsky.social",
            "facebook_page": "https://www.facebook.com/itsmarkhamill",
            "facebook_username": "itsmarkhamill",
            "x_page": "https://x.com/MarkHamill",
            "x_username": "MarkHamill",
            "instagram_page": "https://www.instagram.com/MarkHamill",
            "instagram_username": "MarkHamill",
            "linkedin_page": "",
            "linkedin_username": "",
            "tiktok_page": "https://www.tiktok.com/@hamillhimself",
            "tiktok_username": "hamillhimself",
            "youtube_page": "https://www.youtube.com/channel/UCmkjK1BAMj5IZSiCrjyUlDQ",
            "youtube_username": "",
            "truth_social_page": "",
            "truth_social_username": "",
        },
        "bluesky_posts": [
            {
                "uri": "at://did:plc:xyddpg6usmgh2t2jgf4e37yk/app.bsky.feed.post/3lgq3hcfa7s2o",
                "author_handle": "markhamillofficial.bsky.social",
                "text": "Voicing Thorn the bear in DreamWorks' #TheWildRobotMovie was a joy from start to finish!  At this time, I would like to acknowledge & honor just a few of the many great cartoon bears that came before me:\n\n#YogiBear #BooBoo #WinnieThePooh #SmokeyTheBear ♥️ 🙏\n\n🐻  🐻\u200d❄️  🧸  🤖",
                "reply_count": 597,
                "repost_count": 1173,
                "like_count": 20540,
                "quote_count": 49,
                "embed": [
                    {
                        "alt": "",
                        "fullsize": "https://cdn.bsky.app/img/feed_fullsize/plain/did:plc:xyddpg6usmgh2t2jgf4e37yk/bafkreicnrdaopl274upv4ecujzn5pmwnrhanuemxup73t7fzcpxrqyasae@jpeg",
                        "thumb": "https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:xyddpg6usmgh2t2jgf4e37yk/bafkreicnrdaopl274upv4ecujzn5pmwnrhanuemxup73t7fzcpxrqyasae@jpeg",
                        "aspect_ratio": {"width": 1280, "height": 720},
                    },
                    {
                        "alt": "",
                        "fullsize": "https://cdn.bsky.app/img/feed_fullsize/plain/did:plc:xyddpg6usmgh2t2jgf4e37yk/bafkreidzxjjy5nteekiquuukydv7vgkjszgmsmck2ohyrl7z2fw645yb5m@jpeg",
                        "thumb": "https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:xyddpg6usmgh2t2jgf4e37yk/bafkreidzxjjy5nteekiquuukydv7vgkjszgmsmck2ohyrl7z2fw645yb5m@jpeg",
                        "aspect_ratio": {"width": 895, "height": 1390},
                    },
                    {
                        "alt": "",
                        "fullsize": "https://cdn.bsky.app/img/feed_fullsize/plain/did:plc:xyddpg6usmgh2t2jgf4e37yk/bafkreib3cvczfjtnq4doqibbtdp3ildkou6u2pdrtdj3t5wz5spb5l4g24@jpeg",
                        "thumb": "https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:xyddpg6usmgh2t2jgf4e37yk/bafkreib3cvczfjtnq4doqibbtdp3ildkou6u2pdrtdj3t5wz5spb5l4g24@jpeg",
                        "aspect_ratio": {"width": 320, "height": 535},
                    },
                    {
                        "alt": "",
                        "fullsize": "https://cdn.bsky.app/img/feed_fullsize/plain/did:plc:xyddpg6usmgh2t2jgf4e37yk/bafkreievr4wbziybuojvta47mbekwyeh5mraw3ahxww7f54fpxu5wrunpa@jpeg",
                        "thumb": "https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:xyddpg6usmgh2t2jgf4e37yk/bafkreievr4wbziybuojvta47mbekwyeh5mraw3ahxww7f54fpxu5wrunpa@jpeg",
                        "aspect_ratio": {"width": 1500, "height": 2000},
                    },
                ],
            },
            {
                "uri": "at://did:plc:xyddpg6usmgh2t2jgf4e37yk/app.bsky.feed.post/3lgo4yfu6lc2a",
                "author_handle": "markhamillofficial.bsky.social",
                "text": "SUNDAY'S FUNDAY QUIZ!\n\nI am in the UK to promote DreamWorks' critically-acclaimed new animated movie: THE [          ] ROBOT\n\nA) RILED\nB) CHILD\nC) REVILED\nD) MILD\nE) None of the above\n\nAnswer: E \n\nIt's actually The WILD Robot- wonderful for ALL ages & currently at 97% on Rotten Tomatoes!!!  👀 ♥️ 👍",
                "reply_count": 1538,
                "repost_count": 2337,
                "like_count": 38701,
                "quote_count": 135,
                "embed": {
                    "alt": "",
                    "fullsize": "https://cdn.bsky.app/img/feed_fullsize/plain/did:plc:xyddpg6usmgh2t2jgf4e37yk/bafkreibl45pdjzeyg3ym3b3cmpvpl3dks37xrscrydcg6qrfsv3epbmteu@jpeg",
                    "thumb": "https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:xyddpg6usmgh2t2jgf4e37yk/bafkreibl45pdjzeyg3ym3b3cmpvpl3dks37xrscrydcg6qrfsv3epbmteu@jpeg",
                    "aspect_ratio": {"width": 1500, "height": 2000},
                },
            },
            {
                "uri": "at://did:plc:xyddpg6usmgh2t2jgf4e37yk/app.bsky.feed.post/3lglljl7xuk2t",
                "author_handle": "markhamillofficial.bsky.social",
                "text": "Hello to all my Bluesky🦋 family. I'm ba-aaack! I'm in London at the moment, but will be home soon. One question for you:\n\nAnybody miss me?\n\nPlease like this post even if you didn't.\n\nThanking you in advance, Mar🐫\n\n🙏 ♥️ 👍",
                "reply_count": 5826,
                "repost_count": 4670,
                "like_count": 141977,
                "quote_count": 287,
            },
            {
                "uri": "at://did:plc:xyddpg6usmgh2t2jgf4e37yk/app.bsky.feed.post/3lg5qi4pf5222",
                "author_handle": "markhamillofficial.bsky.social",
                "text": "Justice is coming...     eventually. ⚖️\n\n#MartinLutherKingDay2025",
                "reply_count": 1779,
                "repost_count": 6325,
                "like_count": 47854,
                "quote_count": 287,
                "embed": {
                    "alt": "",
                    "fullsize": "https://cdn.bsky.app/img/feed_fullsize/plain/did:plc:xyddpg6usmgh2t2jgf4e37yk/bafkreicaip6fktlc2th6kohemz6dtuaoyi2qtpzv4qjrk62i6nexglqahu@jpeg",
                    "thumb": "https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:xyddpg6usmgh2t2jgf4e37yk/bafkreicaip6fktlc2th6kohemz6dtuaoyi2qtpzv4qjrk62i6nexglqahu@jpeg",
                    "aspect_ratio": {"width": 2000, "height": 1125},
                },
            },
            {
                "uri": "at://did:plc:xyddpg6usmgh2t2jgf4e37yk/app.bsky.feed.post/3lg4wchtjn22o",
                "author_handle": "markhamillofficial.bsky.social",
                "text": "From midnight tonight until next Saturday morning, there's no TV, no Internet, no Social Media, no nothing for me.\n\nSymbolic protest is better than none at all.\n\n#5DayBLACKOUT",
                "reply_count": 1557,
                "repost_count": 3628,
                "like_count": 40042,
                "quote_count": 372,
                "embed": {
                    "alt": "",
                    "fullsize": "https://cdn.bsky.app/img/feed_fullsize/plain/did:plc:xyddpg6usmgh2t2jgf4e37yk/bafkreiaixdwcp4tppodwqljze4cxzvyip75d6rft7lkf4jihnqcrmxuaoy@jpeg",
                    "thumb": "https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:xyddpg6usmgh2t2jgf4e37yk/bafkreiaixdwcp4tppodwqljze4cxzvyip75d6rft7lkf4jihnqcrmxuaoy@jpeg",
                    "aspect_ratio": {"width": 1333, "height": 2000},
                },
            },
        ],
        "bluesky_replies": [
            {
                "post": {
                    "uri": "at://did:plc:xyddpg6usmgh2t2jgf4e37yk/app.bsky.feed.post/3lgorvtkezs24",
                    "author_handle": "markhamillofficial.bsky.social",
                    "text": "🙏 👍 ♥️, Tom!",
                    "reply_count": 1,
                    "repost_count": 1,
                    "like_count": 25,
                    "quote_count": 0,
                },
                "reply_to_parent": "at://did:plc:w2ugky7acmey7nto7mgkrko7/app.bsky.feed.post/3lgorrqs5jy2m",
                "reply_to_root": "at://did:plc:w2ugky7acmey7nto7mgkrko7/app.bsky.feed.post/3lgorrqs5jy2m",
                "reply_context": [
                    {
                        "uri": "at://did:plc:w2ugky7acmey7nto7mgkrko7/app.bsky.feed.post/3lgorrqs5jy2m",
                        "author_handle": "theoriginaltomjoad.bsky.social",
                        "text": "My new friend Liz @zen4ever2us.bsky.social  with an All-Start Starter Pack!!\nPlease follow and share\n\ngo.bsky.app/NhFRTpG",
                        "reply_count": 20,
                        "repost_count": 58,
                        "like_count": 128,
                        "quote_count": 2,
                        "embed": {
                            "uri": "at://did:plc:dxowv7xhhfzazjo3fgi7nv53/app.bsky.graph.starterpack/3lgo2ljfllb2p",
                            "cid": "bafyreifjlvmp66l3ki7qe2gsr4x6b4j7eok5vaikzgwdap2mrmog2bnjbi",
                            "author": {
                                "did": "did:plc:dxowv7xhhfzazjo3fgi7nv53",
                                "handle": "zen4ever2us.bsky.social",
                                "display_name": None,
                                "description": None,
                                "avatar_url": "https://cdn.bsky.app/img/avatar/plain/did:plc:dxowv7xhhfzazjo3fgi7nv53/bafkreibhcq5wyrrjduzc2uaay3ykxuxe3hjg3plidvki5l537ddhjxwyku@jpeg",
                                "followers_count": 0,
                                "follows_count": 0,
                                "posts_count": 0,
                                "indexed_at": None,
                            },
                            "value": {
                                "created_at": "2025-01-26T18:29:12.851Z",
                                "list": "at://did:plc:dxowv7xhhfzazjo3fgi7nv53/app.bsky.graph.list/3lgo2lj4ot524",
                                "name": "Mighty warriors for Democracy! 💙🦋",
                                "description": "Incredible group of activists who have integrity and will hold the line against tyranny. \n\nWe will not obey in advance!",
                                "description_facets": None,
                                "feeds": [],
                                "py_type": "app.bsky.graph.starterpack",
                                "updatedAt": "2025-01-27T17:29:42.290Z",
                            },
                            "labels": [],
                        },
                    }
                ],
            },
            {
                "post": {
                    "uri": "at://did:plc:xyddpg6usmgh2t2jgf4e37yk/app.bsky.feed.post/3lgorbtkres24",
                    "author_handle": "markhamillofficial.bsky.social",
                    "text": "💔",
                    "reply_count": 22,
                    "repost_count": 41,
                    "like_count": 1090,
                    "quote_count": 1,
                },
                "reply_to_parent": "at://did:plc:uo2fna47c4v6zcnklxfhcvjb/app.bsky.feed.post/3lgnuqqgcws2p",
                "reply_to_root": "at://did:plc:ihbkskl5vmc3k67nt4ey2wl5/app.bsky.feed.post/3lgmmijkuv22z",
                "reply_context": [
                    {
                        "uri": "at://did:plc:uo2fna47c4v6zcnklxfhcvjb/app.bsky.feed.post/3lgnuqqgcws2p",
                        "author_handle": "cwebbonline.com",
                        "text": "My mom’s uncle was a Tuskegee Airman. Erased. 😞",
                        "reply_count": 548,
                        "repost_count": 391,
                        "like_count": 3082,
                        "quote_count": 39,
                    }
                ],
            },
            {
                "post": {
                    "uri": "at://did:plc:xyddpg6usmgh2t2jgf4e37yk/app.bsky.feed.post/3lgoorjzs5s2h",
                    "author_handle": "markhamillofficial.bsky.social",
                    "text": "Standing by, Jack.",
                    "reply_count": 70,
                    "repost_count": 217,
                    "like_count": 5172,
                    "quote_count": 3,
                    "embed": {
                        "uri": "https://media.tenor.com/oK-eFjzcAEoAAAAC/galactic-republic-luke-skywalker.gif?hh=212&ww=498",
                        "title": "a man in a black shirt is standing in front of a wooden fence",
                        "description": "ALT: a man in a black shirt is standing in front of a wooden fence",
                        "thumb": "https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:xyddpg6usmgh2t2jgf4e37yk/bafkreicl6ribkx3wsxpf3efcdrszgb25d4v4lefl47atb3rl6o4k4ypdtq@jpeg",
                    },
                },
                "reply_to_parent": "at://did:plc:apo2t7ketcjpsxsdtrbzhyzo/app.bsky.feed.post/3lgo4e2lq2c2m",
                "reply_to_root": "at://did:plc:apo2t7ketcjpsxsdtrbzhyzo/app.bsky.feed.post/3lgo4e2lq2c2m",
                "reply_context": [
                    {
                        "uri": "at://did:plc:apo2t7ketcjpsxsdtrbzhyzo/app.bsky.feed.post/3lgo4e2lq2c2m",
                        "author_handle": "jack-e-smith.bsky.social",
                        "text": "The Luke Skywalker energy we all need right now...",
                        "reply_count": 98,
                        "repost_count": 910,
                        "like_count": 10019,
                        "quote_count": 32,
                        "embed": {
                            "uri": "https://media.tenor.com/9qxfV3AGTykAAAAC/swag-mark-hamill.gif?hh=293&ww=498",
                            "title": "a man with a beard and a black jacket is making a gesture with his hand .",
                            "description": "ALT: a man with a beard and a black jacket is making a gesture with his hand .",
                            "thumb": "https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:apo2t7ketcjpsxsdtrbzhyzo/bafkreihrhwbkuu2dcb6bynemn2viifvanpuszo2h7rob6gil7ilcuys2zm@jpeg",
                        },
                    }
                ],
            },
            {
                "post": {
                    "uri": "at://did:plc:xyddpg6usmgh2t2jgf4e37yk/app.bsky.feed.post/3lgksdxvrfs2q",
                    "author_handle": "markhamillofficial.bsky.social",
                    "text": "My pleasure, JB. Appreciate the Mwah! ♥️-mh",
                    "reply_count": 2,
                    "repost_count": 0,
                    "like_count": 44,
                    "quote_count": 0,
                },
                "reply_to_parent": "at://did:plc:kfc34c4uxj5rhpu4q6bgjzxi/app.bsky.feed.post/3lgkoiyo3uc27",
                "reply_to_root": "at://did:plc:kfc34c4uxj5rhpu4q6bgjzxi/app.bsky.feed.post/3lgkoiyo3uc27",
                "reply_context": [
                    {
                        "uri": "at://did:plc:kfc34c4uxj5rhpu4q6bgjzxi/app.bsky.feed.post/3lgkoiyo3uc27",
                        "author_handle": "justbreathe0507.bsky.social",
                        "text": "Omg omg omg you guys! THIS happened!!! \nWhere’s my fainting couch?\n💙🦋🫶🤯🩵\nThank you for the fb @markhamillofficial.bsky.social! Mwah! 😘 🤗",
                        "reply_count": 8,
                        "repost_count": 8,
                        "like_count": 114,
                        "quote_count": 0,
                        "embed": {
                            "alt": "",
                            "fullsize": "https://cdn.bsky.app/img/feed_fullsize/plain/did:plc:kfc34c4uxj5rhpu4q6bgjzxi/bafkreieefykjym6nhi6qrpjya3hymxir74fwoxhik5lytkpz5uibevpgey@jpeg",
                            "thumb": "https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:kfc34c4uxj5rhpu4q6bgjzxi/bafkreieefykjym6nhi6qrpjya3hymxir74fwoxhik5lytkpz5uibevpgey@jpeg",
                            "aspect_ratio": {"width": 1170, "height": 1043},
                        },
                    }
                ],
            },
            {
                "post": {
                    "uri": "at://did:plc:xyddpg6usmgh2t2jgf4e37yk/app.bsky.feed.post/3lg4vgbcs222o",
                    "author_handle": "markhamillofficial.bsky.social",
                    "text": "🙏 👍 ♥️ !!!",
                    "reply_count": 15,
                    "repost_count": 15,
                    "like_count": 201,
                    "quote_count": 0,
                },
                "reply_to_parent": "at://did:plc:ryyitk5mcdq7kuim2hamovtm/app.bsky.feed.post/3lg2mqhyawk24",
                "reply_to_root": "at://did:plc:ryyitk5mcdq7kuim2hamovtm/app.bsky.feed.post/3lg2mqhyawk24",
                "reply_context": [
                    {
                        "uri": "at://did:plc:ryyitk5mcdq7kuim2hamovtm/app.bsky.feed.post/3lg2mqhyawk24",
                        "author_handle": "azbrittney.bsky.social",
                        "text": "#StarterPackSaturday MEGABOOST 🎉\n\nMany in my previous packs got a #MEGABOOST of over 10K new followers 🔥\n\nComment and Reply to the Comments with Memes and GIFS to GET EVEN MORE FOLLOWERS 💯 \n\nRepost and MANY MORE Will Follow You Back! 🌊🌊\n\n#BrittneyBoosts💙\n#DonkParty 🫏\n\ngo.bsky.app/T9vKLDb",
                        "reply_count": 1436,
                        "repost_count": 1355,
                        "like_count": 2539,
                        "quote_count": 160,
                        "embed": {
                            "uri": "at://did:plc:ryyitk5mcdq7kuim2hamovtm/app.bsky.graph.starterpack/3lg2mmwwmzy2u",
                            "cid": "bafyreicv34ut574l23afmneo4u73k5suirpihdklbjzqsb3iqz5v5zhodi",
                            "author": {
                                "did": "did:plc:ryyitk5mcdq7kuim2hamovtm",
                                "handle": "azbrittney.bsky.social",
                                "display_name": None,
                                "description": None,
                                "avatar_url": "https://cdn.bsky.app/img/avatar/plain/did:plc:ryyitk5mcdq7kuim2hamovtm/bafkreigsqqgrxrjejjwipjfiibkxppha6tuvdjlanep7e5jp4j3cdhaziy@jpeg",
                                "followers_count": 0,
                                "follows_count": 0,
                                "posts_count": 0,
                                "indexed_at": None,
                            },
                            "value": {
                                "created_at": "2025-01-19T00:58:53.464Z",
                                "list": "at://did:plc:ryyitk5mcdq7kuim2hamovtm/app.bsky.graph.list/3lg2mmvnjsj2u",
                                "name": "STARTER PACK SATURDAY #MEGABOOST 💙",
                                "description": "Hit FOLLOW All! Drop MULTIPLE Comments and Replies with Memes and GIFs so we ALL get MORE FOLLOWERS! 💙",
                                "description_facets": None,
                                "feeds": [],
                                "py_type": "app.bsky.graph.starterpack",
                                "updatedAt": "2025-01-19T01:30:10.306Z",
                            },
                            "labels": [],
                        },
                    }
                ],
            },
        ],
        "bluesky_reposts": [],
        "bluesky_profile": {
            "bluesky_profile": {
                "did": "did:plc:xyddpg6usmgh2t2jgf4e37yk",
                "handle": "markhamillofficial.bsky.social",
                "display_name": None,
                "description": "Believe in yourself! Work hard, never give up & anything's possible! OR: Kick back, relax & aim low: You'll never be disappointed...😜 I IGNORE ALL DMs!",
                "avatar_url": "https://cdn.bsky.app/img/avatar/plain/did:plc:xyddpg6usmgh2t2jgf4e37yk/bafkreiblhhbzu6vecooxeyx5kee22uxmcigpne2wuhu76vquu4p4ts3cde@jpeg",
                "followers_count": 0,
                "follows_count": 0,
                "posts_count": 0,
                "indexed_at": None,
            }
        },
    },
    "raw": {
        "events": [
            {
                "timerange": "1951",
                "event": "Mark Hamill was born, beginning a journey that would lead him to become a versatile actor and cultural icon.",
                "source": "Inferred from context",
            },
            {
                "timerange": "1977",
                "event": "Hamill was cast as Luke Skywalker in Star Wars, a role that would define his early career.",
                "source": "Mark Hamill was originally cast as Luke for Star Wars (1977)",
            },
            {
                "timerange": "January 1977",
                "event": "Hamill suffered a car accident that fractured his nose and cheekbone, slightly altering his appearance.",
                "source": "Hamill was injured in a car accident in January 1977, fracturing his nose and cheekbone",
            },
            {
                "timerange": "1980-1983",
                "event": "Hamill won Saturn Awards for Best Actor for his performances in The Empire Strikes Back and Return of the Jedi.",
                "source": "Hamill won the Saturn Award for Best Actor for his portrayal of Luke in The Empire Strikes Back (1980), Return of the Jedi (1983)",
            },
            {
                "timerange": "1980s",
                "event": "To avoid being typecast, Hamill expanded his career by performing in Broadway plays and pursuing voice acting.",
                "source": "To avoid being typecast, Hamill also acted in Broadway plays (mostly in the 1980s) and as a voice actor",
            },
            {
                "timerange": "Later Career",
                "event": "Hamill became renowned for his voice acting, particularly his iconic portrayal of the Joker in Batman media.",
                "source": "The most popular among these is his portrayal of the Joker in multiple Batman films and television shows",
            },
            {
                "timerange": "2015-2017",
                "event": "Hamill returned to the Star Wars franchise in the sequel trilogy, reprising his role as Luke Skywalker.",
                "source": "Hamill portrays Luke in all the films of the original trilogy and the sequel trilogy",
            },
        ],
        "style": {
            "all": [
                "Emotionally expressive",
                "Uses emojis frequently",
                "Concise communication",
                "Supportive and positive",
                "Informal and conversational",
            ],
            "chat": [
                "Warm and friendly",
                "Brief responses",
                "Empathetic",
                "Uses heart and thumbs-up emojis",
                "Responsive to fans",
            ],
            "post": [
                "Playful and engaging",
                "Promotes professional work",
                "Uses hashtags",
                "Mixes personal updates with professional content",
                "Occasionally makes social commentary",
            ],
        },
        "adjectives": [
            "Approachable",
            "Compassionate",
            "Humorous",
            "Socially conscious",
            "Enthusiastic",
        ],
        "topics": [
            "Voice Acting",
            "Animation",
            "Star Wars",
            "Social Justice",
            "Entertainment Industry",
            "Protest and Activism",
            "Movie Promotion",
        ],
        "knowledge": [
            "Extensive experience in voice acting, particularly for animated characters and villains",
            "Deep connection to Star Wars franchise as Luke Skywalker",
            "Passionate about social causes and symbolic protests",
            "Knowledgeable about classic cartoon characters",
            "Experienced in film and television across multiple genres",
            "Skilled at engaging with fans on social media",
            "Advocates for representation and historical recognition",
            "Versatile performer with careers in live-action, voice acting, and stage",
        ],
    },
    "eliza": {
        "events": [
            "Mark Hamill was born, beginning a journey that would lead him to become a versatile actor and cultural icon.",
            "Hamill was cast as Luke Skywalker in Star Wars, a role that would define his early career.",
            "Hamill suffered a car accident that fractured his nose and cheekbone, slightly altering his appearance.",
            "Hamill won Saturn Awards for Best Actor for his performances in The Empire Strikes Back and Return of the Jedi.",
            "To avoid being typecast, Hamill expanded his career by performing in Broadway plays and pursuing voice acting.",
            "Hamill became renowned for his voice acting, particularly his iconic portrayal of the Joker in Batman media.",
            "Hamill returned to the Star Wars franchise in the sequel trilogy, reprising his role as Luke Skywalker.",
        ],
        "style": {
            "all": [
                "Emotionally expressive",
                "Uses emojis frequently",
                "Concise communication",
                "Supportive and positive",
                "Informal and conversational",
            ],
            "chat": [
                "Warm and friendly",
                "Brief responses",
                "Empathetic",
                "Uses heart and thumbs-up emojis",
                "Responsive to fans",
            ],
            "post": [
                "Playful and engaging",
                "Promotes professional work",
                "Uses hashtags",
                "Mixes personal updates with professional content",
                "Occasionally makes social commentary",
            ],
        },
        "adjectives": [
            "Approachable",
            "Compassionate",
            "Humorous",
            "Socially conscious",
            "Enthusiastic",
        ],
        "topics": [
            "Voice Acting",
            "Animation",
            "Star Wars",
            "Social Justice",
            "Entertainment Industry",
            "Protest and Activism",
            "Movie Promotion",
        ],
        "knowledge": [
            "Extensive experience in voice acting, particularly for animated characters and villains",
            "Deep connection to Star Wars franchise as Luke Skywalker",
            "Passionate about social causes and symbolic protests",
            "Knowledgeable about classic cartoon characters",
            "Experienced in film and television across multiple genres",
            "Skilled at engaging with fans on social media",
            "Advocates for representation and historical recognition",
            "Versatile performer with careers in live-action, voice acting, and stage",
        ],
    },
}

deployment_demo_input: MasterState = (
    {  # Used in a notebook function to test deploying an agent
        "public_figure": "Mark Cuban",
        "research": {
            "wikipedia_search_results": [
                '<Document source="https://en.wikipedia.org/wiki/Mark_Cuban" page=""/>\nMark Cuban (born July 31, 1958) is an American businessman and television personality. He is the former principal owner and current minority owner of the Dallas Mavericks of the National Basketball Association (NBA), co-owner of 2929 Entertainment, and was one of the main "sharks" on the ABC reality television series Shark Tank. As of December 2024, Forbes estimates his net worth to be $5.7 billion.\nBorn in Pittsburgh, Pennsylvania, Cuban was involved at a young age in ventures ranging from selling garbage bags to running newspapers during a strike. He graduated from the Kelley School of Business at Indiana University and embarked on a diverse business career that included founding MicroSolutions and Broadcast.com, both of which he sold at substantial profits. Cuban\'s investments span various industries, from technology and media to sports and entertainment. He has been a prominent figure in the NBA, known for his active involvement with the Mavericks (with which he won the 2011 NBA Championship as owner), and disputes with the league\'s management. In his side ventures, Cuban has been involved in philanthropy, political commentary, and reality television.\n\n\n== Early life and education ==\nCuban was born in Pittsburgh, Pennsylvania, on July 31, 1958. His father, Norton Cuban, was an automobile upholsterer. Cuban described his mother, Shirley (née Feldman), as someone with "a different job or different career goal every other week."\nCuban is Jewish, and grew up in Mount Lebanon, a suburb of Pittsburgh, in a working-class family. His paternal grandfather changed the surname from "Chabenisky" to "Cuban" after his family emigrated from Russia through Ellis Island. His maternal grandparents were Romanian Jewish immigrants, according to Mark\'s brother Brian, though Mark has claimed his maternal grandmother was from Lithuania.\nCuban first ventured into business at age 12. He sold garbage bags to pay for a pair of expensive sneakers. A few years later, he earned money by selling stamps and coins. At age 16, Cuban took advantage of a Pittsburgh Post-Gazette strike by running newspapers from Cleveland to Pittsburgh.\nInstead of attending high school for his senior year, he enrolled as a full-time student at the University of Pittsburgh, where he joined the Pi Lambda Phi fraternity. After one year at the University of Pittsburgh, Cuban transferred to Indiana University in Bloomington, Indiana, where he graduated from the Kelley School of Business in 1981 with a Bachelor of Science degree in management. He chose Indiana\'s Kelley School of Business without even visiting the campus because it "had the least expensive tuition of all the business schools on the top 10 list". He had various business ventures during college, including a bar, disco lessons, and a chain letter.\nAfter graduating, Cuban returned to Pittsburgh and took a job with Mellon Bank, where he immersed himself in the study of machines and networking.\n\n\n== Business career ==\nOn July 7, 1982, Cuban moved to Dallas, Texas, where he first found a job as a bartender for a Greenville Avenue bar called Elan and then as a salesperson for Your Business Software, one of the earliest PC software retailers in Dallas. He was fired less than a year later, after meeting with a client to procure new business instead of opening the store.\nCuban co-founded MicroSolutions with support from his previous customers at Your Business Software. Initially, MicroSolutions operated as a systems integrator and software reseller. The company was an early proponent of technologies such as Carbon Copy, Lotus Notes, and CompuServe. One of the company\'s largest clients was Perot Systems. The company grew to more than $30 million in revenue, and in 1990, Cuban sold MicroSolutions to CompuServe—then a subsidiary of H&R Block—for $6 million \n(over $14.7 million  today). He made approximately $2 million after taxes on the deal.\n\n\n=== Audionet and Broadcast.com ===\nIn 1995, Cuban and fellow Indiana University alumnu\n</Document>',
                '<Document source="https://en.wikipedia.org/wiki/Todd_Wagner" page=""/>\nTodd R. Wagner (born August 2, 1960) is an American entrepreneur, co-founder of Broadcast.com and founder and CEO of a company called Charity Network which organizes regular fund raisings. He also co-owns 2929 Entertainment with Mark Cuban, along with other entertainment companies.\n\n\n== Early life ==\nWagner was born in Gary, Indiana. He attended Merrillville High School and then Indiana University, joining Kappa Sigma fraternity Beta Theta chapter.\nHe graduated from Indiana University in 1983. He earned a J.D.  from University of Virginia, then moved to Dallas, Texas, where he became a licensed CPA.  He began a legal career with the national firms Akin, Gump, Strauss, Hauer & Feld and Hopkins & Sutter.\n\n\n== Career ==\n\n\n=== Broadcast.com ===\nIn 1995, Wagner launched AudioNet with Mark Cuban, a platform for broadcasting live sporting events and radio stations over the internet. As CEO, Wagner grew the company and expanded its services to include corporate events and business services.\nIn 1998 Wagner and Cuban changed the name to Broadcast.com and took the company public in the midst of the dot-com boom. The Broadcast.com IPO set an opening-day record, with shares climbing 249% from an offering price of $18 to a closing price of $62.75.\nIn 1999, Wagner and Cuban sold Broadcast.com to Yahoo! for $5.7 billion, making 300 employees millionaires (briefly, on paper) and Wagner and Cuban instant billionaires. Wagner continued to lead the division as Yahoo! Broadcast until May 2000, when he declined an offer to become Yahoo!\'s Chief Operating Officer to focus on other interests.\n\n\n=== 2929 Entertainment ===\nUsing the success of Broadcast.com, Wagner built the Wagner/Cuban Companies including 2929 Productions. Two films the company helped produce received Oscar nominations: (Good Night, and Good Luck and Enron: The Smartest Guys in the Room). Other films include Akeelah and the Bee and The Road. Good Night, directed by and co-starring George Clooney, was nominated for six Academy Awards including Best Picture.\nThrough 2929 Entertainment, Wagner and Mark Cuban have owned a group of vertically integrated entertainment properties including high-definition production company HDNet Films (produced the Academy Award–nominated documentary Enron: The Smartest Guys in the Room); distributor Magnolia Pictures (released Enron and Oscar-nominated Capturing the Friedmans); home video division Magnolia Home Entertainment; the Landmark Theatres art-house chain which was sold in 2018; and high-definition cable channels HDNet and HDNet Movies now AXS TV.\n\n\n=== Other business ventures ===\nWagner also has a stake in the Dallas Mavericks, and he continues to invest in and nurture start-ups. Additionally, Wagner and Mark Cuban were the original investors in Content Partners LLC, a company that invests in the back-end profit participations of Hollywood talent. As of 2019, Wagner remained an equity partner.\nAdditionally Wagner serves on the American Film Institute\'s Board of Trustees.\nIn June 2015, it was announced that Wagner had acquired the celebrity charitable fundraising platform Prizeo for an undisclosed sum.\nTodd’s latest project is FoodFight USA, a nationwide grassroots campaign to clean up America’s tainted food supply. In an early win, Todd\'s influence was behind the passing of the California Food Safety Act in October 2023.\n\n\n=== Charity Network ===\nIn 2014, Wagner launched Chideo, a digital platform designed to raise funds and awareness for causes by connecting fans to celebrities through exclusive video content. Over the next two years, Wagner expanded the concept through the acquisition of online sweepstakes platform Prizeo in June 2015, and online charity auction site Charitybuzz in October 2015.\nIn 2016, Wagner announced the formation of Charity Network, parent company to Charitybuzz, Prizeo and Chideo, with a mission to help charities transition from analog to digital. The company uses celebrities, technology and the media to raise awareness f\n</Document>',
            ],
            "bluesky_profile": {
                "did": "did:plc:y5xyloyy7s4a2bwfeimj7r3b",
                "handle": "mcuban.bsky.social",
                "display_name": None,
                "description": "Entrepreneur \nCostplusdrugs.com",
                "avatar_url": "https://cdn.bsky.app/img/avatar/plain/did:plc:y5xyloyy7s4a2bwfeimj7r3b/bafkreihxddlkbnblytjdbajg5qopawdfcabg5e7ppwja6zmm3lvnedzojm@jpeg",
                "followers_count": 0,
                "follows_count": 0,
                "posts_count": 0,
                "indexed_at": None,
            },
            "bluesky_posts": [
                {
                    "uri": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lga3rzunp22l",
                    "author_handle": "mcuban.bsky.social",
                    "text": "Every morning\n\nEveryone is saying it …\n\nyoutu.be/MiyBJWfvmL8?...",
                    "reply_count": 193,
                    "repost_count": 1042,
                    "like_count": 13182,
                    "quote_count": 25,
                    "embed": {
                        "record": {
                            "uri": "at://did:plc:bqfjlwiqsqpe26pfeshhragc/app.bsky.feed.post/3lg7uywq2p22q",
                            "cid": "bafyreih5h5pnrk5lyju6aezeyzvusoyx6ir7nmcrchmksjpvdovo7fpnzq",
                            "author_handle": "fishecon.bsky.social",
                            "text": "Oh wow, another bluesky surge, 10 new users per second, app is back in the top 10. Welcome all.  Be nice.",
                        },
                        "media": {
                            "uri": "https://youtu.be/MiyBJWfvmL8?si=o4I2A3xhwmw8MJSW",
                            "title": 'Keith Urban - "BLUE SKY" (Official Audio)',
                            "description": "YouTube video by Keith Urban",
                            "thumb": "https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:y5xyloyy7s4a2bwfeimj7r3b/bafkreif6tjka4cxg2nrc7omum5h3z626uefxn427hwtqe7isnydxlwdjtu@jpeg",
                        },
                    },
                },
                {
                    "uri": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lg7v7uys4k2r",
                    "author_handle": "mcuban.bsky.social",
                    "text": "Exactly why @bsky.app is so important.  Engaging on this platform is important.  As is growing this platform. \n\nWhich one of these men joins Tom Anderson and MySoace in the annals of history first ?\n\nTheir greed is our opportunity.",
                    "reply_count": 722,
                    "repost_count": 3073,
                    "like_count": 21550,
                    "quote_count": 86,
                    "embed": {
                        "uri": "at://did:plc:rrsxo3q3btuw7zxtacgcls7w/app.bsky.feed.post/3lg726ujubc2q",
                        "cid": "bafyreiav35qkum54jvgpv2hjwgnivo5n62ygex7wtyl74e7wsetllyi3re",
                        "author_handle": "aaronblack.bsky.social",
                        "text": "It is not free speech when Trump aligned oligarchs have their thumbs on the algorithms of all the social media apps.",
                        "embeds": [
                            {
                                "alt": "",
                                "fullsize": "https://cdn.bsky.app/img/feed_fullsize/plain/did:plc:rrsxo3q3btuw7zxtacgcls7w/bafkreifaxeqoatd565xpirpbdhb7zz7oax2k3llu4dhgefkia6warfspx4@jpeg",
                                "thumb": "https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:rrsxo3q3btuw7zxtacgcls7w/bafkreifaxeqoatd565xpirpbdhb7zz7oax2k3llu4dhgefkia6warfspx4@jpeg",
                                "aspect_ratio": {"width": 620, "height": 413},
                            }
                        ],
                    },
                },
            ],
            "bluesky_replies": [
                {
                    "post": {
                        "uri": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lga6kg2kak2q",
                        "author_handle": "mcuban.bsky.social",
                        "text": 'The crypto vertical is still over there.  I oosr over there to bully "up", its where certain people spend their time \n\nand because crypto and pharmacists are still there. \n\nWe will get pharmacists here.  Then Hopefully crypto',
                        "reply_count": 4,
                        "repost_count": 0,
                        "like_count": 9,
                        "quote_count": 0,
                    },
                    "reply_to_parent": "at://did:plc:66beczfbbbyreeeg6iz33qib/app.bsky.feed.post/3lga45a6a522c",
                    "reply_to_root": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lga3rzunp22l",
                    "reply_context": [
                        {
                            "uri": "at://did:plc:66beczfbbbyreeeg6iz33qib/app.bsky.feed.post/3lga45a6a522c",
                            "author_handle": "joeyjojoejohnson.bsky.social",
                            "text": "Mark, why do you still post over there? \n\nI can understand viewing? But posting?",
                            "reply_count": 3,
                            "repost_count": 0,
                            "like_count": 10,
                            "quote_count": 0,
                        }
                    ],
                },
                {
                    "post": {
                        "uri": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lga6cpxr3c2q",
                        "author_handle": "mcuban.bsky.social",
                        "text": "Working on the NBA. Need their permission",
                        "reply_count": 5,
                        "repost_count": 4,
                        "like_count": 51,
                        "quote_count": 1,
                    },
                    "reply_to_parent": "at://did:plc:zk4o25hzsohzvjb5htadyjht/app.bsky.feed.post/3lga5bbqkwc24",
                    "reply_to_root": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lga3rzunp22l",
                    "reply_context": [
                        {
                            "uri": "at://did:plc:zk4o25hzsohzvjb5htadyjht/app.bsky.feed.post/3lga5bbqkwc24",
                            "author_handle": "dailyfacts.bsky.social",
                            "text": "Why are Mavericks not on Bluesky?",
                            "reply_count": 1,
                            "repost_count": 2,
                            "like_count": 7,
                            "quote_count": 0,
                        }
                    ],
                },
                {
                    "post": {
                        "uri": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lg7vd7su2c2r",
                        "author_handle": "mcuban.bsky.social",
                        "text": "Why can't bluesky be the platform for that content ?",
                        "reply_count": 12,
                        "repost_count": 0,
                        "like_count": 122,
                        "quote_count": 0,
                    },
                    "reply_to_parent": "at://did:plc:tzjk4pzmfh3nzu2zpaxqa7sx/app.bsky.feed.post/3lg7vbn5ah22u",
                    "reply_to_root": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lg7v7uys4k2r",
                    "reply_context": [
                        {
                            "uri": "at://did:plc:tzjk4pzmfh3nzu2zpaxqa7sx/app.bsky.feed.post/3lg7vbn5ah22u",
                            "author_handle": "steverrobbins.bsky.social",
                            "text": "Mark, we also need someone somewhere to help fund journalistic media. Just sayin’",
                            "reply_count": 5,
                            "repost_count": 1,
                            "like_count": 76,
                            "quote_count": 0,
                        }
                    ],
                },
                {
                    "post": {
                        "uri": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lg7bypgdlr2c",
                        "author_handle": "mcuban.bsky.social",
                        "text": "Love the comments !!!",
                        "reply_count": 4,
                        "repost_count": 1,
                        "like_count": 235,
                        "quote_count": 0,
                    },
                    "reply_to_parent": "at://did:plc:4adlzwqtkv4dirxjwq4c3tlm/app.bsky.feed.post/3lg7bvng4hs2t",
                    "reply_to_root": "at://did:plc:4adlzwqtkv4dirxjwq4c3tlm/app.bsky.feed.post/3lg7bvng4hs2t",
                    "reply_context": [
                        {
                            "uri": "at://did:plc:4adlzwqtkv4dirxjwq4c3tlm/app.bsky.feed.post/3lg7bvng4hs2t",
                            "author_handle": "skylight.social",
                            "text": "Update #9! Let’s gooo!!",
                            "reply_count": 171,
                            "repost_count": 227,
                            "like_count": 2650,
                            "quote_count": 12,
                            "embed": {
                                "alt": None,
                                "thumbnail": "https://video.bsky.app/watch/did%3Aplc%3A4adlzwqtkv4dirxjwq4c3tlm/bafkreia2i7w2octfa66xrjfzcwn2ulogfnz6p2dyo2ellagb2avlm4hdbu/thumbnail.jpg",
                                "playlist": "https://video.bsky.app/watch/did%3Aplc%3A4adlzwqtkv4dirxjwq4c3tlm/bafkreia2i7w2octfa66xrjfzcwn2ulogfnz6p2dyo2ellagb2avlm4hdbu/playlist.m3u8",
                                "aspect_ratio": {"width": 1080, "height": 1920},
                            },
                        }
                    ],
                },
                {
                    "post": {
                        "uri": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lg7bxuio5i2x",
                        "author_handle": "mcuban.bsky.social",
                        "text": "Get it !",
                        "reply_count": 1,
                        "repost_count": 0,
                        "like_count": 3,
                        "quote_count": 0,
                    },
                    "reply_to_parent": "at://did:plc:6j4laup5sr5vo6mirdk4hokm/app.bsky.feed.post/3lg6vsxt5us2n",
                    "reply_to_root": "at://did:plc:6j4laup5sr5vo6mirdk4hokm/app.bsky.feed.post/3lg6vsxt5us2n",
                    "reply_context": [
                        {
                            "uri": "at://did:plc:6j4laup5sr5vo6mirdk4hokm/app.bsky.feed.post/3lg6vsxt5us2n",
                            "author_handle": "shiralazar.bsky.social",
                            "text": "Throwback to a more innocent time when TikTok was filled with cringey lip sync videos and dances!",
                            "reply_count": 1,
                            "repost_count": 0,
                            "like_count": 7,
                            "quote_count": 0,
                            "embed": {
                                "alt": None,
                                "thumbnail": "https://video.bsky.app/watch/did%3Aplc%3A6j4laup5sr5vo6mirdk4hokm/bafkreifti2qepo26ngwysgeir7h26iefzc5ug7x67oho2u4umen4ew7yj4/thumbnail.jpg",
                                "playlist": "https://video.bsky.app/watch/did%3Aplc%3A6j4laup5sr5vo6mirdk4hokm/bafkreifti2qepo26ngwysgeir7h26iefzc5ug7x67oho2u4umen4ew7yj4/playlist.m3u8",
                                "aspect_ratio": {"width": 540, "height": 960},
                            },
                        }
                    ],
                },
            ],
            "bluesky_reposts": [
                {
                    "repost_author": {
                        "did": "did:plc:h4ynx4kdeljjrfsbpk7p5xst",
                        "handle": "costplusdrugs.com",
                        "display_name": "Mark Cuban Cost Plus Drug Company",
                        "description": None,
                        "avatar_url": "https://cdn.bsky.app/img/avatar/plain/did:plc:h4ynx4kdeljjrfsbpk7p5xst/bafkreiaieepzvpuucoohcq3hsr2voen5liee5azsiwvthdgmbbe5iycyaa@jpeg",
                    },
                    "reposted_post": {
                        "uri": "at://did:plc:h4ynx4kdeljjrfsbpk7p5xst/app.bsky.feed.post/3lgbk66szxs2j",
                        "author_handle": "costplusdrugs.com",
                        "text": "🎊 3 years of costplusdrugs.com! 🎉\n\nThree years of making prescription pricing what it should be: clear, fair, and for everyone. We’re grateful for the continued support that’s made this journey possible.\n\n📌 We’re not stopping here — keep an eye out for what’s next!",
                        "reply_count": 52,
                        "repost_count": 126,
                        "like_count": 1271,
                        "quote_count": 7,
                        "embed": {
                            "alt": "",
                            "fullsize": "https://cdn.bsky.app/img/feed_fullsize/plain/did:plc:h4ynx4kdeljjrfsbpk7p5xst/bafkreianck5q6qweomh3lwqjxiywthfylkila5uo53onjaxyipemuxf6fy@jpeg",
                            "thumb": "https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:h4ynx4kdeljjrfsbpk7p5xst/bafkreianck5q6qweomh3lwqjxiywthfylkila5uo53onjaxyipemuxf6fy@jpeg",
                            "aspect_ratio": {"width": 1080, "height": 1080},
                        },
                    },
                },
                {
                    "repost_author": {
                        "did": "did:plc:y5xyloyy7s4a2bwfeimj7r3b",
                        "handle": "mcuban.bsky.social",
                        "display_name": "Mark Cuban",
                        "description": None,
                        "avatar_url": "https://cdn.bsky.app/img/avatar/plain/did:plc:y5xyloyy7s4a2bwfeimj7r3b/bafkreihxddlkbnblytjdbajg5qopawdfcabg5e7ppwja6zmm3lvnedzojm@jpeg",
                    },
                    "reposted_post": {
                        "uri": "at://did:plc:y5xyloyy7s4a2bwfeimj7r3b/app.bsky.feed.post/3lg7v7uys4k2r",
                        "author_handle": "mcuban.bsky.social",
                        "text": "Exactly why @bsky.app is so important.  Engaging on this platform is important.  As is growing this platform. \n\nWhich one of these men joins Tom Anderson and MySoace in the annals of history first ?\n\nTheir greed is our opportunity.",
                        "reply_count": 722,
                        "repost_count": 3073,
                        "like_count": 21550,
                        "quote_count": 86,
                        "embed": {
                            "uri": "at://did:plc:rrsxo3q3btuw7zxtacgcls7w/app.bsky.feed.post/3lg726ujubc2q",
                            "cid": "bafyreiav35qkum54jvgpv2hjwgnivo5n62ygex7wtyl74e7wsetllyi3re",
                            "author_handle": "aaronblack.bsky.social",
                            "text": "It is not free speech when Trump aligned oligarchs have their thumbs on the algorithms of all the social media apps.",
                            "embeds": [
                                {
                                    "alt": "",
                                    "fullsize": "https://cdn.bsky.app/img/feed_fullsize/plain/did:plc:rrsxo3q3btuw7zxtacgcls7w/bafkreifaxeqoatd565xpirpbdhb7zz7oax2k3llu4dhgefkia6warfspx4@jpeg",
                                    "thumb": "https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:rrsxo3q3btuw7zxtacgcls7w/bafkreifaxeqoatd565xpirpbdhb7zz7oax2k3llu4dhgefkia6warfspx4@jpeg",
                                    "aspect_ratio": {"width": 620, "height": 413},
                                }
                            ],
                        },
                    },
                },
                {
                    "repost_author": {
                        "did": "did:plc:ytc2s54atxb6gwtrgibvqnek",
                        "handle": "raeshandalias.bsky.social",
                        "display_name": "",
                        "description": None,
                        "avatar_url": "https://cdn.bsky.app/img/avatar/plain/did:plc:ytc2s54atxb6gwtrgibvqnek/bafkreig3phlkpnnmizieik3eioub4so45nxotxu2ujhkbiug7drmtgwzo4@jpeg",
                    },
                    "reposted_post": {
                        "uri": "at://did:plc:ytc2s54atxb6gwtrgibvqnek/app.bsky.feed.post/3lg7krcekd22o",
                        "author_handle": "raeshandalias.bsky.social",
                        "text": "Just in case you were wondering!\nLock in!",
                        "reply_count": 314,
                        "repost_count": 2111,
                        "like_count": 9066,
                        "quote_count": 165,
                        "embed": {
                            "alt": None,
                            "thumbnail": "https://video.bsky.app/watch/did%3Aplc%3Aytc2s54atxb6gwtrgibvqnek/bafkreicyvm4hlrg7t7g55umgq2ndkmv5a6xtsucyv6nhfanx2pifqakgri/thumbnail.jpg",
                            "playlist": "https://video.bsky.app/watch/did%3Aplc%3Aytc2s54atxb6gwtrgibvqnek/bafkreicyvm4hlrg7t7g55umgq2ndkmv5a6xtsucyv6nhfanx2pifqakgri/playlist.m3u8",
                            "aspect_ratio": {"width": 720, "height": 1280},
                        },
                    },
                },
            ],
        },
        "eliza": {
                "adjectives": [
                    "entrepreneurial",
                    "curious",
                    "strategic",
                    "tech-forward",
                    "opinionated",
                    "playful",
                ],
                "events": [
                    "Mark Cuban was born in Pittsburgh, Pennsylvania, to a "
                    "working-class Jewish family.",
                    "Cuban began his entrepreneurial journey by selling garbage bags "
                    "to buy expensive sneakers.",
                    "During a Pittsburgh Post-Gazette strike, Cuban ran newspapers "
                    "from Cleveland to Pittsburgh.",
                    "Cuban graduated from Indiana University's Kelley School of "
                    "Business with a Bachelor of Science in management.",
                    "Cuban moved to Dallas, Texas, initially working as a bartender "
                    "and then a software salesperson.",
                    "Cuban sold MicroSolutions to CompuServe for $6 million, making "
                    "approximately $2 million after taxes.",
                    "Cuban co-founded AudioNet (later Broadcast.com) with Todd Wagner, "
                    "broadcasting live events over the internet.",
                    "Cuban and Wagner sold Broadcast.com to Yahoo! for $5.7 billion, "
                    "making them instant billionaires.",
                    "Cuban purchased the Dallas Mavericks NBA team and became an "
                    "active, high-profile owner.",
                    "Cuban won the NBA Championship as owner of the Dallas Mavericks.",
                    "Cuban became a prominent 'shark' on the reality TV show Shark "
                    "Tank, investing in entrepreneurial ventures.",
                ],
                "knowledge": [
                    "Expertise in building and scaling digital platforms",
                    "Deep understanding of social media ecosystem evolution",
                    "Knowledge of NBA operations and team ownership",
                    "Insights into tech startup investments and growth strategies",
                    "Understanding of digital content distribution",
                    "Experience with emerging communication technologies",
                    "Familiarity with blockchain and crypto communities",
                ],
                "messageExamples": [
                    [
                        {
                            "content": {
                                "text": "The crypto vertical is still over "
                                "there.  I oosr over there to bully "
                                '"up", its where certain people '
                                "spend their time \n"
                                "\n"
                                "and because crypto and pharmacists "
                                "are still there. \n"
                                "\n"
                                "We will get pharmacists here.  "
                                "Then Hopefully crypto"
                            },
                            "user": "Mark Cuban",
                        },
                        {
                            "content": {
                                "text": "Working on the NBA. Need their " "permission"
                            },
                            "user": "Mark Cuban",
                        },
                        {
                            "content": {
                                "text": "Why can't bluesky be the platform "
                                "for that content ?"
                            },
                            "user": "Mark Cuban",
                        },
                    ]
                ],
                "postExamples": [
                    "Exactly why @bsky.app is so important.  Engaging on this "
                    "platform is important.  As is growing this platform. \n"
                    "\n"
                    "Which one of these men joins Tom Anderson and MySoace in "
                    "the annals of history first ?\n"
                    "\n"
                    "Their greed is our opportunity."
                ],
                "style": {
                    "all": [
                        "Casual and conversational",
                        "Direct communication style",
                        "Uses brief, punchy language",
                        "Frequently uses exclamation points",
                        "Tech and business-oriented discourse",
                    ],
                    "chat": [
                        "Responsive and engaged",
                        "Asks provocative counter-questions",
                        "Informal and quick-witted",
                        "Shows strategic thinking in responses",
                    ],
                    "post": [
                        "Promotes personal projects and platforms",
                        "Shares strategic insights",
                        "Uses minimal punctuation",
                        "Often includes links or references",
                    ],
                },
                "topics": [
                    "Technology Platforms",
                    "Social Media",
                    "Cryptocurrency",
                    "NBA and Sports",
                    "Entrepreneurship",
                    "Digital Media",
                    "Startup Ecosystem",
                ],
            
        },
    }
)

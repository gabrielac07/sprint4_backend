from flask_restful import Api, Resource
from sqlalchemy import Text, JSON
from __init__ import app, db
from sqlalchemy import Column, Integer, String, Text
from sqlite3 import IntegrityError

# Book model definition
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String, nullable=False)
    author = db.Column(String, nullable=False)
    genre = db.Column(String)
    description = db.Column(Text)
    cover_image_url = db.Column(String)

# Book data to insert
def initBooks(): 
    books_data = [
        ("Great Expectations", "Charles Dickens", "Classics", "Great Expectations follows the childhood and young adult years of Pip a blacksmith's apprentice in a country village. He suddenly comes into a large fortune (his great expectations) from a mysterious benefactor. and moves to London where he enters high society.", "https://m.media-amazon.com/images/I/715lBsaI4sL.jpg"),
        ("The Outsiders", "S.E. Hinton", "Classics", "Ponyboy, a greaser from the 'wrong' side of town, struggles to find his place in society alongside his friends after personal tragedies.", "https://m.media-amazon.com/images/I/71Bg39CmhoL.jpg"),
        ("Heart of Darkness", "Joseph Conrad", "Classics", "The novella follows Charles Marlow, a steamboat captain, as he journeys up the Congo River to find Kurtz, an ivory trader with a mysterious reputation. Marlow witnesses the brutal exploitation of the African people and the moral decay of European colonialists, culminating in his encounter with Kurtz, who has descended into madness and godlike tyranny. The story explores themes of imperialism, human nature, and the blurred line between civilization and savagery.", "https://mpd-biblio-covers.imgix.net/9781509850921.jpg"),
        ("Pride and Prejudice", "Jane Austen", "Classics", "Pride and Prejudice follows the turbulent relationship between Elizabeth Bennet, the daughter of a country gentleman, and Fitzwilliam Darcy, a rich aristocratic landowner. They must overcome the titular sins of pride and prejudice in order to fall in love and marry.", "https://images.booksense.com/images/518/439/9780141439518.jpg"),
        ("Little Women", "Louisa May Alcott", "Classics", "Little Women by Louisa May Alcott follows the lives of the four March sisters. Each faces challenges as they grow up during the Civil War. The story explores family, love, and personal dreams.", "https://m.media-amazon.com/images/I/71csCMokg9S.jpg"),
        ("A Game of Thrones", "George R.R. Martin", "Fantasy", "Sweeping from a harsh land of cold to a summertime kingdom of epicurean plenty, A Game of Thrones tells a tale of lords and ladies, soldiers and sorcerers, assassins and bastards, who come together in a time of grim omens. Here an enigmatic band of warriors bear swords of no human metal; a tribe of fierce wildlings carry men off into madness; a cruel young dragon prince barters his sister to win back his throne; a child is lost in the twilight between life and death; and a determined woman undertakes a treacherous journey to protect all she holds dear. Amid plots and counter-plots, tragedy and betrayal, victory and terror, allies and enemies, the fate of the Starks hangs perilously in the balance, as each side endeavors to win that deadliest of conflicts: the game of thrones.", "https://m.media-amazon.com/images/I/81CiRBnk8VL.jpg"),
        ("The Hobbit", "J.R.R. Tolkien", "Fantasy", "Bilbo Baggins, a reluctant and comfort-loving hobbit, is swept into an epic adventure when he joins a company of thirteen dwarves and the wizard Gandalf. Their quest is to reclaim the dwarves’ lost kingdom and treasure from the fearsome dragon Smaug. Along the journey, Bilbo encounters trolls, goblins, giant spiders, and a mysterious creature named Gollum, from whom he obtains a magical ring with the power of invisibility. Bilbo’s courage and resourcefulness grow as he faces challenges, ultimately playing a crucial role in their mission.", "https://m.media-amazon.com/images/I/81hylMcxa3L._AC_UF1000,1000_QL80_.jpg"),
        ("Six of Crows", "Leigh Bardugo", "Fantasy", "Criminal prodigy Kaz Brekker assembles a crew of misfits to pull off an impossible heist: breaking into the impenetrable Ice Court and stealing a scientist with a dangerous secret. Each member of the crew, from acrobat-spy Inej to sharpshooter Jesper, has their own skills and troubled past, which threaten to both strengthen and destabilize the mission. As they face betrayal, danger, and their own demons, the story weaves a thrilling tale of trust, ambition, and survival in a gritty fantasy world.", "https://niasbookfort.wordpress.com/wp-content/uploads/2019/01/six-of-crows.jpg"),
        ("Harry Potter and the Sorcerer's Stone", "J. K. Rowling", "Fantasy", "Orphaned Harry Potter discovers he is a wizard and attends the magical Hogwarts School of Witchcraft and Wizardry. There, he makes friends, uncovers secrets about his past, and learns about the dark wizard Voldemort, who killed his parents and seeks to return to power. As Harry and his friends investigate a hidden object called the Sorcerer’s Stone, they face dangerous trials and prove their courage, setting the stage for an epic battle between good and evil.", "https://m.media-amazon.com/images/I/819GoteowlL._UF1000,1000_QL80_.jpg"),
        ("The Lion, the Witch and the Wardrobe", "C.S. Lewis", "Fantasy", "Four siblings—Lucy, Edmund, Susan, and Peter—discover a magical land called Narnia through a wardrobe. Narnia is under the icy rule of the White Witch, who has cast it into eternal winter, but the siblings join forces with the noble lion Aslan to fight for its freedom. Through bravery and sacrifice, they help overthrow the Witch, bringing peace and becoming Narnia’s kings and queens.", "https://i.harperapps.com/hcuk/covers/9780007115617/x450.JPG"),
        ("Bomb", "Steve Sheinkin", "Nonfiction", "Extensively researched, Bomb employs primary sources from declassified FBI files to simultaneously tell of Robert Oppenheimer and the Manhattan Project, Soviet espionage, and Allied efforts to sabotage Nazi Germany's ability to develop the bomb first.", "https://m.media-amazon.com/images/I/91SE96zuV6L._AC_UF894,1000_QL80_.jpg"),
        ("Night", "Elie Wiesel", "Nonfiction", "Night is an autobiographical recounting of the horrors a young Jewish boy experienced near the end of the Second World War. The author, Eliezer 'Elie' Wiesel, describes how there were signs and warnings as early as 1942 of the difficult times ahead, but people refused to believe them.", "https://m.media-amazon.com/images/I/61jNWUb7rvL._AC_UF894,1000_QL80_.jpg"),
        ("Educated", "Tara Westover", "Nonfiction", "This compelling memoir tells the story of Tara Westover, who grew up in a strict, survivalist family in rural Idaho and had no formal education until she left home at 17. Through sheer determination, she overcame significant obstacles to earn a PhD from the University of Cambridge. The book explores themes of self-discovery, resilience, and the power of education, while also delving into the complexities of family dynamics and personal growth.", "https://m.media-amazon.com/images/I/71-4MkLN5jL.jpg"),
        ("Bad Blood: Secrets and Lies in a Silicon Valley Startup", "John Carreyrou", "Nonfiction", "This investigative thriller unveils the rise and fall of Theranos, the biotech startup founded by Elizabeth Holmes that promised revolutionary blood-testing technology. Carreyrou, the journalist who broke the story, details how the company deceived investors, patients, and employees, all while navigating a culture of secrecy and manipulation. The book is a riveting exposé of ambition, fraud, and the dark side of Silicon Valley.", "https://m.media-amazon.com/images/I/615D72nIelL.jpg"),
        ("Atomic Habits", "James Clear", "Nonfiction", "James Clear’s Atomic Habits is a practical and actionable guide for anyone looking to improve their daily routines and behaviors. Clear breaks down the science of habit formation, explaining how small changes can compound over time to create significant transformations. He introduces the four laws of behavior change—make it obvious, make it attractive, make it easy, and make it satisfying—to help readers design systems that support positive habits and eliminate negative ones. Full of relatable examples and practical tips, this book is a go-to resource for mastering the art of habit change.", "https://m.media-amazon.com/images/I/81ANaVZk5LL.jpg"),
        ("We are Not Free", "Traci Chee", "Historical Fiction", "We Are Not Free, is the collective account of a tight-knit group of young Nisei, second-generation Japanese American citizens, whose lives are irrevocably changed by the mass U.S. incarcerations of World War II.", "https://i0.wp.com/abookwanderer.com/wp-content/uploads/2020/09/49934666.jpg?resize=640%2C1001&ssl=1"),
        ("The Nightingale", "Kristin Hannah", "Historical Fiction", "The Nightingale tells the story of Vianne (Rossignol) Mauriac and Isabelle Rossignol, two French sisters who resist the occupying Nazi forces during World War II (WWII) by hiding Jewish children so they are not taken to concentration camps (the Holocaust) and by leading the escape of Allied pilots whose planes have been shot down over France.", "https://www.bookgarden.biz/wp-content/uploads/2021/05/kristin.jpg"),
        ("Salt to the Sea", "Ruta Sepetys", "Historical Fiction", "While the Titanic and Lusitania are both well-documented disasters, the single greatest tragedy in maritime history is the little-known January 30, 1945 sinking in the Baltic Sea by a Soviet submarine of the Wilhelm Gustloff, a German cruise liner that was supposed to ferry wartime personnel and refugees to safety from the advancing Red Army. The ship was overcrowded with more than 10,500 passengers — the intended capacity was approximately 1,800 — and more than 9,000 people, including 5,000 children, lost their lives.", "https://m.media-amazon.com/images/I/91B-dLMVe7L.jpg"),
        ("Maus", "Art Spiegelman", "Historical Fiction", "Maus by Art Spiegelman is a graphic memoir about the Holocaust. It tells the story of Vladek Spiegelman, a Jewish survivor, and his experiences during World War II. The book also explores Art’s relationship with his father and the lasting effects of trauma.", "https://m.media-amazon.com/images/I/81rV+xVfJAL._AC_UF1000,1000_QL80_.jpg"),
        ("Fever 1793", "Laurie Halse Anderson", "Historical Fiction", "The historical fiction book Fever 1793 is about a young girl named Mattie who survived the yellow fever epidemic of 1793. The plot follows her journey of trying to escape Philadelphia with her grandfather.", "https://www.pluggedin.com/wp-content/uploads/2020/01/fever-1793-cover-image-694x1024.jpeg"),
        ("The Silent Patient", "Laurie Halse Anderson", "Suspense/Thriller", "Alicia Berenson’s life is seemingly perfect. A famous painter married to an in-demand fashion photographer, she lives in a grand house with big windows overlooking a park in one of London’s most desirable areas. One evening her husband Gabriel returns home late from a fashion shoot, and Alicia shoots him five times in the face, and then never speaks another word.", "https://m.media-amazon.com/images/I/81y9uCHoxrL.jpg"),
        ("One of Us is Lying", "Karen M. McManus", "Suspense/Thriller", "In Bayview High, five students walk into detention, but only four make it out alive. When Simon, the creator of the school’s notorious gossip app, dies under suspicious circumstances, the remaining students become prime suspects. Each of them has secrets they’d do anything to keep hidden—but someone knows the truth. One of Us Is Lying by Karen M. McManus is a gripping, fast-paced mystery that explores trust, betrayal, and the lengths people will go to protect their secrets.", "https://prodimage.images-bn.com/pimages/9781524714758_p0_v4_s1200x630.jpg"),
        ("One of Us Knows", "Alyssa Cole", "Suspense/Thriller", "At a picturesque lake house reunion, five childhood friends come together for the first time in years—but the joyful atmosphere is shattered when one of them is found dead. The remaining four each carry secrets from their past, and one of them knows exactly what happened. As the investigation unfolds, tensions rise and long-buried truths come to light. One of Us Knows is a gripping thriller where loyalty and betrayal blur, and no one can be trusted.", "https://m.media-amazon.com/images/I/81Qt6uTWmjL._UF1000,1000_QL80_.jpg"),
        ("The Housemaid", "Freida McFadden", "Suspense/Thriller", "The Housemaid by Freida McFadden is a chilling psychological thriller about Millie, a woman desperate for work who takes a job as a live-in housemaid for the affluent Winchester family. Their stunning mansion seems perfect, but Millie quickly realizes things are far from idyllic as she uncovers the disturbing secrets lurking behind its pristine facade. As tensions rise and paranoia sets in, Millie becomes trapped in a web of lies where nothing—and no one—is what it seems. This gripping tale of deception and survival keeps you guessing until the very last page.", "https://m.media-amazon.com/images/I/81AHTyq2wVL._AC_UF894,1000_QL80_.jpg"),
        ("The Naturals", "Jennifer Lynn Barnes", "Suspense/Thriller", "In The Naturals by Jennifer Lynn Barnes, seventeen-year-old Cassie Hobbes is recruited into a secret FBI program that trains teens with exceptional abilities to solve cold cases. Cassie's knack for profiling makes her a standout, but the pressure mounts as she’s drawn into a dangerous real-life investigation. Alongside a group of gifted but unpredictable teens, she must navigate twisted secrets and deadly stakes. This gripping YA thriller is a blend of mystery, danger, and psychological intrigue that keeps readers on edge.", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLcktkv95sUuuEu99wdzy89foPqR9RlLEQGw&s"),
        ("Gone with the Wind", "Margaret Mitchell", "Romance", "Gone with the Wind by Margaret Mitchell follows Scarlett O’Hara, a Southern belle during the Civil War and Reconstruction. She struggles to survive and rebuild her life after losing everything. The story explores love, ambition, and resilience.", "https://upload.wikimedia.org/wikipedia/commons/4/4a/Gone_with_the_Wind_%281936%2C_first_edition_cover%29.jpg"),
        ("I Hope This Doesn't Find You", "Ann Liang", "Romance", "I Hope This Doesn't Find You by Ann Liang follows Alicia, a high school senior who accidentally sends an unsent email confessing her feelings to her crush. As she scrambles to fix the situation, her best friend helps her navigate the fallout. The story explores love, friendship, and the courage to take risks.", "https://m.media-amazon.com/images/I/8177d5M8ZVL.jpg"),
        ("The Invisible Life of Addie LaRue", "V. E. Schwab", "Romance", "The Invisible Life of Addie LaRue by V.E. Schwab tells the story of Addie, a woman who makes a deal to live forever but is cursed to be forgotten by everyone she meets. For centuries, she navigates life alone until she meets someone who remembers her. The story explores themes of love, freedom, and the lasting impact of a life.", "https://covers.shakespeareandcompany.com/97817890/9781789098754.jpg"),
        ("The Fault in Our Stars", "John Green", "Romance", "The Fault in Our Stars by John Green follows Hazel Grace, a teen with cancer, who meets Augustus Waters in a support group. They fall in love and share a deep bond despite their illnesses. The story explores love, loss, and the meaning of life.", "https://m.media-amazon.com/images/I/61fbVx3W5cL._AC_UF894,1000_QL80_.jpg"),
        ("Heartstopper", "Alice Oseman", "Romance", "Heartstopper by Alice Oseman follows Charlie, a shy high school student, who develops a friendship with Nick, a popular rugby player. As their bond grows, Charlie realizes he has feelings for Nick, and Nick begins to question his own identity. The story explores love, friendship, and self-discovery.", "https://m.media-amazon.com/images/I/81vw0gIzn9L._AC_UF894,1000_QL80_.jpg"),
        ("Legend", "Marie Lu", "Dystopian", "In a future where the United States has become a militaristic society called the Republic, prodigy June Iparis is tasked with capturing Day, the country's most wanted criminal. When their paths cross, they uncover shocking truths about the Republic’s corruption and the lies they’ve been told.", "https://m.media-amazon.com/images/I/81QeWkHC6pL._AC_UF1000,1000_QL80_.jpg"),
        ("1984", "George Orwell", "Dystopian", "In a bleak future, Winston Smith lives under the oppressive rule of the Party, led by the omnipresent Big Brother. The Party controls every aspect of life, even thoughts, through relentless surveillance and propaganda. As Winston secretly rebels by seeking truth and love, he discovers the terrifying extent of the regime's power.", "https://www.magicmurals.com/media/amasty/webp/catalog/product/cache/155d73b570b90ded8a140526fcb8f2da/a/d/adg-0000001048_1_jpg.webp"),
        ("The Hunger Games", "Suzanne Collins", "Dystopian", "Set in a dystopian future where the Capitol rules over twelve districts, teenagers are forced to participate in the Hunger Games, a brutal fight to the death broadcast as entertainment. Katniss Everdeen volunteers in place of her sister and must rely on her wit, survival skills, and alliances to endure.", "https://m.media-amazon.com/images/I/71un2hI4mcL.jpg"),
        ("Divergent", "Veronica Roth", "Dystopian", "In a post-apocalyptic Chicago, society is divided into factions based on human virtues, and sixteen-year-old Tris Prior must choose where she belongs. Discovering she is Divergent—a person who doesn't fit into a single faction—Tris faces danger from a system determined to eliminate her kind.", "https://i.ebayimg.com/images/g/FHEAAOSwrOtZtosM/s-l1200.jpg"),
        ("Brave New World", "Aldous Huxley", "Dystopian", "This novel imagines a future where society is engineered for maximum stability, with people bred in hatcheries, conditioned for their roles, and kept placid through the use of a drug called soma. When Bernard Marx, an outsider within the system, questions the idealized world around him, he confronts the tensions between individuality and societal control.", "https://upload.wikimedia.org/wikipedia/commons/6/68/BraveNewWorld_FirstEdition.jpg"),
        ("Red Queen", "Victoria Aveyard", "Dystopian", "In a world divided by blood—red and silver—Mare Barrow is a Red, born with no special powers. But when she discovers she has a power unlike any Silver, she is thrust into the royal palace and forced to navigate a dangerous game of deceit, betrayal, and rebellion. As Mare becomes entangled in the politics of the elite, she must decide who to trust and how far she will go to change the world.", "https://m.media-amazon.com/images/I/81D1RbD8N0L.jpg"),
        ("A Good Girl's Guide to Murder", "Holly Jackson", "Mystery", "A Good Girl's Guide to Murder is a YA mystery novel following high schooler Pippa Fitz-Amobi. What first started as a school project, Pippa begins to dig into the murder of high schooler Andie Bell, a case that occurred five years ago, in her small town. The case is apparently closed.", "https://m.media-amazon.com/images/I/81x-tjdbZgL.jpg"),
        ("The Inheritance Games", "Jennifer Lynn Barnes", "Mystery", "The book follows Avery Kylie Grambs, a high school girl who lost her mom and is now living with her step-sister Libby. Avery has just discovered that Tobias Hawthorne, a billionaire, has left her in his will. However, Avery will not simply inherit the fortune. She must play Tobias Hawthorne's inheritance game.", "https://m.media-amazon.com/images/I/91ELakTxSZL._AC_UF894,1000_QL80_.jpg"),
        ("We Were Liars", "E. Lockhart", "Mystery", "We Were Liars is a mysterious young adult novel about a wealthy family who spends every summer on their private island. The story focuses on the main character, Cadence. After Cadence suffers a head injury during one of the summers, she cannot remember almost anything from that trip to the island.", "https://images.penguinrandomhouse.com/cover/9780385741279"),
        ("Truly Devious", "Maureen Johnson", "Mystery", "The premise of this book follows Stevie Bell as she is given a once in a lifetime chance to attend a prestigious boarding school. But this isn't a normal school, this is the place where the crime she has always been obsessed with took place, and she is determined to solve it.", "https://m.media-amazon.com/images/I/71yU7yRcd2L._AC_UF894,1000_QL80_.jpg"),
        ("Two Can Keep A Secret", "Karen M. McManus", "Mystery", "Two Can Keep a Secret is a story of two high schoolers told in alternating first-person point of view. The first is Ellery Corcoran, who has moved to live with her grandmother in the small town of Echo Ridge with her twin brother, Ezra, after their actress mother, Sadie, is forced into rehab.", "https://m.media-amazon.com/images/I/91-+JSk4XbL.jpg"),
    ]  
  
    # Insert the books data into the table
    for book in books_data:
        new_book = Book(
            title=book[0],
            author=book[1],
            genre=book[2],
            description=book[3],
            cover_image_url=book[4]
        )
        db.session.add(new_book)
    
    # Commit the transaction to the database
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        print("IntegrityError: Could be a duplicate entry or violation of database constraints.")
    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
    
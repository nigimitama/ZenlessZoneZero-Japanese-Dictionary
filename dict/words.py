from dict import Record, Category


PARTIES = [
    Record(reading="じゃとや", word="邪兎屋", category=Category.NOUN),
    Record(reading="はくぎじゅうこう", word="白祇重工", category=Category.NOUN),
    Record(reading="ゔぃくとりあかせい", word="ヴィクトリア家政", category=Category.NOUN),
    Record(reading="とくむそうさはん", word="特務捜査班", category=Category.NOUN),
    Record(reading="たいほろうろっか", word="対ホロウ6課", category=Category.NOUN),
    Record(reading="かりゅどーんのこ", word="カリュドーンの子", category=Category.NOUN),
    Record(reading="おぼるすしょうたい", word="オボルス小隊", category=Category.NOUN),
]


ITEMS = [
    Record(reading="さいげつのはくへん", word="歳月の薄片", category=Category.NOUN),
    Record(reading="さいげつ", word="歳月の薄片", category=Category.NOUN),
    Record(reading="ねんごくぎあ", word="燃獄ギア", category=Category.NOUN),
    Record(reading="こうばく", word="拘縛", category=Category.NOUN),
    Record(reading="こうばくされしもの", word="拘縛されし者", category=Category.NOUN),
    Record(reading="ぎょっこせいひょう", word="玉壺青氷", category=Category.NOUN),
    Record(reading="かしん", word="花信", category=Category.NOUN),
]


CHARACTERS = [
    Record(reading="ほしみみやび", word="星見雅", category=Category.NAME),
    Record(reading="あさばはるまさ", word="浅羽悠真", category=Category.NAME),
    Record(reading="はるまさ", word="悠真", category=Category.NAME),
    Record(reading="ねこみやまな", word="猫宮又奈", category=Category.NAME),
    Record(reading="しゅえん", word="朱鳶", category=Category.NAME),
    Record(reading="ちんいー", word="青衣", category=Category.NAME),
    Record(reading="そうかく", word="蒼角", category=Category.NAME),
]


LOCATIONS = [
    Record(reading="しんえりーと", word="新エリー都", category=Category.LOCATION),
    Record(reading="ぜろごうほろう", word="零号ホロウ", category=Category.LOCATION),
    Record(reading="ろくぶんがい", word="六分街", category=Category.LOCATION),
    Record(reading="こくがんがい", word="黒雁街", category=Category.LOCATION),
]


OTHERS = [
    Record(reading="おんどうき", word="音動機", category=Category.NOUN),
    Record(reading="しきよぼうえいせん", word="式輿防衛戦", category=Category.NOUN),
    Record(reading="しきよ", word="式輿", category=Category.NOUN),
    Record(reading="とうこうかえん", word="刀耕火炎", category=Category.NOUN),
]


RECORDS = sum([ITEMS, PARTIES, CHARACTERS, LOCATIONS, OTHERS], [])

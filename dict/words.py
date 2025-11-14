from dict import Record, Category


PARTIES = [
    Record(reading="じゃとや", word="邪兎屋", category=Category.NOUN),
    Record(reading="はくぎじゅうこう", word="白祇重工", category=Category.NOUN),
    Record(reading="ゔぃくとりあかせい", word="ヴィクトリア家政", category=Category.NOUN),
    Record(reading="とくむそうさはん", word="特務捜査班", category=Category.NOUN),
    Record(reading="たいほろうろっか", word="対ホロウ6課", category=Category.NOUN),
    Record(reading="かりゅどーんのこ", word="カリュドーンの子", category=Category.NOUN),
    Record(reading="おぼるすしょうたい", word="オボルス小隊", category=Category.NOUN),
    Record(reading="うんがくさん", word="雲嶽山", category=Category.NOUN),
    Record(reading="かいたんや", word="怪啖屋", category=Category.NOUN),
    Record(reading="くらんぷすのくろえだ", word="クランプスの黒枝", category=Category.NOUN),
]


ITEMS = [
    Record(reading="さいげつのはくへん", word="歳月の薄片", category=Category.NOUN),
    Record(reading="さいげつ", word="歳月の薄片", category=Category.NOUN),
    Record(reading="ねんごくぎあ", word="燃獄ギア", category=Category.NOUN),
    Record(reading="こうばく", word="拘縛", category=Category.NOUN),
    Record(reading="こうばくされしもの", word="拘縛されし者", category=Category.NOUN),
    Record(reading="ぎょっこせいひょう", word="玉壺青氷", category=Category.NOUN),
    Record(reading="かしん", word="花信", category=Category.NOUN),
    Record(reading="あられおつせいでん", word="あられ落つ星殿", category=Category.NOUN),
    Record(reading="せいでん", word="星殿", category=Category.NOUN),
    Record(reading="こくりゅう", word="刻流", category=Category.NOUN),
    Record(reading="じょざい", word="助剤", category=Category.NOUN),
]


CHARACTERS = [
    Record(reading="ほしみみやび", word="星見雅", category=Category.NAME),
    Record(reading="あさばはるまさ", word="浅羽悠真", category=Category.NAME),
    Record(reading="はるまさ", word="悠真", category=Category.NAME),
    Record(reading="ねこみやまな", word="猫宮又奈", category=Category.NAME),
    Record(reading="ねこみや", word="猫宮", category=Category.NAME),
    Record(reading="まな", word="又奈", category=Category.NAME),
    Record(reading="しゅえん", word="朱鳶", category=Category.NAME),
    Record(reading="ちんいー", word="青衣", category=Category.NAME),
    Record(reading="そうかく", word="蒼角", category=Category.NAME),
    Record(reading="ちーふーふー", word="橘福福", category=Category.NAME),
    Record(reading="ふーふー", word="福福", category=Category.NAME),
    Record(reading="ざお", word="照", category=Category.NAME),
    Record(reading="いーしぇん", word="儀玄", category=Category.NAME),
    Record(reading="いーしゃん", word="儀降", category=Category.NAME),
    Record(reading="ぱん", word="潘", category=Category.NAME),
    Record(reading="いんふー", word="引壺", category=Category.NAME),
    Record(reading="うきなみゆずは", word="浮波柚葉", category=Category.NAME),
    Record(reading="うきなみ", word="浮波", category=Category.NAME),
    Record(reading="いぇーしゅんがん", word="葉瞬光", category=Category.NAME),
    Record(reading="ようしゅんこう", word="葉瞬光", category=Category.NAME),
    Record(reading="ようしゃくえん", word="葉釈淵", category=Category.NAME),
    Record(reading="こまのまなと", word="狛野真斗", category=Category.NAME),
    Record(reading="こまの", word="狛野", category=Category.NAME),
    Record(reading="まなと", word="真斗", category=Category.NAME),
    Record(reading="ばんがく", word="盤岳", category=Category.NAME),
    Record(reading="ふぉんどー", word="紅豆", category=Category.NAME),
]


LOCATIONS = [
    Record(reading="しんえりーと", word="新エリー都", category=Category.LOCATION),
    Record(reading="ぜろごうほろう", word="零号ホロウ", category=Category.LOCATION),
    Record(reading="ろくぶんがい", word="六分街", category=Category.LOCATION),
    Record(reading="こくがんがい", word="黒雁街", category=Category.LOCATION),
    Record(reading="えいひちく", word="衛非地区", category=Category.LOCATION),
    Record(reading="ちょうきへい", word="澄輝坪", category=Category.LOCATION),
    Record(reading="だいちこうたい", word="大地溝帯", category=Category.LOCATION),
]


OTHERS = [
    Record(reading="おんどうき", word="音動機", category=Category.NOUN),
    Record(reading="しきよぼうえいせん", word="式輿防衛戦", category=Category.NOUN),
    Record(reading="しきよ", word="式輿", category=Category.NOUN),
    Record(reading="とうこうかえん", word="刀耕火炎", category=Category.NOUN),
    Record(reading="とうこう", word="刀耕", category=Category.NOUN),
    Record(reading="ききょくきょうしゅうせん", word="危局強襲戦", category=Category.NOUN),
    Record(reading="きゅうと", word="旧都", category=Category.NOUN),
    Record(reading="さんしょうかい", word="讃頌会", category=Category.NOUN),
    Record(reading="いじょうしょうあく", word="異常掌握", category=Category.NOUN),
    Record(reading="めいは", word="命破", category=Category.NOUN),
    Record(reading="うつろがり", word="虚狩り", category=Category.NOUN),
    Record(reading="こうじ", word="輝磁", category=Category.NOUN),
    Record(reading="こうれいせき", word="輝嶺石", category=Category.NOUN),
    Record(reading="せいめいちょう", word="青溟鳥", category=Category.NOUN),
    Record(reading="せきがぐみ", word="赤牙組", category=Category.NOUN),
    Record(reading="せいめいけん", word="青溟剣", category=Category.NOUN),
]


RECORDS = sum([ITEMS, PARTIES, CHARACTERS, LOCATIONS, OTHERS], [])

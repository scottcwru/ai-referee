# Step 3. Shuffled batch order for the derivation runs

The 337 reports in `step3_corpus_batch01.md`–`batch07.md` are listed there in collection order, which groups them by venue.
For Steps 4–8 they are reshuffled so that every batch mixes venues and a change of venue cannot masquerade as a new dimension.
Method: Python `random.Random(20260924).shuffle()` over report numbers 1–337, then consecutive blocks of 50 (batch 07 holds 37).
The script is deterministic, so the same seed reproduces this order exactly. Report numbers refer to the collection-order files.

## Venue mix per shuffled batch

| Shuffled batch | Reports | eLife | PeerJ | PLOS ONE | PCI RR | RSOS | OpenReview |
|--:|--:|--:|--:|--:|--:|--:|--:|
| 01 | 50 | 9 | 6 | 18 | 11 | 2 | 4 |
| 02 | 50 | 11 | 7 | 22 | 6 | 2 | 2 |
| 03 | 50 | 9 | 10 | 27 | 4 | 0 | 0 |
| 04 | 50 | 15 | 9 | 18 | 3 | 1 | 4 |
| 05 | 50 | 14 | 5 | 18 | 4 | 4 | 5 |
| 06 | 50 | 11 | 6 | 24 | 7 | 0 | 2 |
| 07 | 37 | 5 | 3 | 20 | 6 | 0 | 3 |

## Order

| Shuffled batch | Position | Report # | Venue | Reviewer label | Report URL |
|--:|--:|--:|:--|:--|:--|
| 01 | 1 | 300 | PCI Registered Reports | James Green (round 1) | https://rr.peercommunityin.org/articles/rec?id=966 |
| 01 | 2 | 48 | eLife | Reviewer #1 | https://elifesciences.org/articles/108748/peer-reviews |
| 01 | 3 | 178 | PLOS ONE | Reviewer 4 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0288966 |
| 01 | 4 | 9 | eLife | Reviewer #1 | https://elifesciences.org/articles/94231/peer-reviews |
| 01 | 5 | 225 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0307137 |
| 01 | 6 | 51 | eLife | Reviewer #4 | https://elifesciences.org/articles/108748/peer-reviews |
| 01 | 7 | 80 | PeerJ | Reviewer 3 | https://peerj.com/articles/21199/reviews/ |
| 01 | 8 | 268 | PCI Registered Reports | Marko Nardini (round 1) | https://rr.peercommunityin.org/articles/rec?id=1346 |
| 01 | 9 | 228 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0298523 |
| 01 | 10 | 34 | eLife | Reviewer #1 | https://elifesciences.org/articles/107765/peer-reviews |
| 01 | 11 | 289 | PCI Registered Reports | Fabian Dablander (round 1) | https://rr.peercommunityin.org/articles/rec?id=1664 |
| 01 | 12 | 235 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296421 |
| 01 | 13 | 57 | eLife | Reviewer #1 | https://elifesciences.org/reviewed-preprints/111043/reviews |
| 01 | 14 | 117 | PeerJ | Reviewer 2 | https://peerj.com/articles/18682/reviews/ |
| 01 | 15 | 320 | EMNLP 2020 Workshop NLP-COVID | AnonReviewer4 | https://openreview.net/forum?id=WsZ2gYorQ0u&noteId=93QlqVyv72L |
| 01 | 16 | 288 | PCI Registered Reports | Cameron Brick (round 1) | https://rr.peercommunityin.org/articles/rec?id=1664 |
| 01 | 17 | 325 | Graphics Interface 2021 (2nd cycle) | Reviewer_6VTa | https://openreview.net/forum?id=XpPWPdX6Tv&noteId=cq3HuuexrPO |
| 01 | 18 | 47 | eLife | Reviewer #2 | https://elifesciences.org/articles/106136/peer-reviews |
| 01 | 19 | 233 | PLOS ONE | Reviewer 3 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0297587 |
| 01 | 20 | 263 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0299578 |
| 01 | 21 | 181 | PLOS ONE | Reviewer 1 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296944 |
| 01 | 22 | 125 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0290253 |
| 01 | 23 | 154 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0289845 |
| 01 | 24 | 285 | PCI Registered Reports | Anonymous reviewer 1 (round 1) | https://rr.peercommunityin.org/articles/rec?id=2566 |
| 01 | 25 | 294 | PCI Registered Reports | Matt Williams (round 1) | https://rr.peercommunityin.org/articles/rec?id=1145 |
| 01 | 26 | 315 | Royal Society Open Science | Reviewer 3 (round 1) | https://www.webofscience.com/api/gateway/wos/peer-review/10.1098/rsos.242167 |
| 01 | 27 | 104 | PeerJ | Reviewer 3 | https://peerj.com/articles/19401/reviews/ |
| 01 | 28 | 272 | PCI Registered Reports | Zoltan Dienes (round 2) | https://rr.peercommunityin.org/articles/rec?id=1701 |
| 01 | 29 | 275 | PCI Registered Reports | Leah Petrutiu (round 3) | https://rr.peercommunityin.org/articles/rec?id=1701 |
| 01 | 30 | 146 | PLOS ONE | Reviewer 3 (round 3) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0284179 |
| 01 | 31 | 102 | PeerJ | Reviewer 1 | https://peerj.com/articles/19401/reviews/ |
| 01 | 32 | 37 | eLife | Reviewer #2 | https://elifesciences.org/articles/103734/peer-reviews |
| 01 | 33 | 42 | eLife | Reviewer #2 | https://elifesciences.org/articles/87271/peer-reviews |
| 01 | 34 | 138 | PLOS ONE | Reviewer 2 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0285800 |
| 01 | 35 | 95 | PeerJ | Reviewer 1 | https://peerj.com/articles/19913/reviews/ |
| 01 | 36 | 46 | eLife | Reviewer #1 | https://elifesciences.org/articles/106136/peer-reviews |
| 01 | 37 | 283 | PCI Registered Reports | Katelynn Carter-Rogers (round 2) | https://rr.peercommunityin.org/articles/rec?id=2500 |
| 01 | 38 | 329 | Graphics Interface 2021 | AnonReviewer1 | https://openreview.net/forum?id=OlB9_lxU5GO&noteId=gMblWAy_HNB |
| 01 | 39 | 157 | PLOS ONE | Reviewer 3 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0289845 |
| 01 | 40 | 337 | NeurIPS 2025 Position Paper Track | Reviewer_nFi7 | https://openreview.net/forum?id=mdKzkjY1dM&noteId=t7w7O9k8qI |
| 01 | 41 | 135 | PLOS ONE | Reviewer 2 (round 3) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0293188 |
| 01 | 42 | 314 | Royal Society Open Science | Reviewer 2 (round 1) | https://www.webofscience.com/api/gateway/wos/peer-review/10.1098/rsos.242167 |
| 01 | 43 | 205 | PLOS ONE | Reviewer 2 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0297408 |
| 01 | 44 | 271 | PCI Registered Reports | Zoltan Dienes (round 1) | https://rr.peercommunityin.org/articles/rec?id=1701 |
| 01 | 45 | 121 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0288346 |
| 01 | 46 | 245 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0306629 |
| 01 | 47 | 184 | PLOS ONE | Reviewer 4 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296944 |
| 01 | 48 | 79 | PeerJ | Reviewer 1 | https://peerj.com/articles/21199/reviews/ |
| 01 | 49 | 239 | PLOS ONE | Reviewer 1 (round 3) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296421 |
| 01 | 50 | 301 | PCI Registered Reports | Anonymous reviewer 1 (round 1) | https://rr.peercommunityin.org/articles/rec?id=966 |
| 02 | 51 | 160 | PLOS ONE | Reviewer 3 (round 3) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0289845 |
| 02 | 52 | 149 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0288883 |
| 02 | 53 | 33 | eLife | Reviewer #3 | https://elifesciences.org/articles/93755/peer-reviews |
| 02 | 54 | 251 | PLOS ONE | Reviewer 2 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0302173 |
| 02 | 55 | 309 | Royal Society Open Science | Reviewer 1 (round 1) | https://www.webofscience.com/api/gateway/wos/peer-review/10.1098/rsos.230224 |
| 02 | 56 | 134 | PLOS ONE | Reviewer 1 (round 3) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0293188 |
| 02 | 57 | 124 | PLOS ONE | Reviewer 2 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0288346 |
| 02 | 58 | 38 | eLife | Reviewer #1 | https://elifesciences.org/articles/103736/peer-reviews |
| 02 | 59 | 281 | PCI Registered Reports | Cassandra Grinstead (round 1) | https://rr.peercommunityin.org/articles/rec?id=1949 |
| 02 | 60 | 274 | PCI Registered Reports | Leah Petrutiu (round 2) | https://rr.peercommunityin.org/articles/rec?id=1701 |
| 02 | 61 | 73 | eLife | Reviewer #2 | https://elifesciences.org/reviewed-preprints/106725/reviews |
| 02 | 62 | 101 | PeerJ | Reviewer 2 | https://peerj.com/articles/19444/reviews/ |
| 02 | 63 | 299 | PCI Registered Reports | Tyler Jacobs (round 1) | https://rr.peercommunityin.org/articles/rec?id=966 |
| 02 | 64 | 206 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0307401 |
| 02 | 65 | 267 | PLOS ONE | Reviewer 1 (round 3) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0299578 |
| 02 | 66 | 151 | PLOS ONE | Reviewer 1 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0288883 |
| 02 | 67 | 65 | eLife | Reviewer #1 | https://elifesciences.org/reviewed-preprints/108428/reviews |
| 02 | 68 | 264 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0299578 |
| 02 | 69 | 257 | PLOS ONE | Reviewer 1 (round 3) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0305554 |
| 02 | 70 | 203 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0297408 |
| 02 | 71 | 330 | Graphics Interface 2023 | Reviewer_W7yE | https://openreview.net/forum?id=Ip9enUtMd8d&noteId=ZAsL3mESL_e |
| 02 | 72 | 97 | PeerJ | Reviewer 3 | https://peerj.com/articles/19913/reviews/ |
| 02 | 73 | 114 | PeerJ | Reviewer 1 | https://peerj.com/articles/18900/reviews/ |
| 02 | 74 | 70 | eLife | Reviewer #2 | https://elifesciences.org/reviewed-preprints/90684/reviews |
| 02 | 75 | 305 | PCI Registered Reports | Michele Vicovaro (round 1) | https://rr.peercommunityin.org/articles/rec?id=1213 |
| 02 | 76 | 168 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0292284 |
| 02 | 77 | 64 | eLife | Reviewer #2 | https://elifesciences.org/reviewed-preprints/98487/reviews |
| 02 | 78 | 100 | PeerJ | Reviewer 2 | https://peerj.com/articles/19554/reviews/ |
| 02 | 79 | 17 | eLife | Reviewer #3 | https://elifesciences.org/articles/107223/peer-reviews |
| 02 | 80 | 278 | PCI Registered Reports | Myron Tsikandilakis (round 1) | https://rr.peercommunityin.org/articles/rec?id=2017 |
| 02 | 81 | 133 | PLOS ONE | Reviewer 2 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0293188 |
| 02 | 82 | 2 | eLife | Reviewer #2 | https://elifesciences.org/articles/106073/peer-reviews |
| 02 | 83 | 218 | PLOS ONE | Reviewer 1 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0299381 |
| 02 | 84 | 109 | PeerJ | Reviewer 1 | https://peerj.com/articles/19164/reviews/ |
| 02 | 85 | 14 | eLife | Reviewer #2 | https://elifesciences.org/articles/102800/peer-reviews |
| 02 | 86 | 10 | eLife | Reviewer #1 | https://elifesciences.org/articles/105025/peer-reviews |
| 02 | 87 | 84 | PeerJ | Reviewer 1 | https://peerj.com/articles/20567/reviews/ |
| 02 | 88 | 308 | PCI Registered Reports | Anonymous reviewer 1 (round 1) | https://rr.peercommunityin.org/articles/rec?id=1914 |
| 02 | 89 | 88 | PeerJ | Reviewer 1 | https://peerj.com/articles/20417/reviews/ |
| 02 | 90 | 214 | PLOS ONE | Reviewer 3 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296524 |
| 02 | 91 | 317 | Royal Society Open Science | Reviewer 2 (round 1) | https://www.webofscience.com/api/gateway/wos/peer-review/10.1098/rsos.250377 |
| 02 | 92 | 211 | PLOS ONE | Reviewer 3 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296524 |
| 02 | 93 | 215 | PLOS ONE | Reviewer 4 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296524 |
| 02 | 94 | 242 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0297241 |
| 02 | 95 | 224 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0307137 |
| 02 | 96 | 231 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0297587 |
| 02 | 97 | 63 | eLife | Reviewer #2 | https://elifesciences.org/reviewed-preprints/98487/reviews |
| 02 | 98 | 185 | PLOS ONE | Reviewer 1 (round 3) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296944 |
| 02 | 99 | 248 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0294372 |
| 02 | 100 | 333 | NeurIPS 2024 (poster) | Reviewer_1Xcr | https://openreview.net/forum?id=7XkwzaPMvX&noteId=ELLy1oaGJB |
| 03 | 101 | 244 | PLOS ONE | Reviewer 3 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0297241 |
| 03 | 102 | 208 | PLOS ONE | Reviewer 3 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0307401 |
| 03 | 103 | 59 | eLife | Reviewer #3 | https://elifesciences.org/reviewed-preprints/111043/reviews |
| 03 | 104 | 91 | PeerJ | Reviewer 2 | https://peerj.com/articles/20411/reviews/ |
| 03 | 105 | 246 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0306629 |
| 03 | 106 | 77 | PeerJ | Reviewer 3 | https://peerj.com/articles/21383/reviews/ |
| 03 | 107 | 68 | eLife | Reviewer #3 | https://elifesciences.org/reviewed-preprints/102780/reviews |
| 03 | 108 | 247 | PLOS ONE | Reviewer 3 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0306629 |
| 03 | 109 | 230 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0297587 |
| 03 | 110 | 92 | PeerJ | Reviewer 1 | https://peerj.com/articles/20340/reviews/ |
| 03 | 111 | 237 | PLOS ONE | Reviewer 2 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296421 |
| 03 | 112 | 255 | PLOS ONE | Reviewer 1 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0305554 |
| 03 | 113 | 120 | PeerJ | Reviewer 2 | https://peerj.com/articles/13063/reviews/ |
| 03 | 114 | 53 | eLife | Reviewer #3 | https://elifesciences.org/articles/93887/peer-reviews |
| 03 | 115 | 187 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0310031 |
| 03 | 116 | 175 | PLOS ONE | Reviewer 3 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0288966 |
| 03 | 117 | 221 | PLOS ONE | Reviewer 3 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0314967 |
| 03 | 118 | 256 | PLOS ONE | Reviewer 2 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0305554 |
| 03 | 119 | 69 | eLife | Reviewer #1 | https://elifesciences.org/reviewed-preprints/90684/reviews |
| 03 | 120 | 110 | PeerJ | Reviewer 2 | https://peerj.com/articles/19086/reviews/ |
| 03 | 121 | 262 | PLOS ONE | Reviewer 3 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0310491 |
| 03 | 122 | 199 | PLOS ONE | Reviewer 3 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0301299 |
| 03 | 123 | 243 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0297241 |
| 03 | 124 | 169 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0292284 |
| 03 | 125 | 297 | PCI Registered Reports | Jana Kesenheimer (round 1) | https://rr.peercommunityin.org/articles/rec?id=1560 |
| 03 | 126 | 119 | PeerJ | Reviewer 1 | https://peerj.com/articles/13811/reviews/ |
| 03 | 127 | 164 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0286336 |
| 03 | 128 | 108 | PeerJ | Reviewer 3 | https://peerj.com/articles/19307/reviews/ |
| 03 | 129 | 94 | PeerJ | Reviewer 1 | https://peerj.com/articles/19969/reviews/ |
| 03 | 130 | 191 | PLOS ONE | Reviewer 1 (round 3) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0310031 |
| 03 | 131 | 155 | PLOS ONE | Reviewer 3 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0289845 |
| 03 | 132 | 139 | PLOS ONE | Reviewer 2 (round 3) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0285800 |
| 03 | 133 | 85 | PeerJ | Reviewer 2 | https://peerj.com/articles/20567/reviews/ |
| 03 | 134 | 302 | PCI Registered Reports | Miguel Vadillo (round 1) | https://rr.peercommunityin.org/articles/rec?id=1842 |
| 03 | 135 | 223 | PLOS ONE | Reviewer 3 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0314967 |
| 03 | 136 | 62 | eLife | Reviewer #1 | https://elifesciences.org/reviewed-preprints/98487/reviews |
| 03 | 137 | 196 | PLOS ONE | Reviewer 3 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0306121 |
| 03 | 138 | 18 | eLife | Reviewer #1 | https://elifesciences.org/reviewed-preprints/108521/reviews |
| 03 | 139 | 58 | eLife | Reviewer #2 | https://elifesciences.org/reviewed-preprints/111043/reviews |
| 03 | 140 | 140 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0284179 |
| 03 | 141 | 107 | PeerJ | Reviewer 2 | https://peerj.com/articles/19307/reviews/ |
| 03 | 142 | 122 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0288346 |
| 03 | 143 | 279 | PCI Registered Reports | Surya Gayet (round 1) | https://rr.peercommunityin.org/articles/rec?id=2017 |
| 03 | 144 | 254 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0305554 |
| 03 | 145 | 60 | eLife | Reviewer #1 | https://elifesciences.org/reviewed-preprints/101021/reviews |
| 03 | 146 | 52 | eLife | Reviewer #2 | https://elifesciences.org/articles/93887/peer-reviews |
| 03 | 147 | 197 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0301299 |
| 03 | 148 | 303 | PCI Registered Reports | Lachlan Deer (round 1) | https://rr.peercommunityin.org/articles/rec?id=1842 |
| 03 | 149 | 226 | PLOS ONE | Reviewer 1 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0307137 |
| 03 | 150 | 183 | PLOS ONE | Reviewer 3 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296944 |
| 04 | 151 | 318 | EMNLP 2020 Workshop NLP-COVID (oral) | AnonReviewer3 | https://openreview.net/forum?id=txOTpsCuQwT&noteId=b-3d98B6O6 |
| 04 | 152 | 200 | PLOS ONE | Reviewer 4 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0301299 |
| 04 | 153 | 165 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0286336 |
| 04 | 154 | 336 | NeurIPS 2025 Position Paper Track | Reviewer_FK6j | https://openreview.net/forum?id=mdKzkjY1dM&noteId=bOPTU3OVP8 |
| 04 | 155 | 26 | eLife | Reviewer #1 | https://elifesciences.org/articles/101157/peer-reviews |
| 04 | 156 | 50 | eLife | Reviewer #3 | https://elifesciences.org/articles/108748/peer-reviews |
| 04 | 157 | 174 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0288966 |
| 04 | 158 | 261 | PLOS ONE | Reviewer 1 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0310491 |
| 04 | 159 | 36 | eLife | Reviewer #1 | https://elifesciences.org/articles/103734/peer-reviews |
| 04 | 160 | 163 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0288802 |
| 04 | 161 | 148 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0293306 |
| 04 | 162 | 5 | eLife | Reviewer #2 | https://elifesciences.org/articles/103566/peer-reviews |
| 04 | 163 | 4 | eLife | Reviewer #1 | https://elifesciences.org/articles/103566/peer-reviews |
| 04 | 164 | 44 | eLife | Reviewer #2 | https://elifesciences.org/articles/91011/peer-reviews |
| 04 | 165 | 82 | PeerJ | Reviewer 2 | https://peerj.com/articles/21138/reviews/ |
| 04 | 166 | 105 | PeerJ | Reviewer 1 | https://peerj.com/articles/19314/reviews/ |
| 04 | 167 | 326 | Graphics Interface 2021 (2nd cycle) | Reviewer_ATZe | https://openreview.net/forum?id=HG7FQ7-KKf&noteId=hnJA94aa8XR |
| 04 | 168 | 74 | eLife | Reviewer #3 | https://elifesciences.org/reviewed-preprints/106725/reviews |
| 04 | 169 | 145 | PLOS ONE | Reviewer 1 (round 3) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0284179 |
| 04 | 170 | 202 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0297408 |
| 04 | 171 | 322 | Graphics Interface 2021 | AnonReviewer3 | https://openreview.net/forum?id=3SbafIvrf3F&noteId=O_u3MOKWlS |
| 04 | 172 | 22 | eLife | Reviewer #3 | https://elifesciences.org/articles/101371/peer-reviews |
| 04 | 173 | 153 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0289845 |
| 04 | 174 | 147 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0293306 |
| 04 | 175 | 295 | PCI Registered Reports | Amélie Gourdon-Kanhukamwe (round 1) | https://rr.peercommunityin.org/articles/rec?id=1145 |
| 04 | 176 | 41 | eLife | Reviewer #1 | https://elifesciences.org/articles/87271/peer-reviews |
| 04 | 177 | 24 | eLife | Reviewer #2 | https://elifesciences.org/articles/102228/peer-reviews |
| 04 | 178 | 40 | eLife | Reviewer #3 | https://elifesciences.org/articles/103736/peer-reviews |
| 04 | 179 | 118 | PeerJ | Reviewer 2 | https://peerj.com/articles/18821/reviews/ |
| 04 | 180 | 166 | PLOS ONE | Reviewer 1 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0286336 |
| 04 | 181 | 32 | eLife | Reviewer #2 | https://elifesciences.org/articles/93755/peer-reviews |
| 04 | 182 | 87 | PeerJ | Reviewer 3 | https://peerj.com/articles/20444/reviews/ |
| 04 | 183 | 72 | eLife | Reviewer #1 | https://elifesciences.org/reviewed-preprints/106725/reviews |
| 04 | 184 | 284 | PCI Registered Reports | Christopher Hopwood (round 1) | https://rr.peercommunityin.org/articles/rec?id=2566 |
| 04 | 185 | 83 | PeerJ | Reviewer 1 | https://peerj.com/articles/21130/reviews/ |
| 04 | 186 | 210 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296524 |
| 04 | 187 | 207 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0307401 |
| 04 | 188 | 198 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0301299 |
| 04 | 189 | 186 | PLOS ONE | Reviewer 3 (round 3) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296944 |
| 04 | 190 | 43 | eLife | Reviewer #1 | https://elifesciences.org/articles/91011/peer-reviews |
| 04 | 191 | 127 | PLOS ONE | Reviewer 1 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0290253 |
| 04 | 192 | 161 | PLOS ONE | Reviewer 4 (round 3) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0289845 |
| 04 | 193 | 93 | PeerJ | Reviewer 1 | https://peerj.com/articles/20153/reviews/ |
| 04 | 194 | 99 | PeerJ | Reviewer 2 | https://peerj.com/articles/19587/reviews/ |
| 04 | 195 | 111 | PeerJ | Reviewer 1 | https://peerj.com/articles/19022/reviews/ |
| 04 | 196 | 266 | PLOS ONE | Reviewer 2 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0299578 |
| 04 | 197 | 313 | Royal Society Open Science | Reviewer 1 (round 1) | https://www.webofscience.com/api/gateway/wos/peer-review/10.1098/rsos.242167 |
| 04 | 198 | 116 | PeerJ | Reviewer 1 | https://peerj.com/articles/18682/reviews/ |
| 04 | 199 | 28 | eLife | Reviewer #1 | https://elifesciences.org/articles/96803/peer-reviews |
| 04 | 200 | 270 | PCI Registered Reports | Anonymous reviewer 1 (round 1) | https://rr.peercommunityin.org/articles/rec?id=1346 |
| 05 | 201 | 321 | Graphics Interface 2021 | AnonReviewer1 | https://openreview.net/forum?id=3SbafIvrf3F&noteId=AUOFoxaxkaE |
| 05 | 202 | 195 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0306121 |
| 05 | 203 | 90 | PeerJ | Reviewer 1 | https://peerj.com/articles/20411/reviews/ |
| 05 | 204 | 3 | eLife | Reviewer #3 | https://elifesciences.org/articles/106073/peer-reviews |
| 05 | 205 | 312 | Royal Society Open Science | Reviewer 2 (round 1) | https://www.webofscience.com/api/gateway/wos/peer-review/10.1098/rsos.231240 |
| 05 | 206 | 220 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0314967 |
| 05 | 207 | 15 | eLife | Reviewer #1 | https://elifesciences.org/articles/107223/peer-reviews |
| 05 | 208 | 217 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0299381 |
| 05 | 209 | 319 | EMNLP 2020 Workshop NLP-COVID (oral) | AnonReviewer1 | https://openreview.net/forum?id=txOTpsCuQwT&noteId=4nLNUz4fNgv |
| 05 | 210 | 269 | PCI Registered Reports | Maxine Sherman (round 1) | https://rr.peercommunityin.org/articles/rec?id=1346 |
| 05 | 211 | 21 | eLife | Reviewer #2 | https://elifesciences.org/articles/101371/peer-reviews |
| 05 | 212 | 27 | eLife | Reviewer #2 | https://elifesciences.org/articles/101157/peer-reviews |
| 05 | 213 | 49 | eLife | Reviewer #2 | https://elifesciences.org/articles/108748/peer-reviews |
| 05 | 214 | 144 | PLOS ONE | Reviewer 3 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0284179 |
| 05 | 215 | 67 | eLife | Reviewer #1 | https://elifesciences.org/reviewed-preprints/102780/reviews |
| 05 | 216 | 172 | PLOS ONE | Reviewer 2 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0292284 |
| 05 | 217 | 152 | PLOS ONE | Reviewer 2 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0288883 |
| 05 | 218 | 332 | NeurIPS 2024 (poster) | Reviewer_9s1B | https://openreview.net/forum?id=7XkwzaPMvX&noteId=NlLEC9LGMr |
| 05 | 219 | 23 | eLife | Reviewer #1 | https://elifesciences.org/articles/102228/peer-reviews |
| 05 | 220 | 129 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0289687 |
| 05 | 221 | 259 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0310491 |
| 05 | 222 | 173 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0288966 |
| 05 | 223 | 316 | Royal Society Open Science | Reviewer 1 (round 1) | https://www.webofscience.com/api/gateway/wos/peer-review/10.1098/rsos.250377 |
| 05 | 224 | 204 | PLOS ONE | Reviewer 1 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0297408 |
| 05 | 225 | 290 | PCI Registered Reports | Fabian Dablander (round 2) | https://rr.peercommunityin.org/articles/rec?id=1664 |
| 05 | 226 | 170 | PLOS ONE | Reviewer 3 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0292284 |
| 05 | 227 | 78 | PeerJ | Reviewer 2 | https://peerj.com/articles/21286/reviews/ |
| 05 | 228 | 273 | PCI Registered Reports | Kai Hiraishi (round 2) | https://rr.peercommunityin.org/articles/rec?id=1701 |
| 05 | 229 | 162 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0288802 |
| 05 | 230 | 291 | PCI Registered Reports | Cameron Brick (round 2) | https://rr.peercommunityin.org/articles/rec?id=1664 |
| 05 | 231 | 240 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0307660 |
| 05 | 232 | 16 | eLife | Reviewer #2 | https://elifesciences.org/articles/107223/peer-reviews |
| 05 | 233 | 35 | eLife | Reviewer #2 | https://elifesciences.org/articles/107765/peer-reviews |
| 05 | 234 | 328 | Graphics Interface 2021 (2nd cycle) | Reviewer_C7ZB | https://openreview.net/forum?id=HG7FQ7-KKf&noteId=nSMppCXQsDV |
| 05 | 235 | 132 | PLOS ONE | Reviewer 1 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0293188 |
| 05 | 236 | 29 | eLife | Reviewer #2 | https://elifesciences.org/articles/96803/peer-reviews |
| 05 | 237 | 182 | PLOS ONE | Reviewer 2 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296944 |
| 05 | 238 | 311 | Royal Society Open Science | Reviewer 1 (round 1) | https://www.webofscience.com/api/gateway/wos/peer-review/10.1098/rsos.231240 |
| 05 | 239 | 54 | eLife | Reviewer #1 | https://elifesciences.org/reviewed-preprints/112321/reviews |
| 05 | 240 | 156 | PLOS ONE | Reviewer 1 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0289845 |
| 05 | 241 | 334 | NeurIPS 2024 (poster) | Reviewer_L1hd | https://openreview.net/forum?id=7XkwzaPMvX&noteId=XRUbeX75Dk |
| 05 | 242 | 176 | PLOS ONE | Reviewer 4 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0288966 |
| 05 | 243 | 25 | eLife | Reviewer #3 | https://elifesciences.org/articles/102228/peer-reviews |
| 05 | 244 | 6 | eLife | Reviewer #1 | https://elifesciences.org/articles/106840/peer-reviews |
| 05 | 245 | 76 | PeerJ | Reviewer 2 | https://peerj.com/articles/21383/reviews/ |
| 05 | 246 | 310 | Royal Society Open Science | Reviewer 2 (round 1) | https://www.webofscience.com/api/gateway/wos/peer-review/10.1098/rsos.230224 |
| 05 | 247 | 1 | eLife | Reviewer #1 | https://elifesciences.org/articles/106073/peer-reviews |
| 05 | 248 | 130 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0293188 |
| 05 | 249 | 96 | PeerJ | Reviewer 2 | https://peerj.com/articles/19913/reviews/ |
| 05 | 250 | 103 | PeerJ | Reviewer 2 | https://peerj.com/articles/19401/reviews/ |
| 06 | 251 | 335 | NeurIPS 2024 (poster) | Reviewer_f7Sf | https://openreview.net/forum?id=7XkwzaPMvX&noteId=CvMeP5Fxah |
| 06 | 252 | 188 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0310031 |
| 06 | 253 | 179 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296944 |
| 06 | 254 | 298 | PCI Registered Reports | James Green (round 1) | https://rr.peercommunityin.org/articles/rec?id=1560 |
| 06 | 255 | 81 | PeerJ | Reviewer 1 | https://peerj.com/articles/21138/reviews/ |
| 06 | 256 | 296 | PCI Registered Reports | Amélie Gourdon-Kanhukamwe (round 2) | https://rr.peercommunityin.org/articles/rec?id=1145 |
| 06 | 257 | 128 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0289687 |
| 06 | 258 | 56 | eLife | Reviewer #3 | https://elifesciences.org/reviewed-preprints/112321/reviews |
| 06 | 259 | 11 | eLife | Reviewer #2 | https://elifesciences.org/articles/105025/peer-reviews |
| 06 | 260 | 193 | PLOS ONE | Reviewer 2 (round 4) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0310031 |
| 06 | 261 | 158 | PLOS ONE | Reviewer 4 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0289845 |
| 06 | 262 | 31 | eLife | Reviewer #1 | https://elifesciences.org/articles/93755/peer-reviews |
| 06 | 263 | 192 | PLOS ONE | Reviewer 2 (round 3) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0310031 |
| 06 | 264 | 307 | PCI Registered Reports | Bruno Verschuere (round 1) | https://rr.peercommunityin.org/articles/rec?id=1914 |
| 06 | 265 | 252 | PLOS ONE | Reviewer 3 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0302173 |
| 06 | 266 | 112 | PeerJ | Reviewer 2 | https://peerj.com/articles/19022/reviews/ |
| 06 | 267 | 249 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0302173 |
| 06 | 268 | 180 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296944 |
| 06 | 269 | 194 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0306121 |
| 06 | 270 | 98 | PeerJ | Reviewer 1 | https://peerj.com/articles/19707/reviews/ |
| 06 | 271 | 209 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296524 |
| 06 | 272 | 159 | PLOS ONE | Reviewer 1 (round 3) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0289845 |
| 06 | 273 | 7 | eLife | Reviewer #2 | https://elifesciences.org/articles/106840/peer-reviews |
| 06 | 274 | 13 | eLife | Reviewer #1 | https://elifesciences.org/articles/102800/peer-reviews |
| 06 | 275 | 71 | eLife | Reviewer #3 | https://elifesciences.org/reviewed-preprints/90684/reviews |
| 06 | 276 | 323 | Graphics Interface 2021 (2nd cycle) | Reviewer_WEED | https://openreview.net/forum?id=XpPWPdX6Tv&noteId=M8qyOn6VbOC |
| 06 | 277 | 66 | eLife | Reviewer #2 | https://elifesciences.org/reviewed-preprints/108428/reviews |
| 06 | 278 | 55 | eLife | Reviewer #2 | https://elifesciences.org/reviewed-preprints/112321/reviews |
| 06 | 279 | 213 | PLOS ONE | Reviewer 5 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296524 |
| 06 | 280 | 150 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0288883 |
| 06 | 281 | 115 | PeerJ | Reviewer 2 | https://peerj.com/articles/18900/reviews/ |
| 06 | 282 | 250 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0302173 |
| 06 | 283 | 12 | eLife | Reviewer #3 | https://elifesciences.org/articles/105025/peer-reviews |
| 06 | 284 | 293 | PCI Registered Reports | Micah Amd (round 1) | https://rr.peercommunityin.org/articles/rec?id=2432 |
| 06 | 285 | 123 | PLOS ONE | Reviewer 1 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0288346 |
| 06 | 286 | 260 | PLOS ONE | Reviewer 3 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0310491 |
| 06 | 287 | 216 | PLOS ONE | Reviewer 5 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296524 |
| 06 | 288 | 265 | PLOS ONE | Reviewer 1 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0299578 |
| 06 | 289 | 234 | PLOS ONE | Reviewer 4 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0297587 |
| 06 | 290 | 89 | PeerJ | Reviewer 3 | https://peerj.com/articles/20417/reviews/ |
| 06 | 291 | 141 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0284179 |
| 06 | 292 | 306 | PCI Registered Reports | Christian Seegelke (round 1) | https://rr.peercommunityin.org/articles/rec?id=1213 |
| 06 | 293 | 61 | eLife | Reviewer #2 | https://elifesciences.org/reviewed-preprints/101021/reviews |
| 06 | 294 | 212 | PLOS ONE | Reviewer 4 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296524 |
| 06 | 295 | 201 | PLOS ONE | Reviewer 5 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0301299 |
| 06 | 296 | 282 | PCI Registered Reports | Amy Eshleman (round 2) | https://rr.peercommunityin.org/articles/rec?id=2500 |
| 06 | 297 | 86 | PeerJ | Reviewer 3 | https://peerj.com/articles/20567/reviews/ |
| 06 | 298 | 286 | PCI Registered Reports | Sharon Bertsch (round 1) | https://rr.peercommunityin.org/articles/rec?id=1770 |
| 06 | 299 | 20 | eLife | Reviewer #1 | https://elifesciences.org/articles/101371/peer-reviews |
| 06 | 300 | 142 | PLOS ONE | Reviewer 3 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0284179 |
| 07 | 301 | 229 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0298523 |
| 07 | 302 | 222 | PLOS ONE | Reviewer 2 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0314967 |
| 07 | 303 | 232 | PLOS ONE | Reviewer 1 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0297587 |
| 07 | 304 | 236 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296421 |
| 07 | 305 | 253 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0305554 |
| 07 | 306 | 258 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0310491 |
| 07 | 307 | 113 | PeerJ | Reviewer 3 | https://peerj.com/articles/19022/reviews/ |
| 07 | 308 | 238 | PLOS ONE | Reviewer 3 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296421 |
| 07 | 309 | 131 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0293188 |
| 07 | 310 | 39 | eLife | Reviewer #2 | https://elifesciences.org/articles/103736/peer-reviews |
| 07 | 311 | 167 | PLOS ONE | Reviewer 3 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0286336 |
| 07 | 312 | 241 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0307660 |
| 07 | 313 | 190 | PLOS ONE | Reviewer 2 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0310031 |
| 07 | 314 | 304 | PCI Registered Reports | Peter Wühr (round 1) | https://rr.peercommunityin.org/articles/rec?id=1213 |
| 07 | 315 | 45 | eLife | Reviewer #2 | https://elifesciences.org/articles/91011/peer-reviews |
| 07 | 316 | 19 | eLife | Reviewer #2 | https://elifesciences.org/reviewed-preprints/108521/reviews |
| 07 | 317 | 137 | PLOS ONE | Reviewer 1 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0285800 |
| 07 | 318 | 106 | PeerJ | Reviewer 2 | https://peerj.com/articles/19314/reviews/ |
| 07 | 319 | 136 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0285800 |
| 07 | 320 | 331 | Graphics Interface 2023 | Reviewer_FkZ4 | https://openreview.net/forum?id=7SrRB7RUvgU&noteId=BmYnqGqgw6 |
| 07 | 321 | 126 | PLOS ONE | Reviewer 2 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0290253 |
| 07 | 322 | 277 | PCI Registered Reports | Zoltan Dienes (round 3) | https://rr.peercommunityin.org/articles/rec?id=1701 |
| 07 | 323 | 327 | Graphics Interface 2021 (2nd cycle) | Reviewer_m71B | https://openreview.net/forum?id=HG7FQ7-KKf&noteId=Eib29zyLIZd |
| 07 | 324 | 177 | PLOS ONE | Reviewer 1 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0288966 |
| 07 | 325 | 171 | PLOS ONE | Reviewer 1 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0292284 |
| 07 | 326 | 276 | PCI Registered Reports | Kai Hiraishi (round 3) | https://rr.peercommunityin.org/articles/rec?id=1701 |
| 07 | 327 | 227 | PLOS ONE | Reviewer 2 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0307137 |
| 07 | 328 | 189 | PLOS ONE | Reviewer 1 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0310031 |
| 07 | 329 | 143 | PLOS ONE | Reviewer 2 (round 2) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0284179 |
| 07 | 330 | 219 | PLOS ONE | Reviewer 1 (round 1) | https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0314967 |
| 07 | 331 | 30 | eLife | Reviewer #3 | https://elifesciences.org/articles/96803/peer-reviews |
| 07 | 332 | 292 | PCI Registered Reports | Ivan Ivanchei (round 1) | https://rr.peercommunityin.org/articles/rec?id=2432 |
| 07 | 333 | 287 | PCI Registered Reports | Vanessa Loaiza (round 1) | https://rr.peercommunityin.org/articles/rec?id=1770 |
| 07 | 334 | 75 | PeerJ | Reviewer 1 | https://peerj.com/articles/21383/reviews/ |
| 07 | 335 | 324 | Graphics Interface 2021 (2nd cycle) | Reviewer_df1n | https://openreview.net/forum?id=XpPWPdX6Tv&noteId=rnuRZ_MG8Ut |
| 07 | 336 | 280 | PCI Registered Reports | Michelle Carras (round 1) | https://rr.peercommunityin.org/articles/rec?id=1949 |
| 07 | 337 | 8 | eLife | Reviewer #3 | https://elifesciences.org/articles/106840/peer-reviews |

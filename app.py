from src.read_data import *
from src.embed import *
from src.rank import *
from src.export import *

print(
"Reading JD..."
)

JD = read_docx(
"data/job_description.docx"
)


print(
"Reading Candidates..."
)

df = load_candidates(
"data/candidates.jsonl"
)


print(
"Embedding JD..."
)

jd = encode(
[JD]
)[0]


print(
"Embedding Candidates..."
)

cand = encode(
df["text"].tolist()
)


print(
"Ranking..."
)

top = rank(
jd,
cand,
df
)


print(
"Exporting..."
)

export(
top
)


print(
"Completed")
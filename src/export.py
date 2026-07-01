import pandas as pd


def build_reason(candidate):

    text = candidate.get(
        "text",
        ""
    )

    exp = candidate.get(
        "experience",
        0
    )

    skills = text.split()[:10]

    reason = (
        f"Matched JD using semantic similarity. "
        f"Experience: {exp} years. "
        f"Relevant skills: {' '.join(skills)}"
    )

    return reason[:500]


def export(df):

    rows=[]

    for i,row in enumerate(
        df.itertuples()
    ):

        rows.append({

            "candidate_id":
            row.id,

            "rank":
            i+1,

            "score":
            round(
                float(row.score),
                5
            ),

            "reasoning":
            build_reason(
                {
                    "text": row.text,
                    "experience":
                    row.experience
                }
            )

        })


    output=pd.DataFrame(
        rows,
        columns=[

            "candidate_id",

            "rank",

            "score",

            "reasoning"
        ]
    )


    output.to_csv(

        "outputs/ranked_candidates.csv",

        index=False
    )

    print(
        "Submission CSV Generated"
    )
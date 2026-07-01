import numpy as np


def rank(
    jd,
    cand,
    df
):

    # Semantic similarity
    sim = np.dot(
        cand,
        jd
    )

    # Experience score
    exp = np.minimum(
        df["experience"] / 8,
        1
    )

    # Final score
    score = (
        0.85 * sim
        +
        0.15 * exp
    )

    # Store score
    df["score"] = score

    # Sort:
    # 1. score descending
    # 2. candidate_id ascending (tie-break)
    result = (

        df

        .sort_values(

            by=[

                "score",

                "id"

            ],

            ascending=[

                False,

                True

            ]

        )

        .head(100)

        .reset_index(
            drop=True
        )

    )

    return result
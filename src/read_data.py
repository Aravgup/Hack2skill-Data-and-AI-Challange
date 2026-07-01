import json
import pandas as pd
from docx import Document
from tqdm import tqdm


def read_docx(path):

    doc = Document(path)

    return "\n".join(
        p.text
        for p in doc.paragraphs
    )


def load_candidates(path):

    rows=[]

    with open(
        path,
        "r",
        encoding="utf8"
    ) as f:

        for line in tqdm(
            f,
            desc="Loading"
        ):

            c=json.loads(line)

            profile=c.get(
                "profile",
                {}
            )

            skills=[]

            for s in c.get(
                "skills",
                []
            ):

                if isinstance(
                    s,
                    dict
                ):

                    skills.append(
                        s.get(
                            "name",
                            ""
                        )
                    )

            text=[]

            text.extend(
                skills
            )

            text.append(
                profile.get(
                    "headline",
                    ""
                )
            )

            text.append(
                profile.get(
                    "summary",
                    ""
                )
            )

            rows.append({

                "id":
                c.get(
                    "candidate_id"
                ),

                "text":
                " ".join(text),

                "experience":
                profile.get(
                    "years_of_experience",
                    0
                ),

                "candidate":
                c
            })

    return pd.DataFrame(
        rows
    )
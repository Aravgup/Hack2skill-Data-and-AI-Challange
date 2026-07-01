from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
"all-MiniLM-L6-v2"
)


def encode(text):

    return model.encode(

        text,

        batch_size=128,

        normalize_embeddings=True,

        show_progress_bar=True
    )
"""
    Name-search functionality
"""

from typing import List
from sqlalchemy import text
from .database_provider import data_provider_session, Session, db_engine
from models.name_search import base
from env import ENV


# Create NameSearch table if not exists; make db aware of this model
base.metadata.create_all(db_engine)


def name_search(search_submission: str) -> List:
    """
        Function to query DB for fuzzy name search
    """
    found_names: List = []

    # Clean up search_submission

    session: Session
    with data_provider_session() as session:
        stmt = text(
            """
            SELECT target, comparison_text, display_text, body_type
            FROM name_search
            ORDER BY (name_search.comparison_text <-> :search_submission)
            LIMIT :limit
            """
        )
        r = session.execute(
            stmt,
            {
                "search_submission": search_submission,
                "limit": ENV.MAX_RESULTS,
            },
        )

        # print("<><><><><>")
        for p in r:
            # print(p)
            found_names.append(
                {
                    "target": p.target,
                    "comparison_text": p.comparison_text,
                    "display_text": p.display_text,
                    "body_type": p.body_type,
                }
            )

        # print("**********")
        # print(found_names)
        # print(found_names[0])

    return found_names

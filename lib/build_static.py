import sys
import os
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..'
            )
        )
    )

from flask_frozen import Freezer
from app import app

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()

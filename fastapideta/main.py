from typing import List
from business_logic import Solution
from fastapi import FastAPI

app = FastAPI(
    title="Combination Sum API",
    version="1.0.0",
    redoc_url="",
    description="Find all combinations from a given set of numbers that add up to a given sum target.",
)


@app.get("/", tags=["Welcome"])
def read_root():
    return {"Hello": "To use the tool go to https://combinationsum-1-l6323962.deta.app/docs"}


@app.post("/", name="Combination sum Function", tags=["Test the tool in POST"])
def read_root(
    candidates: List[float],
    target: float,
    tolerance: float = 0.0,
):
    """Limitations:
        - Use only float numbers like "123.23"
        - Body only acept a set max of 20  values
        - Remeber try different tolerance values to get the best combinations, if you result is [], try incrementing tolerance, as:
           5 == 5%
           .2 == .2%

        Returns:
            json: {
      "Posibles Combinaciones": [
        [
          1214.38,
          1187.5
        ]...
      ]
    }
    """
    res = Solution.combination_sum(
        candidates=candidates, target=target, tolerance=tolerance
    )
    return {"Posibles Combinaciones": res}

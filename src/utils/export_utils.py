import pandas as pd
from io import BytesIO


def export_excel(df):

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="xlsxwriter"
    ) as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name="Recommendations"
        )

    return output.getvalue()
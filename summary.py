def build_prompt(summary_dict):
    shape = summary_dict['shape']
    num_cols = [col for col, dtype in summary_dict['dtypes'].items() if 'float' in str(dtype) or 'int' in str(dtype)]
    cat_cols = [col for col, dtype in summary_dict['dtypes'].items() if dtype == 'object']

    prompt = f"""
    Analyze the following dataset:

    - Shape: {shape[0]} rows, {shape[1]} columns
    - Missing values: {summary_dict['missing_values']}
    - Numerical columns: {num_cols}
    - Categorical columns: {cat_cols}

    Provide a plain-English summary describing this dataset, its structure, missing data, and feature types.
    """

    return prompt
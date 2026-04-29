 # import moudles from sciwrite_lint
from sciwrite_lint import pipeline

def analyze_paper(file_path):
    """
        Service wrapper around sciwrite-lint.
        This isolates Django from external logic.
        """

    result = pipeline.run(file_path)

    return {
        "status": "success",
        "raw_result": result
    }
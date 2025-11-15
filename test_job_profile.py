import sys
sys.path.append('../src')
from src.job_profile import JobProfile


def test_job_profile():
    """Test the JobProfile class with our sample job folder."""

    print("=" * 50)
    print("Testing JobProfile")
    print("=" * 50)

    # Create a JobProfile instance
    profile = JobProfile("jobs/test_job")

    profile.load_documents()

    print("\n📋 Available documents:")
    for doc_name in profile.list_documents():
        print(f"  - {doc_name}")

    print("\n📄 Job Description:")
    print("-" * 50)
    job_desc = profile.get_document("job_description")
    print(job_desc)

if __name__ == "__main__":
    test_job_profile()
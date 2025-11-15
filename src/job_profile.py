import os
from pathlib import Path

class JobProfile:
    """
    Loads and stores all documents for a specific job application.
    
    Each document is stored in a dictionary with the filename (without extension)
    as the key and the file contents as the value.
    """
    job_folder: str
    documents: dict[str, str]
    def __init__(self, job_folder):
        """
        Initialize the JobProfile with a job folder path.
        
        Args:
            job_folder (str): Path to the folder containing job documents
        
        Python concepts:
        - __init__ is the constructor - runs when you create a new instance
        - self.job_folder is an instance attribute (each JobProfile has its own)
        - We store the folder path but don't load files yet (separation of concerns)
        """
        self.job_folder = job_folder
        self.documents = {} 
    def load_documents(self) -> dict[str, str]:
        """
        Load all .txt files from the job folder into self.documents.
        
        Returns:
            dict: The loaded documents dictionary
        
        Raises:
            FileNotFoundError: If the job folder doesn't exist
        """
        folder_path = Path(self.job_folder)

        if not folder_path.exists():
            raise FileNotFoundError(f"Job folder \"{self.job_folder}\" does not exist")
        if not folder_path.is_dir():
            raise ValueError(f"Path is not a directory: {self.job_folder}")
        
        txt_files = list(folder_path.glob("*.txt"))
        
        for file_path in txt_files:
            document_name = file_path.stem

            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read().strip() # Remove leading/trailing whitespace
                
                self.documents[document_name] = content
            except Exception as e:
                print(f"Error loading document {document_name}: {e}")
        return self.documents

    def get_document(self, document_name: str):
        """
        Retrieve a specific document by name.
        
        Args:
            doc_name (str): Name of the document (without .txt extension)
        
        Returns:
            str: Document content, or None if not found
        """
        return self.documents.get(document_name)
    
    def list_documents(self) -> list[str]:
        """
        List all document names in the profile.
        
        Returns:
            list[str]: List of document names
        """
        return list(self.documents.keys())

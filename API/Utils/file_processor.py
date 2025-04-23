# file_processor.py
def process_file(file):
    """
    Function to process the uploaded file.
    You can customize this function based on your requirements.
    
    Args:
        file: File object from Flask's request.files
        
    Returns:
        Result of the file processing
    """
    # Example processing: read the file content
    content = file.read()
    
    # Example processing: return the file size
    file_size = len(content)
    
    # You can add your custom processing logic here
    
    return {
        'filename': file.filename,
        'file_size_bytes': file_size,
        'content_type': file.content_type
    }
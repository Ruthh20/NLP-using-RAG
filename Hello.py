import streamlit as st

st.title("Promptly")
st.write("Offline document based generation using rag.")

# Create a textbox for user input
user_input = st.text_input("Enter your prompt:")

# Display the entered text when the button is clicked
if st.button("Submit"):
    st.write("You entered:", user_input)

# Create a file uploader
uploaded_file = st.file_uploader("Choose a file...", type=["ppt", "pptx", "doc", "docx", "pdf"])

# Check if a file has been uploaded
if uploaded_file is not None:
    # Display the file name
    st.write("File name:", uploaded_file.name)
    
    # Read the contents of the file
    bytes_data = uploaded_file.read()
    
    # Optionally, you can display the file type or perform actions based on the file type
    st.write("File type:", uploaded_file.type)
    
    # You can save the file locally if needed
    with open(uploaded_file.name, "wb") as f:
        f.write(bytes_data)
    
    st.success("File uploaded successfully!")
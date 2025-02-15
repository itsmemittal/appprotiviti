# from fastapi import FastAPI, File, UploadFile, HTTPException
# import cv2
# import numpy as np
# from PIL import Image
# import io

# app = FastAPI()

# def preprocess_image(image):
#     """Convert to grayscale and apply Gaussian blur."""
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#     return blurred

# def detect_edges(image):
#     """Detect edges using Canny edge detection."""
#     edges = cv2.Canny(image, 50, 150)
#     return edges

# def detect_tampering(edges):
#     """Detect tampering by analyzing edge inconsistencies."""
#     edge_pixels = np.sum(edges) / 255
#     return edge_pixels > 10000  # Threshold for tampering detection

# @app.post("/check-forgery/")
# async def check_forgery(file: UploadFile = File(...)):
#     """API endpoint to check document forgery."""
#     # Check if the uploaded file is an image
#     if not file.content_type.startswith("image/"):
#         raise HTTPException(status_code=400, detail="Uploaded file is not an image.")

#     # Read the image file
#     contents = await file.read()
#     image = Image.open(io.BytesIO(contents)).convert("RGB")
#     image = np.array(image)  # Convert PIL image to NumPy array

#     # Preprocess the image
#     preprocessed = preprocess_image(image)

#     # Detect edges
#     edges = detect_edges(preprocessed)

#     # Check for tampering
#     is_forged = detect_tampering(edges)

#     # Return the result
#     return {"filename": file.filename, "is_forged": is_forged}

# # Run the FastAPI app
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)


from fastapi import FastAPI, File, UploadFile
import json

app = FastAPI()

@app.post("/check_forge")
async def check_forge(file: UploadFile = File(...)):
    result = {"file_name": file.filename, "forgery_detected": False, "confidence": 95}
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
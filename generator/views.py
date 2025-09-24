from django.shortcuts import render
from google import genai
from django.conf import settings

# Initialize the Gemini client
client = genai.Client(api_key=settings.GEMINI_API_KEY)

def generate_recipe(request):
    recipe = ""
    if request.method == "POST":
        item = request.POST.get("item")
        if item:
            prompt = (
                f"Create a simple, easy-to-follow recipe for the following item: {item}. "
                "Provide clear step-by-step instructions in a numbered list."
            )

            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[{"text": prompt}]
                )
                recipe = response.text
            except Exception as e:
                recipe = f"Error generating recipe: {e}"

    return render(request, "recipe.html", {"recipe": recipe})


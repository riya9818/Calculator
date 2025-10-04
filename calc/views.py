from django.shortcuts import render
import math

def calculator(request):
    result = None
    error = None

    if request.method == "POST":
        expression = request.POST.get("expression", "").strip()

        try:
            # Use a safe evaluation method
            allowed_names = {
                "sqrt": math.sqrt,
                "pow": math.pow,
                "log": math.log,
                "sin": lambda x: math.sin(math.radians(x)),
                "cos": lambda x: math.cos(math.radians(x)),
                "tan": lambda x: math.tan(math.radians(x)),
                "__builtins__": {}
            }

            result = eval(expression, {"__builtins__": None}, allowed_names)

            # Save in session history
            history = request.session.get("history", [])
            history.insert(0, f"{expression} = {result}")
            request.session["history"] = history[:10]

        except ZeroDivisionError:
            error = "Error: Division by zero"
        except ValueError:
            error = "Error: Invalid input"
        except Exception:
            error = "Error: Invalid expression"

    history = request.session.get("history", [])
    return render(request, "calc/calculator.html", {
        "result": result,
        "error": error,
        "history": history
    })

from django.shortcuts import render

def calculator(request):
    result = None
    error = None

    if request.method == "POST":
        try:
            num1_raw = request.POST.get("num1", "").strip()
            num2_raw = request.POST.get("num2", "").strip()
            operator = request.POST.get("operator", "+")

            num1 = float(num1_raw) if num1_raw != "" else 0.0
            num2 = float(num2_raw) if num2_raw != "" else 0.0

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    error = "Error: Division by zero"
                else:
                    result = num1 / num2
            else:
                error = "Unknown operator"

            # ✅ Save history in session
            if error is None:
                history = request.session.get("history", [])
                history.insert(0, f"{num1} {operator} {num2} = {result}")
                request.session["history"] = history[:10]  # keep last 10
        except ValueError:
            error = "Invalid number input"
        except Exception as e:
            error = f"Error: {e}"

    # Get history for display
    history = request.session.get("history", [])
    return render(request, "calc/calculator.html", {
        "result": result,
        "error": error,
        "history": history
    })

from django.shortcuts import render
import math

def calculator(request):
    result = ""
    expression = ""
    history = request.session.get("history", [])

    if request.method == "POST":
        expression = request.POST.get("expression", "")

        try:
            safe_expr = (
                expression.replace("÷", "/")
                .replace("×", "*")
                .replace("^", "**")
            )

            allowed = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
            allowed["abs"] = abs
            allowed["round"] = round

            result = eval(safe_expr, {"__builtins__": {}}, allowed)

            entry = f"{expression} = {result}"
            history.append(entry)
            history = history[-5:]
            request.session["history"] = history

        except Exception:
            result = "Error"

    return render(request, "calculator.html", {
        "result": result,
        "expression": expression,
        "history": history,
    })

import pyscript 

def check(event):

    registered_online = pyscript.document.getElementById("registered").checked
    medical_clearance = pyscript.document.getElementById("medical").checked
    grade = pyscript.document.getElementById("grade").value
    section = pyscript.document.getElementById("section").value

    if registered_online and medical_clearance:

        if grade == "seven":
            if section == "ruby":
                team = "Yellow Tigers"
            elif section == "emerald":
                team = "Green Hornets"

        elif grade  == "eight":
            if section == "emerald":
                team = "Red Bulldogs"
            elif section == "ruby":
                team = "Blue Bears"

        elif grade == "nine":
            if section == "emerald":
                team = "Red Bulldogs"
            elif section == "ruby":
                team = "Blue Bears"

        elif grade == "ten":
            if section == "emerald":
                team = "Green Hornets"
            elif section == "ruby":
                team = "Yellow Tigers"

        elif grade == "eleven":
            if section == "emerald":
                team = "Red Bulldogs"
            elif section == "ruby":
                team = "Blue Bears" 

        elif grade == "twelve":
            if section == "emerald":
                team = "Green Hornets"
            elif section == "ruby":
                team = "Yellow Tigers"

        else:
            team = "ERROR!"

        pyscript.document.getElementById("result").innerHTML = f"You are eligible to join! Your team is: {team}"

    else:

        if not registered_online and not medical_clearance:
            pyscript.document.getElementById("result").innerHTML = "You are not eligible. Please register on our website and secure proper medical clearance."

        elif not registered_online:
            pyscript.document.getElementById("result").innerHTML = "You are not eligible. Please register on our website."

        elif not medical_clearance:
            pyscript.document.getElementById("result").innerHTML = "You are not eligible. Please secure proper medical clearance."

        else:
            pyscript.document.getElementById("result").innerHTML = "Deepest apologies, you are not eligible."

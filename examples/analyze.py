from targer_api.api import analyze_text

arguments = analyze_text(
    "Academic freedom is not absolute. "
    "All major Canadian universities are now publicly funded "
    "but maintain institutional autonomy, "
    "with the ability to decide on admission, tuition and governance."
)
print(arguments)

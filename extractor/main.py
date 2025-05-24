import fitz
import re

doc = fitz.open("test.pdf")

annotations = {}

for page_num, page in enumerate(doc):
    annot = page.first_annot

    while annot:
        if annot.type[1] == "Highlight":
            content = annot.info.get('content', '').strip()
            if content:
                if page_num in annotations:
                    annotations[page_num].append(content)
                else:
                    annotations[page_num] = [content]
        annot = annot.next

sorted_annotations = {}

for page_num in annotations:
    sorted_annotations[page_num] = []
    for i, content in enumerate(annotations[page_num]):

        split_content = re.split(r'(?<=\n)', content)
        resume = split_content[0] if len(split_content) > 0 else None
        print("resume", resume)
        note_content = ""
        for cont in split_content[1:]:
            note_content += cont
        print("note_content", note_content)


def get_annotations(doc):
    extracted_annotations = {}

    for page_num, page in enumerate(doc):
        annot = page.first_annot
        page_num_count_from_1 = page_num + 1

        while annot:
            if annot.type[1] == "Highlight":
                content = annot.info.get('content', '').strip()
                if content:
                    if page_num_count_from_1 in extracted_annotations:
                        extracted_annotations[page_num_count_from_1].append(content)
                    else:
                        extracted_annotations[page_num_count_from_1] = [content]
            annot = annot.next

    return extracted_annotations

def get_sorted_annotations(annotations):
    extracted_sorted_annotations = {}

    for page_num in annotations:
        extracted_sorted_annotations[page_num] = []
        for i, content in enumerate(annotations[page_num]):

            split_content = content.splitlines(keepends=True)
            resume = split_content[0] if len(split_content) > 0 else None
            note_content = ""
            if len(split_content) > 1:
                for cont in split_content[1:]:
                    note_content += cont
            if note_content:
                extracted_sorted_annotations[page_num].append ({
                    "resume": resume,
                    "content": note_content
                })
            else:
                extracted_sorted_annotations[page_num].append ({
                    "content": content
                })
    return extracted_sorted_annotations


def get_hightlighted_annotations(doc):
    annotations = get_annotations(doc)
    return get_sorted_annotations(annotations)

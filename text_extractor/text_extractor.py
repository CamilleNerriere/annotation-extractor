def get_text_annotations(doc):
    extracted_annotations = {}

    for page_num, page in enumerate(doc):
        annot = page.first_annot
        page_num_count_from_1 = page_num + 1

        while annot:
            if annot.type[1] == "FreeText":
                content = annot.info.get('content', '').strip()
                if content:
                    if page_num_count_from_1 in extracted_annotations:
                        extracted_annotations[page_num_count_from_1].append(content)
                    else:
                        extracted_annotations[page_num_count_from_1] = [content]
            annot = annot.next

    return extracted_annotations




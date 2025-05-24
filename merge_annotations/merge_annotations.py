def merge_annotations(highlighted_annotations, text_annotations, doc):
    all_annotations = {}

    for page_num, page in enumerate(doc):
        page_num_count_from_1 = page_num + 1

        page_high_annot = highlighted_annotations[page_num_count_from_1] if page_num_count_from_1 in highlighted_annotations else None
        text_annot = text_annotations[page_num_count_from_1] if page_num_count_from_1 in text_annotations else None

        if page_high_annot :
            all_annotations[page_num_count_from_1] = [page_high_annot]
        if text_annot:
            if page_num_count_from_1 in all_annotations:
                all_annotations[page_num_count_from_1].append(text_annot)
            else:
                all_annotations[page_num_count_from_1] = [text_annot]

    return all_annotations
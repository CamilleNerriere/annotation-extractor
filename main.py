from highlight_extractor import get_highlighted_annotations
from text_extractor import get_text_annotations
from merge_annotations import merge_annotations
from export_word import export_annotations_to_docx
import fitz

doc = fitz.open("test.pdf")

highlighted_annotations = get_highlighted_annotations(doc)
text_annotations = get_text_annotations(doc)
all_annotations = merge_annotations(highlighted_annotations, text_annotations, doc)

export_annotations_to_docx("Simondon", all_annotations, "./test.docx")


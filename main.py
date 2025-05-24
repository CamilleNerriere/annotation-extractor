from highlight_extractor import get_highlighted_annotations
from text_extractor import get_text_annotations
from merge_annotations import merge_annotations
import fitz

doc = fitz.open("test2.pdf")

highlighted_annotations = get_highlighted_annotations(doc)
text_annotations = get_text_annotations(doc)
all_annotations = merge_annotations(highlighted_annotations, text_annotations, doc)


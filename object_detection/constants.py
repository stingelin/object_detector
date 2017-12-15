""" Constants that depend on the object detection model (tensorflow network) being used. """
import os

from object_detection.utils import label_map_util


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Path to frozen detection graph. This is the actual model that is used for the object detection.
MODEL_NAME = 'ssd_mobilenet_v1_coco_11_06_2017'
LABEL_MAP_FILE = 'mscoco_label_map.pbtxt'
PATH_TO_CKPT = os.path.join(BASE_DIR, 'object_detection', MODEL_NAME, 'frozen_inference_graph.pb')
# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join(BASE_DIR, 'object_detection', 'data', LABEL_MAP_FILE)

# Loading label map
LABEL_MAP = label_map_util.load_labelmap(PATH_TO_LABELS)
# though mobilenet can handle
CATEGORIES = label_map_util.convert_label_map_to_categories(LABEL_MAP, max_num_classes=90, use_display_name=True)
CATEGORY_INDEX = label_map_util.create_category_index(CATEGORIES)

LABEL_KEYS = 'category instance'.split()
COLOR_KEYS = 'red orange yellow green indigo violet black white pink'.split()
BB_KEYS = 'x y z width height depth'.split()
OBJECT_VECTOR_KEYS = LABEL_KEYS + BB_KEYS + COLOR_KEYS

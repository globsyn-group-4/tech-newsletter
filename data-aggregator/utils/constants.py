from enum import Enum

TEXT_ATTRIBUTE="text"

class URL_TYPE(str, Enum):
  COMPLETE="COMPLETE"
  INTERNAL="INTERNAL"

class METADATA_CONTAINER_NAMES(str, Enum):
  HEADER="headerContainer"
  URL="urlContainer"
  DATE="publishedDateContainer"

class BLOG_METADATA_KEYS(str, Enum):
  HEADER="header"
  URL="articleUrl"
  DATE="publishedDate"
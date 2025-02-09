---
title: "RandomX"
filename: "randomx.md"
folder: "proof-of-work"
lang: "es"

translated: "yes"
translationOutdated: "yes"

contentOutdated: "no"
---

<!-- If the English version is outdated, all versions (for all languages) will be outdated. No need to check the state of the translations. -->
{% if contentOutdated == "yes" %}
## **{{ notices.outdatedContent }}**

<!-- If page is translated but the English version got updated, the translation is outdated -->
{% elif translationOutdated == "yes" %}
## **{{ notices.outdatedTranslation }}**
{% endif %}

<!-- Show the body -->
{% if translated == "yes" %}
  {% include lang + "/" + folder + "/" + filename %}
{% else %}
  {% include "en" + "/" + folder + "/" + filename %}
{% endif %}

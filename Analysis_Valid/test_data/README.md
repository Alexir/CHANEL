**Datasets used to proof the krippendorff code**

* version found in `ChatEval-AMT-Interface/data/annotated/`. This was used to run the evaluations that were presented at the end of the workshop. It appears to have more data than the raw version.\
`4456   4456 180797 030820_first_public_finding_atts.csv`


* CHANEL Valid data (from `Data-Collection/raws/030820_first_public.pkl`). This is an inital collection to validate the collection procedure and rater agreement. These files have column ordering (UID,ANSWER,ANNOTATOR) / (item answer,annotator) / (I, K, C). \
  `3568  10704 125130 test_data/030820_first_public-raw.csv`
  * split into ratings exerpts and assignment metadata\
 `  893   7415 109141 030820_first_public-assigmt.csv`\
  `2987  11948 198047 030820_first_public-excerpt.csv`\
 `  583    2332   37757 030820_first_public-attnchk.csv`

* test data used by nltk; it is not clear where this actually came from. But that's what they used. The tuples per line are (annotator, item, answer); these are also referred to as (C, I, K). Note this is different from the ChaEval ordering (item,answer,annotator) / (I, K, C). See `https://www.nltk.org/_modules/nltk/metrics/agreement.html`.\
`   200     600    1984 artstein_poesio_example.txt`

* test data embedded in the Python modules krippendorff and fast-krippendorff; the data are the same in both).

** Testing Krippendorff alpha computation

This gets intricate.
* Nominally two ways of computing: a) Python krippendorff code, b) nltk code.
* Two data arrangements: a) (item,answer,annotator) for nltk and (item,answer,annotator) for the compute() function exposed in the ChatEval code.

The Krippendorff code uses a different organization: reliability and value matrices. nlkt and ChatEval use a tuple to code the observations. The Krippendoff code wants reliability NxM matrices where rows N are classes/values and columns M are annotator observations; you might end up with a sparse matrix (as CHANEL does). Both copmputations have preprocessing steps that reshape the raw data to conform to what Krippendorff code needs.

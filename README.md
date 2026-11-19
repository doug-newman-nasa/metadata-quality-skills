# Metadata Quality Skills
This repository is designed to hold an evolving set of AI skills designed to automate the process of metadata quality improvement.

![AI Skills applied to metadata quality improvement](Diagrams/AI%20skills%20and%20metadata%20quality.png)

Specific areas we are targeting
## Science keyword assignment
The determination of appropriate science keywords for a collection based on
- Existing metadata elements
- Documentation referenced in the metadata such as Algorithm Theoretical Basis Documents (ATBD) and User Guides
## Collection provenance
The determination of associated collections that were used as input etc. to the creation of a collection based on
- Documentation referenced in the metadata such as Algorithm Theoretical Basis Documents (ATBD) and User Guides
- Supplementary information found through web searches


## Skill families

Skills are grouped by dependency. Each family folder holds its skills, notebooks, reports and metrics, and has its own README.

- [lineage/](lineage/README.md): collection lineage discovery, UMM-C MetadataAssociations and lineage CSV export
- [processing-level-validation/](processing-level-validation/README.md): checks declared ProcessingLevel against ATBD and User Guide evidence
- [keyword-extraction/](keyword-extraction/README.md): science keyword suggestions from collection documentation

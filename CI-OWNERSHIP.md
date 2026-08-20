# CI ownership

The repository has two complementary workflows:

- `Validate CV source` rebuilds HTML and PDFs in the runner workspace and validates the canonical source, metadata, links, PDF invariants, deterministic generation, and visual baseline. It does not require committed generated artifacts to be current before the rebuild runs.
- `Rebuild generated CV site` owns committed HTML/PDF artifacts and `MANIFEST.sha256`. It regenerates them, validates the final tree, and commits changes only after the full rebuild passes.

This separation avoids a race where validation checks stale generated artifacts while the rebuild workflow is still producing them. The rebuild also runs weekly as a self-healing drift check and remains manually dispatchable.

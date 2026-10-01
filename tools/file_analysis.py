class FileAnalysisTool:
    name = "file_analysis"

    description = (
        "Analyze a file and return its type, hash, reputation, "
        "and whether it is considered suspicious."
    )

    def run(self, filename):
        files = {
            "invoice_update.exe": {
                "filename": "invoice_update.exe",
                "file_type": "Windows executable",
                "sha256": "a7f5c8e91d4b2c7f91e0a123456789abcdef1234567890abcdef1234567890",
                "reputation": "Malicious",
                "suspicious": True
            },
            "report.pdf": {
                "filename": "report.pdf",
                "file_type": "PDF document",
                "sha256": "b8e6d9f02e5c3d8fa2f1b234567890abcdef1234567890abcdef12345678901",
                "reputation": "Clean",
                "suspicious": False
            }
        }

        return files.get(
            filename.lower(),
            {
                "filename": filename,
                "file_type": "Unknown",
                "sha256": "Unknown",
                "reputation": "Unknown",
                "suspicious": False
            }
        )
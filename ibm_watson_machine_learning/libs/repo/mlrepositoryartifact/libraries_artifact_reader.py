#  -----------------------------------------------------------------------------------------
#  (C) Copyright IBM Corp. 2017-2024.
#  https://opensource.org/licenses/BSD-3-Clause
#  -----------------------------------------------------------------------------------------

import logging

from ibm_watson_machine_learning.libs.repo.mlrepository.artifact_reader import ArtifactReader

logger = logging.getLogger('LibraryArtifactReader')


class LibrariesArtifactReader(ArtifactReader):
    def __init__(self, compressed_archive_path):
        self.library = compressed_archive_path

    def read(self):
        return self._open_stream()

    # This is a no. op. for LibraryZipFileReader as we do not want to delete the
    # archive file.
    def close(self):
        pass

    def _open_stream(self):
        return open(self.library, 'rb')


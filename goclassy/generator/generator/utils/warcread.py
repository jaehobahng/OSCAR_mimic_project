
class read:
    """
    This class takes an io.BufferedReader as an argument and reads through the wet file to return a header and a body content
        header: metadata
        body: actual text data
    """

    def __init__(self, reader):
        """
        The __init__ function takes the reader(io.BufferedReader) in as an argument
        """
        self.reader = reader
        
    def read_warc_record(self):
        """
        This funciton iterates through each line for 1 set of header:body pairings in the wet file.
        """

        first_line = self.reader.readline().decode("utf-8")
        # Read the first line of the warc file through io.Bufferreader

        # If the first line is not the given format of a Warc file, raise a value error.
        if first_line != "WARC/1.0\r\n":
            raise ValueError(f"warc version expected 'WARC/1.0' found {first_line}")

        # Initialize blank list to sppend headers
        warc_header_builder = []
        content_length = -1

        # Iterate through lines until \r\n is reached
        for line in iter(self.reader.readline, b"\r\n"):
            
            # Decode each line to utf-8 format
            line = line.decode("utf-8")

            # Break if end of block
            if line == "\r\n":
                break
            
            # If you reach a line that starts with content-length
            if line.lower().startswith("content-length:"):
                if content_length > 0:
                    raise ValueError("exactly one content-length should be present in a WARC header")
                key, value = line.split(":", 1)
                str_value = value.strip()

                # You save the number next to content length and read the number in the body part with reader.read(content_length)
                content_length = int(str_value)

            warc_header_builder.append(line)

        if content_length == 0:
            return {"header": "".join(warc_header_builder), "body": b""}

        
        body = self.reader.read(content_length).decode("utf-8")
        return {"header": "".join(warc_header_builder), "body": body}
import subprocess
import re
from ruxit.api.base_plugin import BasePlugin

class SharedMemoryMetricsPlugin(BasePlugin):
    def initialize(self, **kwargs):
        # Perform any initialization here, if needed.
        pass

    def query(self, **kwargs):
        try:
            # Execute the ipcs -m command
            result = subprocess.run(['ipcs', '-m'], stdout=subprocess.PIPE, text=True)

            # Parse the output
            # Expected output format: "0x00000000 12345 1234 user 600 2048 1634567890"
            output = result.stdout.strip().splitlines()
            
            # Regular expression to extract shared memory segments
            shm_regex = re.compile(r'(\S+)\s+(\d+)\s+(\d+)\s+(\S+)\s+\d+\s+(\d+)\s+\d+')

            total_segments = 0
            total_memory = 0

            # Skip the header (first three lines)
            for line in output[3:]:
                match = shm_regex.match(line)
                if match:
                    total_segments += 1
                    total_memory += int(match.group(5))  # Memory size in bytes

            # Send metrics to Dynatrace
            self.results_builder.absolute(key="shared_memory.total_segments", value=total_segments)
            self.results_builder.absolute(key="shared_memory.total_memory_bytes", value=total_memory)

        except Exception as e:
            self.logger.error(f"Error while fetching shared memory metrics: {e}")


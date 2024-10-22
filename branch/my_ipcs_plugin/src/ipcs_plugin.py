import subprocess
import re
from ruxit.api.base_plugin import BasePlugin

class IpcsPlugin(BasePlugin):
    
    def query(self, **kwargs):
        # Run the `ipcs -m` command
        result = subprocess.run(['ipcs', '-m'], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        
        # Parse the output to get the total number of segments and total memory used
        segments = 0
        total_memory = 0
        
        for line in output.splitlines():
            # Example line format: "0x12345678 1234 1234 987654321 666 666"
            # Parse lines with shared memory info
            if re.match(r'^\s*0x', line):
                segments += 1
                parts = line.split()
                total_memory += int(parts[4])  # Assuming the 5th column is size in bytes
        
        # Push metrics to Dynatrace
        self.results_builder.absolute(key="custom:sharedMemorySegments", value=segments)
        self.results_builder.absolute(key="custom:sharedMemoryTotalSize", value=total_memory)

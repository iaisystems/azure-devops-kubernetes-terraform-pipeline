import subprocess
import json

def get_ipc_data():
    ipc_data = {
        'shared_memory': [],
        'message_queues': [],
        'semaphores': []
    }

    # Function to run a command and parse its output
    def run_ipcs(command):
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Error running {' '.join(command)}: {result.stderr}")
            return []

        lines = result.stdout.strip().split('\n')
        data = []

        # Parse output based on the IPC type
        if command[1] == '-m':
            for line in lines[3:]:  # Skip header lines
                columns = line.split()
                if len(columns) < 6:
                    continue
                data.append({
                    'key': columns[0],
                    'shmid': columns[1],
                    'owner': columns[2],
                    'perms': columns[3],
                    'bytes': columns[4],
                    'nattch': columns[5],
                    'status': columns[6] if len(columns) > 6 else ''
                })
            ipc_data['shared_memory'] = data

        elif command[1] == '-q':
            for line in lines[3:]:  # Skip header lines
                columns = line.split()
                if len(columns) < 5:
                    continue
                data.append({
                    'key': columns[0],
                    'qid': columns[1],
                    'owner': columns[2],
                    'perms': columns[3],
                    'bytes': columns[4],
                })
            ipc_data['message_queues'] = data

        elif command[1] == '-s':
            for line in lines[3:]:  # Skip header lines
                columns = line.split()
                if len(columns) < 5:
                    continue
                data.append({
                    'key': columns[0],
                    'semid': columns[1],
                    'owner': columns[2],
                    'perms': columns[3],
                    'nsems': columns[4],
                })
            ipc_data['semaphores'] = data

    # Run the commands to gather IPC data
    run_ipcs(['ipcs', '-m'])
    run_ipcs(['ipcs', '-q'])
    run_ipcs(['ipcs', '-s'])

    # Log the collected IPC data
    print("Collected IPC Data:", json.dumps(ipc_data, indent=4))

    return ipc_data

# Call the function to test
if __name__ == "__main__":
    get_ipc_data()

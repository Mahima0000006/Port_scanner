import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    """Scan a single port on the target host."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)  # Set a timeout for the connection attempt
        result = sock.connect_ex((host, port))  # Try to connect to the port
        return port, result == 0  # Return the port and whether it's open

def port_scanner(host, start_port, end_port):
    """Scan a range of ports on the target host."""
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_port, host, port): port for port in range(start_port, end_port + 1)}
        for future in futures:
            port, is_open = future.result()
            if is_open:
                open_ports.append(port)
                print(f"Port {port} is open.")
            else:
                print(f"Port {port} is closed.")
    return open_ports

if __name__ == "__main__":
    target_host = input("Enter the target host (IP or domain): ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))

    print(f"Scanning {target_host} from port {start_port} to {end_port}...")
    open_ports = port_scanner(target_host, start_port, end_port)

    print(f"\nOpen ports: {open_ports}")

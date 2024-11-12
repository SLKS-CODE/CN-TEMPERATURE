import socket

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'  # Localhost
    port = 12345        # Port to listen on

    try:
        # Bind the socket to the address and port
        server_socket.bind((host, port))
        print(f"Server started on {host}:{port}")
    except Exception as e:
        print(f"Error occurred while starting the server: {e}")
        return

    # Start listening for incoming connections
    server_socket.listen(1)  # Can queue up to 1 connection
    print("Waiting for a connection...")

    try:
        # Accept a connection from the client
        conn, addr = server_socket.accept()
        print(f"Connection from {addr}")
    except Exception as e:
        print(f"Error accepting connection: {e}")
        return

    while True:
        try:
            # Receive the data sent by the client
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"Received: {data}")

            # Parse the temperature and unit from the received data
            temp, unit = data.split(',')
            temp = float(temp)

            # Convert the temperature based on the unit
            if unit == 'C':
                converted_temp = celsius_to_fahrenheit(temp)
                result = f"{converted_temp:.2f} F"
            elif unit == 'F':
                converted_temp = fahrenheit_to_celsius(temp)
                result = f"{converted_temp:.2f} C"
            else:
                result = "Invalid unit"

            # Send the result back to the client
            conn.send(result.encode())
        except Exception as e:
            print(f"Error during data processing: {e}")
            break

    # Close the connection
    conn.close()
    print("Connection closed.")

if __name__ == '__main__':
    start_server()

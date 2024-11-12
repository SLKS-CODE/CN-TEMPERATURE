import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'  # Server address (localhost)
    port = 12345        # Port to connect to the server

    # Try to connect to the server
    try:
        client_socket.connect((host, port))
        print("Connected to the server.")
    except Exception as e:
        print(f"Error: {e}")
        return  # If there is an error, exit the function

    # Input temperature and unit from the user
    temp = input("Enter temperature: ")
    unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").upper()

    # Send the temperature and unit to the server
    message = f"{temp},{unit}"
    try:
        client_socket.send(message.encode())
        print("Data sent to the server.")
    except Exception as e:
        print(f"Error sending data: {e}")
        client_socket.close()
        return

    # Receive the converted temperature from the server
    try:
        result = client_socket.recv(1024).decode()
        print(f"Converted temperature: {result}")
    except Exception as e:
        print(f"Error receiving data: {e}")

    # Close the connection
    client_socket.close()

if __name__ == '__main__':
    start_client()

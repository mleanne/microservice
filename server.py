import socket

def string_to_dict(data_str):
    # Convert the string back to a dictionary
    # Split the string into key-value pairs
    pairs = data_str.split("|")

    # Create an empty dictionary to store the data
    data_dict = {}

    # Iterate over each key-value pair and add them to the dictionary
    for pair in pairs:
        key, value = pair.split(":")
        data_dict[key] = float(value)

    return data_dict

def string_bar_graph(data, max_bar_width=50):
    """
    Prints a horizontal bar graph in the CLI, accommodating decimal values.

    Parameters:
    data (dict): A dictionary where keys are the labels and values are the lengths of the bars.
    max_bar_width (int): The maximum width of the bar in characters.
    """
    max_label_length = max(len(label) for label in data.keys())
    max_value = max(data.values())
    bar_graph = ""

    for label, value in data.items():
        # Scale the value to fit within the max_bar_width
        bar_length = int((value / max_value) * max_bar_width)
        bar = '█' * bar_length
        bar_graph += f"{label.ljust(max_label_length)} | {bar} ({value}) \n"

    return bar_graph

def bar_graph_service():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address and port
    server_address = ('localhost', 8100)
    server_socket.bind(server_address)
    print("Server is running and listening for incoming connections...")

    # Listen for incoming connections
    server_socket.listen(1)

    try:
        while True:
            # Accept incoming connection
            client_socket, client_address = server_socket.accept()
            print("Connected to main program:", client_address)

            try:
                while True:
                    # Receive data from main program
                    data = client_socket.recv(1024)
                    if not data:
                        break

                    print("Received data from main program:", data.decode())

                    # Process data
                    processed_data = string_bar_graph(string_to_dict(data.decode()))

                    # Send processed data back to main program
                    client_socket.sendall(processed_data.encode())
                    print("Sent processed data back to main program")

            finally:
                # Clean up the connection
                client_socket.close()
                print("Connection with main program closed")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the server socket
        server_socket.close()
        print("Server socket closed")

if __name__ == "__main__":
    bar_graph_service()

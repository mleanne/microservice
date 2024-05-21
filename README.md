# microservice A to display a bar graph 
# prerequisites - import socket in python
# to start server, run server.py


# to display data as a bar graph in CLI, I've included an example call with example data to show how to use the microservice. You'll need the dict_to_string(): and bar_graph(): functions in your main program. You will call bar_graph() with a dictionary of data, and you can print the results to show the graph in the command line. 

      def dict_to_string(data):
            # Convert the dictionary to a string with a custom delimiter
            return '|'.join(f"{key}:{value}" for key, value in data.items())

      def bar_graph(data):
          main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          main_address = ('localhost', 8100)  # Change to your desired host and port


          try:
              # Connect the socket to the server
              main_socket.connect(main_address)
              print("socket has connected to server")

              string_data = dict_to_string(data)
              # Send the
              print("sending data to microservice")
              main_socket.sendall(string_data.encode())

              # Receive the bar graph
              data = main_socket.recv(1024)
              data = data.decode()

          except Exception as e:
              print("An error occurred:", e)
              data = None

          finally:
              # Clean up the connection
              main_socket.close()

          return data

# EXAMPLE CALL:
  example_data = {
        'Food': 5.50,
        'Gas': 72.90,
        'Housing': 33.00,
        'Personal': 9.80
    }
bar_graph_data = bar_graph(example_data)

    print(bar_graph_data)

![image](https://github.com/mleanne/microservice/assets/102642840/0acecd56-f708-47e6-91d1-f7061a34bb63)



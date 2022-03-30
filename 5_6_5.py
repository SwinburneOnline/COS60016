from multiprocessing import Process, Manager


def change_a_list(x_list):
    x_list.append(100)
    print("Inside the process:", x_list)
    return x_list


num_list = [1, 2, 3, 6]
print("Before the process:", num_list)

if __name__ == '__main__':
    with Manager() as manager:
        pass_list = manager.list(num_list)
        our_process = Process(target=change_a_list, args=[pass_list])
        our_process.start()
        our_process.join()
        num_list = list(pass_list)

    print("Outside the process:", list(num_list))
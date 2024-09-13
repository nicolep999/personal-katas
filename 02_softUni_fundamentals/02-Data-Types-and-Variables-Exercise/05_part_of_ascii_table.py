# start_index = int(input())
# end_index = int(input())
#
# end_result = ""
#
# for index in range(start_index, end_index + 1):
#     end_result += f"{chr(index)} "
#
# print(end_result)

start_index = int(input())
end_index = int(input())

end_result = " ".join(chr(index) for index in range(start_index, end_index + 1))

print(end_result)

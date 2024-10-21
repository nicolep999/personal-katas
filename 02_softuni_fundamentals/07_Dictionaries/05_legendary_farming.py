def main():
    legend_items = {
        "shards": "Shadowmourne",
        "fragments": "Valanyr",
        "motes": "Dragonwrath",
    }
    key_mat = {"shards": 0, "fragments": 0, "motes": 0}
    junk_mat = {}
    junk_order = []
    min_key_mat = 250
    leg_item_found = False

    while not leg_item_found:
        text = input()
        text_list = text.split()

        for i in range(0, len(text_list), 2):
            mat_qty = int(text_list[i])
            mat_vid = text_list[i + 1].lower()

            if mat_vid in key_mat:
                key_mat[mat_vid] += mat_qty
                if key_mat[mat_vid] >= min_key_mat:
                    leg_item_found = True
                    key_mat[mat_vid] -= min_key_mat
                    result = legend_items[mat_vid]
                    print(f"{result} obtained!")
                    break
            else:
                if mat_vid in junk_mat:
                    junk_mat[mat_vid] += mat_qty
                else:
                    junk_mat[mat_vid] = mat_qty
                    junk_order.append(mat_vid)

    for mat in ["shards", "fragments", "motes"]:
        print(f"{mat}: {key_mat[mat]}")

    for item in junk_order:
        print(f"{item}: {junk_mat[item]}")


if __name__ == "__main__":
    main()

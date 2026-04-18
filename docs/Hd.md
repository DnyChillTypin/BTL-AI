# Hướng Dẫn Giải Từng Câu Hỏi 10 Điểm (Ghi thẳng vào Output.txt)

Dưới đây là các đoạn code đã được tách tiêng biệt theo từng câu hỏi của thầy. Lần này, điểm khác biệt là kết quả sẽ **được tự động in thẳng vào phần cuối của file `output.txt`** thay vì chỉ in ra màn hình.

**Cách dùng chung:** Bạn copy đoạn code cần thiết và dán vào cuối file `Branch_And_Bound.py`, **NGAY BÊN DƯỚI** hàm chạy thuật toán.

Ví dụ vị trí dán chuẩn:
```python
if __name__ == "__main__":
    try:
        start_node, end_node, heuristics, graph = read_input("input.txt")
        
        # Bắt buộc phải chạy xong thuật toán chính thì file output.txt mới tạo ra
        branch_and_bound(start_node, end_node, heuristics, graph, "output.txt")
        print("Output made")
        
        # ======== COPY CODE VÀ DÁN VÀO ĐÂY ========
        
        # ==========================================

    except Exception as e:
    ...
```

---

## Câu 1: Tính tổng (tổng trọng số mỗi đỉnh, mỗi cạnh)

```python
# Đoạn code tính tổng
    tong_ts_dinh = sum(heuristics.values())
    tong_ts_canh = sum(w for u in graph for v, w in graph.get(u, []))

    with open("output.txt", "a", encoding="utf-8") as f:
        f.write(f"\n--- CÂU 1 ---\n")
        f.write(f"Tổng trọng số các đỉnh (h(v)) là: {tong_ts_dinh}\n")
        f.write(f"Tổng trọng số các cạnh k(u,v) là: {tong_ts_canh}\n")
```

---

## Câu 2: Tính trung bình (trung bình trọng số mỗi đỉnh, mỗi cạnh)

```python
# Đoạn code tính trung bình
    tong_ts_dinh = sum(heuristics.values())
    tong_ts_canh = sum(w for u in graph for v, w in graph.get(u, []))

    so_luong_dinh = len(heuristics)
    so_luong_canh = sum(len(graph.get(u, [])) for u in graph)

    tb_dinh = tong_ts_dinh / so_luong_dinh if so_luong_dinh > 0 else 0
    tb_canh = tong_ts_canh / so_luong_canh if so_luong_canh > 0 else 0

    with open("output.txt", "a", encoding="utf-8") as f:
        f.write(f"\n--- CÂU 2 ---\n")
        f.write(f"Trung bình trọng số đỉnh là: {tb_dinh:.2f}\n")
        f.write(f"Trung bình trọng số cạnh là: {tb_canh:.2f}\n")
```

---

## Câu 3: Tính min max (tìm đỉnh, cạnh min; tìm đỉnh, cạnh max)

```python
# Đoạn code Tìm Min/Max Đỉnh & Cạnh
    dinh_min = min(heuristics, key=heuristics.get)
    dinh_max = max(heuristics, key=heuristics.get)

    danh_sach_canh = [(u, v, w) for u in graph for v, w in graph.get(u, [])]
    if danh_sach_canh:
        canh_min = min(danh_sach_canh, key=lambda x: x[2])
        canh_max = max(danh_sach_canh, key=lambda x: x[2])
        
    with open("output.txt", "a", encoding="utf-8") as f:
        f.write(f"\n--- CÂU 3 ---\n")
        f.write(f"Đỉnh có trọng số NHỎ nhất: {dinh_min} (h={heuristics[dinh_min]})\n")
        f.write(f"Đỉnh có trọng số LỚN nhất: {dinh_max} (h={heuristics[dinh_max]})\n")
        if danh_sach_canh:
            f.write(f"Cạnh NGẮN nhất là: {canh_min[0]}->{canh_min[1]} (w= {canh_min[2]})\n")
            f.write(f"Cạnh DÀI nhất là: {canh_max[0]}->{canh_max[1]} (w= {canh_max[2]})\n")
```

---

## Câu 4: Tính một điểm có bao nhiêu đường nối vào, nối ra

```python
# Điền điểm thầy yêu cầu vào biến này (ví dụ điểm A)
    diem_can_tim = 'A'

    noi_ra = len(graph.get(diem_can_tim, []))
    noi_vao = sum(1 for u in graph for v, w in graph.get(u, []) if v == diem_can_tim)

    with open("output.txt", "a", encoding="utf-8") as f:
        f.write(f"\n--- CÂU 4 ---\n")
        f.write(f"Đỉnh {diem_can_tim} có {noi_vao} đường nối VÀO.\n")
        f.write(f"Đỉnh {diem_can_tim} có {noi_ra} đường nối RA.\n")
```

---

## Câu 5: Tìm đỉnh có min cạnh nối ra

```python
# Lấy trước danh sách toàn bộ đỉnh có mặt 
    all_nodes = set(heuristics.keys())
    for u in graph:
        all_nodes.add(u)
        for v, w in graph.get(u, []):
            all_nodes.add(v)

    # Lập một Dictionary đo đạc số lượng cạnh nối ra
    out_degree = {node: len(graph.get(node, [])) for node in all_nodes}

    dinh_out_min = min(out_degree, key=out_degree.get)

    with open("output.txt", "a", encoding="utf-8") as f:
        f.write(f"\n--- CÂU 5 ---\n")
        f.write(f"Đỉnh có ÍT cạnh nối ra nhất là {dinh_out_min} ({out_degree[dinh_out_min]} cạnh)\n")
```

---

## Câu 6: Tìm đỉnh có min cạnh nối vào

```python
# Lấy trước danh sách toàn bộ đỉnh có mặt
    all_nodes = set(heuristics.keys())
    for u in graph:
        all_nodes.add(u)
        for v, w in graph.get(u, []):
            all_nodes.add(v)

    # Lập Dictionary đo đạc số lượng cạnh bị trỏ vào
    in_degree = {node: 0 for node in all_nodes}
    for u in graph:
        for v, w in graph.get(u, []):
            in_degree[v] += 1

    dinh_in_min = min(in_degree, key=in_degree.get)

    with open("output.txt", "a", encoding="utf-8") as f:
        f.write(f"\n--- CÂU 6 ---\n")
        f.write(f"Đỉnh có ÍT cạnh nối vào nhất là {dinh_in_min} ({in_degree[dinh_in_min]} cạnh)\n")
```

---

## Câu 7: Một đỉnh có bao nhiêu cạnh (Tổng cộng)

```python
# Điền điểm thầy yêu cầu vào biến này
diem_can_tim = 'A'

noi_ra = len(graph.get(diem_can_tim, []))
noi_vao = sum(1 for u in graph for v, w in graph.get(u, []) if v == diem_can_tim)

tong_so_canh = noi_ra + noi_vao

with open("output.txt", "a", encoding="utf-8") as f:
    f.write(f"\n--- CÂU 7 ---\n")
    f.write(f"Đỉnh {diem_can_tim} có tổng cộng {tong_so_canh} cạnh.\n")
    f.write(f"(Chi tiết: gồm {noi_vao} cạnh nối vào và {noi_ra} cạnh nối ra).\n")
```

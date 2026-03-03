class NodeState:
    def __init__(self, node, g, f, path):
        self.node = node
        self.g = g
        self.f = f
        self.path = path

def read_input(file_path):
    heuristics = {}
    graph = {}
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
        start_node, end_node = lines[0].strip().split()
        
        mode = ""
        for line in lines[1:]:
            line = line.strip()
            if not line: continue
            
            if line == "#HEURISTIC":
                mode = "h"
                continue
            elif line == "#GRAPH":
                mode = "g"
                continue
                
            parts = line.split()
            if mode == "h":
                heuristics[parts[0]] = int(parts[1])
            elif mode == "g":
                u, v, weight = parts[0], parts[1], int(parts[2])
                if u not in graph: graph[u] = []
                graph[u].append((v, weight))
                
    return start_node, end_node, heuristics, graph

def branch_and_bound(start_node, end_node, heuristics, graph, output_file):
    best_cost = float('inf')
    best_path = None
    
    start_state = NodeState(start_node, 0, heuristics[start_node], [start_node])
    L = [start_state]
    
    with open(output_file, 'w', encoding='utf-8') as f_out:
        # Header bảng
        header = f"Brand and Bound \n\n{'TT':<5} | {'TTK':<5} | {'k(u,v)':<6} | {'h(v)':<5} | {'g(v)':<5} | {'f(v)':<5} | {'L1':<30} | {'L'}"
        f_out.write(header + "\n")
        f_out.write("—" * 120 + "\n")
        
        while L:
            current = L.pop(0)
            u = current.node
            
            def format_L(lst):
                if not lst: return "Trống"
                return ", ".join([f"{s.node}({s.f})" for s in lst])

            # Nếu cắt tỉa -> KHÔNG in ra bảng nữa (Bỏ qua dòng CẮT)
            if current.f >= best_cost:
                continue
                
            # Đã đến đích -> Lưu kết quả và In trạng thái ĐÍCH
            if u == end_node:
                if current.g < best_cost:
                    best_cost = current.g
                    best_path = current.path
                f_out.write(f"{u:<5} | {'(ĐÍCH)':<5} | {'-':<6} | {'-':<5} | {'-':<5} | {current.f:<5} | {'-':<30} | {format_L(L)}\n")
                f_out.write("—" * 120 + "\n")
                continue
            
            # Khai triển các đỉnh kề
            neighbors = graph.get(u, [])
            L1 = []
            neighbors_info = []
            
            for v, k_uv in neighbors:
                if v in current.path:
                    continue
                    
                g_v = current.g + k_uv
                h_v = heuristics.get(v, 0)
                f_v = g_v + h_v
                
                new_path = list(current.path)
                new_path.append(v)
                
                new_state = NodeState(v, g_v, f_v, new_path)
                L1.append(new_state)
                neighbors_info.append((v, k_uv, h_v, g_v, f_v))
            
            # Sắp xếp L1 tăng dần theo f(v)
            L1.sort(key=lambda x: (x.f, x.node))
            
            # Cập nhật L
            L = L1 + L
            
            L1_str = format_L(L1)
            L_str = format_L(L)
            
            # In ra bảng
            if not neighbors_info:
                f_out.write(f"{u:<5} | {'-':<5} | {'-':<6} | {'-':<5} | {'-':<5} | {'-':<5} | {L1_str:<30} | {L_str}\n")
            else:
                for idx, info in enumerate(neighbors_info):
                    v, k_uv, h_v, g_v, f_v = info
                    tt_out = u if idx == 0 else ""
                    l1_out = L1_str if idx == 0 else ""
                    l_out = L_str if idx == 0 else ""
                    
                    f_out.write(f"{tt_out:<5} | {v:<5} | {k_uv:<6} | {h_v:<5} | {g_v:<5} | {f_v:<5} | {l1_out:<30} | {l_out}\n")
            
            f_out.write("—" * 120 + "\n")
            
        # In kết quả cuối cùng theo yêu cầu: 1 dòng đường đi, 1 dòng độ dài
        f_out.write("\n")
        if best_path:
            path_str = " —> ".join(best_path)
            f_out.write(f"Đường đi: {path_str}\n")
            f_out.write(f"Độ dài: {best_cost}\n")
        else:
            f_out.write("Không tìm thấy đường đi!\n")

if __name__ == "__main__":
    try:
        start_node, end_node, heuristics, graph = read_input("input.txt")
        branch_and_bound(start_node, end_node, heuristics, graph, "output.txt")
        print("Đã xuất file output.txt thành công!")
    except Exception as e:
        print(f"Lỗi: {e}")
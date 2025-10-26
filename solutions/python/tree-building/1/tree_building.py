class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if not records:
        return None
    
    records.sort(key=lambda x: x.record_id)
    
    # Check 1: Continuous IDs
    for index, record in enumerate(records):
        if record.record_id != index:
            raise ValueError('Record id is invalid or out of order.')
    
    # Check 2: Root validation
    if records[0].parent_id != 0:
        raise ValueError('Node parent_id should be smaller than its record_id.')
    
    # Check 3: Non-root validation (TWO separate checks!)
    for record in records[1:]:
        if record.parent_id == record.record_id:
            raise ValueError('Only root should have equal record and parent id.')
        
        if record.parent_id > record.record_id:
            raise ValueError('Node parent_id should be smaller than its record_id.')
    
    # Build tree
    nodes = {record.record_id: Node(record.record_id) for record in records}
    
    for record in records[1:]:
        nodes[record.parent_id].children.append(nodes[record.record_id])
    
    return nodes[0]
from memory import SharedMemory

def test_memory_add_and_retrieve():
    mem = SharedMemory()
    mem.add_entry("AgentA", "input1", "output1")
    mem.add_entry("AgentB", "input2", "output2")
    
    assert len(mem.history) == 2
    assert mem.get_last_output() == "output2"

def test_memory_clear():
    mem = SharedMemory()
    mem.add_entry("AgentA", "input", "output")
    mem.clear()
    assert len(mem.history) == 0

def test_memory_truncation():
    mem = SharedMemory()
    long_str = "A" * 6000
    mem.add_entry("AgentA", "input", long_str)
    history_str = mem.get_full_history()
    # Assuming truncation happens at e.g., 4000 characters total or similar
    assert len(history_str) < 6000

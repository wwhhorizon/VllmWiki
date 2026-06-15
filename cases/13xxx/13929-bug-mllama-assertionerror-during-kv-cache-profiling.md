# vllm-project/vllm#13929: [Bug]: mllama AssertionError during kv cache profiling

| 字段 | 值 |
| --- | --- |
| Issue | [#13929](https://github.com/vllm-project/vllm/issues/13929) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: mllama AssertionError during kv cache profiling

### Issue 正文摘录

### Your current environment Repro command below. ### 🐛 Describe the bug Attempting to serve `meta-llama/Llama-3.2-11B-Vision-Instruct` with recent vLLM (>=v0.7.3), results in the error below during the execution of `determine_num_available_blocks()` during bootup ``` $ vllm serve meta-llama/Llama-3.2-11B-Vision-Instruct --max-num-seqs 8 ``` ``` Traceback (most recent call last): File "/opt/vllm/lib64/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 400, in run_mp_engine engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/vllm/lib64/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 125, in from_engine_args return cls(ipc_path=ipc_path, ^^^^^^^^^^^^^^^^^^^^^^ File "/opt/vllm/lib64/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 77, in __init__ self.engine = LLMEngine(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/vllm/lib64/python3.12/site-packages/vllm/engine/llm_engine.py", line 277, in __init__ self._initialize_kv_caches() File "/opt/vllm/lib64/python3.12/site-packages/vllm/engine/llm_engine.py", line 426, in _initialize_kv_caches sel...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: mllama AssertionError during kv cache profiling bug ### Your current environment Repro command below. ### 🐛 Describe the bug Attempting to serve `meta-llama/Llama-3.2-11B-Vision-Instruct` with recent vLLM (>=v0.7...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: mllama AssertionError during kv cache profiling bug ### Your current environment Repro command below. ### 🐛 Describe the bug Attempting to serve `meta-llama/Llama-3.2-11B-Vision-Instruct` with recent vLLM (>=v0.7...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ata ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: mllama AssertionError during kv cache profiling bug ### Your current environment Repro command below. ### 🐛 Describe the bug Attempting to serve `meta-llama/Llama-3.2-11B-Vision-Instruct` with recent vLLM (>=v0.7...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ults in the error below during the execution of `determine_num_available_blocks()` during bootup ``` $ vllm serve meta-llama/Llama-3.2-11B-Vision-Instruct --max-num-seqs 8 ``` ``` Traceback (most recent call last): File...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

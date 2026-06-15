# vllm-project/vllm#2785: Qwen1.5-7B-Chat failed

| 字段 | 值 |
| --- | --- |
| Issue | [#2785](https://github.com/vllm-project/vllm/issues/2785) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Qwen1.5-7B-Chat failed

### Issue 正文摘录

`Traceback (most recent call last): File "/home/orbbec/VLM/qwen/vllm_test.py", line 11, in llm = LLM(model="/home/orbbec/VLM/qwen/model/qwen1.5/Qwen1.5-7B-Chat", File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py", line 109, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 356, in from_engine_args engine = cls(*engine_configs, File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 114, in __init__ self._init_cache() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 331, in _init_cache raise ValueError( ValueError: The model's max seq len (32768) is larger than the maximum number of tokens that can be stored in KV cache (1984). Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine.` I saw on the Qianwen official website that version 0.30.0 is supported. I tried it and found an error. May I ask what might have caused it?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Qwen1.5-7B-Chat failed `Traceback (most recent call last): File "/home/orbbec/VLM/qwen/vllm_test.py", line 11, in llm = LLM(model="/home/orbbec/VLM/qwen/model/qwen1.5/Qwen1.5-7B-Chat", File "/usr/local/lib/pyth
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `max_model_len` when initializing the engine.` I saw on the Qianwen official website that version 0.30.0 is supported. I tried it and found an error. May I ask what might have caused it?
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 32768) is larger than the maximum number of tokens that can be stored in KV cache (1984). Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine.` I saw on the Qianwen officia...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: d `Traceback (most recent call last): File "/home/orbbec/VLM/qwen/vllm_test.py", line 11, in llm = LLM(model="/home/orbbec/VLM/qwen/model/qwen1.5/Qwen1.5-7B-Chat", File "/usr/local/lib/python3.10/dist-packages/vllm/entr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

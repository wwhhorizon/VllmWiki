# vllm-project/vllm#31027: [Bug]: 0.13.0 start with CUDA error: the provided PTX was compiled with an unsupported toolchain.

| 字段 | 值 |
| --- | --- |
| Issue | [#31027](https://github.com/vllm-project/vllm/issues/31027) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 0.13.0 start with CUDA error: the provided PTX was compiled with an unsupported toolchain.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug test script: ```python import os import torch from vllm import LLM, SamplingParams if __name__ == '__main__': MODEL_PATH = '/ssd/1/xsank.mz/models/qwen3_omni_30b_a3b_instruct/' llm = LLM( model=MODEL_PATH, trust_remote_code=True, gpu_memory_utilization=0.9, tensor_parallel_size=torch.cuda.device_count(), max_num_seqs=8, max_model_len=32768, seed=1234, ) sampling_params = SamplingParams( temperature=0.0, top_p=0.95, top_k=20, max_tokens=16384, ) messages = [ { "role": "user", "content": [ {"type": "text", "text": "这是一个测试"} ], }, ] outputs = llm.generate([messages], sampling_params=sampling_params) print(outputs[0].outputs[0].text) ``` error log ```shell Loading safetensors checkpoint shards: 93% Completed | 14/15 [00:15 llm = LLM( File "/home/admin/.local/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 351, in __init__ self.llm_engine = LLMEngine.from_engine_args( File "/home/admin/.local/lib/python3.10/site-packages/vllm/v1/engine/llm_engine.py", line 183, in from_engine_args return cls( File "/home/admin/.local/lib/python3.10/site-packages/vllm/v1/engine/llm_engine.py", line 109, in __init__ self.engine_core = Engine...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: 0.13.0 start with CUDA error: the provided PTX was compiled with an unsupported toolchain. bug ### Your current environment ### 🐛 Describe the bug test script: ```python import os import torch from vllm import LL...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: 0.13.0 start with CUDA error: the provided PTX was compiled with an unsupported toolchain. bug ### Your current environment ### 🐛 Describe the bug test script: ```python import os import torch from vllm import LL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: h from vllm import LLM, SamplingParams if __name__ == '__main__': MODEL_PATH = '/ssd/1/xsank.mz/models/qwen3_omni_30b_a3b_instruct/' llm = LLM( model=MODEL_PATH, trust_remote_code=True, gpu_memory_utilization=0.9, tenso...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ng;model_support;sampling_logits attention;cuda;kernel;operator;sampling;triton build_error;crash;mismatch env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _logits attention;cuda;kernel;operator;sampling;triton build_error;crash;mismatch env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

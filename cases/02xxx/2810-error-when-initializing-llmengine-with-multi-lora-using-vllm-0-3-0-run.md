# vllm-project/vllm#2810: Error when initializing LLMEngine with multi lora using vllm==0.3.0 - RuntimeError: CUDA error: no kernel image is available for execution on the device

| 字段 | 值 |
| --- | --- |
| Issue | [#2810](https://github.com/vllm-project/vllm/issues/2810) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Error when initializing LLMEngine with multi lora using vllm==0.3.0 - RuntimeError: CUDA error: no kernel image is available for execution on the device

### Issue 正文摘录

Got the error above while trying to run this code ``` from vllm import EngineArgs, LLMEngine def initialize_engine() -> LLMEngine: """Initialize the LLMEngine.""" # max_loras: controls the number of LoRAs that can be used in the same # batch. Larger numbers will cause higher memory usage, as each LoRA # slot requires its own preallocated tensor. # max_lora_rank: controls the maximum supported rank of all LoRAs. Larger # numbers will cause higher memory usage. If you know that all LoRAs will # use the same rank, it is recommended to set this as low as possible. # max_cpu_loras: controls the size of the CPU LoRA cache. engine_args = EngineArgs(model="meta-llama/Llama-2-7b-chat-hf", revision="c1b0db933684edbfe29a06fa47eb19cc48025e93", enable_lora=True, max_loras=8, max_lora_rank=8, max_cpu_loras=8, max_num_seqs=256) return LLMEngine.from_engine_args(engine_args) if __name__ == '__main__': engine = initialize_engine() ``` ### Machine specification ``` uname -vmpo #56~20.04.1-Ubuntu SMP Tue Nov 28 15:43:31 UTC 2023 x86_64 x86_64 GNU/Linux nvcc --version nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2023 NVIDIA Corporation Built on Mon_Apr__3_17:16:06_PDT_2023 Cuda compilatio...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ce stale Got the error above while trying to run this code ``` from vllm import EngineArgs, LLMEngine def initialize_engine() -> LLMEngine: """Initialize the LLMEngine.""" # max_loras: controls the number of LoRAs that...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: s: controls the size of the CPU LoRA cache. engine_args = EngineArgs(model="meta-llama/Llama-2-7b-chat-hf", revision="c1b0db933684edbfe29a06fa47eb19cc48025e93", enable_lora=True, max_loras=8,
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: initializing LLMEngine with multi lora using vllm==0.3.0 - RuntimeError: CUDA error: no kernel image is available for execution on the device stale Got the error above while trying to run this code ``` from vllm import...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: PU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=======================================================================================| | No running processes fou
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tch. Larger numbers will cause higher memory usage, as each LoRA # slot requires its own preallocated tensor. # max_lora_rank: controls the maximum supported rank of all LoRAs. Larger # numbers will cause higher memory...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

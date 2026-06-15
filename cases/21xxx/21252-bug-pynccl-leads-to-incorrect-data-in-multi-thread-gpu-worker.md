# vllm-project/vllm#21252: [Bug]: pynccl leads to incorrect data in multi-thread GPU-worker

| 字段 | 值 |
| --- | --- |
| Issue | [#21252](https://github.com/vllm-project/vllm/issues/21252) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda;operator |
| 症状 | mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: pynccl leads to incorrect data in multi-thread GPU-worker

### Issue 正文摘录

### Your current environment any cuda environment has this bug ### 🐛 Describe the bug I built a KV connector based on the v1 KV connector API. This connector starts a background thread in each worker process. After the main thread calls `save_kv_layer`, the background thread tries to move data from the GPU memory to the system memory using a special CUDA stream (swap_out_stream). Here’s a simplified version of the logic: ```python async def run_in_background(self, blk_ids, kv_cache_layer): with torch.cuda.stream(self.swap_out_stream): # Using a dedicated CUDA stream host_memory = get_available_system_memory() # Find space in system memory ops.swaps_out(kv_cache_layer, host_mem, blk_ids) event = # get cuda event event.record() while not event.query(): await asyncio.sleep(0) ``` When running vLLM with tpsize=4, the model’s intermediate states sometimes contain invalid values (NaN), which leads to incorrect outputs. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: d tries to move data from the GPU memory to the system memory using a special CUDA stream (swap_out_stream). Here’s a simplified version of the logic: ```python async def run_in_background(self, blk_ids, kv_cache_layer)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: data in multi-thread GPU-worker bug ### Your current environment any cuda environment has this bug ### 🐛 Describe the bug I built a KV connector based on the v1 KV connector API. This connector starts a background threa...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: orrectness distributed_parallel;frontend_api;model_support cuda;operator mismatch;nan_inf env_dependency Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: calls `save_kv_layer`, the background thread tries to move data from the GPU memory to the system memory using a special CUDA stream (swap_out_stream). Here’s a simplified version of the logic: ```python async def run_i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: await asyncio.sleep(0) ``` When running vLLM with tpsize=4, the model’s intermediate states sometimes contain invalid values (NaN), which leads to incorrect outputs. ### Before submitting a new issue... - [x] Make sure...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

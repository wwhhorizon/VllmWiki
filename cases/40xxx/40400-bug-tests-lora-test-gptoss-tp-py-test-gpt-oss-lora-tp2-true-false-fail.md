# vllm-project/vllm#40400: [Bug]: tests/lora/test_gptoss_tp.py::test_gpt_oss_lora_tp2[True-False] fails in eager mode

| 字段 | 值 |
| --- | --- |
| Issue | [#40400](https://github.com/vllm-project/vllm/issues/40400) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: tests/lora/test_gptoss_tp.py::test_gpt_oss_lora_tp2[True-False] fails in eager mode

### Issue 正文摘录

### Your current environment [env.txt](https://github.com/user-attachments/files/26910161/env.txt) ### 🐛 Describe the bug tests/lora/test_gptoss_tp.py::test_gpt_oss_lora_tp2[True-False] fails if run in eager mode with an assertion about a non-contiguous tensor. Modification to `test_gptoss_tp.py` ``` diff --git a/tests/lora/test_gptoss_tp.py b/tests/lora/test_gptoss_tp.py index 68dd87233a..3fd1923c8a 100644 --- a/tests/lora/test_gptoss_tp.py +++ b/tests/lora/test_gptoss_tp.py @@ -129,9 +129,10 @@ def test_gpt_oss_lora_tp2( tensor_parallel_size=2, gpu_memory_utilization=0.8, fully_sharded_loras=fully_sharded_loras, - compilation_config=vllm.config.CompilationConfig( # Avoid OOM - cudagraph_specialize_lora=False, - ), + # compilation_config=vllm.config.CompilationConfig( # Avoid OOM + # cudagraph_specialize_lora=False, + # ), + enforce_eager=True, ) generate_and_test(llm, gptoss20b_lora_files, lora_id=1) ``` stack trace [stack.txt](https://github.com/user-attachments/files/26910184/stack.txt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.v...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tion_config=vllm.config.CompilationConfig( # Avoid OOM - cudagraph_specialize_lora=False, - ), + # compilation_config=vllm.config.CompilationConfig( # Avoid OOM + # cudagraph_specialize_lora=False, + # ), + enforce_eag
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: tests/lora/test_gptoss_tp.py::test_gpt_oss_lora_tp2[True-False] fails in eager mode bug ### Your current environment [env.txt](https://github.com/user-attachments/files/26910161/env.txt) ### 🐛 Describe the bug te...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: llm.config.CompilationConfig( # Avoid OOM - cudagraph_specialize_lora=False, - ), + # compilation_config=vllm.config.CompilationConfig( # Avoid OOM + # cudagraph_specialize_lora=False, + # ), + enforce_eager=True,
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: - compilation_config=vllm.config.CompilationConfig( # Avoid OOM - cudagraph_specialize_lora=False, - ), + # compilation_config=vllm.config.CompilationConfig( # Avoid OOM + # cudagraph_specialize_lora=False, + # ), +
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: fully_sharded_loras=fully_sharded_loras, - compilation_config=vllm.config.CompilationConfig( # Avoid OOM - cudagraph_specialize_lora=False, - ), + # compilation_config=vllm.config.CompilationConfig( # Avoid OOM + # cuda...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

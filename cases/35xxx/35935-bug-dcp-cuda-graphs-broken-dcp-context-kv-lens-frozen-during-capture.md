# vllm-project/vllm#35935: [Bug]: DCP + CUDA graphs broken - dcp_context_kv_lens frozen during capture

| 字段 | 值 |
| --- | --- |
| Issue | [#35935](https://github.com/vllm-project/vllm/issues/35935) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;model_support |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda |
| 症状 | mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DCP + CUDA graphs broken - dcp_context_kv_lens frozen during capture

### Issue 正文摘录

## Bug Description DCP (Decode Context Parallel) with CUDA graphs is broken. The model produces garbage output when DCP > 1 and CUDA graphs are enabled. ## Root Cause Commit `77740191d` ("[Attention][Async] Eliminate \`seq_lens_cpu\` in FlashAttention metadata building with DCP > 1 #29449") moved the computation of `dcp_context_kv_lens` from CPU tensors to GPU tensors: **Before (working):** ```python dcp_context_kv_lens_cpu = seq_lens_cpu - query_kv_lens_cpu dcp_context_kv_lens_cpu = get_dcp_local_seq_lens(...) dcp_context_kv_lens = dcp_context_kv_lens_cpu.to(self.device) # Fresh copy each time ``` **After (broken):** ```python dcp_context_kv_lens = seq_lens - query_kv_lens # GPU computation from frozen tensors! dcp_context_kv_lens = get_dcp_local_seq_lens(...) ``` During CUDA graph capture, the GPU tensors `seq_lens` and `query_start_loc` are captured with dummy values. When the graph replays, the computation `seq_lens - query_kv_lens` uses those frozen dummy values instead of the actual runtime values, causing incorrect attention computation. ## Reproduction ```python from vllm import LLM, SamplingParams llm = LLM( model="Qwen/Qwen2.5-1.5B-Instruct", tensor_parallel_size=4, deco...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: DCP + CUDA graphs broken - dcp_context_kv_lens frozen during capture bug ## Bug Description DCP (Decode Context Parallel) with CUDA graphs is broken. The model produces garbage output when DCP > 1 and CUDA graphs...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Attention][Async] Eliminate \`seq_lens_cpu\` in FlashAttention metadata building with DCP > 1 #29449") moved the computation of `dcp_context_kv_lens` from CPU tensors to GPU tensors: **Before (working):** ```python dcp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e Commit `77740191d` ("[Attention][Async] Eliminate \`seq_lens_cpu\` in FlashAttention metadata building with DCP > 1 #29449") moved the computation of `dcp_context_kv_lens` from CPU tensors to GPU tensors: **Before (wo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: scription DCP (Decode Context Parallel) with CUDA graphs is broken. The model produces garbage output when DCP > 1 and CUDA graphs are enabled. ## Root Cause Commit `77740191d` ("[Attention][Async] Eliminate \`seq_lens_...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: - PR: #29449 correctness attention_kv_cache;model_support attention;cuda mismatch env_dependency Bug Description

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

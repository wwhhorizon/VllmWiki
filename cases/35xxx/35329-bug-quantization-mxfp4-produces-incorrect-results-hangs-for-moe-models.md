# vllm-project/vllm#35329: [Bug]: quantization="mxfp4" produces incorrect results / hangs for MoE models at tensor_parallel_size=1

| 字段 | 值 |
| --- | --- |
| Issue | [#35329](https://github.com/vllm-project/vllm/issues/35329) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;gemm_linear;model_support;moe;quantization;sampling_logits |
| 子分类 | shape_align |
| Operator 关键词 | attention;gemm;kernel;moe;quantization |
| 症状 | crash;mismatch |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: quantization="mxfp4" produces incorrect results / hangs for MoE models at tensor_parallel_size=1

### Issue 正文摘录

### Your current environment - vLLM: 0.15.1 (`vllm/vllm-openai:latest`) - Model: `Qwen/Qwen3-30B-A3B` (128 experts, all-MoE layers) - GPU: 2x NVIDIA RTX 5880 Ada (SM89, 49 GB each) - Also tested with a faithful tiny Qwen3-MoE replica (~190M params, same 128-expert architecture) ### 🐛 Describe the bug ## Bug Description When loading any MoE model with `quantization="mxfp4"` and `tensor_parallel_size=1`, vLLM either produces garbage output, hangs during generation, or crashes depending on the model size and attention backend. This is a separate issue from the `FusedMoE.weight_loader` IndexError (#XXXX) — even with that patch applied, the online MXFP4 quantization path is fundamentally broken for MoE architectures at tp=1. ## Steps to Reproduce ```python from vllm import LLM, SamplingParams # With the FusedMoE weight_loader patch applied (otherwise hits IndexError first) llm = LLM( model="Qwen/Qwen3-30B-A3B", quantization="mxfp4", tensor_parallel_size=1, ) ``` # This hangs or produces degenerate output ` outputs = llm.generate(["What is 2+2?"], SamplingParams(max_tokens=50, temperature=0.0))` Observed Behavior Varies by configuration: - FLASH_ATTN backend, tp=1: Model loads but gener...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: quantization="mxfp4" produces incorrect results / hangs for MoE models at tensor_parallel_size=1 bug;stale ### Your current environment - vLLM: 0.15.1 (`vllm/vllm-openai:latest`) - Model: `Qwen/Qwen3-30B-A3B` (12...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: uring generation, or crashes depending on the model size and attention backend. This is a separate issue from the `FusedMoE.weight_loader` IndexError (#XXXX) — even with that patch applied, the online MXFP4 quantization...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: is fundamentally broken for MoE architectures at tp=1. ## Steps to Reproduce ```python from vllm import LLM, SamplingParams # With the FusedMoE weight_loader patch applied (otherwise hits IndexError first) llm = LLM( mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: chitectures at tp=1. ## Steps to Reproduce ```python from vllm import LLM, SamplingParams # With the FusedMoE weight_loader patch applied (otherwise hits IndexError first) llm = LLM( model="Qwen/Qwen3-30B-A3B", quantiza...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: quantization="mxfp4" produces incorrect results / hangs for MoE models at tensor_parallel_size=1 bug;stale ### Your current environment - vLLM: 0.15.1 (`vllm/vllm-openai:latest`) - Model: `Qwen/Qwen3-30B-A3B` (12...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

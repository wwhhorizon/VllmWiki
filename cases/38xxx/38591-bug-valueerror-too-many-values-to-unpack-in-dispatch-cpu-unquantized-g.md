# vllm-project/vllm#38591: Bug: ValueError: too many values to unpack in dispatch_cpu_unquantized_gemm when loading Qwen3.5-4B

| 字段 | 值 |
| --- | --- |
| Issue | [#38591](https://github.com/vllm-project/vllm/issues/38591) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;gemm_linear;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;gemm |
| 症状 | crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Bug: ValueError: too many values to unpack in dispatch_cpu_unquantized_gemm when loading Qwen3.5-4B

### Issue 正文摘录

# Bug Report: `ValueError: too many values to unpack` in `dispatch_cpu_unquantized_gemm` when loading Qwen3.5-4B ### Description When attempting to run offline inference with the newly supported `Qwen/Qwen3.5-4B` model on a non-CUDA environment (macOS Apple Silicon / CPU), the `LLM` initialization crashes during weight loading. The crash occurs inside `dispatch_cpu_unquantized_gemm` because it assumes all linear layer weights are exactly 2-dimensional (`N, K = layer.weight.size()`), but the new `Qwen3_5ForConditionalGeneration` architecture appears to have layers with 1D or 3D+ weights being passed through the unquantized GEMM CPU dispatch. *Note: The model loads and serves correctly when running on CUDA environments via the OpenAI compatible server, indicating this is specifically a bug with the CPU/MPS fallback weight loader in vLLM.* ### Environment * **OS:** macOS (Apple Silicon M-series) * **vLLM Version:** Nightly / Source (commit `ab1a6a43fa9500697dd01e73aa372c8777cd7a5b`) * **Python Version:** 3.12.12 * **Model:** `Qwen/Qwen3.5-4B` ### Steps to Reproduce Run the standard offline `LLM` initialization OR run the `api_server` on a CPU/Mac machine: **Method 1 (Offline inferenc...

## 现有链接修复摘要

#38600 [Bugfix] too many values to unpack in dispatch_cpu_unquantized_gemm

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: UDA environments via the OpenAI compatible server, indicating this is specifically a bug with the CPU/MPS fallback weight loader in vLLM.* ### Environment * **OS:** macOS (Apple Silicon M-series) * **vLLM Version:** Nig...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: too many values to unpack in dispatch_cpu_unquantized_gemm when loading Qwen3.5-4B # Bug Report: `ValueError: too many values to unpack` in `dispatch_cpu_unquantized_gemm` when loading Qwen3.5-4B ### Description When at...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Bug: ValueError: too many values to unpack in dispatch_cpu_unquantized_gemm when loading Qwen3.5-4B # Bug Report: `ValueError: too many values to unpack` in `dispatch_cpu_unquantized_gemm` when loading Qwen3.5-4B ### De...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: line inference with the newly supported `Qwen/Qwen3.5-4B` model on a non-CUDA environment (macOS Apple Silicon / CPU), the `LLM` initialization crashes during weight loading. The crash occurs inside `dispatch_cpu_unquan...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: **Python Version:** 3.12.12 * **Model:** `Qwen/Qwen3.5-4B` ### Steps to Reproduce Run the standard offline `LLM` initialization OR run the `api_server` on a CPU/Mac machine: **Method 1 (Offline inference):** ```python f...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38600](https://github.com/vllm-project/vllm/pull/38600) | closes_keyword | 0.95 | [Bugfix] too many values to unpack in dispatch_cpu_unquantized_gemm | Fix #38591: ValueError when loading Qwen3.5-4B on CPU/Mac environments. The `dispatch_cpu_unquantized_gemm` function assumes all linear layer weights are exactly 2-dimensional ( |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

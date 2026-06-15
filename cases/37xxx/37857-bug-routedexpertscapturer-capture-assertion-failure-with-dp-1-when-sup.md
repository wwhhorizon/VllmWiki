# vllm-project/vllm#37857: [Bug]: RoutedExpertsCapturer.capture() assertion failure with DP>1 when supports_internal_mk=True

| 字段 | 值 |
| --- | --- |
| Issue | [#37857](https://github.com/vllm-project/vllm/issues/37857) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support;moe;quantization;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;moe;quantization;sampling |
| 症状 | crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RoutedExpertsCapturer.capture() assertion failure with DP>1 when supports_internal_mk=True

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `RoutedExpertsCapturer.capture()` crashes with `AssertionError` during CUDA graph capture when `--data-parallel-size > 1` and the quant method uses the Modular Kernel (MK) path (`supports_internal_mk=True`). **Launch args:** ```bash --tensor-parallel-size 8 \ --data-parallel-size 2 \ --enable-expert-parallel \ --enable-return-routed-experts ``` Model: any MoE model (e.g. DeepSeek-V3-like architecture with 128 routed experts, top_k=4). **Error (on Ray worker during CUDA graph warmup):** ``` ray.exceptions.RayTaskError(AssertionError): ray::RayWorkerWrapper.execute_method() File "vllm/model_executor/layers/fused_moe/routed_experts_capturer.py", line 181, in capture assert cumsum[-1] == topk_ids.shape[0] AssertionError ``` **Root cause:** `capture()` assumes `topk_ids` contains all DP ranks' tokens concatenated (the naive dispatch path). It uses `cumsum(num_tokens_across_dp_cpu)` to slice this rank's portion: ```python # routed_experts_capturer.py:178-183 cumsum = torch.cumsum(ctx.dp_metadata.num_tokens_across_dp_cpu, dim=0) assert cumsum[-1] == topk_ids.shape[0] # ← fails end_loc = cumsum[self.dp_rank] start_loc = end_loc - token_n...

## 现有链接修复摘要

#37879 fix(moe): fix RoutedExpertsCapturer assertion failure with DP>1 and MK path

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: RoutedExpertsCapturer.capture() assertion failure with DP>1 when supports_internal_mk=True ### Your current environment ### 🐛 Describe the bug `RoutedExpertsCapturer.capture()` crashes with `AssertionError` durin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: `RoutedExpertsCapturer.capture()` crashes with `AssertionError` during CUDA graph capture when `--data-parallel-size > 1` and the quant method uses the Modular Kernel (MK) path (`supports_internal_mk=True`). **Launch ar...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: python # routed_experts_capturer.py:178-183 cumsum = torch.cumsum(ctx.dp_metadata.num_tokens_across_dp_cpu, dim=0) assert cumsum[-1] == topk_ids.shape[0] # ← fails end_loc = cumsum[self.dp_rank] start_loc = end_loc - to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: -size 2 \ --enable-expert-parallel \ --enable-return-routed-experts ``` Model: any MoE model (e.g. DeepSeek-V3-like architecture with 128 routed experts, top_k=4). **Error (on Ray worker during CUDA graph warmup):** ```...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: assumes `topk_ids` contains all DP ranks' tokens concatenated (the naive dispatch path). It uses `cumsum(num_tokens_across_dp_cpu)` to slice this rank's portion: ```python # routed_experts_capturer.py:178-183 cumsum = t...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37879](https://github.com/vllm-project/vllm/pull/37879) | closes_keyword | 0.95 | fix(moe): fix RoutedExpertsCapturer assertion failure with DP>1 and MK path | Fixes #37857 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

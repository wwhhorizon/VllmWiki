# vllm-project/vllm#22591: [Bug]: CPU penalty operations fail on CUDA-capable systems

| 字段 | 值 |
| --- | --- |
| Issue | [#22591](https://github.com/vllm-project/vllm/issues/22591) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | hardware_porting;model_support;sampling_logits |
| 子分类 | shape_align |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | crash;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CPU penalty operations fail on CUDA-capable systems

### Issue 正文摘录

> PS: i know this bug report was AI generated, but it is an issue i found, and it is described accurately ### Your current environment NA ### 🐛 Describe the bug # VLLM Bug Report: Incorrect CPU Penalty Fallback Condition ## 🐛 **Bug Summary** VLLM's penalty fallback mechanism incorrectly checks `current_platform.is_cuda()` instead of `logits.is_cuda()`, causing CPU tensors to attempt CUDA operations on CUDA-capable systems. ## 📍 **Location** **File:** `vllm/_custom_ops.py` **Function:** `apply_repetition_penalties()` **Line:** ~315 ## 🔍 **Problematic Code** ```python def apply_repetition_penalties(logits: torch.Tensor, prompt_mask: torch.Tensor, output_mask: torch.Tensor, repetition_penalties: torch.Tensor) -> None: """Apply repetition penalties to logits in-place.""" if current_platform.is_cuda() and logits.is_contiguous(): # ❌ BUG HERE apply_repetition_penalties_cuda(logits, prompt_mask, output_mask, repetition_penalties) else: apply_repetition_penalties_torch(logits, prompt_mask, output_mask, repetition_penalties) ``` ## 🚨 **Issue Description** The condition `current_platform.is_cuda()` checks if the **platform** supports CUDA, not if the **tensors** are on CUDA. This causes: 1....

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: s to logits in-place.""" if current_platform.is_cuda() and logits.is_contiguous(): # ❌ BUG HERE apply_repetition_penalties_cuda(logits, prompt_mask, output_mask, repetition_penalties) else: apply_repetition_penalties_to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CPU penalty operations fail on CUDA-capable systems bug > PS: i know this bug report was AI generated, but it is an issue i found, and it is described accurately ### Your current environment NA ### 🐛 Describe the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: nt NA ### 🐛 Describe the bug # VLLM Bug Report: Incorrect CPU Penalty Fallback Condition ## 🐛 **Bug Summary** VLLM's penalty fallback mechanism incorrectly checks `current_platform.is_cuda()` instead of `logits.is_cuda(...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: rence ## 💥 **Error Reproduction** ```python # On a CUDA-capable system: import torch from vllm._custom_ops import apply_repetition_penalties # Create CPU tensors logits = torch.randn(1, 1000, device='cpu') prompt_mask =...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ble systems** → Try to use CUDA operations → **Crash** 2. **Prevents CPU offloading** → Can't use CPU for sampling while GPU handles model inference ## 💥 **Error Reproduction** ```python # On a CUDA-capable system: impo...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

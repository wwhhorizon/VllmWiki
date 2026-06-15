# vllm-project/vllm#18498: [Bug][Failing Test]: LoRA 2 - lora/test_lora_functions.py::test_lora_functions_sync

| 字段 | 值 |
| --- | --- |
| Issue | [#18498](https://github.com/vllm-project/vllm/issues/18498) |
| 状态 | closed |
| 标签 | bug;ci-failure |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;crash;mismatch |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][Failing Test]: LoRA 2 - lora/test_lora_functions.py::test_lora_functions_sync

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug https://buildkite.com/vllm/ci/builds/20460/steps?jid=0196f343-0fdb-4d91-80da-728e0fb8174c Summary: ``` [2025-05-21T16:00:09Z] FAILED lora/test_lora_functions.py::test_lora_functions_sync[True] - Exception: Call to add_lora method failed: CUDA error: an illegal memory access was encountered [2025-05-21T16:00:09Z] CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. [2025-05-21T16:00:09Z] For debugging consider passing CUDA_LAUNCH_BLOCKING=1 [2025-05-21T16:00:09Z] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` Stack: ``` [2025-05-21T15:50:19Z] ERROR 05-21 08:50:19 [core.py:559] Invocation of add_lora method failed [2025-05-21T15:50:19Z] ERROR 05-21 08:50:19 [core.py:559] Traceback (most recent call last): [2025-05-21T15:50:19Z] ERROR 05-21 08:50:19 [core.py:559] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 556, in _handle_client_request [2025-05-21T15:50:19Z] ERROR 05-21 08:50:19 [core.py:559] output.result = method( [2025-05-21T15:50:19Z] ERROR 05-21 08:50:19 [core.py:559] ^^^^^^^ [2025-05-21T15:50:19Z] ER...

## 现有链接修复摘要

#18543 [Bugfix] Use random hidden states in dummy sampler run

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: est]: LoRA 2 - lora/test_lora_functions.py::test_lora_functions_sync bug;ci-failure ### Your current environment N/A ### 🐛 Describe the bug https://buildkite.com/vllm/ci/builds/20460/steps?jid=0196f343-0fdb-4d91-80da-72...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t_lora_functions_sync[True] - Exception: Call to add_lora method failed: CUDA error: an illegal memory access was encountered [2025-05-21T16:00:09Z] CUDA kernel errors might be asynchronously reported at some other API...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: estions. correctness ci_build;frontend_api cuda;kernel build_error;crash;mismatch #18543 [Bugfix] Use random hidden states in dummy sampler run Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: rrect. [2025-05-21T16:00:09Z] For debugging consider passing CUDA_LAUNCH_BLOCKING=1 [2025-05-21T16:00:09Z] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` Stack: ``` [2025-05-21T15:50:19Z] ERROR...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 2025-05-21T15:50:19Z] ERROR 05-21 08:50:19 [core.py:559] return self.model_executor.add_lora(lora_request) [2025-05-21T15:50:19Z] ERROR 05-21 08:50:19 [core.py:559] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [2025-05-21...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#18543](https://github.com/vllm-project/vllm/pull/18543) | closes_keyword | 0.95 | [Bugfix] Use random hidden states in dummy sampler run | FIX #18498 FIX #18525 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

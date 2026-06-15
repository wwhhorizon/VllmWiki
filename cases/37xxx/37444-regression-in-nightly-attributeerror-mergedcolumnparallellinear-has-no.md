# vllm-project/vllm#37444: Regression in nightly: AttributeError 'MergedColumnParallelLinear' has no attribute 'weight' with Qwen3.5-9B

| 字段 | 值 |
| --- | --- |
| Issue | [#37444](https://github.com/vllm-project/vllm/issues/37444) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | fp8;quantization |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Regression in nightly: AttributeError 'MergedColumnParallelLinear' has no attribute 'weight' with Qwen3.5-9B

### Issue 正文摘录

## Bug Report ### Description The latest `cu130-nightly` build (v0.17.2rc1.dev49, image built 2026-03-18) crashes during model loading for `cyankiwi/Qwen3.5-9B-AWQ-4bit` (architecture: `Qwen3_5ForConditionalGeneration`). The previous nightly (v0.17.1rc1.dev177, ~2026-03-16) works correctly. ### Error ``` File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/qwen3_5.py", line 185, in forward self.in_proj_qkvz.weight.shape[0], AttributeError: 'MergedColumnParallelLinear' object has no attribute 'weight' torch._dynamo.exc.ObservedAttributeError: 'MergedColumnParallelLinear' object has no attribute 'weight' ``` ### Steps to Reproduce ```bash docker run --gpus all vllm/vllm-openai:cu130-nightly \ cyankiwi/Qwen3.5-9B-AWQ-4bit \ --quantization compressed-tensors \ --kv-cache-dtype fp8 \ --trust-remote-code ``` ### Environment - **GPU**: NVIDIA RTX 5070 Ti (16 GiB, SM 120 / Blackwell) - **Working image**: `vllm/vllm-openai:cu130-nightly` built ~2026-03-16 (v0.17.1rc1.dev177+gd4c57863f) - **Broken image**: `vllm/vllm-openai:cu130-nightly` built 2026-03-18 (v0.17.2rc1.dev49+g8b6325758) - **Model**: `cyankiwi/Qwen3.5-9B-AWQ-4bit` (Qwen3_5ForConditionalGeneration, hybrid Ma...

## 现有链接修复摘要

#37448 Fix AttributeError in Qwen3.5 GDN layers with quantized models

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ith Qwen3.5-9B ## Bug Report ### Description The latest `cu130-nightly` build (v0.17.2rc1.dev49, image built 2026-03-18) crashes during model loading for `cyankiwi/Qwen3.5-9B-AWQ-4bit` (architecture: `Qwen3_5ForConditio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: -03-18) crashes during model loading for `cyankiwi/Qwen3.5-9B-AWQ-4bit` (architecture: `Qwen3_5ForConditionalGeneration`). The previous nightly (v0.17.1rc1.dev177, ~2026-03-16) works correctly. ### Error ``` File "/usr/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ll vllm/vllm-openai:cu130-nightly \ cyankiwi/Qwen3.5-9B-AWQ-4bit \ --quantization compressed-tensors \ --kv-cache-dtype fp8 \ --trust-remote-code ``` ### Environment - **GPU**: NVIDIA RTX 5070 Ti (16 GiB, SM 120 / Black...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: cyankiwi/Qwen3.5-9B-AWQ-4bit \ --quantization compressed-tensors \ --kv-cache-dtype fp8 \ --trust-remote-code ``` ### Environment - **GPU**: NVIDIA RTX 5070 Ti (16 GiB, SM 120 / Blackwell) - **Working image**: `vllm/vll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tributeError 'MergedColumnParallelLinear' has no attribute 'weight' with Qwen3.5-9B ## Bug Report ### Description The latest `cu130-nightly` build (v0.17.2rc1.dev49, image built 2026-03-18) crashes during model loading...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37448](https://github.com/vllm-project/vllm/pull/37448) | closes_keyword | 0.95 | Fix AttributeError in Qwen3.5 GDN layers with quantized models | Fixes #37444 ## Test plan - [ ] Verify `cyankiwi/Qwen3.5-9B-AWQ-4bit` loads and runs inference without error - [ ] Verify non-quantized Qwen3.5 models still work (no regression fr |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

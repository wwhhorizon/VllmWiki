# vllm-project/vllm#36890: [Bug]: ROCm: tries to allocate 192GB VRAM for Qwen3.5 0.8B

| 字段 | 值 |
| --- | --- |
| Issue | [#36890](https://github.com/vllm-project/vllm/issues/36890) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ROCm: tries to allocate 192GB VRAM for Qwen3.5 0.8B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running vLLM with Qwen/Qwen3.5-0.8B on ROCm causes the engine to fail during initialization. ```bash vllm serve Qwen/Qwen3.5-0.8B --max-model-len 2621 ``` vLLM attempts to allocate ~192GB of GPU memory, even though the GPU only has 32GB VRAM and the model itself is only 0.8B parameters. This full logs in: Extra: use --language-model-only not trigger the vram issue ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#38334 [ROCm] Use Triton attention fallback for ViT to avoid SDPA OOM

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;kernel;sampling;triton build_error;nan_inf;oom env_dependency #3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: ROCm: tries to allocate 192GB VRAM for Qwen3.5 0.8B bug;rocm ### Your current environment ### 🐛 Describe the bug Running vLLM with Qwen/Qwen3.5-0.8B on ROCm causes the engine to fail during initialization. ```bash
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ;model_support;sampling_logits;speculative_decoding cuda;kernel;sampling;triton build_error;nan_inf;oom env_dependency #38334 [ROCm] Use Triton attention fallback for ViT to avoid SDPA OOM Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: en3.5-0.8B --max-model-len 2621 ``` vLLM attempts to allocate ~192GB of GPU memory, even though the GPU only has 32GB VRAM and the model itself is only 0.8B parameters. This full logs in: Extra: use --language-model-onl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: ROCm: tries to allocate 192GB VRAM for Qwen3.5 0.8B bug;rocm ### Your current environment ### 🐛 Describe the bug Running vLLM with Qwen/Qwen3.5-0.8B on ROCm causes the engine to fail during initialization. ```bas...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38334](https://github.com/vllm-project/vllm/pull/38334) | closes_keyword | 0.95 | [ROCm] Use Triton attention fallback for ViT to avoid SDPA OOM | Fixes #36890 Related: #27706 ## Test plan - [ ] Verify Qwen3.5-0.8B starts without OOM on gfx906 - [ ] Verify existing ViT attention tests still pass on MI300X/MI325X - [ ] Verify |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

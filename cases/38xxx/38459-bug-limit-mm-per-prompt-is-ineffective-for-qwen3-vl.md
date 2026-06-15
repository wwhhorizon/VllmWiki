# vllm-project/vllm#38459: [Bug]: `limit_mm_per_prompt` is ineffective for Qwen3-VL

| 字段 | 值 |
| --- | --- |
| Issue | [#38459](https://github.com/vllm-project/vllm/issues/38459) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `limit_mm_per_prompt` is ineffective for Qwen3-VL

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug For Qwen3-VL, the encoder cache remains unchanged regardless of the `limit_mm_per_prompt` setting. As shown below, it reports using only a single image for calculation, ``` Encoder cache will be initialized with a budget of 16384 tokens, and profiled with 1 image items of the maximum feature size. ``` even though I have configured the limit_mm_per_prompt as follows. ``` {"video": 1} {"video": {"count": 1, "width": 1280, "height": 1280, "num_frames": 768}} {"video": {"count": 1, "width": 1280, "height": 1280, "num_frames": 768}, "image": 768} ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#38465 [Bugfix] Fix limit_mm_per_prompt being ignored for encoder cache profiling

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: `limit_mm_per_prompt` is ineffective for Qwen3-VL bug ### Your current environment ### 🐛 Describe the bug For Qwen3-VL, the encoder cache remains unchanged regardless of the `limit_mm_per_prompt` setting. As show...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ``` Encoder cache will be initialized with a budget of 16384 tokens, and profiled with 1 image items of the maximum feature size. ``` even though I have configured the limit_mm_per_prompt as follows. ``` {"video": 1} {"...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency #38465 [Bugfix] Fix limit_mm_per_prompt being ignored for encoder cache profiling Your current environme...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38465](https://github.com/vllm-project/vllm/pull/38465) | closes_keyword | 0.95 | [Bugfix] Fix limit_mm_per_prompt being ignored for encoder cache profiling | Fixes #38459 The encoder cache profiling in `MultiModalBudget` always used a hardcoded count of `1` for each modality when computing max tokens per item via `get_mm_max_toks_per_i |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

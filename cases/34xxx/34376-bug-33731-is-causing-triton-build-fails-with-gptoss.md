# vllm-project/vllm#34376: [Bug]: #33731 is causing Triton build fails with gptoss

| 字段 | 值 |
| --- | --- |
| Issue | [#34376](https://github.com/vllm-project/vllm/issues/34376) |
| 状态 | closed |
| 标签 | bug;rocm;gpt-oss |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: #33731 is causing Triton build fails with gptoss

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After this PR #33731 gpt-oss runs fail with a Triton build error. **Repro:** VLLM_ROCM_USE_AITER=1 vllm serve openai/gpt-oss-120b --tensor-parallel-size 4 --async-scheduling --max-model-len 8192 --load-format dummy ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: #33731 is causing Triton build fails with gptoss bug;rocm;gpt-oss ### Your current environment ### 🐛 Describe the bug After this PR #33731 gpt-oss runs fail with a Triton build error. **Repro:** VLLM_ROCM_USE_AIT...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: #33731 is causing Triton build fails with gptoss bug;rocm;gpt-oss ### Your current environment ### 🐛 Describe the bug After this PR #33731 gpt-oss runs fail with a Triton build error. **Repro:** VLLM_ROCM_USE_AIT...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: #33731 is causing Triton build fails with gptoss bug;rocm;gpt-oss ### Your current environment ### 🐛 Describe the bug After this PR #33731 gpt-oss runs fail with a Triton build error. **Repro:** VLLM_ROCM_USE_AIT...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: #33731 is causing Triton build fails with gptoss bug;rocm;gpt-oss ### Your current environment ### 🐛 Describe the bug After this PR #33731 gpt-oss runs fail with a Triton build error. **Repro:** VLLM_ROCM_USE_AIT...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: uild;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;kernel;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#14911: [Bug]: UserWarning on skipping serialisation of PostGradPassManager

| 字段 | 值 |
| --- | --- |
| Issue | [#14911](https://github.com/vllm-project/vllm/issues/14911) |
| 状态 | closed |
| 标签 | bug;stale;v1 |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: UserWarning on skipping serialisation of PostGradPassManager

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have started to see this serialization warning whenever running `vllm serve` from time to time when running with v1: ```prolog /workspace/project/.venv/lib/python3.12/site-packages/torch/utils/_config_module.py:189: UserWarning: Skipping serialization of post_grad_custom_post_pass value warnings.warn(f"Skipping serialization of {k} value {v}") ``` Not sure how impactful is this, or we can ignore this. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantiza...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: UserWarning on skipping serialisation of PostGradPassManager bug;stale;v1 ### Your current environment ### 🐛 Describe the bug I have started to see this serialization warning whenever running `vllm serve` from ti...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rolog /workspace/project/.venv/lib/python3.12/site-packages/torch/utils/_config_module.py:189: UserWarning: Skipping serialization of post_grad_custom_post_pass value warnings.warn(f"Skipping serialization of {k} value...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: UserWarning on skipping serialisation of PostGradPassManager bug;stale;v1 ### Your current environment ### 🐛 Describe the bug I have started to see this serialization warning whenever running `vllm serve` from ti...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

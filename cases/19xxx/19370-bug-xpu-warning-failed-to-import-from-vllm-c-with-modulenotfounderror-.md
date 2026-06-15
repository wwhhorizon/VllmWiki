# vllm-project/vllm#19370: [Bug]: [XPU] WARNING Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")

| 字段 | 值 |
| --- | --- |
| Issue | [#19370](https://github.com/vllm-project/vllm/issues/19370) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [XPU] WARNING Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm using the dockerfile.xpu available as part of this repository, and right after importing vllm, I see the following warning: > WARNING 06-09 13:02:57 [_logger.py:68] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") The vllm library somehow works (although I havent tested it much yet), and I can query the model, but I'm concerned about what functionalities might be missing due to this warning. I tried running vllm without XPU support, and the warning no longer appears. I checked the following issues on GitHub: https://github.com/vllm-project/vllm/issues/1814 https://github.com/vllm-project/vllm/issues/14714 However, they are closed and dont provide an easy fix (its not a problem with the vllm folder name or windows)- the issue persists, at least with this Dockerfile. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: [XPU] WARNING Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") bug ### Your current environment ### 🐛 Describe the bug I'm using the dockerfile.xpu available as part of this rep...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: le. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pport;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;import_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: mehow works (although I havent tested it much yet), and I can query the model, but I'm concerned about what functionalities might be missing due to this warning. I tried running vllm without XPU support, and the warning...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ons. correctness ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;import_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

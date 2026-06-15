# vllm-project/vllm#25762: [Bug]: AssertionError: Failed to apply prompt replacement for mm_items['image'][1]

| 字段 | 值 |
| --- | --- |
| Issue | [#25762](https://github.com/vllm-project/vllm/issues/25762) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError: Failed to apply prompt replacement for mm_items['image'][1]

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I encountered an error when using lmms-eval to evaluate the model. The model is initialized via vllm, and I encountered an assertion error. Could you please advise what this assertion error might be related to, and where I should start debugging? The Assertion Error: ```bash AssertionError: Failed to apply prompt replacement for mm_items['image'][1] ``` The conda environment I used: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm cuda;operator;triton build_error;crash env_dependency You...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ibe the bug I encountered an error when using lmms-eval to evaluate the model. The model is initialized via vllm, and I encountered an assertion error. Could you please advise what this assertion error might be related...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: nment ### 🐛 Describe the bug I encountered an error when using lmms-eval to evaluate the model. The model is initialized via vllm, and I encountered an assertion error. Could you please advise what this assertion error...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: frontend_api;hardware_porting;model_support;multimodal_vlm cuda;operator;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

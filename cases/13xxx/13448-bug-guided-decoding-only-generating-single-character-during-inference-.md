# vllm-project/vllm#13448: [Bug]: Guided decoding only generating single character during inference with finetuned model

| 字段 | 值 |
| --- | --- |
| Issue | [#13448](https://github.com/vllm-project/vllm/issues/13448) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Guided decoding only generating single character during inference with finetuned model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Getting below generated text while using guided decoding with choices in a list. it happens after the first inference. so if I want to run the inference on 100 test samples. the first one generates required tokens but from next one it starts generating single characters only. Generated text: 'A' Generated text: 'A' Generated text: 'C' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current env...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 'C' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ly generating single character during inference with finetuned model bug;stale ### Your current environment ### 🐛 Describe the bug Getting below generated text while using guided decoding with choices in a list. it happ...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ecoding only generating single character during inference with finetuned model bug;stale ### Your current environment ### 🐛 Describe the bug Getting below generated text while using guided decoding with choices in a lis...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#18468: [Bug]: Host CPU Docker image on Docker Hub

| 字段 | 值 |
| --- | --- |
| Issue | [#18468](https://github.com/vllm-project/vllm/issues/18468) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Host CPU Docker image on Docker Hub

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug There's no CPU Docker image hosted on your docker hub. I did some digging and it seems to me that you do expect to be hosting and pushing Docker CPU images, see for example #12615. Not sure why the images are not being hosted but it would be helpful for the community to have cpu images hosted. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Host CPU Docker image on Docker Hub bug;stale ### Your current environment ### 🐛 Describe the bug There's no CPU Docker image hosted on your docker hub. I did some digging and it seems to me that you do expect to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Host CPU Docker image on Docker Hub bug;stale ### Your current environment ### 🐛 Describe the bug There's no CPU Docker image hosted on your docker hub. I did some digging and it seems to me that you do expect to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ots of frequently asked questions. correctness ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

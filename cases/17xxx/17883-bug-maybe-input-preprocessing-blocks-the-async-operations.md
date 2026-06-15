# vllm-project/vllm#17883: [Bug]: (Maybe) Input preprocessing blocks the async operations

| 字段 | 值 |
| --- | --- |
| Issue | [#17883](https://github.com/vllm-project/vllm/issues/17883) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: (Maybe) Input preprocessing blocks the async operations

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Is the following lines: https://github.com/vllm-project/vllm/blob/3d1e3876520ae60271b14e009829a53e1cfb3e86/vllm/v1/engine/async_llm.py#L223-L226 blocks the async operations? I found `add_request()` is slow and runs in sequential when the input has big data (e.g. video numpy arrays). After checking the code, I think this operation may block the async operation. Is it possible to execute this operation in another process, wait the process done, and transfer the processed data back to main process and continue for the rest of code? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error;slowdown env_dependency;memory_layout Your current e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: de? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: (Maybe) Input preprocessing blocks the async operations bug;stale ### Your current environment ### 🐛 Describe the bug Is the following lines: https://github.com/vllm-project/vllm/blob/3d1e3876520ae60271b14e009829...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: (Maybe) Input preprocessing blocks the async operations bug;stale ### Your current environment ### 🐛 Describe the bug Is the following lines: https://github.com/vllm-project/vllm/blob/3d1e3876520ae60271b14e009829...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error;slowdown env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

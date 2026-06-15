# vllm-project/vllm#26081: [Bug]: .chat() does not clean up in case of validation failure

| 字段 | 值 |
| --- | --- |
| Issue | [#26081](https://github.com/vllm-project/vllm/issues/26081) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: .chat() does not clean up in case of validation failure

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When passing a batch of prompts to `.chat()` on the LLM class it tries to validate and add requests one by one to the internal scheduler queue. If for example one of the requests raises a ValueError due to tokens exceeding the max model length previous requests have already been added to the scheduler queue. Since the exception stops `_run_engine()` from being called and draining the queue there are now orphaned requests in the scheduler queue. In our code base we catch the exception and try to split the batch in 2 halves to isolate the offending request and make progress on the unproblematic ones. However, when we call `.chat()` after catching the exception it's output now contains more outputs than inputs (fresh batch + orphaned requests). The LLM class does not expose the request_ids in anyway and as such it is not possible to correlate inputs and outputs when this happens. It also violates the contract of `.chat()` that "outputs are returned in the same order as inputs" Simplified example: ``` def infer(chat_messages): try: outputs = model.chat(chat_messages ) except Exception as e: if len(chat_messages) == 1: return [ErrorOu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;frontend_api;hardware_porting;model_support;scheduler_memory cuda build_error env_dependency;shape Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ch of prompts to `.chat()` on the LLM class it tries to validate and add requests one by one to the internal scheduler queue. If for example one of the requests raises a ValueError due to tokens exceeding the max model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ()` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: one of the requests raises a ValueError due to tokens exceeding the max model length previous requests have already been added to the scheduler queue. Since the exception stops `_run_engine()` from being called and drai...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;frontend_api;hardware_porting;model_support;scheduler_memory cud...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

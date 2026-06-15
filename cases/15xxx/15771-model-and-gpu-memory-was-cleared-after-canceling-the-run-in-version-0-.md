# vllm-project/vllm#15771: Model and GPU memory was cleared after canceling the run in version 0.8.2

| 字段 | 值 |
| --- | --- |
| Issue | [#15771](https://github.com/vllm-project/vllm/issues/15771) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Model and GPU memory was cleared after canceling the run in version 0.8.2

### Issue 正文摘录

### Your current environment Most updated VLLM version: 0.8.2 ### 🐛 Describe the bug Problem with 0.8.2. This time a very strange error: I was running simulation for 100 iterations, cancel the process after 20 rounds and let it run again, it was not doing anything, then I check the GPU usage and I saw 0% along with 0 GB is used from GPU memory. Very strange to see you can not cancel the run otherwise is like deleting your model. This problem does not happen in 0.7.3. I wonder what went wrong in 0.8.2 that caused this. If you cancel your run the you need start the session from scratch and load your model, etc. all over again. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Model and GPU memory was cleared after canceling the run in version 0.8.2 bug;stale ### Your current environment Most updated VLLM version: 0.8.2 ### 🐛 Describe the bug Problem with 0.8.2. This time a very strange error...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: in. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Model and GPU memory was cleared after canceling the run in version 0.8.2 bug;stale ### Your current environment Most updated VLLM version: 0.8.2 ### 🐛 Describe the bug Problem with 0.8.2. This time a very strange error...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Model and GPU memory was cleared after canceling the run in version 0.8.2 bug;stale ### Your current environment Most updated VLLM version: 0.8.2 ### 🐛 Describe the bug Problem with 0.8.2. This time a very strange err
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: and GPU memory was cleared after canceling the run in version 0.8.2 bug;stale ### Your current environment Most updated VLLM version: 0.8.2 ### 🐛 Describe the bug Problem with 0.8.2. This time a very strange error: I wa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

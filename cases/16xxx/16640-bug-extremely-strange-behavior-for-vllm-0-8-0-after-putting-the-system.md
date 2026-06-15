# vllm-project/vllm#16640: [Bug]: extremely strange behavior for VLLM >0.8.0 after putting the system in running mode

| 字段 | 值 |
| --- | --- |
| Issue | [#16640](https://github.com/vllm-project/vllm/issues/16640) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: extremely strange behavior for VLLM >0.8.0 after putting the system in running mode

### Issue 正文摘录

### Your current environment Databricks. Python: 3.11 Latest version of transformers and VLLM = 0.8.3 Same problem for 0.8.2 ### 🐛 Describe the bug I found very strange issue with release of 0.8.0 onward. This is a very critical, yet super strange issue and I think it needs to be addressed. I notice I can load my model using vllm with no problem, however when I place my system in running mode using the following command: `input()` Then I interrupt or cancel it, the GPU memory and model would reset and I have to reload the model all from scratch. How is something like this even happening? No such problem exists in priors versions especially 0.7.3. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: bug;stale ### Your current environment Databricks. Python: 3.11 Latest version of transformers and VLLM = 0.8.3 Same problem for 0.8.2 ### 🐛 Describe the bug I found very strange issue with release of 0.8.0 onward. This...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .3. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: sing the following command: `input()` Then I interrupt or cancel it, the GPU memory and model would reset and I have to reload the model all from scratch. How is something like this even happening? No such problem exist...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ange issue and I think it needs to be addressed. I notice I can load my model using vllm with no problem, however when I place my system in running mode using the following command: `input()` Then I interrupt or cancel...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ge behavior for VLLM >0.8.0 after putting the system in running mode bug;stale ### Your current environment Databricks. Python: 3.11 Latest version of transformers and VLLM = 0.8.3 Same problem for 0.8.2 ### 🐛 Describe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

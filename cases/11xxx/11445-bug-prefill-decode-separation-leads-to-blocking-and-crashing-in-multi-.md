# vllm-project/vllm#11445: [Bug]: Prefill/decode separation leads to blocking and crashing in multi concurrent scenarios

| 字段 | 值 |
| --- | --- |
| Issue | [#11445](https://github.com/vllm-project/vllm/issues/11445) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Prefill/decode separation leads to blocking and crashing in multi concurrent scenarios

### Issue 正文摘录

### Your current environment pip3 install vllm==0.6.5 bash [disaggregted_prefill.sh](https://github.com/vllm-project/vllm/blob/main/examples/disaggregated_prefill.sh) # Annotate the partial code of pkill to ensure that the service works properly ### Model Input Dumps The model did not crash, using an open-source model models/Qwen1.5-4B-Chat. Believe that the issue does not involve model types, only bugs in communication components. ### 🐛 Describe the bug ### Summary PyNcclConnector is used on H20, and the official example of standardized execution is provided, [disaggregted_prefill.sh](https://github.com/vllm-project/vllm/blob/main/examples/disaggregated_prefill.sh) ### Phenomenon The request is no longer responding and the service has not crashed ![image](https://github.com/user-attachments/assets/829b7e86-d0bb-41df-8471-1b1ed42ae201) ### Step Execute disaggregted_prefill.sh, ensure that the prefill and decode services are started, and test the curl command with feedback of 200. Follow the steps below to start concurrency: 1. Use Locust for stress testing 2. Start the pressure test and enter user=10 ### Info After blocking for a period of time, the proxy displays that the prefill...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Prefill/decode separation leads to blocking and crashing in multi concurrent scenarios bug;stale ### Your current environment pip3 install vllm==0.6.5 bash [disaggregted_prefill.sh](https://github.com/vllm-projec...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: multi concurrent scenarios bug;stale ### Your current environment pip3 install vllm==0.6.5 bash [disaggregted_prefill.sh](https://github.com/vllm-project/vllm/blob/main/examples/disaggregated_prefill.sh) # Annotate the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: the partial code of pkill to ensure that the service works properly ### Model Input Dumps The model did not crash, using an open-source model models/Qwen1.5-4B-Chat. Believe that the issue does not involve model types,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: prefill.sh, ensure that the prefill and decode services are started, and test the curl command with feedback of 200. Follow the steps below to start concurrency: 1. Use Locust for stress testing 2. Start the pressure te...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: og) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

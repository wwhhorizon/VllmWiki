# vllm-project/vllm#14374: [RFC]: Drop Support for OpenVINO

| 字段 | 值 |
| --- | --- |
| Issue | [#14374](https://github.com/vllm-project/vllm/issues/14374) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Drop Support for OpenVINO

### Issue 正文摘录

### Motivation. OpenVINO backend was initially integrated as an alternatively to the CPU backend and has branched out the vLLM execution logic for every levels (executor, model runner, and attention backend). #5377 Over the last 9 months, we have been the following * Relatively low usage as reported in Github Issues and Slack discussions * The Intel CPU codepath is more mature and largely compatible for Arm as well. * The OpenVINO code path complicated with codebase * CI and build became difficult to maintain I would like to propose to move OpenVINO off from the main codebase, and transition to a vLLM out of tree platform plugin if desired. OpenVINO can follow the same approach as Ascend and Spyre with the plugin approach #11162 ### Proposed Change. * Remove OpenVINO codepath, build and test. * Optionally, create vllm-project/vllm-openvino if the developers want to maintain plugin level compatibility. ### Feedback Period. 2 weeks. By March 20. ### CC List. cc @ilya-lavrenov @WoosukKwon @youkaichao @robertgshaw2-redhat @mgoin ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot livin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e for Arm as well. * The OpenVINO code path complicated with codebase * CI and build became difficult to maintain I would like to propose to move OpenVINO off from the main codebase, and transition to a vLLM out of tree...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [RFC]: Drop Support for OpenVINO RFC ### Motivation. OpenVINO backend was initially integrated as an alternatively to the CPU backend and has branched out the vLLM execution logic for every levels (executor, model runne...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: aintain plugin level compatibility. ### Feedback Period. 2 weeks. By March 20. ### CC List. cc @ilya-lavrenov @WoosukKwon @youkaichao @robertgshaw2-redhat @mgoin ### Any Other Things. _No response_ ### Before submitting...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nd has branched out the vLLM execution logic for every levels (executor, model runner, and attention backend). #5377 Over the last 9 months, we have been the following * Relatively low usage as reported in Github Issues...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ach #11162 ### Proposed Change. * Remove OpenVINO codepath, build and test. * Optionally, create vllm-project/vllm-openvino if the developers want to maintain plugin level compatibility. ### Feedback Period. 2 weeks. By...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

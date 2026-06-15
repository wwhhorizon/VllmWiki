# vllm-project/vllm#40329: [Usage]: 部署Qwen3-vl-embedding如何进行视频请求？部署命令是什么？支持么

| 字段 | 值 |
| --- | --- |
| Issue | [#40329](https://github.com/vllm-project/vllm/issues/40329) |
| 状态 | open |
| 标签 | usage |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: 部署Qwen3-vl-embedding如何进行视频请求？部署命令是什么？支持么

### Issue 正文摘录

### Your current environment [0;36m(APIServer pid=1)[0;0m WARNING 04-20 00:16:49 [protocol.py:117] The following fields were present in the request but ignored: {'max_pixels', 'min_pixels', 'max_frames', 'total_pixels', 'fps'}。 ### How would you like to use vllm 我希望可以有个vllm部署Qwen3-vl-embedding docker命令 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ### How would you like to use vllm 我希望可以有个vllm部署Qwen3-vl-embedding docker命令 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: r命令 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: 部署Qwen3-vl-embedding如何进行视频请求？部署命令是什么？支持么 usage ### Your current environment [0;36m(APIServer pid=1)[0;0m WARNING 04-20 00:16:49 [protocol.py:117] The following fields were present in the request but ignored:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 4-20 00:16:49 [protocol.py:117] The following fields were present in the request but ignored: {'max_pixels', 'min_pixels', 'max_frames', 'total_pixels', 'fps'}。 ### How would you like to use vllm 我希望可以有个vllm部署Qwen3-vl-e...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#15597: [Bug]:vllm从0.7.0开始版本部署Qwen2_vl服务存在内存(不是GPU显存)泄漏问题

| 字段 | 值 |
| --- | --- |
| Issue | [#15597](https://github.com/vllm-project/vllm/issues/15597) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 30; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:vllm从0.7.0开始版本部署Qwen2_vl服务存在内存(不是GPU显存)泄漏问题

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 使用0.7.0版本的vllm部署Qwen2_vl模型服务时，对服务进行请求后，服务相关进程内存不会释放，最终打爆服务器内存，导致服务停止，测试发现0.6.6版本无此问题，0.7.0及以上版本均有此问题。 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]:vllm从0.7.0开始版本部署Qwen2_vl服务存在内存(不是GPU显存)泄漏问题 bug ### Your current environment ### 🐛 Describe the bug 使用0.7.0版本的vllm部署Qwen2_vl模型服务时，对服务进行请求后，服务相关进程内存不会释放，最终打爆服务器内存，导致服务停止，测试发现0.6.6版本无此问题，0.7.0及以上版本均有此问题。 ### Before...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

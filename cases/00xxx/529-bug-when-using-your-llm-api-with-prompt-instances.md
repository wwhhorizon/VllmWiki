# vllm-project/vllm#529: Bug when using your LLM API with prompt instances..

| 字段 | 值 |
| --- | --- |
| Issue | [#529](https://github.com/vllm-project/vllm/issues/529) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Bug when using your LLM API with prompt instances..

### Issue 正文摘录

Hi, when using the model.generate API, I just run into this issue (200 dataset samples, stuck at 30%). If possible, could you provide any suggestions? This is really weird, as a rare case to this particular NL prompt, where your api runs smoothly with other prompt cases in my current tests. Thanks in advance!

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: weird, as a rare case to this particular NL prompt, where your api runs smoothly with other prompt cases in my current tests. Thanks in advance!
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: g when using your LLM API with prompt instances.. bug Hi, when using the model.generate API, I just run into this issue (200 dataset samples, stuck at 30%). If possible, could you provide any suggestions? This is really...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ompt, where your api runs smoothly with other prompt cases in my current tests. Thanks in advance!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

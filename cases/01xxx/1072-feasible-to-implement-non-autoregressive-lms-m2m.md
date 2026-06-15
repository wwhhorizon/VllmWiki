# vllm-project/vllm#1072: Feasible to implement  non-autoregressive LMs? (M2M)

| 字段 | 值 |
| --- | --- |
| Issue | [#1072](https://github.com/vllm-project/vllm/issues/1072) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Feasible to implement  non-autoregressive LMs? (M2M)

### Issue 正文摘录

Hey. I'm starting to try to implement M2M in vLLM and noticed that all the currently supported models use Causal language models (decoder only), while M2M is non-autoregressive and has an encoder-decoder architecture. Is it still possible to implement a vLLM version of M2M or should I just give up 🥲 Appreciate any help with this : )

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: n encoder-decoder architecture. Is it still possible to implement a vLLM version of M2M or should I just give up 🥲 Appreciate any help with this : )
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ecoder only), while M2M is non-autoregressive and has an encoder-decoder architecture. Is it still possible to implement a vLLM version of M2M or should I just give up 🥲 Appreciate any help with this : )
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ry to implement M2M in vLLM and noticed that all the currently supported models use Causal language models (decoder only), while M2M is non-autoregressive and has an encoder-decoder architecture. Is it still possible to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: iced that all the currently supported models use Causal language models (decoder only), while M2M is non-autoregressive and has an encoder-decoder architecture. Is it still possible to implement a vLLM version of M2M or...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

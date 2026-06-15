# vllm-project/vllm#16320: [Bug]: `torch.compile` not compatible with Qwen2.5-VL

| 字段 | 值 |
| --- | --- |
| Issue | [#16320](https://github.com/vllm-project/vllm/issues/16320) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `torch.compile` not compatible with Qwen2.5-VL

### Issue 正文摘录

Hello 👋 Im using vllm 0.8.2, engine V1. While running script I got `torch.compile is turned on, but the model does not support it. Please open an issue on GitHub if you want it to be supported.` If I understood it correctly, you use torch.compile by default without option to turn it off (?). Any ideas how to bypass it without switching back to slower engine V0? Ref. to [#15737](https://github.com/vllm-project/vllm/issues/15737)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: `torch.compile` not compatible with Qwen2.5-VL bug;stale Hello 👋 Im using vllm 0.8.2, engine V1. While running script I got `torch.compile is turned on, but the model does not support it. Please open an issue on...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: `torch.compile` not compatible with Qwen2.5-VL bug;stale Hello 👋 Im using vllm 0.8.2, engine V1. While running script I got `torch.compile is turned on, but the model does not support it. Please open an issue on...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: `torch.compile` not compatible with Qwen2.5-VL bug;stale Hello 👋 Im using vllm 0.8.2, engine V1. While running script I got `torch.compile is turned on, but the model does not support it. Please open an issue on...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

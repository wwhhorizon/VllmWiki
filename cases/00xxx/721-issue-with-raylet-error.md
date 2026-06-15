# vllm-project/vllm#721: Issue with raylet error

| 字段 | 值 |
| --- | --- |
| Issue | [#721](https://github.com/vllm-project/vllm/issues/721) |
| 状态 | closed |
| 标签 |  |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Issue with raylet error

### Issue 正文摘录

Hi, I'm using vllm to run llama-13B on two V100-16GB GPUs. I deployed vllm with the API server. However, When the context is long, the server returns: [2023-08-09 22:39:16,002 E 209 223] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2023-08-09_22-27-32_558284_37 is over 95% full, available space: 60427313152; capacity: 1599538507776. Object creation will fail if spilling is required. and the model is stuck and cannot return anything. Is it because the GPU size is too small or is there any other approaches to resolve this issue? Thanks!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Issue with raylet error Hi, I'm using vllm to run llama-13B on two V100-16GB GPUs. I deployed vllm with the API server. However, When the context is long, the server returns: [2023-08-09 22:39:16,002 E 209 223] (raylet)...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 9_22-27-32_558284_37 is over 95% full, available space: 60427313152; capacity: 1599538507776. Object creation will fail if spilling is required. and the model is stuck and cannot return anything. Is it because the GPU s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: l is stuck and cannot return anything. Is it because the GPU size is too small or is there any other approaches to resolve this issue? Thanks!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

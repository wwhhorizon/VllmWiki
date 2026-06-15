# vllm-project/vllm#2466: vLLM Distributed Inference stuck when using multi -GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#2466](https://github.com/vllm-project/vllm/issues/2466) |
| 状态 | closed |
| 标签 |  |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vLLM Distributed Inference stuck when using multi -GPU

### Issue 正文摘录

I am trying to run inferece server on multi GPU using this on (4 * NVIDIA GeForce RTX 3090) server. **python -u -m vllm.entrypoints.api_server --host 0.0.0.0 --model mistralai/Mistral-7B-Instruct-v0.2 --tensor-parallel-size 4** while this works fine when using --tensor-parallel-size =1 , but on using tensor-parallel-size >1 it stuck on strat up. Thanks

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng to run inferece server on multi GPU using this on (4 * NVIDIA GeForce RTX 3090) server. **python -u -m vllm.entrypoints.api_server --host 0.0.0.0 --model mistralai/Mistral-7B-Instruct-v0.2 --tensor-parallel-size 4**...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: **python -u -m vllm.entrypoints.api_server --host 0.0.0.0 --model mistralai/Mistral-7B-Instruct-v0.2 --tensor-parallel-size 4** while this works fine when using --tensor-parallel-size =1 , but on using tensor-parallel-s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

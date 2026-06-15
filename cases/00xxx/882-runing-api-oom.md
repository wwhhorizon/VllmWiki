# vllm-project/vllm#882: Runing API OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#882](https://github.com/vllm-project/vllm/issues/882) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Runing API OOM

### Issue 正文摘录

Hi, I use this command to craete an openai API, and receive OOM: `python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-70b-hf` This seems to be caused by the fact that this command only defaults to the first GPU and my current node is 8 A100-40Gs. so it's causing OOM. Is there any way to make it load on multiple GPUs? I don't need a program, so I can't use the `tensor_parallel_size=8`.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ai API, and receive OOM: `python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-70b-hf` This seems to be caused by the fact that this command only defaults to the first GPU and my current node is 8 A10...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: hat this command only defaults to the first GPU and my current node is 8 A100-40Gs. so it's causing OOM. Is there any way to make it load on multiple GPUs? I don't need a program, so I can't use the `tensor_parallel_siz...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Runing API OOM Hi, I use this command to craete an openai API, and receive OOM: `python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-70b-hf` This seems to be caused by the fact that this command only...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

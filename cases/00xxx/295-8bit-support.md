# vllm-project/vllm#295: 8bit support

| 字段 | 值 |
| --- | --- |
| Issue | [#295](https://github.com/vllm-project/vllm/issues/295) |
| 状态 | closed |
| 标签 |  |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | quantization |
| 子分类 | memory |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> 8bit support

### Issue 正文摘录

Hi, will vllm support 8bit quantization? Like https://github.com/TimDettmers/bitsandbytes In HF, we can run a 13B LLM on a 24G GPU with `load_in_8bit=True`. Although PageAttention can save 25% of GPU memory, but we have to deploy a 13B LLM on a 26G GPU, at least. In the cloud, v100-32G is more expensive than A5000-24G 😭 Is there any way to save video memory usage? 😭

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 8bit support Hi, will vllm support 8bit quantization? Like https://github.com/TimDettmers/bitsandbytes In HF, we can run a 13B LLM on a 24G GPU with `load_in_8bit=True`. Although PageAttention can save 25% of GPU memory...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 4G GPU with `load_in_8bit=True`. Although PageAttention can save 25% of GPU memory, but we have to deploy a 13B LLM on a 26G GPU, at least. In the cloud, v100-32G is more expensive than A5000-24G 😭 Is there any way to s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 8bit quantization? Like https://github.com/TimDettmers/bitsandbytes In HF, we can run a 13B LLM on a 24G GPU with `load_in_8bit=True`. Although PageAttention can save 25% of GPU memory, but we have to deploy a 13B LLM o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

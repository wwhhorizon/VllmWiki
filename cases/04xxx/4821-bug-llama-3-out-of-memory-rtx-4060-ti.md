# vllm-project/vllm#4821: [Bug]: Llama 3 - Out of memory - RTX 4060 TI

| 字段 | 值 |
| --- | --- |
| Issue | [#4821](https://github.com/vllm-project/vllm/issues/4821) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Llama 3 - Out of memory - RTX 4060 TI

### Issue 正文摘录

### Your current environment vllm 0.4.2 ### 🐛 Describe the bug Hello. Would anyone have an example of how I could run Llama 3 on an NVIDIA RTX 4060 TI 16GB? I tried to do inference with this model https://huggingface.co/rhaymison/Llama-3-portuguese-Tom-cat-8b-instruct and a lora adapter but it always gives out of memory. I enabled enforce eager, increased the max GPU memory to 1, even reduced the size of the SWAP but it still overflowed the memory.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Llama 3 - Out of memory - RTX 4060 TI bug ### Your current environment vllm 0.4.2 ### 🐛 Describe the bug Hello. Would anyone have an example of how I could run Llama 3 on an NVIDIA RTX 4060 TI 16GB? I tried to do...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: Llama 3 - Out of memory - RTX 4060 TI bug ### Your current environment vllm 0.4.2 ### 🐛 Describe the bug Hello. Would anyone have an example of how I could run Llama 3 on an NVIDIA RTX 4060 TI 16GB? I tried to do...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: always gives out of memory. I enabled enforce eager, increased the max GPU memory to 1, even reduced the size of the SWAP but it still overflowed the memory.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

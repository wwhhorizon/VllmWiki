# vllm-project/vllm#12215: [Doc]:  FP8 KV Cache feature only supoorts  Llama 2  so far?

| 字段 | 值 |
| --- | --- |
| Issue | [#12215](https://github.com/vllm-project/vllm/issues/12215) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]:  FP8 KV Cache feature only supoorts  Llama 2  so far?

### Issue 正文摘录

### 📚 The doc issue i assume FP8 KV Cache can significantly improve inference speed and save memory space. my questions is how many models does it supports? is it true only Llama 2 is supported? (https://github.com/vllm-project/vllm/tree/main/examples/other/fp8) because i find that kind of hard to believe thank u ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Doc]: FP8 KV Cache feature only supoorts Llama 2 so far? documentation ### 📚 The doc issue i assume FP8 KV Cache can significantly improve inference speed and save memory space. my questions is how many models does it...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Doc]: FP8 KV Cache feature only supoorts Llama 2 so far? documentation ### 📚 The doc issue i assume FP8 KV Cache can significantly improve inference speed and save memory space. my questions is how many models does it...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Doc]: FP8 KV Cache feature only supoorts Llama 2 so far? documentation ### 📚 The doc issue i assume FP8 KV Cache can significantly improve inference speed and save memory space. my questions is how many models does it...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

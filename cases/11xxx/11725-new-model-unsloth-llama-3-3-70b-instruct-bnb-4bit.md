# vllm-project/vllm#11725: [New Model]: unsloth/Llama-3.3-70B-Instruct-bnb-4bit

| 字段 | 值 |
| --- | --- |
| Issue | [#11725](https://github.com/vllm-project/vllm/issues/11725) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: unsloth/Llama-3.3-70B-Instruct-bnb-4bit

### Issue 正文摘录

### The model to consider. https://huggingface.co/unsloth/Llama-3.3-70B-Instruct-bnb-4bit ### The closest model vllm already supports. not sure the closet one. ### What's your difficulty of supporting the model you want? unsloth based is inference faster. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: unsloth/Llama-3.3-70B-Instruct-bnb-4bit new-model ### The model to consider. https://huggingface.co/unsloth/Llama-3.3-70B-Instruct-bnb-4bit ### The closest model vllm already supports. not sure the closet o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: er. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [New Model]: unsloth/Llama-3.3-70B-Instruct-bnb-4bit new-model ### The model to consider. https://huggingface.co/unsloth/Llama-3.3-70B-Instruct-bnb-4bit ### The closest model vllm already supports. not sure the closet o...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

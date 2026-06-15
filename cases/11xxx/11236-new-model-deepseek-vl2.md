# vllm-project/vllm#11236: [New Model]: DeepSeek-VL2

| 字段 | 值 |
| --- | --- |
| Issue | [#11236](https://github.com/vllm-project/vllm/issues/11236) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: DeepSeek-VL2

### Issue 正文摘录

### The model to consider. https://huggingface.co/deepseek-ai/deepseek-vl2 https://huggingface.co/deepseek-ai/deepseek-vl2-small https://huggingface.co/deepseek-ai/deepseek-vl2-tiny ### The closest model vllm already supports. DeepSeekV2 is the base language model, so that should already be supported. From what I can tell the new vision support is simply siglip with an mlp projector. https://huggingface.co/deepseek-ai/deepseek-vl2/blob/e6adb2bce35b94ecc84fbb46d130ce60a7bb4d43/config.json#L129-L144 ### What's your difficulty of supporting the model you want? I think should be similar to supporting any other Llava-style model, we should have all the pieces implemented and just need a new model definition. However support has not landed in transformers yet. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: DeepSeek-VL2 new-model ### The model to consider. https://huggingface.co/deepseek-ai/deepseek-vl2 https://huggingface.co/deepseek-ai/deepseek-vl2-small https://huggingface.co/deepseek-ai/deepseek-vl2-tiny #...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: deepseek-ai/deepseek-vl2 https://huggingface.co/deepseek-ai/deepseek-vl2-small https://huggingface.co/deepseek-ai/deepseek-vl2-tiny ### The closest model vllm already supports. DeepSeekV2 is the base language model, so...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#17264: [New Model]: New model support moonshotai/Kimi-Audio-7B-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#17264](https://github.com/vllm-project/vllm/issues/17264) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: New model support moonshotai/Kimi-Audio-7B-Instruct

### Issue 正文摘录

### The model to consider. https://huggingface.co/moonshotai/Kimi-Audio-7B ### The closest model vllm already supports. OpenAI whisper: https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/whisper.py Qwen2.5 Omni: https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/qwen2_5_omni_thinker.py Step Audio (branch): https://github.com/stepfun-ai/Step-Audio ### What's your difficulty of supporting the model you want? This is the first time I contribute to new model. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: New model support moonshotai/Kimi-Audio-7B-Instruct ### The model to consider. https://huggingface.co/moonshotai/Kimi-Audio-7B ### The closest model vllm already supports. OpenAI whisper: https://github.com...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: l. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

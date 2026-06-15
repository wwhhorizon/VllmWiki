# vllm-project/vllm#16244: [New Model]: efficient-speech/lite-whisper-large-v3

| 字段 | 值 |
| --- | --- |
| Issue | [#16244](https://github.com/vllm-project/vllm/issues/16244) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: efficient-speech/lite-whisper-large-v3

### Issue 正文摘录

### The model to consider. Excerpt from [LiteASR Abstract](https://github.com/efeslab/LiteASR?tab=readme-ov-file#abstract) _We introduce LiteASR, a low-rank compression scheme for ASR encoders that significantly reduces inference costs while maintaining transcription accuracy_ Currently when running: ```bash vllm serve efficient-speech/lite-whisper-large-v3 --trust-remote-code --tokenizer openai/whisper-large-v3 ``` vllm throws following error: ``` ValueError: LiteWhisperForConditionalGeneration has no vLLM implementation and the Transformers implementation is not compatible with vLLM. Try setting VLLM_USE_V1=0. ``` ### The closest model vllm already supports. whisper ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: at significantly reduces inference costs while maintaining transcription accuracy_ Currently when running: ```bash vllm serve efficient-speech/lite-whisper-large-v3 --trust-remote-code --tokenizer openai/whisper-large-v...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: at significantly reduces inference costs while maintaining transcription accuracy_ Currently when running: ```bash vllm serve efficient-speech/lite-whisper-large-v3 --trust-remote-code --tokenizer openai/whisper-large-v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [New Model]: efficient-speech/lite-whisper-large-v3 stale ### The model to consider. Excerpt from [LiteASR Abstract](https://github.com/efeslab/LiteASR?tab=readme-ov-file#abstract) _We introduce LiteASR, a low-rank comp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [New Model]: efficient-speech/lite-whisper-large-v3 stale ### The model to consider. Excerpt from [LiteASR Abstract](https://github.com/efeslab/LiteASR?tab=readme-ov-file#abstract) _We introduce LiteASR, a low-rank comp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

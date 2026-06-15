# vllm-project/vllm#15425: [New Model]: Baichuan-Audio

| 字段 | 值 |
| --- | --- |
| Issue | [#15425](https://github.com/vllm-project/vllm/issues/15425) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Baichuan-Audio

### Issue 正文摘录

### The model to consider. huggingface links: instruct: https://huggingface.co/baichuan-inc/Baichuan-Audio-Instruct base: https://huggingface.co/baichuan-inc/Baichuan-Audio-Base github repo: https://github.com/baichuan-inc/Baichuan-Audio ### The closest model vllm already supports. Its audio tokenizer includes `Whisper encoder`. And its decoder uses a U-Net structure inspired by Matcha-TTS and CosyVoice. ### What's your difficulty of supporting the model you want? This is an end to end large audio model. It may possess a new model architecture. Please see its repo or report paper for details. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: Baichuan-Audio new-model;stale ### The model to consider. huggingface links: instruct: https://huggingface.co/baichuan-inc/Baichuan-Audio-Instruct base: https://huggingface.co/baichuan-inc/Baichuan-Audio-Ba...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [New Model]: Baichuan-Audio new-model;stale ### The model to consider. huggingface links: instruct: https://huggingface.co/baichuan-inc/Baichuan-Audio-Instruct base: https://huggingface.co/baichuan-inc/Baichuan-Audio-Ba...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: : Baichuan-Audio new-model;stale ### The model to consider. huggingface links: instruct: https://huggingface.co/baichuan-inc/Baichuan-Audio-Instruct base: https://huggingface.co/baichuan-inc/Baichuan-Audio-Base github r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nt? This is an end to end large audio model. It may possess a new model architecture. Please see its repo or report paper for details. ### Before submitting a new issue... - [x] Make sure you already searched for releva...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#10737: [New Model]: Qwen/QwQ-32B-Preview

| 字段 | 值 |
| --- | --- |
| Issue | [#10737](https://github.com/vllm-project/vllm/issues/10737) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 27; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Qwen/QwQ-32B-Preview

### Issue 正文摘录

### The model to consider. https://huggingface.co/Qwen/QwQ-32B-Preview ### The closest model vllm already supports. Qwen/Qwen2.5-32B-Instruct ### What's your difficulty of supporting the model you want? Processing Long Texts The current config.json is set for context length up to 32,768 tokens. To handle extensive inputs exceeding 32,768 tokens, we utilize [YaRN](https://arxiv.org/abs/2309.00071), a technique for enhancing model length extrapolation, ensuring optimal performance on lengthy texts. For supported frameworks, you could add the following to config.json to enable YaRN: { ..., "rope_scaling": { "factor": 4.0, "original_max_position_embeddings": 32768, "type": "yarn" } } For deployment, we recommend using vLLM. Please refer to our [Documentation](https://qwen.readthedocs.io/en/latest/deployment/vllm.html) for usage if you are not familar with vLLM. Presently, vLLM only supports static YARN, which means the scaling factor remains constant regardless of input length, potentially impacting performance on shorter texts. We advise adding the rope_scaling configuration only when processing long contexts is required. ### Before submitting a new issue... - [X] Make sure you alrea...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: Qwen/QwQ-32B-Preview new-model;stale ### The model to consider. https://huggingface.co/Qwen/QwQ-32B-Preview ### The closest model vllm already supports. Qwen/Qwen2.5-32B-Instruct ### What's your difficulty...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e utilize [YaRN](https://arxiv.org/abs/2309.00071), a technique for enhancing model length extrapolation, ensuring optimal performance on lengthy texts. For supported frameworks, you could add the following to config.js...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Qwen/QwQ-32B-Preview new-model;stale ### The model to consider. https://huggingface.co/Qwen/QwQ-32B-Preview ### The closest model vllm already supports. Qwen/Qwen2.5-32B-Instruct ### What's your difficulty...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: LM. Please refer to our [Documentation](https://qwen.readthedocs.io/en/latest/deployment/vllm.html) for usage if you are not familar with vLLM. Presently, vLLM only supports static YARN, which means the scaling factor r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

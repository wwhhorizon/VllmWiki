# vllm-project/vllm#39964: [New Model]: Support for microsoft/VibeVoice-ASR

| 字段 | 值 |
| --- | --- |
| Issue | [#39964](https://github.com/vllm-project/vllm/issues/39964) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Support for microsoft/VibeVoice-ASR

### Issue 正文摘录

### The model to consider. I would like to request support for the microsoft/VibeVoice-ASR model in vLLM. The recommended way to run VibeVoice with vLLM is through a specific Docker setup provided in the [Microsoft VibeVoice repository](https://github.com/microsoft/VibeVoice/blob/main/docs/vibevoice-vllm-asr.md), which often uses a plugin-based approach with specific vLLM versions (e.g., v0.14.1). However, I have encountered the following issues. While it seems to work within the specific Docker container environment, attempting to serve the model directly using the standard vllm serve microsoft/VibeVoice-ASR command does not work, as the architecture is not natively recognized by vLLM. (vLLM version : v0.19.0) Serve the model using the standard CLI: vllm serve microsoft/VibeVoice-ASR. - Model Link: https://huggingface.co/microsoft/VibeVoice-ASR - Reference Implementation: [Microsoft VibeVoice GitHub](https://github.com/microsoft/VibeVoice)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: in vLLM. The recommended way to run VibeVoice with vLLM is through a specific Docker setup provided in the [Microsoft VibeVoice repository](https://github.com/microsoft/VibeVoice/blob/main/docs/vibevoice-vllm-asr.md), w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: Support for microsoft/VibeVoice-ASR ### The model to consider. I would like to request support for the microsoft/VibeVoice-ASR model in vLLM. The recommended way to run VibeVoice with vLLM is through a spec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tandard vllm serve microsoft/VibeVoice-ASR command does not work, as the architecture is not natively recognized by vLLM. (vLLM version : v0.19.0) Serve the model using the standard CLI: vllm serve microsoft/VibeVoice-A...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: for microsoft/VibeVoice-ASR ### The model to consider. I would like to request support for the microsoft/VibeVoice-ASR model in vLLM. The recommended way to run VibeVoice with vLLM is through a specific Docker setup pro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

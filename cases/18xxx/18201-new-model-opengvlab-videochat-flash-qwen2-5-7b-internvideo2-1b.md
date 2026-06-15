# vllm-project/vllm#18201: [New Model]: OpenGVLab/VideoChat-Flash-Qwen2_5-7B_InternVideo2-1B

| 字段 | 值 |
| --- | --- |
| Issue | [#18201](https://github.com/vllm-project/vllm/issues/18201) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: OpenGVLab/VideoChat-Flash-Qwen2_5-7B_InternVideo2-1B

### Issue 正文摘录

### The model to consider. Hey, I want to make a request for adding a new model [OpenGVLab/VideoChat-Flash-Qwen2_5-7B_InternVideo2-1B](https://huggingface.co/OpenGVLab/VideoChat-Flash-Qwen2_5-7B_InternVideo2-1B). Thank you! ### The closest model vllm already supports. The closest model vllm already supports would be https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/llava_onevision.py. ### What's your difficulty of supporting the model you want? New processor. 1B InternVL vision processor. Also 16 tokens for a frame that's something I really want to test using vllm. from official Huggingface model card: "_VideoChat-Flash-Qwen2_5-7B_InternVideo2-1B is constructed upon InternVideo2-1B and Qwen2.5-7B, employing only **16 tokens per frame**. By leveraging Yarn to extend the context window to 128k (Qwen2's native context window is 32k), our model supports input sequences of up to approximately **10,000 frames.**_" Thank you! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of freq...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: OpenGVLab/VideoChat-Flash-Qwen2_5-7B_InternVideo2-1B stale ### The model to consider. Hey, I want to make a request for adding a new model [OpenGVLab/VideoChat-Flash-Qwen2_5-7B_InternVideo2-1B](https://hugg...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [New Model]: OpenGVLab/VideoChat-Flash-Qwen2_5-7B_InternVideo2-1B stale ### The model to consider. Hey, I want to make a request for adding a new model [OpenGVLab/VideoChat-Flash-Qwen2_5-7B_InternVideo2-1B](https://hugg...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: or a frame that's something I really want to test using vllm. from official Huggingface model card: "_VideoChat-Flash-Qwen2_5-7B_InternVideo2-1B is constructed upon InternVideo2-1B and Qwen2.5-7B, employing only **16 to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ou! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: processor. Also 16 tokens for a frame that's something I really want to test using vllm. from official Huggingface model card: "_VideoChat-Flash-Qwen2_5-7B_InternVideo2-1B is constructed upon InternVideo2-1B and Qwen2.5...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

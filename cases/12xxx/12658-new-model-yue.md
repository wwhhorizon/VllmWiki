# vllm-project/vllm#12658: [New Model]: YuE

| 字段 | 值 |
| --- | --- |
| Issue | [#12658](https://github.com/vllm-project/vllm/issues/12658) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: YuE

### Issue 正文摘录

### The model to consider. https://huggingface.co/collections/m-a-p/yue-6797d55e22990ae89b90a3d6 Repo and paper: https://github.com/multimodal-art-projection/YuE ### The closest model vllm already supports. Qwen2AudioForConditionalGeneration ### What's your difficulty of supporting the model you want? The difference between the input and output of text generation and audio models ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: YuE new-model;stale ### The model to consider. https://huggingface.co/collections/m-a-p/yue-6797d55e22990ae89b90a3d6 Repo and paper: https://github.com/multimodal-art-projection/YuE ### The closest model vl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: els ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: YuE new-model;stale ### The model to consider. https://huggingface.co/collections/m-a-p/yue-6797d55e22990ae89b90a3d6 Repo and paper: https://github.com/multimodal-art-projection/YuE ### The closest model vl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

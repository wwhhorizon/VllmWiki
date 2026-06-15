# vllm-project/vllm#13190: [New Model]:  Request for LLaVA-Video-7B-Qwen2 Model Implementation

| 字段 | 值 |
| --- | --- |
| Issue | [#13190](https://github.com/vllm-project/vllm/issues/13190) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]:  Request for LLaVA-Video-7B-Qwen2 Model Implementation

### Issue 正文摘录

### The model to consider. Hello, I would like to ask for this model ([LLaVA-Video-7B-Qwen2](https://huggingface.co/lmms-lab/LLaVA-Video-7B-Qwen2)) conversion to hf-weights. I’ve been testing llava-hf/LLaVA-NeXT-Video-7B-32K-hf (vicuna base) and LLaVA-Video-7B-Qwen2 (qwen2 base), and I’ve noticed that LLaVA-Video-7B-Qwen2 LLM outperforms LLaVA-NeXT-Video-7B-32K-hf in terms of video understanding (video description). Given the performance difference, I would like to request an implementation of a new model LLaVA-Video-7B-Qwen2. Thanks! ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: Request for LLaVA-Video-7B-Qwen2 Model Implementation new-model ### The model to consider. Hello, I would like to ask for this model ([LLaVA-Video-7B-Qwen2](https://huggingface.co/lmms-lab/LLaVA-Video-7B-Qw...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ideo-7B-Qwen2](https://huggingface.co/lmms-lab/LLaVA-Video-7B-Qwen2)) conversion to hf-weights. I’ve been testing llava-hf/LLaVA-NeXT-Video-7B-32K-hf (vicuna base) and LLaVA-Video-7B-Qwen2 (qwen2 base), and I’ve noticed...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Request for LLaVA-Video-7B-Qwen2 Model Implementation new-model ### The model to consider. Hello, I would like to ask for this model ([LLaVA-Video-7B-Qwen2](https://huggingface.co/lmms-lab/LLaVA-Video-7B-Qw...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: .co/lmms-lab/LLaVA-Video-7B-Qwen2)) conversion to hf-weights. I’ve been testing llava-hf/LLaVA-NeXT-Video-7B-32K-hf (vicuna base) and LLaVA-Video-7B-Qwen2 (qwen2 base), and I’ve noticed that LLaVA-Video-7B-Qwen2 LLM out...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#31975: [New Model]: Qwen3Guard Stream

| 字段 | 值 |
| --- | --- |
| Issue | [#31975](https://github.com/vllm-project/vllm/issues/31975) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Qwen3Guard Stream

### Issue 正文摘录

### The model to consider. Hello I was wondering if the Qwen3Guard stream family is going to be supported by vLLM. Closest issue / PR related to this topic I found in the repo is this PR #25463 HF models: - [0.6B](https://huggingface.co/Qwen/Qwen3Guard-Stream-0.6B) - [4B](https://huggingface.co/Qwen/Qwen3Guard-Stream-4B) - [8B](https://huggingface.co/Qwen/Qwen3Guard-Stream-8B) Best ### The closest model vllm already supports. The closest models that vLLM supports are the non-stream versions of the Qwen3Guard family HF models: - [0.6B](https://huggingface.co/Qwen/Qwen3Guard-Gen-0.6B) - [4B](https://huggingface.co/Qwen/Qwen3Guard-Gen-4B) - [8B](https://huggingface.co/Qwen/Qwen3Guard-Gen-8B) ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: Qwen3Guard Stream stale ### The model to consider. Hello I was wondering if the Qwen3Guard stream family is going to be supported by vLLM. Closest issue / PR related to this topic I found in the repo is thi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: eady supports. The closest models that vLLM supports are the non-stream versions of the Qwen3Guard family HF models: - [0.6B](https://huggingface.co/Qwen/Qwen3Guard-Gen-0.6B) - [4B](https://huggingface.co/Qwen/Qwen3Guar...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Qwen3Guard Stream stale ### The model to consider. Hello I was wondering if the Qwen3Guard stream family is going to be supported by vLLM. Closest issue / PR related to this topic I found in the repo is thi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

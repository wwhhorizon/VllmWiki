# vllm-project/vllm#27011: [Usage]: Runnig GLM4.5-Air with Speculative Decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#27011](https://github.com/vllm-project/vllm/issues/27011) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Runnig GLM4.5-Air with Speculative Decoding

### Issue 正文摘录

### Your current environment ``` The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [GLM-4.5-Air](https://huggingface.co/zai-org/GLM-4.5-Air-FP8) with speculative decoding. From [GLM 4.5](https://huggingface.co/zai-org/GLM-4.5) page, it mentioned `All models use MTP layers and specify --speculative-num-steps 3 --speculative-eagle-topk 1 --speculative-num-draft-tokens 4 to ensure competitive inference speed.` They gave examples of how to use speculative decoding in sglang, but not in vLLM. I was wondering if it is being supported in vLLM ### Before submitting a new issue... - [x]Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: Runnig GLM4.5-Air with Speculative Decoding usage;stale ### Your current environment ``` The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [GLM-4.5-Air](h...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: you like to use vllm I want to run inference of a [GLM-4.5-Air](https://huggingface.co/zai-org/GLM-4.5-Air-FP8) with speculative decoding. From [GLM 4.5](https://huggingface.co/zai-org/GLM-4.5) page, it mentioned `All m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: co/zai-org/GLM-4.5) page, it mentioned `All models use MTP layers and specify --speculative-num-steps 3 --speculative-eagle-topk 1 --speculative-num-draft-tokens 4 to ensure competitive inference speed.` They gave examp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: inference of a [GLM-4.5-Air](https://huggingface.co/zai-org/GLM-4.5-Air-FP8) with speculative decoding. From [GLM 4.5](https://huggingface.co/zai-org/GLM-4.5) page, it mentioned `All models use MTP layers and specify --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n vLLM ### Before submitting a new issue... - [x]Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/),...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

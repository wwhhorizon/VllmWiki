# vllm-project/vllm#21800: [Usage]: How to implement the inference test of LLM model PD (Prefill-Decode) disaggregation using the vllm framework ?

| 字段 | 值 |
| --- | --- |
| Issue | [#21800](https://github.com/vllm-project/vllm/issues/21800) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to implement the inference test of LLM model PD (Prefill-Decode) disaggregation using the vllm framework ?

### Issue 正文摘录

### Your current environment Dear vllm developers, First of all, on behalf of our university laboratory, I would like to express our highest gratitude and respect for the work you have done. However, for students like us, it is quite challenging to implement the inference test of LLM model PD (Prefill-Decode) disaggregation using the vllm framework. Is there a manual or tutorial available to help beginners carry out the inference test of LLM model PD disaggregation? We offer our sincere thanks and admiration once again. New we have installed vllm 0.9.2 in our servers. ``` root@5468a704:/workspace/vllm-0.9.2# pip show vllm Name: vllm Version: 0.9.2 Summary: A high-throughput and memory-efficient inference and serving engine for LLMs Home-page: https://github.com/vllm-project/vllm Author: vLLM Team Author-email: License-Expression: Apache-2.0 Location: /usr/local/lib/python3.12/dist-packages Requires: aiohttp, blake3, cachetools, cloudpickle, compressed-tensors, depyf, einops, fastapi, filelock, gguf, huggingface-hub, lark, llguidance, lm-format-enforcer, mistral_common, msgspec, ninja, numba, numpy, openai, opencv-python-headless, outlines, partial-json-parser, pillow, prometheus-f...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ion? We offer our sincere thanks and admiration once again. New we have installed vllm 0.9.2 in our servers. ``` root@5468a704:/workspace/vllm-0.9.2# pip show vllm Name: vllm Version: 0.9.2 Summary: A high-throughput an...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: How to implement the inference test of LLM model PD (Prefill-Decode) disaggregation using the vllm framework ? usage;stale ### Your current environment Dear vllm developers, First of all, on behalf of our unive...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Usage]: How to implement the inference test of LLM model PD (Prefill-Decode) disaggregation using the vllm framework ? usage;stale ### Your current environment Dear vllm developers, First of all, on behalf of our unive...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Usage]: How to implement the inference test of LLM model PD (Prefill-Decode) disaggregation using the vllm framework ? usage;stale ### Your current environment Dear vllm developers, First of all, on behalf of our unive...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

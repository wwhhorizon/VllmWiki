# vllm-project/vllm#12108: [New Model]: Сenturio

| 字段 | 值 |
| --- | --- |
| Issue | [#12108](https://github.com/vllm-project/vllm/issues/12108) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Сenturio

### Issue 正文摘录

### The model to consider. https://huggingface.co/WueNLP/centurio_qwen https://huggingface.co/WueNLP/centurio_aya ### The closest model vllm already supports. qwen/Qwen2.5 CohereForAI/aya-expanse-8b InternVL2_5 ### What's your difficulty of supporting the model you want? Dear developers and vLLM community, The **Centurio** model, introduced in the paper *["On Drivers of Multilingual Ability of Large Vision-Language Model"](https://arxiv.org/abs/2501.05122)* , offers a breakthrough in multilingual Large Vision-Language Models (LVLMs). Its integration into vLLM could significantly enhance the framework's capabilities for multilingual tasks. **Key advantages of Centurio:** 1. **Multilingualism:** Centurio supports **100 languages**, making it one of the most versatile models for text and image processing. 2. **Improved text-in-image understanding:** Centurio is optimized for multilingual text-in-image (OCR) tasks, which is critical for visual content analysis. 3. **Ready-to-use solutions:** The model demonstrates state-of-the-art results on **14 tasks and 56 languages**, making it a ready-to-use solution for integration. **Why this matters for vLLM:** - **Versatility:** Centurio expa...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [New Model]: Сenturio new-model;stale ### The model to consider. https://huggingface.co/WueNLP/centurio_qwen https://huggingface.co/WueNLP/centurio_aya ### The closest model vllm already supports. qwen/Qwen2.5 CohereFor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ltilingual tasks. **Key advantages of Centurio:** 1. **Multilingualism:** Centurio supports **100 languages**, making it one of the most versatile models for text and image processing. 2. **Improved text-in-image unders...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Сenturio new-model;stale ### The model to consider. https://huggingface.co/WueNLP/centurio_qwen https://huggingface.co/WueNLP/centurio_aya ### The closest model vllm already supports. qwen/Qwen2.5 CohereFor...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

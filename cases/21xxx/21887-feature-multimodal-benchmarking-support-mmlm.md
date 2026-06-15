# vllm-project/vllm#21887: [Feature]:  Multimodal Benchmarking Support (MMLM)

| 字段 | 值 |
| --- | --- |
| Issue | [#21887](https://github.com/vllm-project/vllm/issues/21887) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]:  Multimodal Benchmarking Support (MMLM)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch #### 1. Motivation vLLM’s built-in benchmark currently reports * **TTFT** – *Time-to-First-Token* * **TPT** – *Tokens-Per-Second* * **ITL** – *Inter-Token-Latency* Those latency-centric numbers are perfect for pure-text LLMs, but they do **not** capture the quality or unique execution characteristics of **multimodal large models (MMLMs)** that take both text *and* images. Adding a fit-for-purpose multimodal benchmark would make vLLM even more valuable for researchers and practitioners. --- #### 2. What is missing right now? 1. **Dataset** – No out-of-the-box multimodal test set that exercises image → text or text → image abilities. 2. **Metrics** – Current numbers show speed only; they don’t answer *“How well is the model performing on the task?”* 3. **Evaluation harness** – vLLM lacks a driver that loads multimodal samples, feeds them, and aggregates both **quality** *and* **latency** into one report. --- #### 3. Proposed Solution ##### 3.1 Candidate Benchmark Datasets | Category | Suggested dataset | License | Rationale | |----------|------------------|---------|-----------| | VQA | `VQAv2`, `OK-VQA` | CC-BY-4.0 | Classic image-to-text Q&A...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Feature]: Multimodal Benchmarking Support (MMLM) feature request;stale ### 🚀 The feature, motivation and pitch #### 1. Motivation vLLM’s built-in benchmark currently reports * **TTFT** – *Time-to-First-Token* * **TPT**...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Multimodal Benchmarking Support (MMLM) feature request;stale ### 🚀 The feature, motivation and pitch #### 1. Motivation vLLM’s built-in benchmark currently reports * **TTFT** – *Time-to-First-Token* * **TPT**...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -purpose multimodal benchmark would make vLLM even more valuable for researchers and practitioners. --- #### 2. What is missing right now? 1. **Dataset** – No out-of-the-box multimodal test set that exercises image → te...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Multimodal Benchmarking Support (MMLM) feature request;stale ### 🚀 The feature, motivation and pitch #### 1. Motivation vLLM’s built-in benchmark currently reports * **TTFT** – *Time-to-First-Token* * **TPT**...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ght now? 1. **Dataset** – No out-of-the-box multimodal test set that exercises image → text or text → image abilities. 2. **Metrics** – Current numbers show speed only; they don’t answer *“How well is the model performi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

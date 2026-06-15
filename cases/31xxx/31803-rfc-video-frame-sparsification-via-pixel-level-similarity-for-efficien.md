# vllm-project/vllm#31803: [RFC]: Video Frame Sparsification via Pixel-Level Similarity for Efficient Multimodal Long-Video Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#31803](https://github.com/vllm-project/vllm/issues/31803) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Video Frame Sparsification via Pixel-Level Similarity for Efficient Multimodal Long-Video Inference

### Issue 正文摘录

### Motivation. The exponential growth of video content and rising demand for "long-video intelligence" (e.g., video summarization, multimodal QA, video generation) have made long-video inference a standard requirement for multimodal large models. However, current models suffer from critical efficiency bottlenecks, necessitating a lightweight, adaptive, and scalable sparsification solution. Key challenges include: 1.1 High Redundancy Videos exhibit inherent temporal redundancy (e.g., near-identical consecutive frames in static scenes) and spatial redundancy (e.g., repeated encoding of similar content across frames), causing models to waste computation on duplicated information. 1.2 Input Sequence Overflow Video encoding generates excessive visual tokens that frequently exceed the context window limits of language models. ### Proposed Change. This solution implements adaptive sparsification through three stages: 1. Downsampling Preprocessing: Apply spatial downsampling (e.g., 4× reduction) to raw frames to lower computational load. 2. Similarity Assessment: Compute SSIM + L1 loss between adjacent frames to generate inter-frame similarity sequences. 3. Adaptive Keyframe Extraction:...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: FC]: Video Frame Sparsification via Pixel-Level Similarity for Efficient Multimodal Long-Video Inference RFC;stale ### Motivation. The exponential growth of video content and rising demand for "long-video intelligence"...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: reduction) to raw frames to lower computational load. 2. Similarity Assessment: Compute SSIM + L1 loss between adjacent frames to generate inter-frame similarity sequences. 3. Adaptive Keyframe Extraction: - Calculate r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [RFC]: Video Frame Sparsification via Pixel-Level Similarity for Efficient Multimodal Long-Video Inference RFC;stale ### Motivation. The exponential growth of video content and rising demand for "long-video intelligence...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Pixel-Level Similarity for Efficient Multimodal Long-Video Inference RFC;stale ### Motivation. The exponential growth of video content and rising demand for "long-video intelligence" (e.g., video summarization, multimod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

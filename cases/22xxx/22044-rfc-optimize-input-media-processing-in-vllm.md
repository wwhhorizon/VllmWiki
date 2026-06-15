# vllm-project/vllm#22044: [RFC]: Optimize Input Media Processing in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#22044](https://github.com/vllm-project/vllm/issues/22044) |
| 状态 | closed |
| 标签 | RFC;stale;multi-modality |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Optimize Input Media Processing in vLLM

### Issue 正文摘录

### Motivation. The current processing flow of media inputs (image/video/audio/embeddings) has several inefficiencies when media is used repeatedly (e.g. multi-turn or when the same media is used in different requests). The current processing flow looks like this when a media is provided in the input: 1. MediaConnector runs to download the input (if a remote URL is provided), incurring network delays 2. MediaConnector loads the downloaded bytes into python objects (e.g. PIL.Image, audio/video decoding), incurring CPU delays 3. BaseMultiModalProcessor then hashes the entire media using its full bytes to do cache lookup from ProcessingCache, incurring CPU delays All three are run before any cache is checked, therefore repeated media still incur these costs even if there’s a cache hit later on. Additionally, decoding long video & hashing based on all bytes can be slow (millisecs to tens of millisecs) and inefficient. For media that are sent repeatedly, we want to bypass all three steps. ### Proposed Change. ### Proposal 1. Add a user provided “uuid” field in media inputs as the media’s identifier & hash key Example: `{"type": "image_url", "image_url": {"url": image_url}, "uuid": “abc...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: cked, therefore repeated media still incur these costs even if there’s a cache hit later on. Additionally, decoding long video & hashing based on all bytes can be slow (millisecs to tens of millisecs) and inefficient. F...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Optimize Input Media Processing in vLLM RFC;stale;multi-modality ### Motivation. The current processing flow of media inputs (image/video/audio/embeddings) has several inefficiencies when media is used repeatedly...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ng flow of media inputs (image/video/audio/embeddings) has several inefficiencies when media is used repeatedly (e.g. multi-turn or when the same media is used in different requests). The current processing flow looks l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: l. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ects (e.g. PIL.Image, audio/video decoding), incurring CPU delays 3. BaseMultiModalProcessor then hashes the entire media using its full bytes to do cache lookup from ProcessingCache, incurring CPU delays All three are...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

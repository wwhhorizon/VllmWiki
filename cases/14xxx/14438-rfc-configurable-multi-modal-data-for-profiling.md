# vllm-project/vllm#14438: [RFC]: Configurable multi-modal data for profiling

| 字段 | 值 |
| --- | --- |
| Issue | [#14438](https://github.com/vllm-project/vllm/issues/14438) |
| 状态 | closed |
| 标签 | RFC;keep-open;multi-modality |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Configurable multi-modal data for profiling

### Issue 正文摘录

### Motivation. We can control the data used in profiling multi-modal models using `limit_mm_per_prompt`. However, this is insufficient for the following use-cases: - ~~Restrict models that accept multiple modalities to only accept single modality inputs to avoid unnecessary memory allocation, e.g.:~~ This is not needed for V1 anymore because we only encode one modality at a time - ~~Make Qwen2-VL only accept 10 images *or* 1 video, but not 10 images *and* 1 video per prompt~~ - Limit the duration of multi-modal data items with temporal components to save memory, e.g.: - Make Whisper accept only 20s of audio instead of 30s - Make Qwen2-VL accept only 10 frames of video instead of 16 - Increase the maximum duration of multi-modal data items, e.g.: - https://github.com/vllm-project/vllm/issues/18329#issuecomment-3264433726 - Alternative: https://github.com/vllm-project/vllm/issues/22695 ### Proposed Change. This RFC proposes to expand the current `limit_mm_per_prompt` to support additional information for dummy data generation and thus profiling. This results in the following schema change: ```py class DummyDataOptions(TypedDict): count: int # Allow additional keys # Previously, thi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [RFC]: Configurable multi-modal data for profiling RFC;keep-open;multi-modality ### Motivation. We can control the data used in profiling multi-modal models using `limit_mm_per_prompt`. However, this is insufficient for...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [RFC]: Configurable multi-modal data for profiling RFC;keep-open;multi-modality ### Motivation. We can control the data used in profiling multi-modal models using `limit_mm_per_prompt`. However, this is insufficient for...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: multi-modal models using `limit_mm_per_prompt`. However, this is insufficient for the following use-cases: - ~~Restrict models that accept multiple modalities to only accept single modality inputs to avoid unnecessary m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: re. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: : # def get_dummy_mm_data( # self, # seq_len: int, # mm_counts: Mapping[str, int], # ) -> MultiModalDataDict: ... def get_dummy_mm_data( self, seq_len: int, mm_options: Mapping[str, DummyDataOptions], ) -> MultiModalDat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

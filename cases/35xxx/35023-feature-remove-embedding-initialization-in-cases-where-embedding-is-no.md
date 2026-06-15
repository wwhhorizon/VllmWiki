# vllm-project/vllm#35023: [Feature]: Remove embedding initialization in cases where embedding is not needed in gpu_model_runner init

| 字段 | 值 |
| --- | --- |
| Issue | [#35023](https://github.com/vllm-project/vllm/issues/35023) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Remove embedding initialization in cases where embedding is not needed in gpu_model_runner init

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Title: [Feature] Lazily allocate inputs_embeds buffer to save GPU memory ### Problem Currently, `inputs_embeds` buffer is always pre-allocated in `vllm/worker/model_runner.py` (or similar location) using `_make_buffer` with size `(max_num_tokens, inputs_embeds_size)`. This allocation occurs regardless of whether the inputs are token IDs or embeddings. For example: https://github.com/vllm-project/vllm/blob/main/vllm/v1/worker/gpu_model_runner.py#L583-L585 ```python self.inputs_embeds = self._make_buffer( self.max_num_tokens, self.inputs_embeds_size, dtype=self.dtype, numpy=False ) ``` Is it possible to remove embedding initialization in cases where embedding is not needed by adding conditional checks, in order to reduce memory usage? For example, pure text generation with token IDs and non-pp. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: in cases where embedding is not needed in gpu_model_runner init feature request;stale ### 🚀 The feature, motivation and pitch ## Title: [Feature] Lazily allocate inputs_embeds buffer to save GPU memory ### Problem Curre...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: s = self._make_buffer( self.max_num_tokens, self.inputs_embeds_size, dtype=self.dtype, numpy=False ) ``` Is it possible to remove embedding initialization in cases where embedding is not needed by adding conditional che...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: pitch ## Title: [Feature] Lazily allocate inputs_embeds buffer to save GPU memory ### Problem Currently, `inputs_embeds` buffer is always pre-allocated in `vllm/worker/model_runner.py` (or similar location) using `_make...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: self.max_num_tokens, self.inputs_embeds_size, dtype=self.dtype, numpy=False ) ``` Is it possible to remove embedding initialization in cases where embedding is not needed by adding conditional checks, in order to reduce...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

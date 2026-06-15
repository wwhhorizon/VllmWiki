# vllm-project/vllm#38297: [Bug]: Gemma3n concurrent audio requests crash EngineCore — missing dynamic_dims on audio sequence dimension

| 字段 | 值 |
| --- | --- |
| Issue | [#38297](https://github.com/vllm-project/vllm/issues/38297) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gemma3n concurrent audio requests crash EngineCore — missing dynamic_dims on audio sequence dimension

### Issue 正文摘录

### Your current environment - vLLM 0.17.1 (also checked current main @ `ba2f0acc`, same code) - transformers 4.57.6 - model: `google/gemma-3n-E4B-it` - GPU: NVIDIA A10G (24GB) - API: `/v1/chat/completions` with `input_audio` items ### Describe the bug When two concurrent `/v1/chat/completions` requests with audio of different durations get batched together, EngineCore crashes: ``` ValueError: input_features_padded contains inconsistent shapes: torch.Size([496, 128]) (index 0) vs torch.Size([449, 128]) (index 1) ``` The first dimension (496 vs 449) is the audio sequence length, which naturally varies with duration. Each request has a single `input_audio` item — these are separate concurrent requests, not one request with multiple audios. This kills EngineCore and every in-flight request gets a 500. ### Root cause This is the same bug that #31219 reported for Qwen2Audio/AudioFlamingo3/MiniCPM-V, fixed in #31223 — but Gemma3n wasn't included in that fix. `Gemma3nAudioInputs` in `gemma3n_mm.py` declares its shapes without `dynamic_dims`: ```python class Gemma3nAudioInputs(TensorSchema): input_features_padded: Annotated[torch.Tensor, TensorShape("bn", "s", "f")] input_features_mask: A...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma3n concurrent audio requests crash EngineCore — missing dynamic_dims on audio sequence dimension ### Your current environment - vLLM 0.17.1 (also checked current main @ `ba2f0acc`, same code) - transformers...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Gemma3n concurrent audio requests crash EngineCore — missing dynamic_dims on audio sequence dimension ### Your current environment - vLLM 0.17.1 (also checked current main @ `ba2f0acc`, same code) - transformers...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Gemma3n concurrent audio requests crash EngineCore — missing dynamic_dims on audio sequence dimension ### Your current environment - vLLM 0.17.1 (also checked current main @ `ba2f0acc`, same code) - transformers...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

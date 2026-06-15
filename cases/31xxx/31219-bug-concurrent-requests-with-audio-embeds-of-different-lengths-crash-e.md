# vllm-project/vllm#31219: [Bug]: Concurrent requests with audio_embeds of different lengths crash EngineCore: "audio_embeds contains inconsistent shapes"

| 字段 | 值 |
| --- | --- |
| Issue | [#31219](https://github.com/vllm-project/vllm/issues/31219) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | shape_align |
| Operator 关键词 | cuda;gemm;operator;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Concurrent requests with audio_embeds of different lengths crash EngineCore: "audio_embeds contains inconsistent shapes"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Describe the bug When sending concurrent OpenAI-compatible `/v1/chat/completions` requests that include `content: [{type:"audio_embeds", audio_embeds:" "}]`, vLLM (v0.12.0) sometimes batches multiple requests together for multimodal embedding processing, and then crashes with: `ValueError: audio_embeds contains inconsistent shapes: torch.Size([19, 3584]) (index 0) vs torch.Size([31, 3584]) (index 1)` This kills EngineCore and all in-flight requests return 500. ### Expected behavior vLLM should support batching multimodal `audio_embeds` with different time lengths (T) by padding/packing, or bucket by shape and run the MM encoder separately. At minimum, it should not kill EngineCore for a recoverable input-shape mismatch. ### Actual behavior EngineCore crashes with `audio_embeds contains inconsistent shapes` once concurrency is high enough. ### Reproduction (minimal) - Start vLLM server with Qwen2Audio model and `--enable-mm-embeds`. - Send 2+ concurrent requests with `audio_embeds` tensors whose shapes are `[1, T, 3584]` and different `T` (e.g. 19 and 31). - With concurrency >= 8 in our workload, the crash becomes frequent. ##...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: :" "}]`, vLLM (v0.12.0) sometimes batches multiple requests together for multimodal embedding processing, and then crashes with: `ValueError: audio_embeds contains inconsistent shapes: torch.Size([19, 3584]) (index 0) v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;gem...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t minimum, it should not kill EngineCore for a recoverable input-shape mismatch. ### Actual behavior EngineCore crashes with `audio_embeds contains inconsistent shapes` once concurrency is high enough. ### Reproduction...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Concurrent requests with audio_embeds of different lengths crash EngineCore: "audio_embeds contains inconsistent shapes" bug ### Your current environment ### 🐛 Describe the bug ### Describe the bug When sending c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: t;multimodal_vlm;sampling_logits;speculative_decoding cuda;gemm;operator;triton build_error;crash;mismatch env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#22109: [Bug]: Audio file cap in vLLM 0.10.0 (Docker): unable to use more than 5 audio files per conversation with Voxtral-Mini-3B-2507 regardless of --limit-mm-per-prompt flag

| 字段 | 值 |
| --- | --- |
| Issue | [#22109](https://github.com/vllm-project/vllm/issues/22109) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Audio file cap in vLLM 0.10.0 (Docker): unable to use more than 5 audio files per conversation with Voxtral-Mini-3B-2507 regardless of --limit-mm-per-prompt flag

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi vLLM developers, I'm hitting a persistent “5 audio files per request” limit when using the latest **vLLM 0.10.0** (Docker) with **Voxtral-Mini-3B-2507**, even though docs state the limit should be much higher (or unlimited, only context/token-limited) and the `--limit-mm-per-prompt` flag should not be needed anymore. ### What I'm Doing - **Setup:** Docker, latest `vllm/vllm-openai:latest` (which points to v0.10.0 as of August 2, 2025). - **Model:** Voxtral-Mini-3B-2507 - (Hugging Face model, July 2025). - **Usage:** Multi-turn audio conversation, each user message as an audio file (multi-audio, accumulating conversation history). - **Hardware:** RTX 4090, lots of VRAM, not running near limits (32K token context). ### The Problem No matter what I try, **any conversation stops working at the 6th audio message** (first five audio turns work; from turn 6 I always get): ``` ❌ Audio processing failed: Error code: 400 - {'object': 'error', 'message': 'At most 5 audio(s) may be provided in one request. You can set --limit-mm-per-prompt to increase this limit if the model supports it. None', 'type': 'BadRequestError', 'param': None, 'c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: /vllm-openai:latest` (which points to v0.10.0 as of August 2, 2025). - **Model:** Voxtral-Mini-3B-2507 - (Hugging Face model, July 2025). - **Usage:** Multi-turn audio conversation, each user message as an audio file (m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Audio file cap in vLLM 0.10.0 (Docker): unable to use more than 5 audio files per conversation with Voxtral-Mini-3B-2507 regardless of --limit-mm-per-prompt flag bug ### Your current environment ### 🐛 Describe th...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: istral --config-format mistral --load-format mistral --dtype bfloat16 --max-model-len ${MAX_MODEL_LEN} --gpu-memory-utilization ${GPU_MEMORY_UTILIZATION} --max-num-seqs 1 --max-num-batched-tokens ${MAX_MODEL_LEN} --enab...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: o file (multi-audio, accumulating conversation history). - **Hardware:** RTX 4090, lots of VRAM, not running near limits (32K token context). ### The Problem No matter what I try, **any conversation stops working at the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: he bug Hi vLLM developers, I'm hitting a persistent “5 audio files per request” limit when using the latest **vLLM 0.10.0** (Docker) with **Voxtral-Mini-3B-2507**, even though docs state the limit should be much higher...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

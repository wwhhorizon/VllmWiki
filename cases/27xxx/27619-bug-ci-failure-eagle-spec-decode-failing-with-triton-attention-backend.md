# vllm-project/vllm#27619: [Bug][CI Failure]: EAGLE Spec Decode failing with Triton Attention Backend

| 字段 | 值 |
| --- | --- |
| Issue | [#27619](https://github.com/vllm-project/vllm/issues/27619) |
| 状态 | closed |
| 标签 | bug;speculative-decoding;ci-failure |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;sampling;triton |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][CI Failure]: EAGLE Spec Decode failing with Triton Attention Backend

### Issue 正文摘录

### Name of failing test test_eagle_correctness[TRITON_ATTN-qwen3_eagle3] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ## Summary EAGLE speculative decoding is failing on AMD MI325X (gfx942) GPUs with a `HSA_STATUS_ERROR_MEMORY_APERTURE_VIOLATION` error. The error occurs immediately when processing prompts starts, after successful CUDA graph capturing. It can be reproduced with spec decode + EAGLE + Triton Attention Backend(default for AMD), example: ``` python3 offline_inference/spec_decode.py --test --method eagle --num_spec_tokens 3 --dataset-name hf --dataset-path philschmid/mt-bench --num-prompts 80 --temp 0 --top-p 1.0 --top-k -1 --tp 1 --enable-chunked-prefill --max-model-len 2048 ``` ## Error Details ``` :0:rocdevice.cpp:3675: Callback: Queue 0x7f4db0300000 aborting with error: HSA_STATUS_ERROR_MEMORY_APERTURE_VIOLATION: The agent attempted to access memory beyond the largest legal address. code: 0x29 ``` (using a different backend could work: eg. `ROCM_AITER_FA`, `ROCM_AITER_UNIFIED_ATTN`, but `TritonAttentionBackend` is the **default** attention backend f...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug][CI Failure]: EAGLE Spec Decode failing with Triton Attention Backend bug;speculative-decoding;ci-failure ### Name of failing test test_eagle_correctness[TRITON_ATTN-qwen3_eagle3] ### Basic information - [ ] Flaky...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ;ci-failure ### Name of failing test test_eagle_correctness[TRITON_ATTN-qwen3_eagle3] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ##...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug][CI Failure]: EAGLE Spec Decode failing with Triton Attention Backend bug;speculative-decoding;ci-failure ### Name of failing test test_eagle_correctness[TRITON_ATTN-qwen3_eagle3] ### Basic information - [ ] Flaky...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug][CI Failure]: EAGLE Spec Decode failing with Triton Attention Backend bug;speculative-decoding;ci-failure ### Name of failing test test_eagle_correctness[TRITON_ATTN-qwen3_eagle3] ### Basic information - [ ] Flaky...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rror occurs immediately when processing prompts starts, after successful CUDA graph capturing. It can be reproduced with spec decode + EAGLE + Triton Attention Backend(default for AMD), example: ``` python3 offline_infe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

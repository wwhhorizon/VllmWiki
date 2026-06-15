# vllm-project/vllm#33439: [Bug]: Race condition in V1 engine serial_utils.py - aux_buffers is None during concurrent llm.score()  calls with multimodal inputs

| 字段 | 值 |
| --- | --- |
| Issue | [#33439](https://github.com/vllm-project/vllm/issues/33439) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Race condition in V1 engine serial_utils.py - aux_buffers is None during concurrent llm.score()  calls with multimodal inputs

### Issue 正文摘录

### 🐛 Describe the bug --- ⚠️ I apologize that this issue was generated with help from Claude Code, but I've verified it accurately describes a real problem. I've been trying to get Qwen3-VL-Reranker running with optimal performance for several days, and this race condition blocks any concurrency improvements. --- Summary When using the offline `LLM.score()` API with concurrent requests containing multimodal (image) inputs, a race condition occurs in serial_utils.py. The aux_buffers field is None when it shouldn't be, causing crashes under concurrent load. This appears related to #31679 and PR #31841, but affects the offline LLM API rather than the async server, and the crash location is different (aux_buffers vs is_mm_embed). --- Environment - vLLM version: 0.15 - Python version: 3.13 - GPU: NVIDIA RTX (CUDA enabled) - OS: Linux (Arch) --- Model Qwen3-VL-Reranker-2B using configuration from the model card: ``` LLM( model="./models/model", runner="pooling", dtype="bfloat16", trust_remote_code=True, gpu_memory_utilization=0.35, max_model_len=4096, hf_overrides={ "architectures": ["Qwen3VLForSequenceClassification"], "classifier_from_token": ["no", "yes"], "is_original_qwen3_reranke...

## 现有链接修复摘要

#31841 [Bugfix] Fix race condition in async-scheduling for vlm model

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: s different (aux_buffers vs is_mm_embed). --- Environment - vLLM version: 0.15 - Python version: 3.13 - GPU: NVIDIA RTX (CUDA enabled) - OS: Linux (Arch) --- Model Qwen3-VL-Reranker-2B using configuration from the model...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: utils.py - aux_buffers is None during concurrent llm.score() calls with multimodal inputs bug ### 🐛 Describe the bug --- ⚠️ I apologize that this issue was generated with help from Claude Code, but I've verified it accu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ronment - vLLM version: 0.15 - Python version: 3.13 - GPU: NVIDIA RTX (CUDA enabled) - OS: Linux (Arch) --- Model Qwen3-VL-Reranker-2B using configuration from the model card: ``` LLM( model="./models/model", runner="po...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: : ``` LLM( model="./models/model", runner="pooling", dtype="bfloat16", trust_remote_code=True, gpu_memory_utilization=0.35, max_model_len=4096, hf_overrides={ "architectures": ["Qwen3VLForSequenceClassification"], "clas...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: -- Summary When using the offline `LLM.score()` API with concurrent requests containing multimodal (image) inputs, a race condition occurs in serial_utils.py. The aux_buffers field is None when it shouldn't be, causing...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31841](https://github.com/vllm-project/vllm/pull/31841) | mentioned | 0.45 | [Bugfix] Fix race condition in async-scheduling for vlm model | location)](https://github.com/vllm-project/vllm/issues/31679) - pr #31841 - [fix race condition in async-scheduling for vlm model](https://github.com/vllm-project/vllm/pull/31841)… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

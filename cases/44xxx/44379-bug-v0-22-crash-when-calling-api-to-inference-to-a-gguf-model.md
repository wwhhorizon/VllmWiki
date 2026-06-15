# vllm-project/vllm#44379: [Bug]: [v0.22] Crash when calling API to inference to a GGUF model

| 字段 | 值 |
| --- | --- |
| Issue | [#44379](https://github.com/vllm-project/vllm/issues/44379) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;operator;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [v0.22] Crash when calling API to inference to a GGUF model

### Issue 正文摘录

### Your current environment Docker image: vllm/vllm-openai:latest(v0.22) AKS + Helm, node: GPU VM with 1 T4 card ``` modelURL: "Qwen/Qwen3-8B-GGUF:Q8_0" requestCPU: 1 limitCPU: 3 requestMemory: "8Gi" limitMemory: "20Gi" requestGPU: 1 vllmConfig: extraArgs: - "--tokenizer" - "Qwen/Qwen3-8B" - "--hf-config-path" - "Qwen/Qwen3-8B" - "--max-model-len" - "16384" - "--max-num-seqs" - "4" - "--gpu-memory-utilization" - "0.85" ``` ### 🐛 Describe the bug Behavior: runing is OK, but after any API calling to models through vllm-router, model crash **If downgrade to v0.21.0 without changing configuration, working fine** > (EngineCore pid=101) ERROR 06-03 03:39:03 [dump_input.py:72] Dumping input data for V1 LLM engine (v0.22.0) with config: model='Qwen/Qwen3-8B-GGUF:Q8_0', speculative_config=None, tokenizer='Qwen/Qwen3-8B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_r evision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=16384, download_dir=None, load_format=gguf, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1, decode_context_parallel_size=1, dcp_comm_backend=ag_rs, disable_custom_all_reduce=False, qua ntization=gguf, qu...

## 现有链接修复摘要

#44403 Fix FlashInfer attention auto-selection on SM75 GPUs

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: PU VM with 1 T4 card ``` modelURL: "Qwen/Qwen3-8B-GGUF:Q8_0" requestCPU: 1 limitCPU: 3 requestMemory: "8Gi" limitMemory: "20Gi" requestGPU: 1 vllmConfig: extraArgs: - "--tokenizer" - "Qwen/Qwen3-8B" - "--hf-config
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: lling API to inference to a GGUF model bug ### Your current environment Docker image: vllm/vllm-openai:latest(v0.22) AKS + Helm, node: GPU VM with 1 T4 card ``` modelURL: "Qwen/Qwen3-8B-GGUF:Q8_0" requestCPU: 1 limitCPU...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: [v0.22] Crash when calling API to inference to a GGUF model bug ### Your current environment Docker image: vllm/vllm-openai:latest(v0.22) AKS + Helm, node: GPU VM with 1 T4 card ``` modelURL: "Qwen/Qwen3-8B-GGUF:...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: Behavior: runing is OK, but after any API calling to models through vllm-router, model crash **If downgrade to v0.21.0 without changing configuration, working fine** > (EngineCore pid=101) ERROR 06-03 03:39:03 [dump_inp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: =auto, revision=None, tokenizer_r evision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=16384, download_dir=None, load_format=gguf, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#44403](https://github.com/vllm-project/vllm/pull/44403) | closes_keyword | 0.95 | Fix FlashInfer attention auto-selection on SM75 GPUs | Fixes #44379. Avoid auto-selecting FlashInfer attention on SM75/Turing GPUs, where the native FlashInfer prefill path can crash at runtime with `BatchPrefillWithPagedKVCache faile |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

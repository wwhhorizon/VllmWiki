# vllm-project/vllm#34619: [Bug]: Qwen3.5. `illegal memory access`

| 字段 | 值 |
| --- | --- |
| Issue | [#34619](https://github.com/vllm-project/vllm/issues/34619) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5. `illegal memory access`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Got `illegal memory access` on Qwen3.5 with `vllm bench` client ``` VLLM_ENGINE_READY_TIMEOUT_S=3600 VLLM_USE_FLASHINFER_MOE_FP16=1 vllm serve Qwen/Qwen3.5-397B-A17B -dp 8 --enable-expert-parallel ``` ``` vllm bench serve --backend vllm --model Qwen/Qwen3.5-397B-A17B --endpoint /v1/completions --dataset-name random --random-input 1000 --random-output 1000 --max-concurrency 1 --num-prompt 4 --ignore-eos ``` ``` (EngineCore_DP0 pid=231878) ERROR 02-16 16:41:04 [dump_input.py:72] Dumping input data for V1 LLM engine (v0.16.0rc2.dev147+gf120bd42d) with config: model='Qwen/Qwen3.5-397B-A17B', speculative_config=None, tokenizer='Qwen/Qwen3.5-397B-A17B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=262144, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=8, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, enable_return_routed_experts=False, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fal...

## 现有链接修复摘要

#34685 [WIP][Bugfix] Fix type mismatch in causal_conv1d Triton kernels PAD_SLOT_ID checks

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: .16.0rc2.dev147+gf120bd42d) with config: model='Qwen/Qwen3.5-397B-A17B', speculative_config=None, tokenizer='Qwen/Qwen3.5-397B-A17B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=Non...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: with `vllm bench` client ``` VLLM_ENGINE_READY_TIMEOUT_S=3600 VLLM_USE_FLASHINFER_MOE_FP16=1 vllm serve Qwen/Qwen3.5-397B-A17B -dp 8 --enable-expert-parallel ``` ``` vllm bench serve --backend vllm --model Qwen/Qwen3.5-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, kv_cache_metrics=False, kv_cache_metrics_sample=0.01, cudagraph_metrics=Fal...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=262144, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_siz...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: , enable_return_routed_experts=False, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_p...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34685](https://github.com/vllm-project/vllm/pull/34685) | mentioned | 0.6 | [WIP][Bugfix] Fix type mismatch in causal_conv1d Triton kernels PAD_SLOT_ID checks | on with multi-GPU access would be needed to fully diagnose. Related: #34619 ## Test Plan 1. Run existing causal_conv1d kernel tests: ``` python -m pytest tests/kernels/mamba/tes |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

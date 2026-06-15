# vllm-project/vllm#27364: [Bug]: Qwen3-VL {4B,8B} FP8 on vLLM returns only exclamation marks ("!!!!!...") on Jetson Thor

| 字段 | 值 |
| --- | --- |
| Issue | [#27364](https://github.com/vllm-project/vllm/issues/27364) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL {4B,8B} FP8 on vLLM returns only exclamation marks ("!!!!!...") on Jetson Thor

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Summary** When serving FP8 variants of Qwen3-VL (4B/8B Instruct FP8) with vLLM 0.11 (V1 engine) on Jetson AGX Thor (JetPack 7 / CUDA 13), text responses degenerate into a long sequence of exclamation mark '!' characters. The same models without FP8 generate normal text. **Models** Qwen/Qwen3-VL-4B-Instruct-FP8 ← broken (!!!!!) Qwen/Qwen3-VL-8B-Instruct-FP8 ← broken (!!!!!) Qwen/Qwen3-VL-4B-Instruct ← OK (non-FP8 or with dynamic FP quantization via --quantize fp8) Qwen/Qwen3-VL-8B-Instruct ← OK (non-FP8 or with dynamic FP quantization via --quantize fp8) **Exact server command** vllm serve Qwen/Qwen3-VL-4B-Instruct-FP8 \ --async-scheduling \ --max-model-len 2000 \ --max-num-seqs 128 \ --gpu-memory-utilization 0.9 \ --skip-mm-profiling \ --trust_remote_code **Minimal client to reproduce** #!/usr/bin/env python3 from openai import OpenAI client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY") resp = client.chat.completions.create( model="Qwen/Qwen3-VL-4B-Instruct-FP8", messages=[{"role": "user", "content": [{"type":"text","text": "What's the capital of Japan?"}]}], temperature=0.0, top_p=1.0, extra_body={"top_k": 1},...

## 现有链接修复摘要

#39666 [Bugfix] Add bias to SKIP_TENSORS to fix online FP8 for models with biased linears

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: Qwen3-VL {4B,8B} FP8 on vLLM returns only exclamation marks ("!!!!!...") on Jetson Thor bug;unstale ### Your current environment ### 🐛 Describe the bug **Summary** When serving FP8 variants of Qwen3-VL (4B/8B Ins...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: on vLLM returns only exclamation marks ("!!!!!...") on Jetson Thor bug;unstale ### Your current environment ### 🐛 Describe the bug **Summary** When serving FP8 variants of Qwen3-VL (4B/8B Instruct FP8) with vLLM 0.11 (V...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: code **Minimal client to reproduce** #!/usr/bin/env python3 from openai import OpenAI client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY") resp = client.chat.completions.create( model="Qwen/Qwen3-VL-4B-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Qwen3-VL {4B,8B} FP8 on vLLM returns only exclamation marks ("!!!!!...") on Jetson Thor bug;unstale ### Your current environment ### 🐛 Describe the bug **Summary** When serving FP8 variants of Qwen3-VL (4B/8B Ins...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: he issue appears specific to the FP8 path. * Forcing different attention backends: -- VLLM_ATTENTION_BACKEND=FLASH_ATTN → same issue. -- VLLM_ATTENTION_BACKEND=TORCH_SDPA → same issue. * Changing KV cache dtype: `--kv-c...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39666](https://github.com/vllm-project/vllm/pull/39666) | closes_keyword | 0.95 | [Bugfix] Add bias to SKIP_TENSORS to fix online FP8 for models with biased linears | Fixes #39663. Likely related to #27364 and #24025. ## Test Plan ```bash python -m pytest tests/quantization/test_fp8.py::test_fp8_online_bias_model -xvs ``` New integrat |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

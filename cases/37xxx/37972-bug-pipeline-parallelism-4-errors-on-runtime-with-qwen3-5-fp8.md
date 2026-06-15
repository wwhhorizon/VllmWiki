# vllm-project/vllm#37972: [Bug]: Pipeline Parallelism >=4 errors on runtime with Qwen3.5-FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#37972](https://github.com/vllm-project/vllm/issues/37972) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Pipeline Parallelism >=4 errors on runtime with Qwen3.5-FP8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using pipeline parallelism for Qwen3.5 is required because the number of attention heads is only 2, meaning that KV cache will be duplicated for any tensor parallelism over 2 (DCP for Qwen3 does not work properly in vLLM yet). Command that works fine (8x A100): `python3 -m vllm.entrypoints.openai.api_server --port 5000 --host 0.0.0.0 --download-dir /workspace/.cache/huggingface/hub --model Qwen/Qwen3.5-397B-A17B-FP8 --api-server-count 8 --tensor-parallel-size 4 --pipeline-parallel-size 2 --trust-remote-code --enable-chunked-prefill --enable-prefix-caching --max-num-seqs 128 --gpu-memory-utilization 0.9 --max-model-len 1010000 --hf-overrides '{"text_config": {"max_position_embeddings": 1010000, "rope_parameters": {"mrope_interleaved": true, "mrope_section": [11, 11, 10], "rope_type": "yarn", "rope_theta": 10000000, "partial_rotary_factor": 0.25, "factor": 4.0, "original_max_position_embeddings": 262144}}}' --max-num-batched-tokens 16384 --enable-auto-tool-choice --tool-call-parser qwen3_coder --reasoning-parser qwen3 --mm-processor-cache-gb 8 --mm-processor-cache-type shm --mm-encoder-tp-mode data` Command that also works fine (4x...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Pipeline Parallelism >=4 errors on runtime with Qwen3.5-FP8 bug ### Your current environment ### 🐛 Describe the bug Using pipeline parallelism for Qwen3.5 is required because the number of attention heads is only...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Pipeline Parallelism >=4 errors on runtime with Qwen3.5-FP8 bug ### Your current environment ### 🐛 Describe the bug Using pipeline parallelism for Qwen3.5 is required because the number of attention heads is only...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding attention;...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Pipeline Parallelism >=4 errors on runtime with Qwen3.5-FP8 bug ### Your current environment ### 🐛 Describe the bug Using pipeline parallelism for Qwen3.5 is required because the number of attention heads is only...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: l-size 4 --pipeline-parallel-size 2 --trust-remote-code --enable-chunked-prefill --enable-prefix-caching --max-num-seqs 128 --gpu-memory-utilization 0.9 --max-model-len 1010000 --hf-overrides '{"text_config": {"max_posi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

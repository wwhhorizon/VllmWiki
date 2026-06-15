# vllm-project/vllm#33242: [Bug]: Qwen3-VL-30B (MoE): CUDA error 'illegal memory access' when max_model_len > 128k

| 字段 | 值 |
| --- | --- |
| Issue | [#33242](https://github.com/vllm-project/vllm/issues/33242) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Qwen3-VL-30B (MoE): CUDA error 'illegal memory access' when max_model_len > 128k

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After upgrading from v0.12.0 to v0.14.1, I encountered a 'torch.AcceleratorError: CUDA error: an illegal memory access was encountered' during startup when running the Qwen3-VL-30B (MoE) model with a high --max-model-len. The service starts up successfully when --max-model-len is set to 128k or lower. However, setting it to 160k or higher causes the crash. Testing results: 4096: OK 131072 (128k): OK 163840 (160k): Error 196608 (192k): Error (Note: The exact boundary value triggering the error has not been determined.) Regression: This issue was not present in v0.12.0. It started appearing in v0.13.0 and persists in v0.14.1. Startup script used in v0.12.0 : ```startup script ExecStart=/home/usr/vllm-env/bin/python -m vllm.entrypoints.openai.api_server \ --model /home/usr/models/qwen3_VL_30b_instruct \ --host 101.210.241.117 \ --port 8000 \ --gpu-memory-utilization 0.94 \ --trust-remote-code \ --dtype auto \ --max-model-len 200000 \ --max-num-seqs 1 \ --max-num-batched-tokens 200000 \ --enable-chunked-prefill \ --enable-prefix-caching \ --seed 0 ``` Full error message : ```error msg 2026-01-28 15:47:19 gx10-0ea2 systemd[1]: Started...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Qwen3-VL-30B (MoE): CUDA error 'illegal memory access' when max_model_len > 128k bug ### Your current environment ### 🐛 Describe the bug After upgrading from v0.12.0 to v0.14.1, I encountered a 'torch.Accelerator...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rver pid=11452) INFO 01-28 15:47:23 [api_server.py:1272] vLLM API server version 0.14.1 2026-01-28 15:47:23 gx10-0ea2 vllm-server[11452]: (APIServer pid=11452) INFO 01-28 15:47:23 [utils.py:263] non-default args: {'host...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: 128k or lower. However, setting it to 160k or higher causes the crash. Testing results: 4096: OK 131072 (128k): OK 163840 (160k): Error 196608 (192k): Error (Note: The exact boundary value triggering the error has not b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 00 \ --gpu-memory-utilization 0.94 \ --trust-remote-code \ --dtype auto \ --max-model-len 200000 \ --max-num-seqs 1 \ --max-num-batched-tokens 200000 \ --enable-chunked-prefill \ --enable-prefix-caching \ --seed 0 ``` F...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

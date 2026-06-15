# vllm-project/vllm#44022: [Bug]: Unable to start Nemotron NVFP4 on 5090 after upgrade to vLLM 0.22

| 字段 | 值 |
| --- | --- |
| Issue | [#44022](https://github.com/vllm-project/vllm/issues/44022) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to start Nemotron NVFP4 on 5090 after upgrade to vLLM 0.22

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I was running vLLM 0.18 successfully with Nemotron-3-Nano-30B-A3b-NVFP4. After updating to vLLM 0.22.0, and using the same serve command, this failed, generally with the "RuntimeError: CUDA driver error: device not ready" . Below is my serve command (a script I start with): #!/usr/bin/env bash source /home/vrosu/LLM/vllm312/bin/activate export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True #export VLLM_SLEEP_WHEN_IDLE=1 export CUDA_LAUNCH_BLOCKING=1 vllm serve nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 \ --served-model-name model \ --max-num-seqs 1 \ --tensor-parallel-size 1 \ --max-model-len 8192 \ --port 8000 \ --trust-remote-code \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --reasoning-parser-plugin nano_v3_reasoning_parser.py \ --reasoning-parser nano_v3 \ --kv-cache-dtype fp8 \ --gpu-memory-utilization 0.65 \ --moe-backend auto This is the output: WARNING 05-29 22:55:06 [interface.py:729] Using 'pin_memory=False' as WSL is detected. This may slow down the performance. (APIServer pid=402) INFO 05-29 22:55:06 [utils.py:344] (APIServer pid=402) INFO 05-29 22:55:06 [utils.py:344] █ █ █▄ ▄█ (APIServer pid=402...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: [Bug]: Unable to start Nemotron NVFP4 on 5090 after upgrade to vLLM 0.22 bug ### Your current environment ### 🐛 Describe the bug I was running vLLM 0.18 successfully with Nemotron-3-Nano-30B-A3b-NVFP4. After updating to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: _v3 \ --kv-cache-dtype fp8 \ --gpu-memory-utilization 0.65 \ --moe-backend auto This is the output: WARNING 05-29 22:55:06 [interface.py:729] Using 'pin_memory=False' as WSL is detected. This may slow down the performan...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: pid=402) INFO 05-29 22:55:06 [utils.py:344] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.22.0 (APIServer pid=402) INFO 05-29 22:55:06 [utils.py:344] █▄█▀ █ █ █ █ model nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 (APIServer pid=402) INFO...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: G=1 vllm serve nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 \ --served-model-name model \ --max-num-seqs 1 \ --tensor-parallel-size 1 \ --max-model-len 8192 \ --port 8000 \ --trust-remote-code \ --enable-auto-tool-choice...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: nano_v3 \ --kv-cache-dtype fp8 \ --gpu-memory-utilization 0.65 \ --moe-backend auto This is the output: WARNING 05-29 22:55:06 [interface.py:729] Using 'pin_memory=False' as WSL is detected. This may slow down the perfo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

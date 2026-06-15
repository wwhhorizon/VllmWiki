# vllm-project/vllm#32093: [Bug]: Nemotron Nano V3 FP16 on Jetson THOR

| 字段 | 值 |
| --- | --- |
| Issue | [#32093](https://github.com/vllm-project/vllm/issues/32093) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Nemotron Nano V3 FP16 on Jetson THOR

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Can't run Nemotron V3 BF16 or FP8 on Jetson Thor using the flashinfer 0.6.0 or 0.5.2/0.5.3. I've tried all recent flashinfer releases manually custom compiled on the Jetson thor. Using older than 0.5.3 will not have some essential functions implemented like `gen_fp8_blockscale_gemm_sm90_module`. Command-line: ``` export VLLM_USE_FLASHINFER_MOE_FP8=0 export VLLM_FLASHINFER_MOE_BACKEND=throughput vllm serve nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 \ --dtype auto \ --trust-remote-code \ --max-num-seqs 8 \ --tensor-parallel-size 1 \ --max-model-len 262144 \ --port 8001 \ --kv-cache-dtype auto \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --reasoning-parser-plugin nano_v3_reasoning_parser.py \ --reasoning-parser nano_v3 ``` Command-line for FP8: ``` export PYTHONWARNINGS="ignore" export VLLM_USE_V1=1 export VLLM_USE_FLASHINFER_MOE_FP8=1 export VLLM_FLASHINFER_MOE_BACKEND=throughput vllm serve nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 \ --dtype auto \ --trust-remote-code \ --max-num-seqs 8 \ --tensor-parallel-size 1 \ --max-model-len 262144 \ --port 8001 \ --kv-cache-dtype fp8 \ --enable-auto-tool-choice \ --tool-cal...

## 现有链接修复摘要

#32704 [Bugfix] Auto-configure TRITON_PTXAS_PATH for new GPU architectures

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: r 0.5.2/0.5.3. I've tried all recent flashinfer releases manually custom compiled on the Jetson thor. Using older than 0.5.3 will not have some essential functions implemented like `gen_fp8_blockscale_gemm_sm90_module`....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ur current environment ### 🐛 Describe the bug Can't run Nemotron V3 BF16 or FP8 on Jetson Thor using the flashinfer 0.6.0 or 0.5.2/0.5.3. I've tried all recent flashinfer releases manually custom compiled on the Jetson...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: -remote-code \ --max-num-seqs 8 \ --tensor-parallel-size 1 \ --max-model-len 262144 \ --port 8001 \ --kv-cache-dtype auto \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --reasoning-parser-plugin nano_v3_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: have some essential functions implemented like `gen_fp8_blockscale_gemm_sm90_module`. Command-line: ``` export VLLM_USE_FLASHINFER_MOE_FP8=0 export VLLM_FLASHINFER_MOE_BACKEND=throughput vllm serve nvidia/NVIDIA-Nemotro...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: l not have some essential functions implemented like `gen_fp8_blockscale_gemm_sm90_module`. Command-line: ``` export VLLM_USE_FLASHINFER_MOE_FP8=0 export VLLM_FLASHINFER_MOE_BACKEND=throughput vllm serve nvidia/NVIDIA-N...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32704](https://github.com/vllm-project/vllm/pull/32704) | closes_keyword | 0.95 | [Bugfix] Auto-configure TRITON_PTXAS_PATH for new GPU architectures | Fixes #32093 Related to #29469 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

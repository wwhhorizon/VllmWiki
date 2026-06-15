# vllm-project/vllm#35566: CUDA illegal memory access in MoE layer with MiniMax-M2.5 NVFP4 on Blackwell (SM120)

| 字段 | 值 |
| --- | --- |
| Issue | [#35566](https://github.com/vllm-project/vllm/issues/35566) |
| 状态 | open |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;gemm;kernel;moe;quantization |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> CUDA illegal memory access in MoE layer with MiniMax-M2.5 NVFP4 on Blackwell (SM120)

### Issue 正文摘录

## Description Running `lukealonso/MiniMax-M2.5-REAP-139B-A10B-NVFP4` with `--quantization modelopt_fp4` on a Blackwell GPU (SM 12.0) results in a `CUDA error: an illegal memory access was encountered` during inference in the MoE gate/routing layer. The model loads and the server starts successfully, but the first inference request causes the crash. ## Reproduction ### Hardware - GPU: NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition (96 GB) - Driver: 590.48.01 - Compute capability: 12.0 ### Docker images tested (all reproduce the issue) - `vllm/vllm-openai:v0.15.1-cu130` - `vllm/vllm-openai:v0.16.0-cu130` - `vllm/vllm-openai:cu130-nightly` (as of 2026-02-27) ### Launch command ```bash docker run --gpus all --shm-size 1g -p 8000:8000 \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -e CUDA_DEVICE_ORDER=PCI_BUS_ID \ -e CUDA_VISIBLE_DEVICES=0 \ -e SAFETENSORS_FAST_GPU=1 \ -e VLLM_NVFP4_GEMM_BACKEND=cutlass \ -e VLLM_USE_FLASHINFER_MOE_FP4=0 \ -e NCCL_IB_DISABLE=1 \ -e OMP_NUM_THREADS=8 \ -e LD_LIBRARY_PATH=/lib/x86_64-linux-gnu \ vllm/vllm-openai:v0.15.1-cu130 \ --model lukealonso/MiniMax-M2.5-REAP-139B-A10B-NVFP4 \ --host 0.0.0.0 --port 8000 \ --served-model-name minimax-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: tion Edition (96 GB) - Driver: 590.48.01 - Compute capability: 12.0 ### Docker images tested (all reproduce the issue) - `vllm/vllm-openai:v0.15.1-cu130` - `vllm/vllm-openai:v0.16.0-cu130` - `vllm/vllm-openai:cu130-nigh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: CUDA illegal memory access in MoE layer with MiniMax-M2.5 NVFP4 on Blackwell (SM120) ## Description Running `lukealonso/MiniMax-M2.5-REAP-139B-A10B-NVFP4` with `--quantization modelopt_fp4` on a Blackwell GPU (SM 12.0)
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: illegal memory access was encountered` during inference in the MoE gate/routing layer. The model loads and the server starts successfully, but the first inference request causes the crash. ## Reproduction ### Hardware -...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: CUDA illegal memory access in MoE layer with MiniMax-M2.5 NVFP4 on Blackwell (SM120) ## Description Running `lukealonso/MiniMax-M2.5-REAP-139B-A10B-NVFP4` with `--quantization modelopt_fp4` on a Blackwell GPU (SM 12.0)...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: CUDA illegal memory access in MoE layer with MiniMax-M2.5 NVFP4 on Blackwell (SM120) ## Description Running `lukealonso/MiniMax-M2.5-REAP-139B-A10B-NVFP4` with `--quantization modelopt_fp4` on a Blackwell GPU (SM 12.0)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

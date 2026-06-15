# vllm-project/vllm#30064: [Performance]: Degradation on rocm from v0.11.1 to v0.12.0

| 字段 | 值 |
| --- | --- |
| Issue | [#30064](https://github.com/vllm-project/vllm/issues/30064) |
| 状态 | closed |
| 标签 | performance;rocm |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Degradation on rocm from v0.11.1 to v0.12.0

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression TL;DR: on v0.11.1 I get much better performance (specifically TTFT) with deepseek on rocm than on v0.12.0. # What I did for v0.12.0 ## Built the image `git clone https://github.com/vllm-project/vllm.git` `git checkout v0.12.0` `DOCKER_BUILDKIT=1 docker build -f docker/Dockerfile.rocm -t vllm-rocm-v0.12.0 .` ## Benchmark Run vllm: ``` docker run -it --rm --ipc=host -p 8001:8001 --group-add render --privileged --security-opt seccomp=unconfined --cap-add=CAP_SYS_ADMIN --cap-add=SYS_PTRACE --device=/dev/kfd --device=/dev/dri --device=/dev/mem -v /mnt/nvme_models/deepseek-ai/DeepSeek-V3-0324:/app/model -e HIP_FORCE_DEV_KERNARG=1 -e TORCH_BLAS_PREFER_HIPBLASLT=1 -e NCCL_MIN_NCHANNELS=112 -e VLLM_USE_ROCM=1 -e VLLM_PLATFORM=rocm -e VLLM_MLA_DISABLE=0 -e VLLM_USE_AITER_MLA=1 -e VLLM_USE_TRITON_FLASH_ATTN=0 -e VLLM_ROCM_USE_AITER=1 -e VLLM_USE_AITER_MOE=1 -e VLLM_USE_AITER_BLOCK_GEMM=1 -e VLLM_ROCM_FP8_FLASH_ATTN=0 -e VLLM_ROCM_USE_AITER_MHA=0 -e VLLM_ROCM_USE_AITER_UNIFIED_ATTENTION=1 -e VLLM_FP8_PADDING=1 -e HF_HOME=/models/ -e HF_TOKEN=... vllm-rocm-v0.12.0 vllm serve /app/model --served-model-name de...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: formance regression TL;DR: on v0.11.1 I get much better performance (specifically TTFT) with deepseek on rocm than on v0.12.0. # What I did for v0.12.0 ## Built the image `git clone https://github.com/vllm-project/vllm....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Performance]: Degradation on rocm from v0.11.1 to v0.12.0 performance;rocm ### Proposal to improve performance _No response_ ### Report of performance regression TL;DR: on v0.11.1 I get much better performance (specifi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: roposal to improve performance _No response_ ### Report of performance regression TL;DR: on v0.11.1 I get much better performance (specifically TTFT) with deepseek on rocm than on v0.12.0. # What I did for v0.12.0 ## Bu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: tensor-parallel-size 8 --enable-expert-parallel --enable-chunked-prefill --gpu-memory-utilization 0.95 --max-log-len 4096 --dtype auto --max-num-seqs 1024 --max-num-batched-tokens 131072 --max-model-len 131072 --trust-r...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: -e VLLM_USE_AITER_MOE=1 -e VLLM_USE_AITER_BLOCK_GEMM=1 -e VLLM_ROCM_FP8_FLASH_ATTN=0 -e VLLM_ROCM_USE_AITER_MHA=0 -e VLLM_ROCM_USE_AITER_UNIFIED_ATTENTION=1 -e VLLM_FP8_PADDING=1 -e HF_HOME=/models/ -e HF_TOKEN=... vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#41190: [Bug]: TP=2 spec-decode (qwen3_next_mtp / DFlash) on Qwen3.6 hybrid GDN crashes at gpu_model_runner.py:1927 num_accepted_tokens_event.synchronize() (cudaErrorIllegalAddress)

| 字段 | 值 |
| --- | --- |
| Issue | [#41190](https://github.com/vllm-project/vllm/issues/41190) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;kernel;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: TP=2 spec-decode (qwen3_next_mtp / DFlash) on Qwen3.6 hybrid GDN crashes at gpu_model_runner.py:1927 num_accepted_tokens_event.synchronize() (cudaErrorIllegalAddress)

### Issue 正文摘录

### Your current environment - vLLM: `0.19.2rc1.dev226+g53b9640fb` (built off PR #40898 head — DFlash + SWA support) - GPU: 2× NVIDIA RTX 6000 Ada Generation (sm_89, 48 GB each, no NVLink, P2P over PCIe) - Driver: 580.126.09 / CUDA 13.0 - OS: Ubuntu, Linux 6.8.0-110-generic - Python 3.12 - NCCL env: `NCCL_P2P_DISABLE=1 NCCL_SHM_DISABLE=0 NCCL_IB_DISABLE=1` ### 🐛 Describe the bug Enabling speculative decoding (tested both `qwen3_next_mtp` and `DFlash` methods) on a hybrid-GDN Qwen3.6-35B-A3B model with **TP=2** causes a hard crash on the very first chat completion request. The error is `cudaErrorIllegalAddress`, with the stack landing at `self.num_accepted_tokens_event.synchronize()` in `gpu_model_runner.py:1927`. Both TP0 and TP1 workers raise the same error, and the NCCL ProcessGroup watchdog thread subsequently terminates with the same illegal address exception. Note: GDN prefill backend was auto-selected as **Triton/FLA** (not FlashInfer) in this build at the time of the crash, so this appears distinct from the FlashInfer-GDN line of bugs in #37729 and #37035, despite affecting the same model family. ### Reproduction Launch: ```bash vllm serve QuantTrio/Qwen3.6-35B-A3B-AWQ \ --...

## 现有链接修复摘要

#40898 [Spec Decode] Add Sliding Window Attention support to DFlash drafter

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: TP=2 spec-decode (qwen3_next_mtp / DFlash) on Qwen3.6 hybrid GDN crashes at gpu_model_runner.py:1927 num_accepted_tokens_event.synchronize() (cudaErrorIllegalAddress) ### Your current environment - vLLM: `0.19.2r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: pport) - GPU: 2× NVIDIA RTX 6000 Ada Generation (sm_89, 48 GB each, no NVLink, P2P over PCIe) - Driver: 580.126.09 / CUDA 13.0 - OS: Ubuntu, Linux 6.8.0-110-generic - Python 3.12 - NCCL env: `NCCL_P2P_DISABLE=1 NCCL_SHM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: hes at gpu_model_runner.py:1927 num_accepted_tokens_event.synchronize() (cudaErrorIllegalAddress) ### Your current environment - vLLM: `0.19.2rc1.dev226+g53b9640fb` (built off PR #40898 head — DFlash + SWA support) - GP...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: y terminates with the same illegal address exception. Note: GDN prefill backend was auto-selected as **Triton/FLA** (not FlashInfer) in this build at the time of the crash, so this appears distinct from the FlashInfer-G...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ng the same model family. ### Reproduction Launch: ```bash vllm serve QuantTrio/Qwen3.6-35B-A3B-AWQ \ --tensor-parallel-size 2 \ --max-model-len 65536 \ --gpu-memory-utilization 0.85 \ --max-num-batched-tokens 16384 \ -...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40898](https://github.com/vllm-project/vllm/pull/40898) | mentioned | 0.45 | [Spec Decode] Add Sliding Window Attention support to DFlash drafter | rent environment - vllm: `0.19.2rc1.dev226+g53b9640fb` (built off pr #40898 head — dflash + swa support) - gpu: 2× nvidia rtx 6000 ada generation (sm_89, 48 gb each, no nvlink, p2… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

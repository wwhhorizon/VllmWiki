# vllm-project/vllm#20522: [Bug]: HELP!!! RTX Pro 6000(Newest GPU 202504) RuntimeError: no kernel image available when starting vLLM with Qwen3-32B + YaRN

| 字段 | 值 |
| --- | --- |
| Issue | [#20522](https://github.com/vllm-project/vllm/issues/20522) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: HELP!!! RTX Pro 6000(Newest GPU 202504) RuntimeError: no kernel image available when starting vLLM with Qwen3-32B + YaRN

### Issue 正文摘录

### Your current environment ```text When I try to launch vLLM with the Qwen3-32B model (rope-scaling "YaRN") on an RTX Pro 6000(202504 newest GPU), the server fails to start and throws: RuntimeError: CUDA error: no kernel image is available for execution on the device CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Command: CUDA_VISIBLE_DEVICES=0 \ python -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen3-32B \ --served-model-name Qwen3-32B \ --rope-scaling '{"rope_type":"yarn","factor":4.0,"original_max_position_embeddings":32768}' \ --max-model-len 131072 \ --tensor-parallel-size 1 Env: INFO 07-06 16:50:52 [__init__.py:244] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu128...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug]: HELP!!! RTX Pro 6000(Newest GPU 202504) RuntimeError: no kernel image available when starting vLLM with Qwen3-32B + YaRN usage ### Your current environment ```text When I try to launch vLLM with the Qwen3-32B mod...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 202504) RuntimeError: no kernel image available when starting vLLM with Qwen3-32B + YaRN usage ### Your current environment ```text When I try to launch vLLM with the Qwen3-32B model (rope-scaling "YaRN") on an RTX Pro...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Command: CUDA_VISIBLE_DEVICES=0 \ python -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen3-32B \ --served-model-name Qwen3-32B...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affecte...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

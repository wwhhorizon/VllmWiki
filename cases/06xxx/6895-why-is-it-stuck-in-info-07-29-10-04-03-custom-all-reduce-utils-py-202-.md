# vllm-project/vllm#6895: Why is it stuck in 'INFO 07-29 10:04:03 custom_all_reduce_utils.py:202] generating GPU P2P access cache in /root/.cache/vllm/gpu_p2p_access_cache_for_0,1.json'?

| 字段 | 值 |
| --- | --- |
| Issue | [#6895](https://github.com/vllm-project/vllm/issues/6895) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Why is it stuck in 'INFO 07-29 10:04:03 custom_all_reduce_utils.py:202] generating GPU P2P access cache in /root/.cache/vllm/gpu_p2p_access_cache_for_0,1.json'?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... /workspace/vllm-main/vllm/connections.py:8: RuntimeWarning: Failed to read commit hash: No module named 'vllm.commit_id' from vllm.version import __version__ as VLLM_VERSION PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.31 Python version: 3.10.13 (main, Sep 11 2023, 13:44:35) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-107-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB Nvidia driver version: 535.183.01 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.0 /usr/lib/x8...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Failed to read commit hash: No module named 'vllm.commit_id' from vllm.version import __version__ as VLLM_VERSION PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build Py...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected Vulnerability...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ion__ as VLLM_VERSION PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: `text The output of `python collect_env.py` ``` Collecting environment information... /workspace/vllm-main/vllm/connections.py:8: RuntimeWarning: Failed to read commit hash: No module named 'vllm.commit_id' from vllm.ve...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ntrypoints.openai.api_server --served-model-name Qwen2-72B-Instruct-GPTQ-Int4-tisson --model /models/Qwen2-72B-Instruct-GPTQ-Int4 --host 0.0.0.0 --port 30000 --tensor-parallel-size 2 --quantization gptq` and then it stu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

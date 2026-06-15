# vllm-project/vllm#7679: [Usage, bug]: vLLM Docker |  ValueError: OpenTelemetry packages must be installed before configuring 'otlp_traces_endpoint' during vLLM startup

| 字段 | 值 |
| --- | --- |
| Issue | [#7679](https://github.com/vllm-project/vllm/issues/7679) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage, bug]: vLLM Docker \|  ValueError: OpenTelemetry packages must be installed before configuring 'otlp_traces_endpoint' during vLLM startup

### Issue 正文摘录

### Your current environment ```text binishb.ttl@vzneuronsr01:~/Vipul$ python3.10 collect_env_vllm.py Collecting environment information... WARNING 08-20 12:51:20 ray_utils.py:34] Failed to import Ray with ModuleNotFoundError("No module named 'ray.core'"). For distributed inference, please install Ray with `pip install ray pandas pyarrow`. PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.26.1 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-113-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 11.5.119 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-PCIE-40GB GPU 1: NVIDIA A100-PCIE-40GB Nvidia driver version: 535.183.01 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.6 /usr/lib/x86_6...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Usage, bug]: vLLM Docker | ValueError: OpenTelemetry packages must be installed before configuring 'otlp_traces_endpoint' during vLLM startup usage;stale ### Your current environment ```text binishb.ttl@vzneuronsr01:~/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ray pandas pyarrow`. PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: lled before configuring 'otlp_traces_endpoint' during vLLM startup usage;stale ### Your current environment ```text binishb.ttl@vzneuronsr01:~/Vipul$ python3.10 collect_env_vllm.py Collecting environment information......
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: LM Docker | ValueError: OpenTelemetry packages must be installed before configuring 'otlp_traces_endpoint' during vLLM startup usage;stale ### Your current environment ```text binishb.ttl@vzneuronsr01:~/Vipul$ python3.1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=64000, guided_decoding_backend='outlines', distributed_executor_b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

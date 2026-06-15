# vllm-project/vllm#6340: [Bug]: get that Exception in thread Thread-3 (_report_usage_worker): (vllm OpenVINO，When python3 vllm/benchmarks/benchmark_throughput.py，)

| 字段 | 值 |
| --- | --- |
| Issue | [#6340](https://github.com/vllm-project/vllm/issues/6340) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: get that Exception in thread Thread-3 (_report_usage_worker): (vllm OpenVINO，When python3 vllm/benchmarks/benchmark_throughput.py，)

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... WARNING 07-11 22:54:46 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.3.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.35 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.5.0-41-generic-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: 架构： x86_64 CPU 运行模式： 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual 字节序： Little Endian CPU: 20 在线 CPU 列表： 0-19 厂商 ID： GenuineIntel 型号名称： Intel(R) Xeon(R) CPU E5-2666 v3 @ 2.90GHz CPU 系列： 6 型号： 63 每个核的线程数： 2 每个座的核数： 10 座： 1 步进： 2 CPU 最大 MHz： 3500.000...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: nment information... WARNING 07-11 22:54:46 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.3.0+cpu Is debug build: False CUDA used to build PyTo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: odule named 'vllm._C'") PyTorch version: 2.3.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ```text The output of `python collect_env.py` Collecting environment information... WARNING 07-11 22:54:46 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: CE=10 \ VLLM_OPENVINO_CPU_KV_CACHE_PRECISION=u8 \ VLLM_OPENVINO_ENABLE_QUANTIZED_WEIGHTS=ON \ python3 vllm/benchmarks/benchmark_throughput.py \ --input-len 128 --output-len 128 \ --num_prompts 100 ``` The log ： ``` (vll...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: e Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected Vulnerability...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

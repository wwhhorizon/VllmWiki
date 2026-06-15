# vllm-project/vllm#7204: [Bug]: GPTQ Marlin with cpu-offload-gb fails on `0.5.4`

| 字段 | 值 |
| --- | --- |
| Issue | [#7204](https://github.com/vllm-project/vllm/issues/7204) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: GPTQ Marlin with cpu-offload-gb fails on `0.5.4`

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.31 Python version: 3.10.14 (main, Apr 6 2024, 18:45:05) [GCC 9.4.0] (64-bit runtime) Python platform: Linux-4.18.0-425.19.2.el8_7.x86_64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB Nvidia driver version: 525.105.17 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 43 bits physical, 48 bits virtual CPU(s): 256 On-line CPU(s) list: 0-255 Thread(s) per core: 2 Core(s) per socket: 64 Socket(s): 2 NUMA node(s): 8 Vendor ID: AuthenticAMD CPU family: 23 Model: 49 Model name: AMD EPYC 7742 64-Core Processor Stepping: 0...

## 现有链接修复摘要

#6960 [Bugfix] Support cpu offloading with quant_method.process_weights_after_loading

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 9: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Mitigation; untrained return thunk; SMT enabled with STIBP protection Vulnerability Spec store bypass: Mit...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: l clzero irperf xsaveerptr wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip rdpid overflow_recov succor smca sme...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: .5.4` bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#6960](https://github.com/vllm-project/vllm/pull/6960) | mentioned | 0.45 | [Bugfix] Support cpu offloading with quant_method.process_weights_after_loading | un a gptq model with cpu offloading. this should have been fixed with #6960 but it appears not. ``` python3 -m vllm.entrypoints.openai.api_server --model /home/ndurkee/ndurkee/met… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

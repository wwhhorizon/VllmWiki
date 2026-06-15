# vllm-project/vllm#5740: [Bug]: KeyError: '/psm_ed65b7e3'

| 字段 | 值 |
| --- | --- |
| Issue | [#5740](https://github.com/vllm-project/vllm/issues/5740) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KeyError: '/psm_ed65b7e3'

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.29.6 Libc version: glibc-2.31 Python version: 3.10.14 | packaged by conda-forge | (main, Mar 20 2024, 12:45:18) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-5.4.0-144-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A40 GPU 1: NVIDIA A40 GPU 2: NVIDIA A40 GPU 3: NVIDIA A40 GPU 4: NVIDIA A40 GPU 5: NVIDIA A40 GPU 6: NVIDIA A40 GPU 7: NVIDIA A40 Nvidia driver version: 550.54.14 cuDNN version: Probably one of the following: /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn.so.9.1.0 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn_adv.so.9.1.0 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn_cnn.so.9.1.0 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn_engines_precompiled.so.9.1.0 /usr/local/cuda-12.1/targets/x86_64-linux/lib...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Your current environment Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC vers...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: psm_ed65b7e3' bug ### Your current environment Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Sto...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: KeyError: '/psm_ed65b7e3' bug ### Your current environment Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e='auto', trust_remote_code=True, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_ba...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

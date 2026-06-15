# vllm-project/vllm#4810: Qwen1.5-14B-Chat-GPTQ-Int4: quantization is not fully optimized yet. The speed can be slower than non-quantized models.

| 字段 | 值 |
| --- | --- |
| Issue | [#4810](https://github.com/vllm-project/vllm/issues/4810) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Qwen1.5-14B-Chat-GPTQ-Int4: quantization is not fully optimized yet. The speed can be slower than non-quantized models.

### Issue 正文摘录

### Your current environment PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.1 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.35 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-72-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A800-SXM4-80GB GPU 1: NVIDIA A800-SXM4-80GB GPU 2: NVIDIA A800-SXM4-80GB GPU 3: NVIDIA A800-SXM4-80GB GPU 4: NVIDIA A800-SXM4-80GB GPU 5: NVIDIA A800-SXM4-80GB GPU 6: NVIDIA A800-SXM4-80GB GPU 7: NVIDIA A800-SXM4-80GB Nvidia driver version: 535.154.05 cuDNN version: Probably one of the following: /usr/local/cuda-12.3/targets/x86_64-linux/lib/libcudnn.so.8.9.7 /usr/local/cuda-12.3/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.9.7 /usr/local/cuda-12.3/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.9.7 /usr/local/cuda-12.3/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.9.7 /usr/local/c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: wer than non-quantized models. bug ### Your current environment PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.1 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: current environment PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.1 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Qwen1.5-14B-Chat-GPTQ-Int4: quantization is not fully optimized yet. The speed can be slower than non-quantized models. bug ### Your current environment PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to bu
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Vulnerable Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Vulnerable Vulnerability Spectre v1: Vulnerable: __user pointe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Qwen1.5-14B-Chat-GPTQ-Int4: quantization is not fully optimized yet. The speed can be slower than non-quantized models. bug ### Your current environment PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to bu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

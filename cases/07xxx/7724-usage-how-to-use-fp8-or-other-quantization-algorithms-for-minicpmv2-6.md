# vllm-project/vllm#7724: [Usage]: How to use FP8 or other quantization algorithms for Minicpmv2_6

| 字段 | 值 |
| --- | --- |
| Issue | [#7724](https://github.com/vllm-project/vllm/issues/7724) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization |
| 子分类 | throughput |
| Operator 关键词 | cuda;fp8;operator;quantization;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to use FP8 or other quantization algorithms for Minicpmv2_6

### Issue 正文摘录

### Your current environment ```shell # The output of `python collect_env.py` PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 9.3.1 20200408 (Red Hat 9.3.1-2) Clang version: Could not collect CMake version: version 3.25.0-rc2 Libc version: glibc-2.17 Python version: 3.9.16 (main, Jul 10 2023, 11:13:07) [GCC 8.3.1 20190311 (Red Hat 8.3.1-3)] (64-bit runtime) Python platform: Linux-4.18.0-147.mt20200626.413.el8_1.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L40 Nvidia driver version: 535.129.03 cuDNN version: Probably one of the following: /usr/lib64/libcudnn.so.8.9.2 /usr/lib64/libcudnn_adv_infer.so.8.9.2 /usr/lib64/libcudnn_adv_train.so.8.9.2 /usr/lib64/libcudnn_cnn_infer.so.8.9.2 /usr/lib64/libcudnn_cnn_train.so.8.9.2 /usr/lib64/libcudnn_ops_infer.so.8.9.2 /usr/lib64/libcudnn_ops_train.so.8.9.2 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: nt environment ```shell # The output of `python collect_env.py` PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ython collect_env.py` PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 9.3.1 20200408 (Red Hat 9.3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L40 Nvidia driver version: 535.129.03 cuDNN version: Probably one of the following: /usr/lib64/libcudnn.so....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Usage]: How to use FP8 or other quantization algorithms for Minicpmv2_6 usage ### Your current environment ```shell # The output of `python collect_env.py` PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: els, not multimodal models. And which quantization algorithm has the greatest throughput improvement? performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization cud...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

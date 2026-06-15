# vllm-project/vllm#16427: [Installation]: Installing only with Flash-Attn2

| 字段 | 值 |
| --- | --- |
| Issue | [#16427](https://github.com/vllm-project/vllm/issues/16427) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Installing only with Flash-Attn2

### Issue 正文摘录

### Your current environment ```text INFO 04-10 14:33:55 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0a0+df5bbc09d1.nv24.11 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (aarch64) GCC version: (Ubuntu 13.2.0-23ubuntu4) 13.2.0 Clang version: Could not collect CMake version: version 3.31.0 Libc version: glibc-2.39 Python version: 3.12.3 (main, Sep 11 2024, 14:17:37) [GCC 13.2.0] (64-bit runtime) Python platform: Linux-5.14.21-150500.55.65_13.0.73-cray_shasta_c_64k-aarch64-with-glibc2.39 Is CUDA available: True CUDA runtime version: 12.6.85 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GH200 120GB Nvidia driver version: 550.144.03 cuDNN version: Probably one of the following: /usr/lib/aarch64-linux-gnu/libcudnn.so.9.5.1 /usr/lib/aarch64-linux-gnu/libcudnn_adv.so.9.5.1 /usr/lib/aarch64-linux-gnu/libcudnn_cnn.so.9.5.1 /usr/lib/aarch64-linux-gnu/libcudnn_engines_precompiled.so.9.5.1 /usr/lib/aarch64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.5.1 /usr/lib/aarch64-linux-gnu/libcudnn_graph.so.9.5.1 /usr/lib/aarch64-linux...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: Installing only with Flash-Attn2 installation;stale ### Your current environment ```text INFO 04-10 14:33:55 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... P
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: xt INFO 04-10 14:33:55 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0a0+df5bbc09d1.nv24.11 Is debug build: False CUDA used to build PyTorch: 12.6 ROC...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: _.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0a0+df5bbc09d1.nv24.11 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: p sve2 sveaes svepmull svebitperm svesha3 svesm4 flagm2 frint svei8mm svebf16 i8mm bf16 dgh bti L1d cache: 18 MiB (288 instances) L1i cache: 18 MiB (288 instances) L2 cache: 288 MiB (288 instances) L3 cache:
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Installation]: Installing only with Flash-Attn2 installation;stale ### Your current environment ```text INFO 04-10 14:33:55 [__init__.py:239] Automatically detected platform cuda. Collecting environment information......

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

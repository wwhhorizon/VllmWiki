# vllm-project/vllm#30834: [Bug]: vllm0.12.0 h100 PTX was compiled with an unsupported toolchain

| 字段 | 值 |
| --- | --- |
| Issue | [#30834](https://github.com/vllm-project/vllm/issues/30834) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm0.12.0 h100 PTX was compiled with an unsupported toolchain

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 22.04.3 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.0 (default, Mar 3 2022, 09:58:08) [GCC 7.5.0] (64-bit runtime) Python platform : Linux-5.15.0-135-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA H100 80GB HBM3 GPU 5: NVIDIA H100 80GB HBM3 GPU 6: NVIDIA H100 80GB HBM3 GPU 7: NVIDIA H100 80GB HBM3 Nvidia driver version : 550.144.03 cuDNN version : Prob...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: vllm0.12.0 h100 PTX was compiled with an unsupported toolchain bug ### Your current environment ==============================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: vllm0.12.0 h100 PTX was compiled with an unsupported toolchain bug ### Your current environment ==============================
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA H100 80GB HBM3 GPU 5: NVIDIA...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ERROR 12-17 11:14:51 [core.py:843] self.model_runner.load_model(eep_scale_up=eep_scale_up) (EngineCore_DP0 pid=2445681) ERROR 12-17 11:14:51 [core.py:843] File "/data03/liqy-a/miniconda3/envs/vllm/lib/python3.10/site-pa
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: Is debug build : False CUDA used to build PyTorch : 12.8

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

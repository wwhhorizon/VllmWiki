# vllm-project/vllm#28371: [Installation]: Recipe Installation fails due to missing linux aarch64.whl

| 字段 | 值 |
| --- | --- |
| Issue | [#28371](https://github.com/vllm-project/vllm/issues/28371) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Recipe Installation fails due to missing linux aarch64.whl

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (aarch64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 3.28.3 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cpu Is debug build : False CUDA used to build PyTorch : Could not collect ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.11.0-1016-nvidia-aarch64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : False CUDA runtime version : 12.6.85 CUDA_MODULE_LOADING set to : N/A GPU models and configuration : GPU 0: NVIDIA GB10 Nvidia driver version : 580.95.05 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info =======================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]: Recipe Installation fails due to missing linux aarch64.whl installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ============================== System I
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Installation]: Recipe Installation fails due to missing linux aarch64.whl installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ============================== System Info ===...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: p sve2 sveaes svepmull svebitperm svesha3 svesm4 flagm2 frint svei8mm svebf16 i8mm bf16 dgh bti ecv afp wfxt Model name: Cortex-A725 Model: 1 Thread(s) per core: 1 Core(s) per socket: 10 Socket(s):
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: runtime version : 12.6.85 CUDA_MODULE_LOADING set to : N/A GPU models and configuration : GPU 0: NVIDIA GB10 Nvidia driver version : 580.95.05 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Recipe Installation fails due to missing linux aarch64.whl installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ============================== System Info ===================...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

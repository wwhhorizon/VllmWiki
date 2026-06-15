# vllm-project/vllm#19802: [Bug]: Reproduction failed when evaluate model

| 字段 | 值 |
| --- | --- |
| Issue | [#19802](https://github.com/vllm-project/vllm/issues/19802) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Reproduction failed when evaluate model

### Issue 正文摘录

### Your current environment ```bash ============================== System Info ============================== OS : Ubuntu 20.04.6 LTS (x86_64) GCC version : (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version : Could not collect CMake version : version 3.29.3 Libc version : glibc-2.31 ============================== PyTorch Info ============================== PyTorch version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.13 (main, Sep 11 2023, 13:44:35) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-3.10.0-1160.76.1.el7.x86_64-x86_64-with-glibc2.31 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.1.105 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A800-SXM4-80GB GPU 1: NVIDIA A800-SXM4-80GB GPU 2: NVIDIA A800-SXM4-80GB GPU 3: NVIDIA A800-SXM4-80GB GPU 4: NVIDIA A800-SXM4-80GB GPU 5: NVIDIA A800-SXM4-80GB GPU 6: NVIDIA A800-SXM4-80GB GPU 7: NVIDIA A800-SXM4-80GB Nvidia driver version : 550.54.14 cuDNN versi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 20.04.6 LTS (x86_64) GCC version : (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version : Could not collect CMake version : version 3.29.3 Libc version : glibc-2.31 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.13 (...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Reproduction failed when evaluate model bug ### Your current environment ```bash ============================== System Info ============================== OS : Ubuntu 20.04.6 LTS (x86_64) GCC version
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Reproduction failed when evaluate model bug ### Your current environment ```bash ============================== System Info ============================== OS : Ubuntu 20.04.6 LTS (x86_64) GCC version :
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: .manual_seed(seed) torch.cuda.manual_seed_all(seed) torch.backends.cudnn.deterministic = True torch.backends.cudnn.benchmark = False ``` And evaluate with: ```python llm = LLM(model=model_path,tensor_parallel_size=8, se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

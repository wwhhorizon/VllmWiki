# vllm-project/vllm#23153: [Bug]: 5090 LapTop Notebook will kill the vLLM in Docker

| 字段 | 值 |
| --- | --- |
| Issue | [#23153](https://github.com/vllm-project/vllm/issues/23153) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 5090 LapTop Notebook will kill the vLLM in Docker

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Could not collect GCC version : Could not collect Clang version : Could not collect CMake version : Could not collect Libc version : N/A ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cpu Is debug build : False CUDA used to build PyTorch : Could not collect ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.9 (tags/v3.11.9:de54cf5, Apr 2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] (64-bit runtime) Python platform : Windows-10-10.0.26100-SP0 ============================== CUDA / GPU Info ============================== Is CUDA available : False CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : N/A GPU models and configuration : GPU 0: NVIDIA GeForce RTX 5090 Laptop GPU Nvidia driver version : 572.84 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================== 'wmic' 不是内部或外部命令，也不是可运行的程序 或批处理文件。 ====...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: 5090 LapTop Notebook will kill the vLLM in Docker bug;stale ### Your current environment ============================== System Info ============================== OS : Could not collect GCC version : Could not c
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ch version : 2.8.0+cpu Is debug build : False CUDA used to build PyTorch : Could not collect ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python versi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: rsion : Could not collect CUDA_MODULE_LOADING set to : N/A GPU models and configuration : GPU 0: NVIDIA GeForce RTX 5090 Laptop GPU Nvidia driver version : 572.84 cuDNN version : Could not collect HIP runtime version :...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: legal instruction was encountered # 增加了 --enforce-eager # 去掉了 --quantization awq command: > --model /models/Qwen2___5-7B-Instruct --tensor-parallel-size 1 --dtype auto --trust-remote-code --enforce-eager --gpu-memory-ut...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: 5090 LapTop Notebook will kill the vLLM in Docker bug;stale ### Your current environment ============================== System Info ============================== OS : Could not collect GCC version : Could not co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

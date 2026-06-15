# vllm-project/vllm#22091: [Installation]: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at /pytorch/torch/csrc/utils/tensor_numpy.cpp:81.)

| 字段 | 值 |
| --- | --- |
| Issue | [#22091](https://github.com/vllm-project/vllm/issues/22091) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at /pytorch/torch/csrc/utils/tensor_numpy.cpp:81.)

### Issue 正文摘录

### Your current environment /home/sdp/fmt/vllm/vllm_ov_env/lib/python3.12/site-packages/torch/_subclasses/functional_tensor.py:276: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at /pytorch/torch/csrc/utils/tensor_numpy.cpp:81.) cpu = _conversion_method_template(device=torch.device("cpu")) Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.0.3 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cpu Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Jun 18 2025, 17:59:45) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.14.0-27-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : False CUDA runtime version : No CUDA CUDA_MODULE_LOADING se...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at /pytorch/torch/csrc/utils/tensor_numpy.cpp:81.) installation;stale ### Your current environment /home/sdp/fmt/vllm
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ch version : 2.7.1+cpu Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ion_method_template(device=torch.device("cpu")) Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ternally at /pytorch/torch/csrc/utils/tensor_numpy.cpp:81.) installation;stale ### Your current environment /home/sdp/fmt/vllm/vllm_ov_env/lib/python3.12/site-packages/torch/_subclasses/functional_tensor.py:276: UserWar...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ai/en/v0.6.3/getting_started/openvino-installation.html#install-openvino-backend-from-source I think there is some typo in this page also. It talks about command pip install -r requirements-build.txt --extra-index-url h...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

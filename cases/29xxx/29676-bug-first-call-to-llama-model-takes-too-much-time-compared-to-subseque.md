# vllm-project/vllm#29676: [Bug]: First call to llama model takes too much time compared to subsequent ones

| 字段 | 值 |
| --- | --- |
| Issue | [#29676](https://github.com/vllm-project/vllm/issues/29676) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: First call to llama model takes too much time compared to subsequent ones

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : Could not collect Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.9.0a0+145a3a7bda.nv25.10 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.14.0-1017-aws-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.0.88 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA A10G Nvidia driver version : 580.105.08 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.14.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.14.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.14.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : Could not collect Libc version : glibc-2.39 ==============
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.4.0+6690ebbc.nv25.10.37063217 [pip3] numpy==1.26.4 [pip3] nvidia-cudnn-frontend==1.15.0 [pip3] nvidia-cutlass-dsl==4.2.1 [pip...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: : 2.9.0a0+145a3a7bda.nv25.10 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: call to llama model takes too much time compared to subsequent ones bug;stale ### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: First call to llama model takes too much time compared to subsequent ones bug;stale ### Your current environment ============================== System Info ============================== OS : Ubuntu

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#19865: [Bug]: NCCL issues when running vllm v0.9.1 for the Deepseek-R1 model [B200 GPU]

| 字段 | 值 |
| --- | --- |
| Issue | [#19865](https://github.com/vllm-project/vllm/issues/19865) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | crash;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NCCL issues when running vllm v0.9.1 for the Deepseek-R1 model [B200 GPU]

### Issue 正文摘录

### Your current environment Machine: NV B200 GPU Docker image: vllm/vllm-openai:v0.9.1 model: deepseek-ai/DeepSeek-R1 CUDA: 12.8 Driver Version: 570.133.20 Command: VLLM_USE_V1=1 vllm serve /models/DeepSeek-R1 --tensor-parallel-size 8 --disable-log-requests --trust-remote-code ### 🐛 Describe the bug While running the online serving: VLLM_USE_V1=1 vllm serve /models/DeepSeek-R1 --tensor-parallel-size 8 --disable-log-requests --trust-remote-code The following NCCL error message : NCCL_DEBUG=INFO VLLM_USE_V1=1 vllm serve /models/DeepSeek-R1 --tensor-parallel-size 8 --disable-log-requests --trust-remote-code Errors: (VllmWorker rank=3 pid=15164) ERROR 06-19 07:06:13 [multiproc_executor.py:527] torch.distributed.DistBackendError: NCCL error in: /pytorch/torch/csrc/distributed/c10d/NCCLUtils.cpp:77, unhandled cuda error (run with NCCL_DEBUG=INFO for details), NCCL version 2.26.2 (VllmWorker rank=3 pid=15164) ERROR 06-19 07:06:13 [multiproc_executor.py:527] ncclUnhandledCudaError: Call to CUDA function failed. (VllmWorker rank=3 pid=15164) ERROR 06-19 07:06:13 [multiproc_executor.py:527] Last error: (VllmWorker rank=3 pid=15164) ERROR 06-19 07:06:13 [multiproc_executor.py:527] Cuda fail...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: B200 GPU] bug;stale ### Your current environment Machine: NV B200 GPU Docker image: vllm/vllm-openai:v0.9.1 model: deepseek-ai/DeepSeek-R1 CUDA: 12.8 Driver Version: 570.133.20 Command: VLLM_USE_V1=1 vllm serve /models/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: NCCL issues when running vllm v0.9.1 for the Deepseek-R1 model [B200 GPU] bug;stale ### Your current environment Machine: NV B200 GPU Docker image: vllm/vllm-openai:v0.9.1 model: deepseek-ai/DeepSeek-R1 CUDA: 12....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: issues when running vllm v0.9.1 for the Deepseek-R1 model [B200 GPU] bug;stale ### Your current environment Machine: NV B200 GPU Docker image: vllm/vllm-openai:v0.9.1 model: deepseek-ai/DeepSeek-R1 CUDA: 12.8 Driver Ver...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ) ERROR 06-19 07:06:13 [multiproc_executor.py:527] torch.distributed.DistBackendError: NCCL error in: /pytorch/torch/csrc/distributed/c10d/NCCLUtils.cpp:77, unhandled cuda error (run with NCCL_DEBUG=INFO for details), N...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: NCCL issues when running vllm v0.9.1 for the Deepseek-R1 model [B200 GPU] bug;stale ### Your current environment Machine: NV B200 GPU Docker image: vllm/vllm-openai:v0.9.1 model: deepseek-ai/DeepSeek-R1 CUDA: 12....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

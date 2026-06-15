# vllm-project/vllm#39384: [Bug]: DP replica under-utilization with Qwen3-8B (tp=4, dp=2) on 8x A100 PCIe

| 字段 | 值 |
| --- | --- |
| Issue | [#39384](https://github.com/vllm-project/vllm/issues/39384) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DP replica under-utilization with Qwen3-8B (tp=4, dp=2) on 8x A100 PCIe

### Issue 正文摘录

### Your current environment - vLLM version: 0.16.0 - CUDA driver: 550.54.15 - CUDA version: 12.4 - GPUs: 8 x NVIDIA A100-PCIE-40GB - Interconnect: PCIe-only (no NVLink) - NCCL version reported by vLLM: 2.27.5 - Python: 3.10 - OS: Ubuntu Linux ### 🐛 Describe the bug ### Model - Problematic model: Qwen3-8B - Comparison model: Qwen2.5-Coder-7B-Instruct ### Command For Qwen3-8B: ```bash vllm serve /home/skl/mkx/model/Qwen3-8B \ --host 127.0.0.1 \ --port 10842 \ --served-model-name Qwen3-8B \ --tensor-parallel-size 4 \ --data-parallel-size 2 ``` For Qwen2.5-Coder-7B-Instruct: ```bash vllm serve /home/skl/mkx/model/Qwen2.5-Coder-7B-Instruct \ --host 127.0.0.1 \ --port 10872 \ --served-model-name Qwen2.5-Coder-7B-Instruct \ --tensor-parallel-size 4 \ --data-parallel-size 2 ``` vLLM logs show that api_server_count defaults to data_parallel_size (2) in both cases. What I observe When serving Qwen3-8B with tp=4, dp=2 on 8 A100 PCIe GPUs: All 8 GPUs load model weights into memory successfully. The two TP groups appear to be: DP replica 0: local_rank 0,1,2,3 DP replica 1: local_rank 4,5,6,7 However, during inference, only GPUs 4-7 show high utilization, while GPUs 0-3 remain near 0% utilizat...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: DP replica under-utilization with Qwen3-8B (tp=4, dp=2) on 8x A100 PCIe bug ### Your current environment - vLLM version: 0.16.0 - CUDA driver: 550.54.15 - CUDA version: 12.4 - GPUs: 8 x NVIDIA A100-PCIE-40GB - In...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ug]: DP replica under-utilization with Qwen3-8B (tp=4, dp=2) on 8x A100 PCIe bug ### Your current environment - vLLM version: 0.16.0 - CUDA driver: 550.54.15 - CUDA version: 12.4 - GPUs: 8 x NVIDIA A100-PCIE-40GB - Inte...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: U utilization appears more distributed in practice, even though the HTTP request logs may still mostly show a single API server process handling requests. ### Why this seems suspicious This does not look like a simple m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: DP replica under-utilization with Qwen3-8B (tp=4, dp=2) on 8x A100 PCIe bug ### Your current environment - vLLM version: 0.16.0 - CUDA driver: 550.54.15 - CUDA version: 12.4 - GPUs: 8 x NVIDIA A100-PCIE-40GB - In...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: aph capture and DP scheduling / replica utilization? Would you recommend testing with: --api-server-count 1 --enforce-eager smaller --max-model-len or a newer vLLM version first? Minimal reproduction On a machine with 8...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

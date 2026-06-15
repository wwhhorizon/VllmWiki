# vllm-project/vllm#9373: [Bug]: Tensor Parallelism performs poorly 

| 字段 | 值 |
| --- | --- |
| Issue | [#9373](https://github.com/vllm-project/vllm/issues/9373) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Tensor Parallelism performs poorly 

### Issue 正文摘录

### Your current environment This issue is easy to reproduce. In AWS: 1) Spin up EC2 2) Use the Deep Learning OSS Nvidia Driver AMI GPU PyTorch 2.3.1 (Ubuntu 20.04) 3) Select g5.12xlarge (which contains 4 GPUS, A10Gs, each with 24GiB GDDR6 RAM) That's the current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have 4 A10Gs, each with 24GiB of GDDR6 Memory: nvidia-smi ip-172-31-64-123: Tue Oct 15 12:00:52 2024 Tue Oct 15 12:00:52 2024 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 550.90.07 Driver Version: 550.90.07 CUDA Version: 12.4 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA A10G On | 00000000:00:1B.0 Off | 0 | | 0% 23C P8 28W / 300W | 1MiB / 23028MiB | 0% Default | | | | N/A | +-----------------------------------------+------------------------+----------------------+ | 1 NVIDIA A10G On | 00000000:00...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 9: [Bug]: Tensor Parallelism performs poorly bug;stale ### Your current environment This issue is easy to reproduce. In AWS: 1) Spin up EC2 2) Use the Deep Learning OSS Nvidia Driver AMI GPU PyTorch 2.3.1 (Ubuntu 20.04) 3)...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ----------------------------+ | NVIDIA-SMI 550.90.07 Driver Version: 550.90.07 CUDA Version: 12.4 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M |...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: , A10Gs, each with 24GiB GDDR6 RAM) That's the current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have 4 A10Gs, each with 24GiB of GDDR6 Memory: nvidia-smi ip-172-31-64-123: Tue Oct 15 12:0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: -trust-remote-code --max-model-len 30000 --gpu-memory-utilization 0.90 --dtype float16 --disable-custom-all-reduce --tensor-parallel-size 4 Unable to find image 'vllm/vllm-openai:latest' locally latest: Pulling from vll...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Tensor Parallelism performs poorly bug;stale ### Your current environment This issue is easy to reproduce. In AWS: 1) Spin up EC2 2) Use the Deep Learning OSS Nvidia Driver AMI GPU PyTorch 2.3.1 (Ubuntu 20.04) 3)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#4940: [Bug]: run vllm api with docker

| 字段 | 值 |
| --- | --- |
| Issue | [#4940](https://github.com/vllm-project/vllm/issues/4940) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: run vllm api with docker

### Issue 正文摘录

### Your current environment docker images :vllm/vllm-openai:latest ### 🐛 Describe the bug `docker run --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface -v /mnt/ddata/models/Baichuan2-13B-Chat:/Baichuan2-13B-Chat --env "HUGGING_FACE_HUB_TOKEN= " -p 5000:5000 --ipc=host vllm/vllm-openai:latest --model /Baichuan2-13B-Chat --trust-remote-code --tensor-parallel-size 2` I use the command above to test and occur "RuntimeError: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error? Error 804: forward compatibility was attempted on non supported HW" how to solve this problem, thx.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: run vllm api with docker bug;stale ### Your current environment docker images :vllm/vllm-openai:latest ### 🐛 Describe the bug `docker run --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.cache/huggingfa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 🐛 Describe the bug `docker run --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface -v /mnt/ddata/models/Baichuan2-13B-Chat:/Baichuan2-13B-Chat --env "HUGGING_FACE_HUB_TOKEN= " -p 5000:5000 --ipc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: the command above to test and occur "RuntimeError: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error? Error 804: forward com...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: run vllm api with docker bug;stale ### Your current environment docker images :vllm/vllm-openai:latest ### 🐛 Describe the bug `docker run --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.cache/huggingfa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ug;stale ### Your current environment docker images :vllm/vllm-openai:latest ### 🐛 Describe the bug `docker run --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface -v /mnt/ddata/models/Baichuan2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

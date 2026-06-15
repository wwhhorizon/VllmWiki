# vllm-project/vllm#6025: [Bug]: Producer process has been terminated before all shared CUDA tensors released (v 0.5.0 post1, v 0.4.3)

| 字段 | 值 |
| --- | --- |
| Issue | [#6025](https://github.com/vllm-project/vllm/issues/6025) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Producer process has been terminated before all shared CUDA tensors released (v 0.5.0 post1, v 0.4.3)

### Issue 正文摘录

### Your current environment Docker Image: vllm/vllm-openai:v0.4.3 as well as 0.5.0 post-1 Params: ``` --model=microsoft/Phi-3-medium-4k-instruct --tensor-parallel-size=2 --disable-log-requests --trust-remote-code --max-model-len=2048 --gpu-memory-utilization=0.9 ``` The container freezes (does nothing) after presenting the following exception in the log. ### 🐛 Describe the bug ``` Original exception was: [rank0]:[W CudaIPCTypes.cpp:16] Producer process has been terminated before all shared CUDA tensors released. See Note [Sharing CUDA tensors] ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: eleased (v 0.5.0 post1, v 0.4.3) bug;stale ### Your current environment Docker Image: vllm/vllm-openai:v0.4.3 as well as 0.5.0 post-1 Params: ``` --model=microsoft/Phi-3-medium-4k-instruct --tensor-parallel-size=2 --dis...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ted before all shared CUDA tensors released (v 0.5.0 post1, v 0.4.3) bug;stale ### Your current environment Docker Image: vllm/vllm-openai:v0.4.3 as well as 0.5.0 post-1 Params: ``` --model=microsoft/Phi-3-medium-4k-ins...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: Producer process has been terminated before all shared CUDA tensors released (v 0.5.0 post1, v 0.4.3) bug;stale ### Your current environment Docker Image: vllm/vllm-openai:v0.4.3 as well as 0.5.0 post-1 Params: `...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Image: vllm/vllm-openai:v0.4.3 as well as 0.5.0 post-1 Params: ``` --model=microsoft/Phi-3-medium-4k-instruct --tensor-parallel-size=2 --disable-log-requests --trust-remote-code --max-model-len=2048 --gpu-memory-utiliza...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

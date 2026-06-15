# vllm-project/vllm#44061: [Bug]: P2pNcclConnector ZMQ port conflict when restarting disaggregated_prefill.py

| 字段 | 值 |
| --- | --- |
| Issue | [#44061](https://github.com/vllm-project/vllm/issues/44061) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: P2pNcclConnector ZMQ port conflict when restarting disaggregated_prefill.py

### Issue 正文摘录

### Your current environment **Environment**: - vLLM version: 0.22.0 - Hardware: 2x NVIDIA L40 46GB - OS: Ubuntu, CUDA 13.0 - Model: Qwen/Qwen3-8B ### 🐛 Describe the bug **Description**: Running `examples/disaggregated/disaggregated_prefill.py`, the script fails immediately with ZMQError because both the prefill and decode processes attempt to bind the same port: zmq.error.ZMQError: Address already in use (addr='tcp:// :14579') Root cause: In `p2p_nccl_engine.py` line 91, the port is calculated as `kv_port + port_offset` where `port_offset=0` for both processes. Both prefill (rank=0) and decode (rank=1) end up binding the same port 14579. **Expected behavior**: Each process should bind a different port. The fix should use `kv_rank` as `port_offset` to differentiate the two instances. **Steps to reproduce**: 1. Run `python examples/disaggregated/disaggregated_prefill.py` with any model 2. Script fails immediately with ZMQError on the prefill process [disaggregated_prefill_error2.log](https://github.com/user-attachments/files/28419725/disaggregated_prefill_error2.log) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ted_prefill.py bug ### Your current environment **Environment**: - vLLM version: 0.22.0 - Hardware: 2x NVIDIA L40 46GB - OS: Ubuntu, CUDA 13.0 - Model: Qwen/Qwen3-8B ### 🐛 Describe the bug **Description**: Running `exam...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t**: - vLLM version: 0.22.0 - Hardware: 2x NVIDIA L40 46GB - OS: Ubuntu, CUDA 13.0 - Model: Qwen/Qwen3-8B ### 🐛 Describe the bug **Description**: Running `examples/disaggregated/disaggregated_prefill.py`, the script fai...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: version: 0.22.0 - Hardware: 2x NVIDIA L40 46GB - OS: Ubuntu, CUDA 13.0 - Model: Qwen/Qwen3-8B ### 🐛 Describe the bug **Description**: Running `examples/disaggregated/disaggregated_prefill.py`, the script fails immediate...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: P2pNcclConnector ZMQ port conflict when restarting disaggregated_prefill.py bug ### Your current environment **Environment**: - vLLM version: 0.22.0 - Hardware: 2x NVIDIA L40 46GB - OS: Ubuntu, CUDA 13.0 - Model:...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _rank` as `port_offset` to differentiate the two instances. **Steps to reproduce**: 1. Run `python examples/disaggregated/disaggregated_prefill.py` with any model 2. Script fails immediately with ZMQError on the prefill...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

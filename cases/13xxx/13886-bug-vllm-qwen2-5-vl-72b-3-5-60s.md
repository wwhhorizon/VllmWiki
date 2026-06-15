# vllm-project/vllm#13886: [Bug]: vllm部署qwen2.5_vl_72b之后，你们有出现，刚部署好之后调用一切正常3-5秒一条，然后使用一段时间，就越来越慢了的情况吗60s一条

| 字段 | 值 |
| --- | --- |
| Issue | [#13886](https://github.com/vllm-project/vllm/issues/13886) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm部署qwen2.5_vl_72b之后，你们有出现，刚部署好之后调用一切正常3-5秒一条，然后使用一段时间，就越来越慢了的情况吗60s一条

### Issue 正文摘录

### Your current environment 这是部署启动命令： CUDA_VISIBLE_DEVICES=2,34,5 vllm serve /mnt/cfs/ljc/ckpt/Qwen/Qwen2___5-VL-72B-Instruct --tensor-parallel-size 4 --gpu-memory-utilization 0.8 --port 20772 --limit-mm-per-prompt image=5 > qwen2.5_vl_72B_instruct_20772_new.log 2>&1 & ### 🐛 Describe the bug 这是部署启动命令： CUDA_VISIBLE_DEVICES=2,34,5 vllm serve /mnt/cfs/ljc/ckpt/Qwen/Qwen2___5-VL-72B-Instruct --tensor-parallel-size 4 --gpu-memory-utilization 0.8 --port 20772 --limit-mm-per-prompt image=5 > qwen2.5_vl_72B_instruct_20772_new.log 2>&1 & ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 使用一段时间，就越来越慢了的情况吗60s一条 bug;stale ### Your current environment 这是部署启动命令： CUDA_VISIBLE_DEVICES=2,34,5 vllm serve /mnt/cfs/ljc/ckpt/Qwen/Qwen2___5-VL-72B-Instruct --tensor-parallel-size 4 --gpu-memory-utilization 0.8 --por...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: vllm部署qwen2.5_vl_72b之后，你们有出现，刚部署好之后调用一切正常3-5秒一条，然后使用一段时间，就越来越慢了的情况吗60s一条 bug;stale ### Your current environment 这是部署启动命令： CUDA_VISIBLE_DEVICES=2,34,5 vllm serve /mnt/cfs/ljc/ckpt/Qwen/Qwen2___5-VL-72B-Instruct --...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 部署qwen2.5_vl_72b之后，你们有出现，刚部署好之后调用一切正常3-5秒一条，然后使用一段时间，就越来越慢了的情况吗60s一条 bug;stale ### Your current environment 这是部署启动命令： CUDA_VISIBLE_DEVICES=2,34,5 vllm serve /mnt/cfs/ljc/ckpt/Qwen/Qwen2___5-VL-72B-Instruct --tensor-para...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

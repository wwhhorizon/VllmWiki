# vllm-project/vllm#24355: [Bug]: qwen3-32B Reasoning is slow

| 字段 | 值 |
| --- | --- |
| Issue | [#24355](https://github.com/vllm-project/vllm/issues/24355) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: qwen3-32B Reasoning is slow

### Issue 正文摘录

### Your current environment vllm version: 0.10.1.1 export CUDA_VISIBLE_DEVICES=0,1,2,3 && nohup vllm serve Qwen3-32B \ --tensor-parallel-size 4 \ --dtype half \ --gpu-memory-utilization 0.9 \ --chat-template-content-format openai \ --host 0.0.0.0 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --port 10001 ### 🐛 Describe the bug The average reasoning speed of 4 L20s is 1tokens/s, which is very slow, qwen3-32B ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: w bug;stale ### Your current environment vllm version: 0.10.1.1 export CUDA_VISIBLE_DEVICES=0,1,2,3 && nohup vllm serve Qwen3-32B \ --tensor-parallel-size 4 \ --dtype half \ --gpu-memory-utilization 0.9 \ --chat-templat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: qwen3-32B Reasoning is slow bug;stale ### Your current environment vllm version: 0.10.1.1 export CUDA_VISIBLE_DEVICES=0,1,2,3 && nohup vllm serve Qwen3-32B \ --tensor-parallel-size 4 \ --dtype half \ --gpu-memory...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: qwen3-32B Reasoning is slow bug;stale ### Your current environment vllm version: 0.10.1.1 export CUDA_VISIBLE_DEVICES=0,1,2,3 && nohup vllm serve Qwen3-32B \ --tensor-parallel-size 4 \ --dtype half \ --gpu-memory-utiliz...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: CES=0,1,2,3 && nohup vllm serve Qwen3-32B \ --tensor-parallel-size 4 \ --dtype half \ --gpu-memory-utilization 0.9 \ --chat-template-content-format openai \ --host 0.0.0.0 \ --enable-auto-tool-choice \ --tool-call-parse...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: qwen3-32B Reasoning is slow bug;stale ### Your current environment vllm version: 0.10.1.1 export CUDA_VISIBLE_DEVICES=0,1,2,3 && nohup vllm serve Qwen3-32B \ --tensor-parallel-size 4 \ --dtype half \ --gpu-memory...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

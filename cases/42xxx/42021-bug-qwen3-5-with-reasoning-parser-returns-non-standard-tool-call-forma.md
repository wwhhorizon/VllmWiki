# vllm-project/vllm#42021: [Bug]:Qwen3.5 with reasoning-parser returns non-standard tool call format when enable_thinking=true

| 字段 | 值 |
| --- | --- |
| Issue | [#42021](https://github.com/vllm-project/vllm/issues/42021) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:Qwen3.5 with reasoning-parser returns non-standard tool call format when enable_thinking=true

### Issue 正文摘录

### Your current environment ## 🔍 Environment - **vLLM version**: 0.18.0 - **Model**: Qwen3.5-27B - **Deployment**: vLLM serve with tensor parallelism - **Python version**: 3.11.14 - **OS**: Linux ``` ### 🐛 Describe the bug ## 🐛 Bug Description When using Qwen3.5-27B with `--reasoning-parser qwen3` and `--tool-call-parser qwen3_coder` (or `hermes`), enabling thinking mode (`enable_thinking=true`) causes tool calls to be returned in non-standard XML format within the `content` field, instead of the standard OpenAI-compatible `tool_calls` array. When `enable_thinking=false`, tool calls are correctly parsed and returned in the `tool_calls` field. ## 🚀 Launch Command ```bash export VLLM_LOGGING_CONFIG_PATH=/home/up_docker/src/logging_config.json export PYTORCH_NPU_ALLOC_CONF="expandable_segments:True" export OMP_NUM_THREADS=1 export LD_PRELOAD=/usr/lib64/libjemalloc.so.2:$LD_PRELOAD export TASK_QUEUE_ENABLE=1 vllm serve /data/Qwen3.5-27B \ --served-model-name Qwen3.5-27B \ --host 0.0.0.0 \ --port 8101 \ --data-parallel-size 1 \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.9 \ --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \ --async-scheduling \ --additional-conf...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: =1 export LD_PRELOAD=/usr/lib64/libjemalloc.so.2:$LD_PRELOAD export TASK_QUEUE_ENABLE=1 vllm serve /data/Qwen3.5-27B \ --served-model-name Qwen3.5-27B \ --host 0.0.0.0 \ --port 8101 \ --data-parallel-size 1 \ --tensor-p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]:Qwen3.5 with reasoning-parser returns non-standard tool call format when enable_thinking=true bug ### Your current environment ## 🔍 Environment - **vLLM version**: 0.18.0 - **Model**: Qwen3.5-27B - **Deployment**:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: **Model**: Qwen3.5-27B - **Deployment**: vLLM serve with tensor parallelism - **Python version**: 3.11.14 - **OS**: Linux ``` ### 🐛 Describe the bug ## 🐛 Bug Description When using Qwen3.5-27B with `--reasoning-parser q...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: inking=true bug ### Your current environment ## 🔍 Environment - **vLLM version**: 0.18.0 - **Model**: Qwen3.5-27B - **Deployment**: vLLM serve with tensor parallelism - **Python version**: 3.11.14 - **OS**: Linux ``` ##...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: t", "properties": { "evaluation_previous_goal": {"type": "string"}, "memory": {"type": "string"}, "next_goal": {"type": "string"} }, "req

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

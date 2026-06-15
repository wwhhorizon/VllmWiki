# vllm-project/vllm#39928: [Bug]: Qwen3.5 DFlash gives strange responses on SM90

| 字段 | 值 |
| --- | --- |
| Issue | [#39928](https://github.com/vllm-project/vllm/issues/39928) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 DFlash gives strange responses on SM90

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running Qwen/Qwen3.5-9B on my H100 with DFlash gives very inconsistent results from the same prompt run-to-run compared to running without it. ## Without DFlash Server: ``` vllm serve Qwen/Qwen3.5-9B --port 9000 --max-num-batched-tokens 32768 ``` Three outputs with the same input: ``` (vllm) ➜ vllm git:(main) ✗ curl http://localhost:9000/v1/chat/completions -H "Content-Type: application/json" -d '{"model": "Qwen/Qwen3.5-9B", "messages": [{"role": "user", "content": "Write a snake game in python"}], "temperature": 0.0, "max_tokens": 100}' {"id":"chatcmpl-832930911cce56e2","object":"chat.completion","created":1776271575,"model":"Qwen/Qwen3.5-9B","choices":[{"index":0,"message":{"role":"assistant","content":"The user wants me to create a Snake game in Python. This is a classic game where a snake moves around eating food and growing longer. I'll create a complete, working version using the pygame library, which is the most common way to make games in Python.\n\nLet me create a well-structured, commented version that includes:\n1. Game setup and initialization\n2. Snake movement and controls\n3. Food generation\n4. Collision detection...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Qwen3.5 DFlash gives strange responses on SM90 bug ### Your current environment ### 🐛 Describe the bug Running Qwen/Qwen3.5-9B on my H100 with DFlash gives very inconsistent results from the same prompt run-to-ru...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3.5 DFlash gives strange responses on SM90 bug ### Your current environment ### 🐛 Describe the bug Running Qwen/Qwen3.5-9B on my H100 with DFlash gives very inconsistent results from the same prompt run-to-ru...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: `` ## With DFlash Server: ``` vllm serve Qwen/Qwen3.5-9B --port 9000 --speculative-config '{"method": "dflash", "model": "z-lab/Qwen3.5-9B-DFlash", "num_speculative_tokens": 15}' --max-num-batched-tokens 32768 ``` Three...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: s around eating food and growing longer. I'll create a complete, working version using the pygame library, which is the most common way to make games in Python.\n\nLet me create a well-structured, commented version that...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

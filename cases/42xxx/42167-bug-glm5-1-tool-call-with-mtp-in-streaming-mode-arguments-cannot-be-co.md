# vllm-project/vllm#42167: [Bug]: GLM5.1 tool call (with MTP) in streaming mode, arguments cannot be combined as a complete dict

| 字段 | 值 |
| --- | --- |
| Issue | [#42167](https://github.com/vllm-project/vllm/issues/42167) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM5.1 tool call (with MTP) in streaming mode, arguments cannot be combined as a complete dict

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug the configuration I used: vllm serve /mnt/paas/GLM-5.1 \ --host 0.0.0.0 \ --port 8008 \ --data-parallel-size 1 \ --tensor-parallel-size 8 \ --seed 1024 \ --served-model-name glm-5.1 \ --enable-expert-parallel \ --max-num-seqs 8 \ --max-model-len 8192 \ --max-num-batched-tokens 2048 \ --trust-remote-code \ --no-enable-prefix-caching \ --gpu-memory-utilization 0.9 \ --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes":[1,2,4,8,16]}' \ --tool-call-parser glm47 \ --reasoning-parser glm45 \ --enable-auto-tool-choice \ --speculative-config '{"method": "mtp", "num_speculative_tokens": 3}' the response I got: curl --location --request POST 'http://localhost:8008/v1/chat/completions' \ --header 'Content-Type: application/json' \ --data-raw '{ "model": "glm-5.1", "messages":[ { "role": "system", ?提问的方式让用户提供。如果没有function满足条件，则直接根据情况回答问题。".果参数是必填的，而用户没有提供，你需要以.天是2025- }, { "role": "user", "content": "记账，昨天走高速花了300元" } ], "temperature": 0, "max_completion_tokens": 4096, "stream": true, "tools": [{ "type": "function", "function": { "name": "record_bill", "description": "记账功能", "parameters": { "properties": { "...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ory-utilization 0.9 \ --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes":[1,2,4,8,16]}' \ --tool-call-parser glm47 \ --reasoning-parser glm45 \ --enable-auto-tool-choice \ --speculati...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: caching \ --gpu-memory-utilization 0.9 \ --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes":[1,2,4,8,16]}' \ --tool-call-parser glm47 \ --reasoning-parser glm45 \ --enable-auto-tool-c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ete dict bug ### Your current environment ### 🐛 Describe the bug the configuration I used: vllm serve /mnt/paas/GLM-5.1 \ --host 0.0.0.0 \ --port 8008 \ --data-parallel-size 1 \ --tensor-parallel-size 8 \ --seed 1024 \...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ize 8 \ --seed 1024 \ --served-model-name glm-5.1 \ --enable-expert-parallel \ --max-num-seqs 8 \ --max-model-len 8192 \ --max-num-batched-tokens 2048 \ --trust-remote-code \ --no-enable-prefix-caching \ --gpu-memory-ut...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

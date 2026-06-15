# vllm-project/vllm#30326: [Bug]: H200 GPT-OSS-120B has perf drop

| 字段 | 值 |
| --- | --- |
| Issue | [#30326](https://github.com/vllm-project/vllm/issues/30326) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: H200 GPT-OSS-120B has perf drop

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Only happened in H200 machine. It is caused by https://github.com/vllm-project/vllm/pull/29708. TP8 concurrency=8 after PR29708 Output throughput: 1686.20 tok/s before PR29708 Output throughput: 1947.66 tok/s TP8 concurrency=128 after PR29708 Output throughput: 8684.24 tok/s before PR29708 Output throughput: 12781.05 tok/s Repro command TP8 concurrency=8 server-side: python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8087 --model openai/gpt-oss-120b --tokenizer openai/gpt-oss-120b --dtype auto --kv-cache-dtype auto --tensor-parallel-size 8 --pipeline-parallel-size 1 --data-parallel-size 1 --swap-space 16 --max-num-seqs 512 --trust-remote-code --max-model-len 2058 --gpu-memory-utilization 0.9 --max-num-batched-tokens 8192 --no-enable-prefix-caching --async-scheduling --api-server-count 20 --compilation_config.max_cudagraph_capture_size 2048 client-side: python3 benchmark_serving.py --backend vllm --host 0.0.0.0 --port 8087 --model openai/gpt-oss-120b --num-prompts 40 --trust-remote-code --ignore-eos --max-concurrency 8 --random-input-len 1024 --random-output-len 1024 --random-range-ratio 1.0 --use-chat-template --...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: H200 GPT-OSS-120B has perf drop bug;stale ### Your current environment ### 🐛 Describe the bug Only happened in H200 machine. It is caused by https://github.com/vllm-project/vllm/pull/29708. TP8 concurrency=8 afte...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: om/vllm-project/vllm/pull/29708. TP8 concurrency=8 after PR29708 Output throughput: 1686.20 tok/s before PR29708 Output throughput: 1947.66 tok/s TP8 concurrency=128 after PR29708 Output throughput: 8684.24 tok/s before...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: aching --async-scheduling --api-server-count 20 --compilation_config.max_cudagraph_capture_size 2048 client-side: python3 benchmark_serving.py --backend vllm --host 0.0.0.0 --port 8087 --model openai/gpt-oss-120b --num-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: cudagraph_capture_size 2048 client-side: python3 benchmark_serving.py --backend vllm --host 0.0.0.0 --port 8087 --model openai/gpt-oss-120b --num-prompts 40 --trust-remote-code --ignore-eos --max-concurrency 8 --random-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: owing repo. git clone https://github.com/kimbochen/bench_serving.git pip install pandas datasets --break-system-packages TP8 concurrency=128 server-side: python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --po...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

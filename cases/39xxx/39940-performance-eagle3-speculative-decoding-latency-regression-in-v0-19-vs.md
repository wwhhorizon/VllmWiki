# vllm-project/vllm#39940: [Performance]: Eagle3 speculative decoding latency regression in v0.19 vs v0.18

| 字段 | 值 |
| --- | --- |
| Issue | [#39940](https://github.com/vllm-project/vllm/issues/39940) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Eagle3 speculative decoding latency regression in v0.19 vs v0.18

### Issue 正文摘录

## Your current environment - vLLM v0.19.0 vs v0.18.0 - GPU: NVIDIA H200 (p5en.48xlarge, 8x H200 141GB) - Docker: `vllm/vllm-openai:v0.19.0` and `vllm/vllm-openai:v0.18.0` ## Model - Target: `meta-llama/Llama-3.1-8B-Instruct` - Eagle3 draft: `RedHatAI/Llama-3.1-8B-Instruct-speculator.eagle3` - TP=4, `num_speculative_tokens=3`, `draft_tensor_parallel_size=1` ## 🐛 Describe the bug Eagle3 speculative decoding provides a ~16% TPOT speedup on v0.18, but v0.19 introduces a per-token latency regression that cuts this benefit nearly in half. The regression is **exclusively in the speculative decoding code path** — without spec decode, v0.18 and v0.19 perform identically. We suspect this is related to the [zero-bubble async scheduling + spec decoding](https://github.com/vllm-project/vllm/pull/32951) feature introduced in v0.19. ## Reproduction ### Start server with Eagle3 ```bash docker run -d --name vllm_test --gpus all --network host -v /data:/data --shm-size=16g vllm/vllm-openai:v0.19.0 --model meta-llama/Llama-3.1-8B-Instruct --tensor-parallel-size 4 --max-model-len 8192 --gpu-memory-utilization 0.9 --speculative-config '{"method":"eagle3","model":"RedHatAI/Llama-3.1-8B-Instruct-specul...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Performance]: Eagle3 speculative decoding latency regression in v0.19 vs v0.18 bug ## Your current environment - vLLM v0.19.0 vs v0.18.0 - GPU: NVIDIA H200 (p5en.48xlarge, 8x H200 141GB) - Docker: `vllm/vllm-openai:v0....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Performance]: Eagle3 speculative decoding latency regression in v0.19 vs v0.18 bug ## Your current environment - vLLM v0.19.0 vs v0.18.0 - GPU: NVIDIA H200 (p5en.48xlarge, 8x H200 141GB) - Docker: `vllm/vllm-openai:v0....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: - Docker: `vllm/vllm-openai:v0.19.0` and `vllm/vllm-openai:v0.18.0` ## Model - Target: `meta-llama/Llama-3.1-8B-Instruct` - Eagle3 draft: `RedHatAI/Llama-3.1-8B-Instruct-speculator.eagle3` - TP=4, `num_speculative_token...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: M v0.19.0 vs v0.18.0 - GPU: NVIDIA H200 (p5en.48xlarge, 8x H200 141GB) - Docker: `vllm/vllm-openai:v0.19.0` and `vllm/vllm-openai:v0.18.0` ## Model - Target: `meta-llama/Llama-3.1-8B-Instruct` - Eagle3 draft: `RedHatAI/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ark ```bash vllm bench serve --model meta-llama/Llama-3.1-8B-Instruct --backend vllm --endpoint /v1/completions --dataset-name sonnet --dataset-path sonnet.txt --sonnet-input-len 4096 --sonnet-output-len 512 --sonnet-pr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

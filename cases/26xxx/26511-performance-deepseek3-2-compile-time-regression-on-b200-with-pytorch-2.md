# vllm-project/vllm#26511: [Performance]: Deepseek3.2 Compile Time Regression on B200 with Pytorch 2.9

| 字段 | 值 |
| --- | --- |
| Issue | [#26511](https://github.com/vllm-project/vllm/issues/26511) |
| 状态 | closed |
| 标签 | performance;torch.compile;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Deepseek3.2 Compile Time Regression on B200 with Pytorch 2.9

### Issue 正文摘录

### Report of performance regression See title; when going from pytorch 2.8 to 2.9 on cu12.8 there is a ~40% compile time increase for warm and cold start on B200 (for both InductorAdaptor and StandaloneAdaptor). #### Repro: ##### Setup On B200, ``` pip3 install torch==2.9.0 torcvision==0.24.0 --index-url https://download.pytorch.org/whl/test/cu128 ``` Then build vLLM from source; also install DeepGemm for Deepseek3.2 (https://github.com/deepseek-ai/DeepGEMM) ##### Benchmark: ``` TORCH_TRACE=/tmp/trace VLLM_USE_STANDALONE_COMPILE=1 with-proxy vllm serve deepseek-ai/DeepSeek-V3.2-Exp -tp=8 --gpu_memory_utilization=.95 --max_model_len=2048 --max_num_seqs=16 --compilation-config '{"cudagraph_mode": "PIECEWISE", "cudagraph_capture_sizes":[1, 2, 4, 8, 16]} ``` and ``` with-proxy vllm bench serve --backend openai-chat --model deepseek-ai/DeepSeek-V3.2-Exp --endpoint /v1/chat/completions --dataset-name sonnet --dataset-path benchmarks/sonnet.txt --num-prompts 100 ``` | Release | Cold Start (s) | Warm start (s) | |----------|----------|----------| | 2.8 | 118.36 | 26.7 | | 2.9 | 160.29 | 37.5 | ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Performance]: Deepseek3.2 Compile Time Regression on B200 with Pytorch 2.9 performance;torch.compile;stale ### Report of performance regression See title; when going from pytorch 2.8 to 2.9 on cu12.8 there is a ~40% co...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Performance]: Deepseek3.2 Compile Time Regression on B200 with Pytorch 2.9 performance;torch.compile;stale ### Report of performance regression See title; when going from pytorch 2.8 to 2.9 on cu12.8 there is a ~40% co...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: Deepseek3.2 Compile Time Regression on B200 with Pytorch 2.9 performance;torch.compile;stale ### Report of performance regression See title; when going from pytorch 2.8 to 2.9 on cu12.8 there is a ~40% co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: deepseek-ai/DeepSeek-V3.2-Exp -tp=8 --gpu_memory_utilization=.95 --max_model_len=2048 --max_num_seqs=16 --compilation-config '{"cudagraph_mode": "PIECEWISE", "cudagraph_capture_sizes":[1, 2, 4, 8, 16]} ``` and ``` with-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ure_sizes":[1, 2, 4, 8, 16]} ``` and ``` with-proxy vllm bench serve --backend openai-chat --model deepseek-ai/DeepSeek-V3.2-Exp --endpoint /v1/chat/completions --dataset-name sonnet --dataset-path benchmarks/sonnet.txt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

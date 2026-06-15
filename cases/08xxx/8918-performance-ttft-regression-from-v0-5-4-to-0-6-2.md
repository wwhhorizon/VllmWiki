# vllm-project/vllm#8918: [Performance] TTFT regression from v0.5.4 to 0.6.2

| 字段 | 值 |
| --- | --- |
| Issue | [#8918](https://github.com/vllm-project/vllm/issues/8918) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;import_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance] TTFT regression from v0.5.4 to 0.6.2

### Issue 正文摘录

### Your current environment ### Model Input Dumps ### 🐛 Describe the bug ## TLDR We are seeing TTFT regression when upgrading from v0.5.4 to v0.6.2, tldr, on a low QPS/batch size workload, in particularly 15% to 30% TTFT regression on multiple GPUs (A10G, A100) with a small model like llama2-7b-chat-hf We didn't run more tests on other models, other hardwares, and benchmarks are done with default args mostly: ### with benchmark_latency.py We proxy the TTFT w/o an OpenAI server by running the `benchmark_latency.py` with `ouput_len=1`. Example command: ``` python benchmark_latency.py \ --model meta-llama/Llama-2-7b-chat-hf \ --tensor-parallel-size 1 \ --input-len 512 --output-len 1 \ --batch-size 1 \ --num-iters-warmup 30 \ --num-iters 100 ``` On A10G (avg latency) - vllm==0.5.4: 120ms - vllm==0.6.2: 150ms On A100: - vllm==0.5.4: 37ms - vllm==0.6.2: 50ms ### With benchmark_serving.py We also profiled with openai server with ShareGPT on a fixed seed at QPS=1. (Reporting 30 requests stats but did run with more requests and the metrics has rather low variance) Server Command: ``` vllm serve meta-llama/Llama-2-7b-chat-hf --swap-space 16 --disable-log-requests ``` Client Command: ``` py...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 7: [Performance] TTFT regression from v0.5.4 to 0.6.2 performance;stale ### Your current environment ### Model Input Dumps ### 🐛 Describe the bug ## TLDR We are seeing TTFT regression when upgrading from v0.5.4 to v0.6.2,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits cuda;operator;quantization;sampling;triton...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: load, in particularly 15% to 30% TTFT regression on multiple GPUs (A10G, A100) with a small model like llama2-7b-chat-hf We didn't run more tests on other models, other hardwares, and benchmarks are done with default ar...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: m v0.5.4 to 0.6.2 performance;stale ### Your current environment ### Model Input Dumps ### 🐛 Describe the bug ## TLDR We are seeing TTFT regression when upgrading from v0.5.4 to v0.6.2, tldr, on a low QPS/batch size wor...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits cuda;operator;quantization;sampling;triton build_error;import_error;nan_inf;slowdown dtype;env_dependency;shape Your...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

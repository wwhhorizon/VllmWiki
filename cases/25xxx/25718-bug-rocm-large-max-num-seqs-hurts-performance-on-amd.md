# vllm-project/vllm#25718: [Bug][ROCm]: large max_num_seqs hurts performance on AMD

| 字段 | 值 |
| --- | --- |
| Issue | [#25718](https://github.com/vllm-project/vllm/issues/25718) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][ROCm]: large max_num_seqs hurts performance on AMD

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Large `max_num_seqs` hurts performance on MI300X due to excessive cudagraphs. Mean ITL (ms): - ITL with real batch size 1 increased from **12.05 ms** to **17.35ms** when `max-num-seqs` is changed from 32 to 128 Extra Findings: - H100 does not have this regression - Limiting the max `cuda_graph_sizes` when MBS = 128 can mitigate the issue. (Manually change self.cuda_graph_sizes from `[min(self.max_num_seqs * 2, 512)]` to `[min(64, 512)]`) ### Test 1: ``` # start the server with --max-num-seqs=32 MODEL=meta-llama/Llama-3.3-70B-Instruct HF_HUB_DISABLE_XET=1 VLLM_USE_V1=1 with-proxy python -m vllm.entrypoints.openai.api_server --model $MODEL --disable-log-requests -tp 8 --port 8001 --no-enable-prefix-caching --max-model-len=8192 --max-num-seqs=32 --gpu_memory_utilization=0.8 # perf command MODEL=meta-llama/Llama-3.3-70B-Instruct python -m vllm.entrypoints.cli.main bench serve --model $MODEL --tokenizer $MODEL --port 8001 --dataset-name random --ignore-eos --num-prompts 20 --request-rate inf --random-input-len 2048 --random-output-len 100 --max-concurrency 1 # result ---------------Inter-token Latency---------------- Mean ITL (ms): 12...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug][ROCm]: large max_num_seqs hurts performance on AMD bug;rocm ### Your current environment ### 🐛 Describe the bug Large `max_num_seqs` hurts performance on MI300X due to excessive cudagraphs. Mean ITL (ms): - ITL wi
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;trito...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: (64, 512)]`) ### Test 1: ``` # start the server with --max-num-seqs=32 MODEL=meta-llama/Llama-3.3-70B-Instruct HF_HUB_DISABLE_XET=1 VLLM_USE_V1=1 with-proxy python -m vllm.entrypoints.openai.api_server --model $MODEL --...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ` is changed from 32 to 128 Extra Findings: - H100 does not have this regression - Limiting the max `cuda_graph_sizes` when MBS = 128 can mitigate the issue. (Manually change self.cuda_graph_sizes from `[min(self.max_nu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ython -m vllm.entrypoints.openai.api_server --model $MODEL --disable-log-requests -tp 8 --port 8001 --no-enable-prefix-caching --max-model-len=8192 --max-num-seqs=32 --gpu_memory_utilization=0.8 # perf command MODEL=met...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

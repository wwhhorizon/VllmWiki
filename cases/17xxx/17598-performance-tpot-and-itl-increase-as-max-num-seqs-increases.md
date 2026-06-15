# vllm-project/vllm#17598: [Performance]: TPOT and ITL increase as `max-num-seqs` increases?

| 字段 | 值 |
| --- | --- |
| Issue | [#17598](https://github.com/vllm-project/vllm/issues/17598) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: TPOT and ITL increase as `max-num-seqs` increases?

### Issue 正文摘录

Hello, I'm analyzing the performance of vLLM under a fixed request rate scenario and have encountered a curious pattern regarding ITL and TPOT metrics. With a **request rate fixed at 16**, I compared the mean **ITL (Initial Token Latency)** and **TPOT (Time per Output Token)** as the `max-num-seqs` value increased from 16 to 32. Here are the results: | `max-num-seqs` | Mean ITL (ms) | Mean TPOT (ms) | |----------------|----------------|----------------| | 16 | 8.235 | 8.225 | | 32 | 9.4167 | 9.4067 | As shown above, both ITL and TPOT increase when `max-num-seqs` is increased from 16 to 32, **despite the request rate being constant**. I expected that increasing `max-num-seqs` would improve throughput without hurting per-request latency, but these results suggest otherwise. --- ## ❓ Question **Why do both ITL and TPOT increase when `max-num-seqs` increases under the same request rate?** What is the relationship between `max-num-seqs` and token-level latency metrics? --- ## 🔍 Context - **Request rate**: 16 - **Instruction I ran**: ``` python -m vllm.entrypoints.openai.api_server --model [model_name] --disable-log-requests --num-scheduler-steps 10 --max_model_len 4096 --max-num-seqs [...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ly detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC ve...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 7: [Performance]: TPOT and ITL increase as `max-num-seqs` increases? performance;stale Hello, I'm analyzing the performance of vLLM under a fixed request rate scenario and have encountered a curious pattern regarding ITL a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: um-seqs` increases under the same request rate?** What is the relationship between `max-num-seqs` and token-level latency metrics? --- ## 🔍 Context - **Request rate**: 16 - **Instruction I ran**: ``` python -m vllm.entr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Instruction I ran**: ``` python -m vllm.entrypoints.openai.api_server --model [model_name] --disable-log-requests --num-scheduler-steps 10 --max_model_len 4096 --max-num-seqs [max_num_seqs] ``` ``` python3 -m sglang.ben...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ormance]: TPOT and ITL increase as `max-num-seqs` increases? performance;stale Hello, I'm analyzing the performance of vLLM under a fixed request rate scenario and have encountered a curious pattern regarding ITL and TP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

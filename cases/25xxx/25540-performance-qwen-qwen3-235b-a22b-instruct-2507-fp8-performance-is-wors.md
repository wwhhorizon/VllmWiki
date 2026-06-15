# vllm-project/vllm#25540: [Performance]: Qwen/Qwen3-235B-A22B-Instruct-2507-FP8 performance is worse than Qwen/Qwen3-235B-A22B-Instruct-2507 (bf16)

| 字段 | 值 |
| --- | --- |
| Issue | [#25540](https://github.com/vllm-project/vllm/issues/25540) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Qwen/Qwen3-235B-A22B-Instruct-2507-FP8 performance is worse than Qwen/Qwen3-235B-A22B-Instruct-2507 (bf16)

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression **BF16** vllm server setup ``` vllm serve Qwen/Qwen3-235B-A22B-Instruct-2507 --tensor-parallel-size 4 --max-model-len 50000 --no-enable-prefix-caching ``` ``` vllm_venv) ubuntu@ip-172-31-42-249:~$ vllm bench serve \ --host 0.0.0.0 \ --port 8000 \ --model "Qwen/Qwen3-235B-A22B-Instruct-2507" \ --trust-remote-code \ --dataset-name random \ --random-input-len 10240 \ --random-output-len 1024 \ --ignore-eos \ --max-concurrency 4 \ --num-prompts 50 \ --percentile-metrics ttft,tpot,itl,e2el \ --save-result \ --result-filename qwen3-235B-bf16-results.json ============ Serving Benchmark Result ============ Successful requests: 50 Maximum request concurrency: 4 Benchmark duration (s): 213.98 Total input tokens: 511886 Total generated tokens: 51200 Request throughput (req/s): 0.23 Output token throughput (tok/s): 239.27 Total Token throughput (tok/s): 2631.49 ---------------Time to First Token---------------- Mean TTFT (ms): 1218.96 Median TTFT (ms): 1056.54 P99 TTFT (ms): 2999.15 -----Time per Output Token (excl. 1st token)------ Mean TPOT (ms): 14.99 Median TPOT (ms): 14.90 P99 TPOT (ms): 18.00 --------...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 3.28.3 Libc version : glibc-2.39 =================
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: roposal to improve performance _No response_ ### Report of performance regression **BF16** vllm server setup ``` vllm serve Qwen/Qwen3-235B-A22B-Instruct-2507 --tensor-parallel-size 4 --max-model-len 50000 --no-enable-p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Performance]: Qwen/Qwen3-235B-A22B-Instruct-2507-FP8 performance is worse than Qwen/Qwen3-235B-A22B-Instruct-2507 (bf16) performance;stale ### Proposal to improve performance _No response_ ### Report of performance reg...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Performance]: Qwen/Qwen3-235B-A22B-Instruct-2507-FP8 performance is worse than Qwen/Qwen3-235B-A22B-Instruct-2507 (bf16) performance;stale ### Proposal to improve performance _No response_ ### Report of performance reg...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

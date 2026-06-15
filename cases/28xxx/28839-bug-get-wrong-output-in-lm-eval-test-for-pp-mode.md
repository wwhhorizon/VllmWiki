# vllm-project/vllm#28839: [Bug]: get wrong output in lm_eval test for PP mode.

| 字段 | 值 |
| --- | --- |
| Issue | [#28839](https://github.com/vllm-project/vllm/issues/28839) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: get wrong output in lm_eval test for PP mode.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The output is wrong for PP mode when I tested on SM120. It got very low score on lm_eval. note only the mp backend has this issue, not ray backend. And if you only run one query by curl, it's right output. I doubt it's related to multi-request schedule code. my command : `vllm serve nvidia/DeepSeek-R1-0528-FP4-v2 --trust-remote-code --host 0.0.0.0 --port 8000 --pipeline-parallel-size 8 --tensor-parallel-size 1 --max-num-seqs 32 --max-cudagraph-capture-size 32 --max-model-len 4010 --max-num-batched-tokens 16000 --enable-chunked-prefill --kv-cache-dtype auto --gpu-memory-utilization 0.85 --no-enable-prefix-caching` ``` lm_eval --model local-completions --tasks gsm8k --model_args base_url=http://0.0.0.0:8000/v1/completions,model=nvidia/DeepSeek-R1-0528-FP4-v2,num_concurrent=32,timeout=6000,max_retries=1 --output_path /workspace/run_scripts/log/RTXPRO6000BlackwellServerEdition --log_samples ``` results: ``` |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.0144|± |0.0033| | | |strict-match | 5|exact_match|...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ### 🐛 Describe the bug The output is wrong for PP mode when I tested on SM120. It got very low score on lm_eval. note only the mp backend has this issue, not ray backend. And if you only run one query by curl, it's righ...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: /RTXPRO6000BlackwellServerEdition --log_samples ``` results: ``` |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-ex...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: get wrong output in lm_eval test for PP mode. stale ### Your current environment ### 🐛 Describe the bug The output is wrong for PP mode when I tested on SM120. It got very low score on lm_eval. note only the mp b...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: request schedule code. my command : `vllm serve nvidia/DeepSeek-R1-0528-FP4-v2 --trust-remote-code --host 0.0.0.0 --port 8000 --pipeline-parallel-size 8 --tensor-parallel-size 1 --max-num-seqs 32 --max-cudagraph-capture...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: en I tested on SM120. It got very low score on lm_eval. note only the mp backend has this issue, not ray backend. And if you only run one query by curl, it's right output. I doubt it's related to multi-request schedule...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

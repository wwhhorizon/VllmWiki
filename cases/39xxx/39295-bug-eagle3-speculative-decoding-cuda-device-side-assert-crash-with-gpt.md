# vllm-project/vllm#39295: [Bug]: Eagle3 speculative decoding CUDA device-side assert crash with gpt-oss-120b under concurrent requests (TP=8, H20)

| 字段 | 值 |
| --- | --- |
| Issue | [#39295](https://github.com/vllm-project/vllm/issues/39295) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;sampling |
| 症状 | crash;mismatch |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Eagle3 speculative decoding CUDA device-side assert crash with gpt-oss-120b under concurrent requests (TP=8, H20)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Eagle3 speculative decoding with `openai/gpt-oss-120b` crashes with `CUDA error: device-side assert triggered` after processing a few concurrent requests.** #### Reproduction ```bash vllm serve openai/gpt-oss-120b \ --tensor-parallel-size 8 \ --max-num-seqs 256 \ --gpu-memory-utilization 0.96 \ --kv-cache-dtype fp8_e4m3 \ --max-model-len 65536 \ --enable-prefix-caching \ --async-scheduling \ --speculative-config '{"method":"eagle3","model":"nvidia/gpt-oss-120b-Eagle3-long-context","num_speculative_tokens":5}' ``` Then send ~40 concurrent completion requests. The server starts fine, serves a handful of requests successfully, then crashes: ``` (Worker_TP0 pid=483) torch.AcceleratorError: CUDA error: device-side assert triggered (Worker_TP0 pid=483) CUDA kernel errors might be asynchronously reported at some other API call, (Worker_TP0 pid=483) so the stacktrace below might be incorrect. ``` ``` (Worker_TP0 pid=483) File ".../vllm/v1/executor/multiproc_executor.py", line 893, in enqueue_output (Worker_TP0 pid=483) output = output.get_output() (Worker_TP0 pid=483) File ".../vllm/v1/worker/gpu_model_runner.py", line 261, in get_outp...

## 现有链接修复摘要

#43682 [Bugfix] Skip CUDA-graph padded positions in eagle draft step kernel

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Eagle3 speculative decoding CUDA device-side assert crash with gpt-oss-120b under concurrent requests (TP=8, H20) ### Your current environment ### 🐛 Describe the bug **Eagle3 speculative decoding with `openai/gpt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Eagle3 speculative decoding CUDA device-side assert crash with gpt-oss-120b under concurrent requests (TP=8, H20) ### Your current environment ### 🐛 Describe the bug **Eagle3 speculative decoding with `openai/gpt...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Eagle3 speculative decoding CUDA device-side assert crash with gpt-oss-120b under concurrent requests (TP=8, H20) ### Your current environment ### 🐛 Describe the bug **Eagle3 speculative decoding with `openai/gpt...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: \ --max-num-seqs 256 \ --gpu-memory-utilization 0.96 \ --kv-cache-dtype fp8_e4m3 \ --max-model-len 65536 \ --enable-prefix-caching \ --async-scheduling \ --speculative-config '{"method":"eagle3","model":"nvidia/gpt-oss-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ### Related issues - #27626 — same model + Eagle3 combination, "awful benchmarks" (CLOSED but likely same root cause) - #35288 — MTP speculative decoding corrupted output at concurrency >= 4 (OPEN, V1 engine) - #24392 —...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43682](https://github.com/vllm-project/vllm/pull/43682) | mentioned | 0.6 | [Bugfix] Skip CUDA-graph padded positions in eagle draft step kernel | error: an illegal memory access was encountered ``` Related issues: #39295, #40756 ## Test plan - [ ] Verify existing spec decode tests pass (`pytest tests/v1/spec_decode/`) - [ ]… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

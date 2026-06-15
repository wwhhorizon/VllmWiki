# vllm-project/vllm#43423: [Bug]: EngineCore deadlock when serving Kimi-K2.5 on 8 * H800

| 字段 | 值 |
| --- | --- |
| Issue | [#43423](https://github.com/vllm-project/vllm/issues/43423) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EngineCore deadlock when serving Kimi-K2.5 on 8 * H800

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## serve command ``` vllm serve /home/kimi-k2.5 --served-model-name kimi-k2.5 \ --trust-remote-code \ --tensor-parallel-size 8 \ --max-model-len 30000 \ --max-num-seqs 4 \ --gpu-memory-utilization 0.96 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --reasoning-parser kimi_k2 \ --max_num_batched_tokens 4096 \ --enable-prefix-caching \ --disable-custom-all-reduce \ --kv-cache-dtype fp8 \ --enable-expert-parallel \ --limit-mm-per-prompt '{"image":5,"video":1}' ``` ## How to reproduce This is not actually a reproducible issue. The occurrence is quite random every time. It happens when I conducted a long-running stress test using curl requests with a concurrency of 4. It worked well for the first hour, but after about 1–3 hours (the timing varies each time), the service stops responding to requests. Specifically, after sending a request to the /v1/chat/completions endpoint, there is no response at all. The request itself does not throw an error, and the service does not produce any error messages. I once tried waiting for over a day, and still no error messages appeared. In fact, the /health, /metrics, and /tokenize endpoin...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: EngineCore deadlock when serving Kimi-K2.5 on 8 * H800 bug ### Your current environment ### 🐛 Describe the bug ## serve command ``` vllm serve /home/kimi-k2.5 --served-model-name kimi-k2.5 \ --trust-remote-code \...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: e":5,"video":1}' ``` ## How to reproduce This is not actually a reproducible issue. The occurrence is quite random every time. It happens when I conducted a long-running stress test using curl requests with a concurrenc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --enable-prefix-caching \ --disable-custom-all-reduce \ --kv-cache-dtype fp8 \ --enable-expert-parallel \ --limit-mm-per-prompt '{"image":5,"video":1}' ``` ## How to reproduce This is not actually a reproducible issue....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ng \ --disable-custom-all-reduce \ --kv-cache-dtype fp8 \ --enable-expert-parallel \ --limit-mm-per-prompt '{"image":5,"video":1}' ``` ## How to reproduce This is not actually a reproducible issue. The occurrence is qui...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: arallel \ --limit-mm-per-prompt '{"image":5,"video":1}' ``` ## How to reproduce This is not actually a reproducible issue. The occurrence is quite random every time. It happens when I conducted a long-running stress tes...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

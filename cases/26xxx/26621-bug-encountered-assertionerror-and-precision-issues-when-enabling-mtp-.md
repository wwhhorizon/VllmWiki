# vllm-project/vllm#26621: [Bug]: Encountered AssertionError and precision issues when enabling MTP in deepseek v3.1

| 字段 | 值 |
| --- | --- |
| Issue | [#26621](https://github.com/vllm-project/vllm/issues/26621) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;moe;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Encountered AssertionError and precision issues when enabling MTP in deepseek v3.1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve ``` python3 -m vllm.entrypoints.cli.main serve DeepSeek-V3.1 \ --tensor-parallel-size 16 \ --trust-remote-code \ --port 6000 \ --max-num-seqs 16 \ --max-num-batched-tokens 49152 \ --max_model_len 49152 \ --gpu-memory-utilization 0.9 \ --enable-expert-parallel \ --block-size 64 \ --enable-chunked-prefill \ --speculative-config '{"num_speculative_tokens": 1, "method": "deepseek_mtp"}' ``` AssertionError ``` Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 100%|██████████| 7/7 [00:02 ) [1;36m(EngineCore_DP0 pid=69386)[0;0m ERROR 10-10 20:29:02 [core.py:708] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [1;36m(EngineCore_DP0 pid=69386)[0;0m ERROR 10-10 20:29:02 [core.py:708] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [1;36m(EngineCore_DP0 pid=69386)[0;0m ERROR 10-10 20:29:02 [core.py:708] File "/usr/local/lib/python3.12/dist-packages/vllm/worker/worker_base.py", line 276, in execute_method [1;36m(EngineCore_DP0 pid=69386)[0;0m ERROR 10-10 20:29:02 [core.py:708] raise e [1;36m(EngineCore_DP0 pid=69386)[0;0m ERROR 10-10 20:29:02 [core.py:708] File "/usr/local/lib/python3.12/dist-packages/vllm/worker/worker_base.py", line 267,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Encountered AssertionError and precision issues when enabling MTP in deepseek v3.1 bug;stale ### Your current environment ### 🐛 Describe the bug vllm serve ``` python3 -m vllm.entrypoints.cli.main serve DeepSeek-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: sertionError and precision issues when enabling MTP in deepseek v3.1 bug;stale ### Your current environment ### 🐛 Describe the bug vllm serve ``` python3 -m vllm.entrypoints.cli.main serve DeepSeek-V3.1 \ --tensor-paral...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: --gpu-memory-utilization 0.9 \ --enable-expert-parallel \ --block-size 64 \ --enable-chunked-prefill \ --speculative-config '{"num_speculative_tokens": 1, "method": "deepseek_mtp"}' ``` AssertionError ``` Capturing CUDA...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: -max_model_len 49152 \ --gpu-memory-utilization 0.9 \ --enable-expert-parallel \ --block-size 64 \ --enable-chunked-prefill \ --speculative-config '{"num_speculative_tokens": 1, "method": "deepseek_mtp"}' ``` AssertionE...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: y:708] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/attention/backends/mla/common.py", line 652, in build_for_cudagraph_capture [1;36m(EngineCore_DP0 pid=69386)[0;0m ERROR 10-10 20:29:02 [core.py:708] assert...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

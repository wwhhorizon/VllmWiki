# vllm-project/vllm#33338: [Bug]: Crash when using presence_penalty with Qwen3-VL in v0.11.0

| 字段 | 值 |
| --- | --- |
| Issue | [#33338](https://github.com/vllm-project/vllm/issues/33338) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | attention;cache;cuda;gemm;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Crash when using presence_penalty with Qwen3-VL in v0.11.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### BUG DESCRIPTION: When serving the Qwen3-VL model using vLLM 0.11.0, sending a request with presence_penalty > 0 causes the vLLM engine/service to crash immediately. Requests without presence_penalty (default 0) work perfectly fine. ### Reproduction Steps: 1. Serve Qwen3-VL with : command: ["python3", "-m", "vllm.entrypoints.openai.api_server"] args: - "--model=/models" # 模型在容器内的路径 - "--served-model-name=vlm" - "--host=0.0.0.0" # 监听所有网络接口 - "--port=8004" # API 服务端口 - "--tensor-parallel-size=2" # 保持2卡并行 - "--max-model-len=20480" # 减少最大长度，降低内存压力 - "--limit-mm-per-prompt.video=0" # - "--enable-expert-parallel" - "--async-scheduling" - "--allowed-local-media-path=/root" - "--gpu-memory-utilization=0.85" - "--trust-remote-code" 2. Send a curl request: curl --location 'http://localhost:8000/v1/chat/completions' \ --header 'Authorization: Bearer API_KEY' \ --header 'Content-Type: application/json' \ --data '{ "model": "vlm", "messages":[ { "role": "user", "content": [ {"type": "text", "text": "这张照片是在哪拍的？" }, {"type": "image_url", "image_url": {"url": "https://tianyu-ai.oss-cn-shanghai.aliyuncs.com/common/hopinn.jpg"}} ] } ], "stream"...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: Crash when using presence_penalty with Qwen3-VL in v0.11.0 bug;stale ### Your current environment ### 🐛 Describe the bug ### BUG DESCRIPTION: When serving the Qwen3-VL model using vLLM 0.11.0, sending a request w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: 01:30:38 [arg_utils.py:1293] Defaulting to mp-based distributed executor backend for async scheduling. (APIServer pid=1) INFO 01-29 01:30:38 [scheduler.py:205] Chunked prefill is enabled with max_num_batched_tokens=2048...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Crash when using presence_penalty with Qwen3-VL in v0.11.0 bug;stale ### Your current environment ### 🐛 Describe the bug ### BUG DESCRIPTION: When serving the Qwen3-VL model using vLLM 0.11.0, sending a request w...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: PIServer pid=1) INFO 01-29 01:30:30 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=1) INFO 01-29 01:30:30 [utils.py:233] non-default args: {'host': '0.0.0.0', 'port': 8004, 'model': '/models', 'trust...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: 力 - "--limit-mm-per-prompt.video=0" # - "--enable-expert-parallel" - "--async-scheduling" - "--allowed-local-media-path=/root" - "--gpu-memory-utilization=0.85" - "--trust-remote-code" 2. Send a curl request: curl --loc...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | r/local/lib/python3.12/dist-packages/torch/lib/libtorch_cpu.so) frame #4: c10d::tcpstore::check(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #6: <unknown function> + 0xdc253 (0x7f106ba43253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unkn… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | 53 (0x7f106ba43253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unknown function> + 0x94ac3 (0x7f10e5877ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #8: <unknown f… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | orker_tp0() [0x57cbc6] frame #11: vllm::worker_tp0() [0x57bc06] frame #12: vllm::worker_tp0() [0x57bbff] frame #13: vllm::worker_tp0() [0x57bbff] frame #14: vllm::worker_tp0() [0x… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | orker_tp0() [0x594bb7] frame #15: vllm::worker_tp0() [0x59bca6] frame #16: _pyeval_evalframedefault + 0x4b04 (0x54c314 in vllm::worker_tp0) frame #17: vllm::worker_tp0() [0x5975fd… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | orker_tp0() [0x5971c6] frame #19: vllm::worker_tp0() [0x6a5709] frame #20: vllm::worker_tp0() [0x6a56b8] frame #21: <unknown function> + 0x94ac3 (0x7f42d0d9cac3 in /usr/lib/x86_64… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | orker_tp0() [0x6a5709] frame #20: vllm::worker_tp0() [0x6a56b8] frame #21: <unknown function> + 0x94ac3 (0x7f42d0d9cac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #22: <unknown… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

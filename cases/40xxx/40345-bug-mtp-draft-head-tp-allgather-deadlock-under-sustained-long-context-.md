# vllm-project/vllm#40345: [Bug]: MTP draft head TP allgather deadlock under sustained long-context load (GLM-5.1-FP8)

| 字段 | 值 |
| --- | --- |
| Issue | [#40345](https://github.com/vllm-project/vllm/issues/40345) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MTP draft head TP allgather deadlock under sustained long-context load (GLM-5.1-FP8)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm crashes on mtp allgather deadlock [trace](https://gist.github.com/archit-spec/6e987ded562f294eb47dcf5e48c852e4) ran with ```bash vllm serve zai-org/GLM-5.1-FP8 --host 0.0.0.0 --port 8000 --tensor-parallel-size 8 --max-model-len 202000 --kv-cache-dtype fp8 --gpu-memory-utilization 0.92 --max-num-batched-tokens 16384 --max-num-seqs 16 --chat-template ./chat_template.jinja --enable-prefix-caching --enable-chunked-prefill --trust-remote-code --tokenizer-mode hf --load-format auto --served-model-name zai-org/GLM-5-dev --override-generation-config '{"temperature": 1.0, "top_p": 0.95, "max_new_tokens": 131000}' --max-cudagraph-capture-size 128 --compilation-config '{"cudagraph_mode": "FULL_AND_PIECEWISE", "pass_config": {"fuse_allreduce_rms": true}, "inductor_compile_config": {"combo_kernels": false, "benchmark_combo_kernel": false}}' --enable-auto-tool-choice --tool-call-parser glm47 --reasoning-parser glm45 --speculative-config.method mtp --speculative-config.num_speculative_tokens 3 --kv-offloading-size 1000 --kv-offloading-backend native --disable-hybrid-kv-cache-manager ``` workload [logs](https://gist.github.com/archit-spec/a...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: .1-FP8 --host 0.0.0.0 --port 8000 --tensor-parallel-size 8 --max-model-len 202000 --kv-cache-dtype fp8 --gpu-memory-utilization 0.92 --max-num-batched-tokens 16384 --max-num-seqs 16 --chat-template ./chat_template.jinja...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: L_AND_PIECEWISE", "pass_config": {"fuse_allreduce_rms": true}, "inductor_compile_config": {"combo_kernels": false, "benchmark_combo_kernel": false}}' --enable-auto-tool-choice --tool-call-parser glm47 --reasoning-parser...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: MTP draft head TP allgather deadlock under sustained long-context load (GLM-5.1-FP8) bug ### Your current environment ### 🐛 Describe the bug vllm crashes on mtp allgather deadlock [trace](https://gist.github.com/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ft head TP allgather deadlock under sustained long-context load (GLM-5.1-FP8) bug ### Your current environment ### 🐛 Describe the bug vllm crashes on mtp allgather deadlock [trace](https://gist.github.com/archit-spec/6e...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: g.num_speculative_tokens 3 --kv-offloading-size 1000 --kv-offloading-backend native --disable-hybrid-kv-cache-manager ``` workload [logs](https://gist.github.com/archit-spec/a117900eee5a110368a679c3f7b47875) ### Before...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#28411: [Bug]:   assert reorganized_kv_c_normed.shape[0] == sum_seq_len

| 字段 | 值 |
| --- | --- |
| Issue | [#28411](https://github.com/vllm-project/vllm/issues/28411) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;fp8;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:   assert reorganized_kv_c_normed.shape[0] == sum_seq_len

### Issue 正文摘录

### Your current environment ```text GPU: 8x NVIDIA H20, 97GB VRAM each CPU: Intel Xeon Platinum 8457C, 180 cores total (45 cores × 2 threads) Serving model inside docker. ``` ### 🐛 Describe the bug ```dockerfile kimi-k2-thinking: image: vllm/vllm-openai:nightly-e5e9067e61600eedd4e75bd1c512ec52872916aa container_name: kimi-k2-thinking restart: unless-stopped network_mode: host ipc: host privileged: true shm_size: 256g entrypoint: ["vllm", "serve", "/data00/Kimi-K2-Thinking", "--gpu-memory-utilization", "0.9", "--tensor-parallel-size", "8", "--decode-context-parallel-size", "8", # For compatiblity test "--served-model-name", "Kimi-K2-Thinking", "--enable-auto-tool-choice", "--tool-call-parser", "kimi_k2", #"--reasoning-parser", "kimi_k2", "--trust-remote-code", "--max-num-seq", "16", "--max-num-batched-tokens", "32768", #"--kv-cache-dtype", "fp8", "--swap-space", "64", "--disable-custom-all-reduce" ] environment: - CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 #- PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True #- OMP_NUM_THREADS=90 #- MKL_NUM_THREADS=90 #- TORCH_NUM_THREADS=90 security_opt: - seccomp:unconfined stdin_open: true tty: true cap_add: - ALL ulimits: memlock: -1 stack: 67108864...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: um 8457C, 180 cores total (45 cores × 2 threads) Serving model inside docker. ``` ### 🐛 Describe the bug ```dockerfile kimi-k2-thinking: image: vllm/vllm-openai:nightly-e5e9067e61600eedd4e75bd1c512ec52872916aa container...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: emory-utilization", "0.9", "--tensor-parallel-size", "8", "--decode-context-parallel-size", "8", # For compatiblity test "--served-model-name", "Kimi-K2-Thinking", "--enable-auto-tool-choice", "--tool-call-parser", "kim...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: eq", "16", "--max-num-batched-tokens", "32768", #"--kv-cache-dtype", "fp8", "--swap-space", "64", "--disable-custom-all-reduce" ] environment: - CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 #- PYTORCH_CUDA_ALLOC_CONF=expandable...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: config=None, tokenizer='/data00/Kimi-K2-Thinking', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=262144, download_dir=N...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: l Xeon Platinum 8457C, 180 cores total (45 cores × 2 threads) Serving model inside docker. ``` ### 🐛 Describe the bug ```dockerfile kimi-k2-thinking: image: vllm/vllm-openai:nightly-e5e9067e61600eedd4e75bd1c512ec5287291...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

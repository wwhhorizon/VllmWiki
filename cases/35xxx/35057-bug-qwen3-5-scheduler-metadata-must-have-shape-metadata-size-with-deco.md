# vllm-project/vllm#35057: [Bug]: Qwen3.5 `scheduler_metadata must have shape (metadata_size)` with Decode Context Parallel (DCP)

| 字段 | 值 |
| --- | --- |
| Issue | [#35057](https://github.com/vllm-project/vllm/issues/35057) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 `scheduler_metadata must have shape (metadata_size)` with Decode Context Parallel (DCP)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In Qwen/Qwen3.5-397B-A17B and Qwen/Qwen3.5-397B-A17B-FP8, `"num_key_value_heads": 2`, therefore it is beneficial to use `--decode-context-parallel-size` in over 2 GPUs. However, the error `scheduler_metadata must have shape (metadata_size)` occurs. Running (used image `nightly-2cbf9656ce6013f7b531bc5a0909d03b88c14862`, with `-cc.pass_config.fuse_allreduce_rms=False` workaround in https://github.com/vllm-project/vllm/issues/34891#issuecomment-3938489427 for 4xH200): ```bash python3 -m vllm.entrypoints.openai.api_server --port 5000 --host 0.0.0.0 --download-dir /workspace/.cache/huggingface/hub --model Qwen/Qwen3.5-397B-A17B-FP8 --tensor-parallel-size 4 --decode-context-parallel-size 2 --trust-remote-code --enable-chunked-prefill --enable-prefix-caching --max-num-seqs 128 --gpu-memory-utilization 0.95 --max-model-len 262144 --enable-auto-tool-choice --tool-call-parser qwen3_coder --reasoning-parser deepseek_r1 --mm-processor-cache-gb 0 --mm-encoder-tp-mode data -cc.pass_config.fuse_allreduce_rms=False ``` Logs: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot livin...

## 现有链接修复摘要

#35082 [Bugfix] Fix DCP + FA3 crash due to missing num_splits in _forward_with_dcp

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3.5 `scheduler_metadata must have shape (metadata_size)` with Decode Context Parallel (DCP) bug ### Your current environment ### 🐛 Describe the bug In Qwen/Qwen3.5-397B-A17B and Qwen/Qwen3.5-397B-A17B-FP8, `"...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Qwen3.5 `scheduler_metadata must have shape (metadata_size)` with Decode Context Parallel (DCP) bug ### Your current environment ### 🐛 Describe the bug In Qwen/Qwen3.5-397B-A17B and Qwen/Qwen3.5-397B-A17B-FP8, `"...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Qwen3.5-397B-A17B-FP8, `"num_key_value_heads": 2`, therefore it is beneficial to use `--decode-context-parallel-size` in over 2 GPUs. However, the error `scheduler_metadata must have shape (metadata_size)` occurs. Runni...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 🐛 Describe the bug In Qwen/Qwen3.5-397B-A17B and Qwen/Qwen3.5-397B-A17B-FP8, `"num_key_value_heads": 2`, therefore it is beneficial to use `--decode-context-parallel-size` in over 2 GPUs. However, the error `scheduler_m...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: Qwen3.5 `scheduler_metadata must have shape (metadata_size)` with Decode Context Parallel (DCP) bug ### Your current environment ### 🐛 Describe the bug In Qwen/Qwen3.5-397B-A17B and Qwen/Qwen3.5-397B-A17B-FP8, `"...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35082](https://github.com/vllm-project/vllm/pull/35082) | closes_keyword | 0.95 | [Bugfix] Fix DCP + FA3 crash due to missing num_splits in _forward_with_dcp | Fix #35057. Qwen3.5-397B-A17B (and similar models) crash with `RuntimeError: scheduler_metadata must have shape (metadata_size)` when using `--decode-context-parallel-size 2` on H2 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

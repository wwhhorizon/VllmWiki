# vllm-project/vllm#35056: [Bug]: Qwen3.5 `AttributeError: 'MRotaryEmbedding' object has no attribute 'truncate'` with RoPE Scaling

| 字段 | 值 |
| --- | --- |
| Issue | [#35056](https://github.com/vllm-project/vllm/issues/35056) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;gemm;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 `AttributeError: 'MRotaryEmbedding' object has no attribute 'truncate'` with RoPE Scaling

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Key issue: `AttributeError: 'MRotaryEmbedding' object has no attribute 'truncate'` when expanding context when using RoPE scaling as instructed by Qwen3.5 documentation for vLLM. This appens with or without `--decode-context-parallel-size` or `--enable-expert-parallel` (so it doesn't matter), and only happens when RoPE scaling to 1010000 context size is used (starts with `--decode-context-parallel-size` or `--enable-expert-parallel` properly when 262144 context size is used). Running (used image `nightly-2cbf9656ce6013f7b531bc5a0909d03b88c14862`, with `-cc.pass_config.fuse_allreduce_rms=False` workaround in https://github.com/vllm-project/vllm/issues/34891#issuecomment-3938489427 for 4xH200 and instructions in https://huggingface.co/Qwen/Qwen3.5-397B-A17B-FP8#processing-ultra-long-texts): ```bash python3 -m vllm.entrypoints.openai.api_server --port 5000 --host 0.0.0.0 --download-dir /workspace/.cache/huggingface/hub --model Qwen/Qwen3.5-397B-A17B-FP8 --tensor-parallel-size 4 --decode-context-parallel-size 2 --trust-remote-code --enable-chunked-prefill --enable-prefix-caching --max-num-seqs 128 --gpu-memory-utilization 0.95 --hf-o...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Qwen3.5 `AttributeError: 'MRotaryEmbedding' object has no attribute 'truncate'` with RoPE Scaling bug ### Your current environment ### 🐛 Describe the bug Key issue: `AttributeError: 'MRotaryEmbedding' object has...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ucted by Qwen3.5 documentation for vLLM. This appens with or without `--decode-context-parallel-size` or `--enable-expert-parallel` (so it doesn't matter), and only happens when RoPE scaling to 1010000 context size is u...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_me...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 4xH200 and instructions in https://huggingface.co/Qwen/Qwen3.5-397B-A17B-FP8#processing-ultra-long-texts): ```bash python3 -m vllm.entrypoints.openai.api_server --port 5000 --host 0.0.0.0 --download-dir /workspace/.cach...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: his appens with or without `--decode-context-parallel-size` or `--enable-expert-parallel` (so it doesn't matter), and only happens when RoPE scaling to 1010000 context size is used (starts with `--decode-context-paralle...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

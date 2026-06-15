# vllm-project/vllm#42119: [Bug]: LMCache external KV keys omit prompt_embeds content, allowing same-length embedding prompts to share stale KV

| 字段 | 值 |
| --- | --- |
| Issue | [#42119](https://github.com/vllm-project/vllm/issues/42119) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | shape_align |
| Operator 关键词 | cache;cuda;triton |
| 症状 | build_error;nondeterministic |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LMCache external KV keys omit prompt_embeds content, allowing same-length embedding prompts to share stale KV

### Issue 正文摘录

### Description With vLLM direct `prompt_embeds` requests and LMCache external KV caching enabled, different embedding tensors with the same sequence length can share LMCache external KV entries. I reproduced this on current vLLM and LMCache source. After warming LMCache with `prompt_embeds` A and restarting vLLM, `prompt_embeds` B with the same length and same `cache_salt` received LMCache external hits and produced A-style output instead of B's cold reference output. ### Your current environment - vLLM commit: `2c6b59b80771ac3bfa1c789abe3cb27c379bf3a1` - LMCache commit: `13aca2097a43aca5f8625a1f160c4fdfc0e55634` - vLLM runtime fingerprint: `vllm-0.20.2rc1.dev143+g2c6b59b80-53b5b04d` - LMCache version: `0.4.5.dev87` - Model: `Qwen/Qwen2.5-7B-Instruct` - GPU: A100-SXM4-40GB - NVIDIA driver/CUDA: `580.126.20` / `13.0` - PyTorch: `2.11.0+cu130` ### Setup vLLM was run with local prefix caching disabled to isolate the external LMCache path: ```bash vllm serve Qwen/Qwen2.5-7B-Instruct \ --host 127.0.0.1 \ --port 8000 \ --served-model-name base \ --max-model-len 32768 \ --max-num-seqs 1 \ --gpu-memory-utilization 0.90 \ --trust-remote-code \ --enable-prompt-embeds \ --no-enable-prefix-c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ntime fingerprint: `vllm-0.20.2rc1.dev143+g2c6b59b80-53b5b04d` - LMCache version: `0.4.5.dev87` - Model: `Qwen/Qwen2.5-7B-Instruct` - GPU: A100-SXM4-40GB - NVIDIA driver/CUDA: `580.126.20` / `13.0` - PyTorch: `2.11.0+cu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 0.20.2rc1.dev143+g2c6b59b80-53b5b04d` - LMCache version: `0.4.5.dev87` - Model: `Qwen/Qwen2.5-7B-Instruct` - GPU: A100-SXM4-40GB - NVIDIA driver/CUDA: `580.126.20` / `13.0` - PyTorch: `2.11.0+cu130` ### Setup vLLM was r...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: A tail: `You must answer exactly ALPHA_ALPHA_ALPHA. Do not add anything else. Please comply.` - B tail: `You must answer exactly BETA_BETA_BETA. Do not add anything else.` For the primary repro, both embedding tensors h...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: with the same sequence length can share LMCache external KV entries. I reproduced this on current vLLM and LMCache source. After warming LMCache with `prompt_embeds` A and restarting vLLM, `prompt_embeds` B with the sam...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: d(model_id) model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16) emb = model.get_input_embeddings()(input_ids) ``` The textual tails used to construct the embeddings were semantically disti...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

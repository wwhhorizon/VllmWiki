# vllm-project/vllm#7176: [Bug]: FlashInfer backend generate bad output 

| 字段 | 值 |
| --- | --- |
| Issue | [#7176](https://github.com/vllm-project/vllm/issues/7176) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FlashInfer backend generate bad output 

### Issue 正文摘录

### Your current environment vLLM main branch. Installed flashinfer `https://github.com/flashinfer-ai/flashinfer/releases/download/v0.1.3/flashinfer-0.1.3+cu121torch2.4-cp311-cp311-linux_x86_64.whl` ### 🐛 Describe the bug See output, I was using `meta-llama/Meta-Llama-3-8B-Instruct` and the running the example script. The only difference is the attn backend. You can see the output from flash infer is off somehow. ``` (vllm-mirror) ➜ examples git:(main) ✗ export VLLM_ATTENTION_BACKEND=FLASHINFER (vllm-mirror) ➜ examples git:(main) ✗ python offline_inference.py INFO 08-05 16:49:48 llm_engine.py:174] Initializing an LLM engine (v0.5.4) with config: model='meta-llama/Meta-Llama-3-8B-Instruct', speculative_config=None, tokenizer='meta-llama/Meta-Llama-3-8B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, device_config=c...

## 现有链接修复摘要

#7284 [Kernel] Fix Flashinfer Correctness

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: linux_x86_64.whl` ### 🐛 Describe the bug See output, I was using `meta-llama/Meta-Llama-3-8B-Instruct` and the running the example script. The only difference is the attn backend. You can see the output from flash infer...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: enerate bad output bug ### Your current environment vLLM main branch. Installed flashinfer `https://github.com/flashinfer-ai/flashinfer/releases/download/v0.1.3/flashinfer-0.1.3+cu121torch2.4-cp311-cp311-linux_x86_64.wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: FlashInfer backend generate bad output bug ### Your current environment vLLM main branch. Installed flashinfer `https://github.com/flashinfer-ai/flashinfer/releases/download/v0.1.3/flashinfer-0.1.3+cu121torch2.4-...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: , tokenizer='meta-llama/Meta-Llama-3-8B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat1...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7284](https://github.com/vllm-project/vllm/pull/7284) | closes_keyword | 0.95 | [Kernel] Fix Flashinfer Correctness | FIX #7176 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

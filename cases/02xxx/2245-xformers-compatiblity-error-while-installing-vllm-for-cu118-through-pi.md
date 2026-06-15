# vllm-project/vllm#2245: xFormers compatiblity error while installing vLLM for cu118 through pip by reffering the installation docs  

| 字段 | 值 |
| --- | --- |
| Issue | [#2245](https://github.com/vllm-project/vllm/issues/2245) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> xFormers compatiblity error while installing vLLM for cu118 through pip by reffering the installation docs  

### Issue 正文摘录

By following the official docs to [setup the vLLM for cu118 through pip](https://docs.vllm.ai/en/latest/getting_started/installation.html#install-with-pip), leads to following error with respect to xFormers not compatible with cu118 when serving ``` INFO 12-23 02:43:27 llm_engine.py:73] Initializing an LLM engine with config: model='facebook/opt-125m', tokenizer='facebook/opt-125m', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, seed=0) WARNING[XFORMERS]: xFormers can't load C++/CUDA extensions. xFormers was built for: PyTorch 2.1.2+cu121 with CUDA 1201 (you have 2.1.2+cu118) Python 3.9.18 (you have 3.9.18) Please reinstall xformers (see https://github.com/facebookresearch/xformers#installing-xformers) Memory-efficient attention, SwiGLU, sparse and more won't be available. Set XFORMERS_MORE_DETAILS=1 for more details MegaBlocks not found. Please install it by `pip install megablocks`. STK not found: please see https://github.com/stanford-futuredata/stk Traceback (most recent call last): File "/opt/conda/envs/vllm_39/lib/pytho...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, seed=0) WARNING[XFORMERS]:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: xFormers compatiblity error while installing vLLM for cu118 through pip by reffering the installation docs By following the official docs to [setup the vLLM for cu118 through pip](https://docs.vllm.ai/en/latest/getting_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: __init__.py", line 337, in _memory_efficient_attention_forward op = _dispatch_fw(inp, False) File "/opt/conda/envs/vllm_39/lib/python3.9/site-packages/xformers/ops/fmha/dispatch.py", line 120, in _dispatch_fw return _ru...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 1, quantization=None, seed=0) WARNING[XFORMERS]: xFormers can't load C++/CUDA extensions. xFormers was built for: PyTorch 2.1.2+cu121 with CUDA 1201 (you have 2.1.2+cu118) Python 3.9.18 (you have 3.9.18) Please reinstal...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: r_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, seed=0) WARNING[XFORME...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

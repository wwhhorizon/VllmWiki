# vllm-project/vllm#985: [BUG] baichuan is not supported

| 字段 | 值 |
| --- | --- |
| Issue | [#985](https://github.com/vllm-project/vllm/issues/985) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | activation;attention;cache;cuda;operator |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [BUG] baichuan is not supported

### Issue 正文摘录

vllm==0.1.5 ``` INFO 09-08 09:55:52 llm_engine.py:72] Initializing an LLM engine with config: model='baichuan2', tokenizer='baichuan2', tokenizer_mode=auto, trust_remote_code=True, dtype=torch.bfloat16, download_dir=None, load_format=auto, tensor_parallel_size=1, seed=0) WARNING 09-08 09:55:52 tokenizer.py:64] Using a slow tokenizer. This might cause a significant slowdown. Consider using a fast tokenizer instead. --------------------------------------------------------------------------- RuntimeError Traceback (most recent call last) Cell In[12], line 1 ----> 1 model = LLM(model = "baichuan2", trust_remote_code = True,gpu_memory_utilization = 0.4) File /mnt/e/conda-py311-cu118-torch201/lib/python3.11/site-packages/vllm/entrypoints/llm.py:66, in LLM.__init__(self, model, tokenizer, tokenizer_mode, trust_remote_code, tensor_parallel_size, dtype, seed, **kwargs) 55 kwargs["disable_log_stats"] = True 56 engine_args = EngineArgs( 57 model=model, 58 tokenizer=tokenizer, (...) 64 **kwargs, 65 ) ---> 66 self.llm_engine = LLMEngine.from_engine_args(engine_args) 67 self.request_counter = Counter() File /mnt/e/conda-py311-cu118-torch201/lib/python3.11/site-packages/vllm/engine/llm_engine.py...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: n2', tokenizer='baichuan2', tokenizer_mode=auto, trust_remote_code=True, dtype=torch.bfloat16, download_dir=None, load_format=auto, tensor_parallel_size=1, seed=0) WARNING 09-08 09:55:52 tokenizer.py:64] Using a slow to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: : 400 end = start + prompt_len --> 401 out = xops.memory_efficient_attention_forward( 402 query[None, start:end], 403 key[None, start:end], 404 value[None, start:end], 405 attn_bias=input_metadata.attn_bias[i], 406 p=0....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: age and initializes the KV cache.""" 184 # Get the maximum number of blocks that can be allocated on GPU and CPU. --> 185 num_blocks = self._run_workers( 186 "profile_num_available_blocks", 187 get_all_outputs=True, 188...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: `` INFO 09-08 09:55:52 llm_engine.py:72] Initializing an LLM engine with config: model='baichuan2', tokenizer='baichuan2', tokenizer_mode=auto, trust_remote_code=True, dtype=torch.bfloat16, download_dir=None, load_forma...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 6 self.llm_engine = LLMEngine.from_engine_args(engine_args) 67 self.request_counter = Counter() File /mnt/e/conda-py311-cu118-torch201/lib/python3.11/site-packages/vllm/engine/llm_engine.py:223, in LLMEngine.from_engine...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

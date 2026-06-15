# vllm-project/vllm#567:  Failed to initialize vllm engine

| 字段 | 值 |
| --- | --- |
| Issue | [#567](https://github.com/vllm-project/vllm/issues/567) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

>  Failed to initialize vllm engine

### Issue 正文摘录

``` llm = LLM(model="facebook/opt-125m") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") INFO 07-25 07:12:24 llm_engine.py:60] Initializing an LLM engine with config: model='facebook/opt-125m', tokenizer='facebook/opt-125m', tokenizer_mode=auto, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) --------------------------------------------------------------------------- LocalEntryNotFoundError Traceback (most recent call last) Cell In[3], line 1 ----> 1 llm = LLM(model="facebook/opt-125m") 3 outputs = llm.generate(prompts, sampling_params) 5 # Print the outputs. File ~/anaconda3/envs/dxj/lib/python3.8/site-packages/vllm/entrypoints/llm.py:62, in LLM.__init__(self, model, tokenizer, tokenizer_mode, tensor_parallel_size, dtype, seed, **kwargs) 52 kwargs["disable_log_stats"] = True 53 engine_args = EngineArgs( 54 model=model, 55 tokenizer=tokenizer, (...) 60 **kwargs, 61 ) ---> 62 self.llm_engine = LLMEngine.from_engine_args(engine_args) 63 self.r...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: oad(repo_id, revision, repo_type, cache_dir, local_dir, local_dir_use_symlinks, library_name, library_version, user_agent, proxies, etag_timeout, resume_download, force_download, token, local_files_only, allow_patterns,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Failed to initialize vllm engine ``` llm = LLM(model="facebook/opt-125m") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outpu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 'facebook/opt-125m', tokenizer='facebook/opt-125m', tokenizer_mode=auto, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) ---------------------------...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: model_config.use_np_weights) 51 model = model.cuda() 52 return model.eval() File ~/anaconda3/envs/dxj/lib/python3.8/site-packages/vllm/model_executor/models/opt.py:304, in OPTForCausalLM.load_weights(self, model_name_or...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: opt-125m', tokenizer_mode=auto, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) --------------------------------------------------------------------...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

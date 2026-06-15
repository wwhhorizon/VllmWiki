# vllm-project/vllm#31901: [Bug]: Guided decoding with xgrammar failed on macOS CPU inference

| 字段 | 值 |
| --- | --- |
| Issue | [#31901](https://github.com/vllm-project/vllm/issues/31901) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Guided decoding with xgrammar failed on macOS CPU inference

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running inference with guided decoding (xgrammar), it failed: ```python from vllm import LLM, SamplingParams llm = LLM(model="Qwen/Qwen3-0.6B", max_model_len=512) print("Loading model Qwen/Qwen3-0.6B...") # Example Pydantic model class OutputJsonFormat(BaseModel): python_code: str # Apply ASCII-only restriction to the Pydantic model's schema base_schema = OutputJsonFormat.model_json_schema() prompts = [ """ The e with an accent in French in unicode encoding is (but I want it starting with '\\x' in Python representation) """, ] for prompt in prompts: print(f"\tGenerating for prompt: {prompt}") sampling_params = SamplingParams( temperature=0.0, top_p=0.95, structured_outputs=StructuredOutputsParams( json=base_schema, ), repetition_penalty=50.0, # Alleviate repetition ) outputs = llm.generate(prompt, sampling_params) print(outputs[0].outputs[0].text) ``` The error info: ``` (EngineCore_DP0 pid=45029) ERROR 01-07 15:12:55 [dump_input.py:72] Dumping input data for V1 LLM engine (v0.11.1rc3.dev1883+g727c41f3f) with config: model='Qwen/Qwen3-4B-Instruct-2507', speculative_config=None, tokenizer='Qwen/Qwen3-4B-Instruct-2507', skip_t...

## 现有链接修复摘要

#32384 [Bugfix] Fix xgrammar dtype mismatch on macOS CPU inference | #37706 [Bugfix] Fix structured output crash on CPU due to pin_memory=True

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ference with guided decoding (xgrammar), it failed: ```python from vllm import LLM, SamplingParams llm = LLM(model="Qwen/Qwen3-0.6B", max_model_len=512) print("Loading model Qwen/Qwen3-0.6B...") # Example Pydantic model...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: c3.dev1883+g727c41f3f) with config: model='Qwen/Qwen3-4B-Instruct-2507', speculative_config=None, tokenizer='Qwen/Qwen3-4B-Instruct-2507', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revisio...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=512, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ), it failed: ```python from vllm import LLM, SamplingParams llm = LLM(model="Qwen/Qwen3-0.6B", max_model_len=512) print("Loading model Qwen/Qwen3-0.6B...") # Example Pydantic model class OutputJsonFormat(BaseModel): py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ailed_traces=None, kv_cache_metrics=False, kv_cache_metrics_sample=0.01, cudagraph_metrics=False, enable_layerwise_nvtx_tracing=False, enable_mfu_metrics=False), seed=0, served_model_name=Qwen/Qwen3-4B-Instruct-2507, en...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32384](https://github.com/vllm-project/vllm/pull/32384) | closes_keyword | 0.95 | [Bugfix] Fix xgrammar dtype mismatch on macOS CPU inference | Fixes #31901 |
| [#37706](https://github.com/vllm-project/vllm/pull/37706) | mentioned | 0.6 | [Bugfix] Fix structured output crash on CPU due to pin_memory=True | dices` argument. Note: the existing CPU float32 workaround (added in #31901) was never reachable because the `pin_memory=True` crash occurs first. ## Fix On CPU, pass `out_indices… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

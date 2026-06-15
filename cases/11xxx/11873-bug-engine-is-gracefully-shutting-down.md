# vllm-project/vllm#11873: [Bug]: Engine is gracefully shutting down

| 字段 | 值 |
| --- | --- |
| Issue | [#11873](https://github.com/vllm-project/vllm/issues/11873) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;operator;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Engine is gracefully shutting down

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug my goal is to create an asynchronous engine and keep it running. I want to continuously add requests to the engine and retrieve their outputs. At the same time, I need the ability to abort certain requests during generation if they no longer require additional tokens. #### generate catch exception after final call ```python import asyncio from vllm.engine.async_llm_engine import ( AsyncLLMEngine, AsyncEngineArgs, SamplingParams, ) async def generate_text(engine, prompt: str, request_id: str): sampling_params = SamplingParams( temperature=0.0, max_tokens=16, ) final_output = None async for output in engine.generate(prompt, sampling_params, request_id=request_id): final_output = output return final_output async def main(): engine = AsyncLLMEngine.from_engine_args( AsyncEngineArgs(model="facebook/opt-125m") ) print("===> Start first async inference") output1 = await generate_text(engine, "Test first call.", request_id="1") print(f"[First result] {output1}") print("===> Call async inference again (expect graceful shutdown error)") output2 = await generate_text(engine, "Test second call.", request_i...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: Engine is gracefully shutting down bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug my goal is to create an asynchronous engine and keep it running. I want to cont...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tional tokens. #### generate catch exception after final call ```python import asyncio from vllm.engine.async_llm_engine import ( AsyncLLMEngine, AsyncEngineArgs, SamplingParams, ) async def generate_text(engine, prompt...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_c...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: lative_config=None, tokenizer='facebook/opt-125m', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

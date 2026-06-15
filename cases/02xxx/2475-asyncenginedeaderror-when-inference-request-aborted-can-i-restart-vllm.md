# vllm-project/vllm#2475: AsyncEngineDeadError when inference request aborted. Can I restart vllm-engine?

| 字段 | 值 |
| --- | --- |
| Issue | [#2475](https://github.com/vllm-project/vllm/issues/2475) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;quantization |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> AsyncEngineDeadError when inference request aborted. Can I restart vllm-engine?

### Issue 正文摘录

I trying use vllm with fastAPI as backend for [llm-vscode](https://github.com/huggingface/llm-vscode). Client send many requests for server, and abandon some requests when user write code before return inference results. on that case AsyncEngineDeadError happens frequently. My question - to avoid this, can I fix my code? - or can restart vllm engine with some code? ## ENV - docker image based nvcr.io/nvidia/pytorch:23.10-py3 - Nvidia Driver Version: 525.85.12 - CUDA Version: 12.0 - GPU Tesla T4 - Model octocoder(awq) - transformers==4.36.0 - autoawq==0.1.8 - xformers==0.0.23.post1 - vllm build from latest main branch ## Engin Args ``` INFO 01-18 02:14:41 llm_engine.py:70] Initializing an LLM engine with config: model='/usr/local/model/llm', tokenizer='/usr/local/model/llm', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=awq, enforce_eager=True, seed=0) ``` ## My Code(Partial) ``` python async def _get_vllm_res(self,request:Chat_Request , inputs:BatchEncoding , sampling_params:SamplingParams , req_client: Request , return_final:bool=...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: an I fix my code? - or can restart vllm engine with some code? ## ENV - docker image based nvcr.io/nvidia/pytorch:23.10-py3 - Nvidia Driver Version: 525.85.12 - CUDA Version: 12.0 - GPU Tesla T4 - Model octocoder(awq) -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ing use vllm with fastAPI as backend for [llm-vscode](https://github.com/huggingface/llm-vscode). Client send many requests for server, and abandon some requests when user write code before return inference results. on...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=awq, enforce_eager=True, seed=0)...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: , req_client: Request , return_final:bool=False)->AsyncGenerator[str, None]: request_id = random_uuid() results_generator = self.engine.generate( prompt=None, prompt_token_ids=inputs.input_ids, sampling_params=sa
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: AsyncEngineDeadError when inference request aborted. Can I restart vllm-engine? I trying use vllm with fastAPI as backend for [llm-vscode](https://github.com/huggingface/llm-vscode). Client send many requests for server...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#28033: [Bug]: CUDA Illegal Memory Access with VLM Models (Qwen3-VL/Qwen2.5-VL) when using logprobs=True under high concurrency

| 字段 | 值 |
| --- | --- |
| Issue | [#28033](https://github.com/vllm-project/vllm/issues/28033) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA Illegal Memory Access with VLM Models (Qwen3-VL/Qwen2.5-VL) when using logprobs=True under high concurrency

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi: ### Description When running Qwen3-VL-4B (bf16) or Qwen2.5-VL-7B (bf16) models with 24 concurrent threads, the inference fails with CUDA illegal memory access errors after successfully processing some queries. The issue occurs specifically when logprobs=True is enabled. ### Environment - vLLM version: 0.11.0 -Models tested: Qwen3-VL-4B (bf16), Qwen2.5-VL-7B (bf16) -vLLM 0.10 does not exhibit this issue with the same model(Qwen2.5-VL-7B) ### Code example ```python self._llm_client = ChatOpenAI( base_url=self._cfg.OPENAI_API_BASE, api_key=self._cfg.OPENAI_API_KEY, model=self._cfg.MODEL_NAME, streaming=True, max_tokens=10000, temperature=0., logprobs=True, top_p=0.01, timeout=60, max_retries=0, seed=42, ) messages = [ SystemMessage(content=system_prompt), HumanMessage(content=[ {"type": "image_url", "image_url": {"url": image_data_uri, "detail": "high"}} ]) ] try: async for chunk in self._llm_client.astream(messages): if not chunk.content: continue token = chunk.content if response_id is None and hasattr(chunk, "id"): response_id = chunk.id logprob = chunk.response_metadata['logprobs']['content'][0]['logprob'] logprobs.append(di...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: s errors after successfully processing some queries. The issue occurs specifically when logprobs=True is enabled. ### Environment - vLLM version: 0.11.0 -Models tested: Qwen3-VL-4B (bf16), Qwen2.5-VL-7B (bf16) -vLLM 0.1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: CUDA Illegal Memory Access with VLM Models (Qwen3-VL/Qwen2.5-VL) when using logprobs=True under high concurrency bug;stale ### Your current environment ### 🐛 Describe the bug Hi: ### Description When running Qwen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA Illegal Memory Access with VLM Models (Qwen3-VL/Qwen2.5-VL) when using logprobs=True under high concurrency bug;stale ### Your current environment ### 🐛 Describe the bug Hi: ### Description When running Qwen...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ### 🐛 Describe the bug Hi: ### Description When running Qwen3-VL-4B (bf16) or Qwen2.5-VL-7B (bf16) models with 24 concurrent threads, the inference fails with CUDA illegal memory access errors after successfully process...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: response_id = chunk.id logprob = chunk.response_metadata['logprobs']['content'][0]['logprob'] logprobs.append(dict(token=token, logprob=logprob)) full_response += token ```` ### Error log ``` [2025-11-04 15:01:38] [1;3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

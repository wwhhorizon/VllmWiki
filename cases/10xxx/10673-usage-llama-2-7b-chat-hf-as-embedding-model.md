# vllm-project/vllm#10673: [Usage]: Llama-2-7b-chat-hf as embedding model

| 字段 | 值 |
| --- | --- |
| Issue | [#10673](https://github.com/vllm-project/vllm/issues/10673) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Llama-2-7b-chat-hf as embedding model

### Issue 正文摘录

### Your current environment Following the code example provided [here](https://github.com/vllm-project/vllm/blob/main/examples%2Foffline_inference_embedding.py), I modified the model to Llama-2-7b-chat-hf and attempted to run the code, but I encountered the following error: ```text --------------------------------------------------------------------------- RuntimeError Traceback (most recent call last) Cell In[3], line 4 2 model = LLM(model="//common/public/LLAMA2-HF/Llama-2-7b-chat-hf", enforce_eager=True, task="embedding") 3 # Generate embedding. The output is a list of EmbeddingRequestOutputs. ----> 4 outputs = model.encode(prompts) 6 # # Print the outputs. 7 # for output in outputs: 8 # print(output.outputs.embedding) # list of 4096 floats File ~/second/lib/python3.10/site-packages/vllm/utils.py:1063, in deprecate_kwargs. .wrapper. .inner(*args, **kwargs) 1056 msg += f" {additional_message}" 1058 warnings.warn( 1059 DeprecationWarning(msg), 1060 stacklevel=3, # The inner function takes up one level 1061 ) -> 1063 return fn(*args, **kwargs) File ~/second/lib/python3.10/site-packages/vllm/entrypoints/llm.py:781, in LLM.encode(self, prompts, pooling_params, prompt_token_ids, use...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Llama-2-7b-chat-hf as embedding model usage ### Your current environment Following the code example provided [here](https://github.com/vllm-project/vllm/blob/main/examples%2Foffline_inference_embedding.py), I m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: odule._wrapped_call_impl(self, *args, **kwargs) 1734 return self._compiled_call_impl(*args, **kwargs) # type: ignore[misc] 1735 else: -> 1736 return self._call_impl(*args, **kwargs) File ~/second/lib/python3.10/site-pac...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: e[worker_input.virtual_engine] 346 if self.kv_cache is not None else None, 347 intermediate_tensors=intermediate_tensors, 348 num_steps=num_steps, 349 **kwargs, 350 ) 352 model_execute_time = time.perf_counter() - start...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: bedding") 3 # Generate embedding. The output is a list of EmbeddingRequestOutputs. ----> 4 outputs = model.encode(prompts) 6 # # Print the outputs. 7 # for output in outputs: 8 # print(output.outputs.embedding) # list o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

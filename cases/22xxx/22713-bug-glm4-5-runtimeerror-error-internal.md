# vllm-project/vllm#22713: [Bug]: GLM4.5 RuntimeError: Error Internal

| 字段 | 值 |
| --- | --- |
| Issue | [#22713](https://github.com/vllm-project/vllm/issues/22713) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM4.5 RuntimeError: Error Internal

### Issue 正文摘录

### Your current environment VLLM 0.10.0 8 * H800 ### 🐛 Describe the bug Launch server success. When Infer, the model server raises an error: ``` bash INFO 08-11 21:49:48 [chat_utils.py:473] Detected the chat template content format to be 'openai'. You can set `--chat-template-content-format` to override this. INFO 08-11 21:49:48 [logger.py:41] Received request chatcmpl-44934821f4c7449b9a1f79c6ff578b98: prompt: '[gMASK] \n你是一名运行于VSCode环境中的专业软件开发助理。 \n我买的莲藕里面为什么有孔？/nothink \n ', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=899, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None), prompt_token_ids: None, prompt_embeds shape: None, lora_request: None. INFO 08-11 21:49:48 [engine.py:315] Added request chatcmpl-44934821f4c7449b9a1f79c6ff578b98. (VllmWorkerProcess pid=4576) ERROR 08-11 21:49:52 [multiproc_worker_utils.py:239] Exception in worker Vl...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: GLM4.5 RuntimeError: Error Internal bug;stale ### Your current environment VLLM 0.10.0 8 * H800 ### 🐛 Describe the bug Launch server success. When Infer, the model server raises an error: ``` bash INFO 08-11 21:4...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 21:49:52 [multiproc_worker_utils.py:239] final_hidden_states = self.quant_method.apply( (VllmWorkerProcess pid=4576) ERROR 08-11 21:49:52 [multiproc_worker_utils.py:239] ^^^^^^^^^^^^^^^^^^^^^^^^ (VllmWorkerProcess pid=4...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/glm4_moe.py", line 656, in forward (VllmWorkerProcess pid=4576) ERROR 08-11 21:49:52 [multiproc_worker_utils.py:239] hidden_states = self.model(input_i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: H800 ### 🐛 Describe the bug Launch server success. When Infer, the model server raises an error: ``` bash INFO 08-11 21:49:48 [chat_utils.py:473] Detected the chat template content format to be 'openai'. You can set `--...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: id=4576) ERROR 08-11 21:49:52 [multiproc_worker_utils.py:239] return cutlass_moe_fp8( (VllmWorkerProcess pid=4576) ERROR 08-11 21:49:52 [multiproc_worker_utils.py:239] ^^^^^^^^^^^^^^^^ (VllmWorkerProcess pid=4576) ERROR...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

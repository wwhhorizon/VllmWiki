# vllm-project/vllm#11807: [Bug]: AttributeError: 'Int8Params' object has no attribute 'bnb_shard_offsets', It seems that vllm's bnb prequantification support for cls models is not yet complete.

| 字段 | 值 |
| --- | --- |
| Issue | [#11807](https://github.com/vllm-project/vllm/issues/11807) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'Int8Params' object has no attribute 'bnb_shard_offsets', It seems that vllm's bnb prequantification support for cls models is not yet complete.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug It seems that vllm's bnb prequantification support for cls models is not yet complete. This problem occurs only in the score layer of any bnb format cls model. ```python outputs = llm.classify( all_prompts, use_tqdm=True, ) ``` ```python Processed prompts: 0%| | 0/6 [00:00 in () 5 6 all_prompts = [TokensPrompt(prompt_token_ids=ids) for ids in data["input_ids"].values] ----> 7 outputs = llm.classify( 8 all_prompts, 9 lora_request=LoRARequest("lora_adapter", 1, WEIGHTS_PATH), /usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py in classify(self, prompts, use_tqdm, lora_request, prompt_adapter_request) 946 "Classification API is only enabled for `--task classify`") 947 --> 948 items = self.encode(prompts, 949 use_tqdm=use_tqdm, 950 lora_request=lora_request, /usr/local/lib/python3.10/dist-packages/vllm/utils.py in inner(*args, **kwargs) 1019 ) 1020 -> 1021 return fn(*args, **kwargs) 1022 1023 return inner # type: ignore /usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py in encode(self, prompts, pooling_params, prompt_token_ids, use_tqdm, lora_request, prompt_adapter_request...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ard_offsets', It seems that vllm's bnb prequantification support for cls models is not yet complete. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug It seems that vllm's...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: teps) 107 108 with set_forward_context(model_input.attn_metadata, self.vllm_config): --> 109 hidden_or_intermediate_states = model_executable( 110 input_ids=model_input.input_tokens, 111 positions=model_input.input_posi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 's bnb prequantification support for cls models is not yet complete. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug It seems that vllm's bnb prequantification support f...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rapped_call_impl(self, *args, **kwargs) 1734 return self._compiled_call_impl(*args, **kwargs) # type: ignore[misc] 1735 else: -> 1736 return self._call_impl(*args, **kwargs) 1737 1738 # torchrec tests the code consisten...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: object has no attribute 'bnb_shard_offsets', It seems that vllm's bnb prequantification support for cls models is not yet complete. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Descri...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

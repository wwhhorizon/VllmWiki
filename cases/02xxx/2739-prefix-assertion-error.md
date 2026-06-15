# vllm-project/vllm#2739: Prefix Assertion Error 

| 字段 | 值 |
| --- | --- |
| Issue | [#2739](https://github.com/vllm-project/vllm/issues/2739) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;quantization;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Prefix Assertion Error 

### Issue 正文摘录

I'm running into an assertion error when trying to use adapt the offline inference w/ prefix example. I've double checked the entire dataset, the prefix itself is 198 tokens and none of the prompts exceeded 1k tokens... When i run inference w/o prefix, it ran just fine. The max prompt length was 699 tokens. ``` # Model & Sampling params llm = LLM( model="TheBloke/Mixtral_34Bx2_MoE_60B-AWQ", quantization='awq', dtype='half', gpu_memory_utilization=.85, max_model_len=4096 ) sampling_params = SamplingParams(temperature=0.0, top_p=1.0, max_tokens=512) # inference w/ Prefix code: # -1 since the last token can change when concatenating prompts. prefix_pos = len(llm.llm_engine.tokenizer.encode(prefix)) - 1 # The llm.generate call will batch all prompts and send the batch at once if resources allow. # The prefix will only be cached after the first batch is processed, so we need to call generate once # to calculate the prefix and cache it. outputs = llm.generate(prompts[0], sampling_params, prefix_pos=[prefix_pos]) # Subsequent batches can leverage the cached prefix outputs = llm.generate(prompts, sampling_params, prefix_pos=[prefix_pos] * len(prompts)) # Load the data df_training = pd.rea...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: 189 dtype=torch.long) 190 slot_mapping = _make_tensor_with_pad(slot_mapping, 191 max_prompt_len, 192 pad=_PAD_SLOT_ID, 193
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ng params llm = LLM( model="TheBloke/Mixtral_34Bx2_MoE_60B-AWQ", quantization='awq', dtype='half', gpu_memory_utilization=.85, max_model_len=4096 ) sampling_params = SamplingParams(temperature=0.0, top_p=1.0, max_tokens...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: upport;quantization;sampling_logits cuda;quantization;sampling dtype;env_dependency;memory_layout;shape I'm running into an assertion error when trying to use adapt the offline inference w/ prefix example. I've double c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: dtype=torch.int, 200 device='cuda') 201 # Prepare prefix block tables File /usr/local/lib/python3.9/dist-packages/vllm/worker/model_runner.py:783, in _pad_to_max(x, max_len, pad) 782 def _pad_to_max(x: List[int], max_le...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: device='cuda') 201 # Prepare prefix block tables File /usr/local/lib/python3.9/dist-packages/vllm/worker/model_runner.py:783, in _pad_to_max(x, max_len, pad) 782 def _pad_to_max(x: List[int], max_len: int, pad: int) ->...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

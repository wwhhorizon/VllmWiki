# vllm-project/vllm#2612: Prefix cache run into assert.

| 字段 | 值 |
| --- | --- |
| Issue | [#2612](https://github.com/vllm-project/vllm/issues/2612) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Prefix cache run into assert.

### Issue 正文摘录

@Yard1 Hello, I found prefix can't run in the newest version. Maybe it due to the lora? But I am not familiar with lora, I just did a try. Using code below make prefix run again. It seems work. Could you please take a look at this issue. I replaced code in model_runner.py (191-194 row) by this. ``` max_lora_index_len = max(len(mapping) for mapping in lora_index_mapping) lora_index_mapping = [ _pad_to_max(mapping, max_lora_index_len, pad=0) for mapping in lora_index_mapping ] ``` Ran into assert as below. ``` Traceback (most recent call last): File "/home/yangchunhao/vllm-newest/vllm/examples/offline_inference_with_prefix.py", line 53, in outputs = llm.generate(generating_prompts, File "/data/home/yangchunhao/vllm-newest/vllm/vllm/entrypoints/llm.py", line 179, in generate return self._run_engine(use_tqdm) File "/data/home/yangchunhao/vllm-newest/vllm/vllm/entrypoints/llm.py", line 205, in _run_engine step_outputs = self.llm_engine.step() File "/data/home/yangchunhao/vllm-newest/vllm/vllm/engine/llm_engine.py", line 790, in step all_outputs = self._run_workers( File "/data/home/yangchunhao/vllm-newest/vllm/vllm/engine/llm_engine.py", line 977, in _run_workers driver_worker_output =...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: nner.py (191-194 row) by this. ``` max_lora_index_len = max(len(mapping) for mapping in lora_index_mapping) lora_index_mapping = [ _pad_to_max(mapping, max_lora_index_len, pad=0) for mapping in lora_index_mapping ] ```...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: he run into assert. @Yard1 Hello, I found prefix can't run in the newest version. Maybe it due to the lora? But I am not familiar with lora, I just did a try. Using code below make prefix run again. It seems work. Could...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Prefix cache run into assert. @Yard1 Hello, I found prefix can't run in the newest version. Maybe it due to the lora? But I am not familiar with lora, I just did a try. Using code below make prefix run again. It seems wo
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ms work. Could you please take a look at this issue. I replaced code in model_runner.py (191-194 row) by this. ``` max_lora_index_len = max(len(mapping) for mapping in lora_index_mapping) lora_index_mapping = [ _pad_to_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: llm/worker/model_runner.py", line 445, in prepare_input_tensors lora_requests) = self._prepare_prompt(seq_group_metadata_list) File "/data/home/yangchunhao/vllm-newest/vllm/vllm/worker/model_runner.py", line 196, in _pr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

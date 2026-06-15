# vllm-project/vllm#11792: [Bug]: Run Pixtral-Large-Instruct-2411 raised a error Attempted to assign 1 x 2074 = 2074 multimodal tokens to 2040 placeholders

| 字段 | 值 |
| --- | --- |
| Issue | [#11792](https://github.com/vllm-project/vllm/issues/11792) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Run Pixtral-Large-Instruct-2411 raised a error Attempted to assign 1 x 2074 = 2074 multimodal tokens to 2040 placeholders

### Issue 正文摘录

### Your current environment ### Model Input Dumps [err_execute_model_input_20250107-133808.zip](https://github.com/user-attachments/files/18328117/err_execute_model_input_20250107-133808.zip) ### 🐛 Describe the bug (VllmWorkerProcess pid=8989) ERROR 01-07 13:38:08 multiproc_worker_utils.py:236] ValueError: Error in model execution (input dumped to /tmp/err_execute_model_input_20250107-133808.pkl): Attempted to assign 1 x 2074 = 2074 multimodal tokens to 2040 placeholders (VllmWorkerProcess pid=8990) ERROR 01-07 13:38:08 multiproc_worker_utils.py:236] return func(*args, **kwargs) (VllmWorkerProcess pid=8990) ERROR 01-07 13:38:08 multiproc_worker_utils.py:236] ^^^^^^^^^^^^^^^^^^^^^ (VllmWorkerProcess pid=8990) ERROR 01-07 13:38:08 multiproc_worker_utils.py:236] File "/usr/local/lib/python3.12/dist-packages/vllm/worker/model_runner_base.py", line 152, in _wrapper (VllmWorkerProcess pid=8990) ERROR 01-07 13:38:08 multiproc_worker_utils.py:236] raise type(err)( (VllmWorkerProcess pid=8990) ERROR 01-07 13:38:08 multiproc_worker_utils.py:236] ValueError: Error in model execution (input dumped to /tmp/err_execute_model_input_20250107-133808.pkl): Attempted to assign 1 x 2074 = 2074 multi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: l-Large-Instruct-2411 raised a error Attempted to assign 1 x 2074 = 2074 multimodal tokens to 2040 placeholders bug;stale ### Your current environment ### Model Input Dumps [err_execute_model_input_20250107-133808.zip](...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ted to assign 1 x 2074 = 2074 multimodal tokens to 2040 placeholders bug;stale ### Your current environment ### Model Input Dumps [err_execute_model_input_20250107-133808.zip](https://github.com/user-attachments/files/1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: and third and fourth? Name the country, its color on the map and one its city that is visible on the map, but is not the capital. Make absolutely sure to only name a city that can be seen on the map.", "text": "describe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tral", tensor_parallel_size=8, limit_mm_per_prompt={"image": 4}, device='cuda', allowed_local_media_path='/dfs/data/mistral/', max_model_len=8192, enable_chunked_prefill=False, max_num_batched_tokens=10240) outputs = ll...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: _path='/dfs/data/mistral/', max_model_len=8192, enable_chunked_prefill=False, max_num_batched_tokens=10240) outputs = llm.chat(messages, sampling_params=sampling_params) print(outputs[0].outputs[0].text) ``` ### Before...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

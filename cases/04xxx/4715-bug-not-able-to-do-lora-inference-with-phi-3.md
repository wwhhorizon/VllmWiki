# vllm-project/vllm#4715: [Bug]: Not able to do lora inference with phi-3

| 字段 | 值 |
| --- | --- |
| Issue | [#4715](https://github.com/vllm-project/vllm/issues/4715) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Not able to do lora inference with phi-3

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug The following error appeared when trying to do lora inference with phi-3 using the newest vllm version: ``` Exception while reading stream response: Loading lora data/loras/jt_snc_dpo failed Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/vllm/lora/worker_manager.py", line 150, in _load_lora lora = self._lora_model_cls.from_local_checkpoint( File "/usr/local/lib/python3.10/dist-packages/vllm/lora/models.py", line 225, in from_local_checkpoint raise ValueError( ValueError: While loading data/loras/jt_snc_dpo, expected target modules in ['q_proj', 'k_proj', 'v_proj', 'o_proj', 'gate_proj', 'up_proj', 'down_proj', 'embed_tokens', 'lm_head'] but received ['gate_up_proj', 'qkv_proj']. Please verify that the loaded LoRA module is correct The above exception was the direct cause of the following exception: Traceback (most recent call last): File "/app/model_wrapper.py", line 269, in write_response_to_queue async for chunk in generator: File "/app/model/model.py", line 50, in generator async for output in vllm_generator: File "/usr/local/lib/python3.10/dis...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: in execute_model output = self.model_runner.execute_model(seq_group_metadata_list, File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) Fi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: peared when trying to do lora inference with phi-3 using the newest vllm version: ``` Exception while reading stream response: Loading lora data/loras/jt_snc_dpo failed Traceback (most recent call last): File "/usr/loca...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: m/lora/worker_manager.py", line 150, in _load_lora lora = self._lora_model_cls.from_local_checkpoint( File "/usr/local/lib/python3.10/dist-packages/vllm/lora/models.py", line 225, in from_local_checkpoint raise ValueErr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ll last): File "/app/model_wrapper.py", line 269, in write_response_to_queue async for chunk in generator: File "/app/model/model.py", line 50, in generator async for output in vllm_generator: File "/usr/local/lib/pytho...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

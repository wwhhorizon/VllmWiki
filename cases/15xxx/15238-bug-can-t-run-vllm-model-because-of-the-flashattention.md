# vllm-project/vllm#15238: [Bug]: Can't run vllm model because of the FlashAttention.

| 字段 | 值 |
| --- | --- |
| Issue | [#15238](https://github.com/vllm-project/vllm/issues/15238) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't run vllm model because of the FlashAttention.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Description The code in https://github.com/vllm-project/vllm/pull/13454 hasn't been merged for nearly a week. As a result, the code that could run previously can no longer work properly. However, if I roll back the code to the state it was in a week ago, everything runs fine again. ## Error Logs Here are some of the error messages I'm getting: ``` ERROR 03-20 09:51:26 [core.py:340] File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1739, in _wrapped_call_impl ERROR 03-20 09:51:26 [core.py:340] return self._call_impl(*args, **kwargs) ERROR 03-20 09:51:26 [core.py:340] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 03-20 09:51:26 [core.py:340] File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1750, in _call_impl ERROR 03-20 09:51:26 [core.py:340] return forward_call(*args, **kwargs) ERROR 03-20 09:51:26 [core.py:340] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 03-20 09:51:26 [core.py:340] File "/data4/qinggangying/qingjun/vllm/vllm/model_executor/models/minimax_text_01.py", line 1031, in forward ERROR 03-20 09:51:26 [core.py:340] hidden_states = self.model(input_ids, positions, self.kv_c...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: eError: flash_attn_varlen_func() got an unexpected keyword argument 'q_descale' ``` There are many more error messages like these. ## Investigation The main problem seems to be related to FlashAttentionMetadata. The rec...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Can't run vllm model because of the FlashAttention. bug;stale ### Your current environment ### 🐛 Describe the bug # Description The code in https://github.com/vllm-project/vllm/pull/13454 hasn't been merged for n...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. development attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding attention;cuda;operator;quantizatio...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Can't run vllm model because of the FlashAttention. bug;stale ### Your current environment ### 🐛 Describe the bug # Description The code in https://github.com/vllm-project/vllm/pull/13454 hasn't been merged for n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

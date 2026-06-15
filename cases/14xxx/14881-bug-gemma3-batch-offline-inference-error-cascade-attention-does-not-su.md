# vllm-project/vllm#14881: [Bug]: Gemma3 Batch Offline Inference Error: Cascade attention does not support sliding window

| 字段 | 值 |
| --- | --- |
| Issue | [#14881](https://github.com/vllm-project/vllm/issues/14881) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma3 Batch Offline Inference Error: Cascade attention does not support sliding window

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug For gemma-3-72b, llm.chat() works with a single message, but fails when inputting multiple messages (where each message can have multiple images). ``` Environment steps 1 INFO 03-16 00:20:22 [chat_utils.py:346] Detected the chat template content format to be 'openai'. You can set `--chat-template-content-format` to override this. [rank0]:W0316 00:20:26.470743 178163 site-packages/torch/_dynamo/convert_frame.py:906] [0/8] torch._dynamo hit config.cache_size_limit (8) [rank0]:W0316 00:20:26.470743 178163 site-packages/torch/_dynamo/convert_frame.py:906] [0/8] function: 'forward_static' (/home/agi/vllm/vllm/model_executor/layers/layernorm.py:170) [rank0]:W0316 00:20:26.470743 178163 site-packages/torch/_dynamo/convert_frame.py:906] [0/8] last reason: 0/0: tensor 'L['x']' size mismatch at index 0. expected 64, actual 1 [rank0]:W0316 00:20:26.470743 178163 site-packages/torch/_dynamo/convert_frame.py:906] [0/8] To log all recompilation reasons, use TORCH_LOGS="recompiles". [rank0]:W0316 00:20:26.470743 178163 site-packages/torch/_dynamo/convert_frame.py:906] [0/8] To diagnose recompilation issues, see https://pytorch.org/docs/main/tor...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: _frame.py:906] [0/8] To log all recompilation reasons, use TORCH_LOGS="recompiles". [rank0]:W0316 00:20:26.470743 178163 site-packages/torch/_dynamo/convert_frame.py:906] [0/8] To diagnose recompilation issues, see http...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Gemma3 Batch Offline Inference Error: Cascade attention does not support sliding window bug ### Your current environment ### 🐛 Describe the bug For gemma-3-72b, llm.chat() works with a single message, but fails w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: /convert_frame.py:906] [0/8] last reason: 0/0: tensor 'L['x']' size mismatch at index 0. expected 64, actual 1 [rank0]:W0316 00:20:26.470743 178163 site-packages/torch/_dynamo/convert_frame.py:906] [0/8] To log all reco...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: OR 03-16 00:20:26 [core.py:340] File "/home/agi/vllm/vllm/v1/attention/backends/flash_attn.py", line 286, in forward ERROR 03-16 00:20:26 [core.py:340] cascade_attention( ERROR 03-16 00:20:26 [core.py:340] File "/home/a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 16 00:20:26 [core.py:340] output = self.model_executor.execute_model(scheduler_output) ERROR 03-16 00:20:26 [core.py:340] File "/home/agi/vllm/vllm/v1/executor/abstract.py", line 80, in execute_model ERROR 03-16 00:20:2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

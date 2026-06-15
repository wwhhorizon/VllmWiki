# vllm-project/vllm#12917: [Feature]: log model weights load time in one log message

| 字段 | 值 |
| --- | --- |
| Issue | [#12917](https://github.com/vllm-project/vllm/issues/12917) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;sampling |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: log model weights load time in one log message

### Issue 正文摘录

### 🚀 The feature, motivation and pitch As someone trying to automate analysis of vLLM logs to extract components of latency, I would prefer to be able to read the model weight loading time from one log message rather than have to parse two log messages---including their timestamps---and compute the difference between the timestamps. The latter is currently my only choice, right? Following is an excerpt of the logging that I got from release 0.7.2 in V1 mode, from the first relevant log message to the second. ``` INFO 02-07 19:23:56 gpu_model_runner.py:867] Starting to load model ibm-granite/granite-3.0-3b-a800m-instruct... INFO 02-07 19:23:56 cuda.py:158] Using Flash Attention backend on V1 engine. WARNING 02-07 19:23:56 topk_topp_sampler.py:46] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best performance, please install FlashInfer. INFO 02-07 19:23:57 weight_utils.py:252] Using model weights format ['*.safetensors'] model-00002-of-00002.safetensors: 100%|█████████████████████████████████| 1.75G/1.75G [00:56<00:00, 30.8MB/s] model-00001-of-00002.safetensors: 100%|█████████████████████████████████| 5.00G/5.00G [...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: /granite-3.0-3b-a800m-instruct... INFO 02-07 19:23:56 cuda.py:158] Using Flash Attention backend on V1 engine. WARNING 02-07 19:23:56 topk_topp_sampler.py:46] FlashInfer is not available. Falling back to the PyTorch-nat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d model ibm-granite/granite-3.0-3b-a800m-instruct... INFO 02-07 19:23:56 cuda.py:158] Using Flash Attention backend on V1 engine. WARNING 02-07 19:23:56 topk_topp_sampler.py:46] FlashInfer is not available. Falling back...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: log model weights load time in one log message feature request;stale ### 🚀 The feature, motivation and pitch As someone trying to automate analysis of vLLM logs to extract components of latency, I would prefe...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: :158] Using Flash Attention backend on V1 engine. WARNING 02-07 19:23:56 topk_topp_sampler.py:46] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best pe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: log model weights load time in one log message feature request;stale ### 🚀 The feature, motivation and pitch As someone trying to automate analysis of vLLM logs to extract components of latency, I would prefe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

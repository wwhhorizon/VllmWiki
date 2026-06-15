# vllm-project/vllm#19800: [Bug]: After receiving the request, the service froze

| 字段 | 值 |
| --- | --- |
| Issue | [#19800](https://github.com/vllm-project/vllm/issues/19800) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: After receiving the request, the service froze

### Issue 正文摘录

### Your current environment Python 3.9.21 pydantic-ai 0.3.0 vllm 0.9.0.1 deploy code： CUDA_VISIBLE_DEVICES=3 nohup python -m vllm.entrypoints.openai.api_server \ --model /data/ckpt/Qwen/Qwen2.5-14B-Instruct\ --tensor-parallel-size 1 \ --max-model-len 16384 \ --port 7509 \ --gpu-memory-utilization 0.95 \ --disable-log-stats \ --served-model-name qwen2.5-14b-instruct \ --max-num-batched-tokens 100000 \ --max-num-seqs 1500 \ --enable-prefix-caching \ --tokenizer-pool-size=32 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --trust-remote-code ### 🐛 Describe the bug After receiving the request, the service froze，Long term no response, new requests cannot be returned server log： INFO 06-18 16:48:22 [logger.py:42] Received request chatcmpl-b2fba3c87bfb4896bf83656515c8ecca: prompt: ' system\nplease extract the user profile information from the following text. The output should be a JSON object with the keys "name", "dob" (date of birth), and "bio" (a short biography). If any information is not available, leave that key out of the JSON object.\n\n# Tools\n\nYou may call one or more functions to assist with the user query.\n\nYou are provided with function signatures within XML t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: BLE_DEVICES=3 nohup python -m vllm.entrypoints.openai.api_server \ --model /data/ckpt/Qwen/Qwen2.5-14B-Instruct\ --tensor-parallel-size 1 \ --max-model-len 16384 \ --port 7509 \ --gpu-memory-utilization 0.95 \ --disable...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rameters']}]}}, regex=None, choice=None, grammar=None, json_object=None, backend=None, backend_was_auto=False, disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, whitespace_patter...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: tokens=16126, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=GuidedDecodingParams(json={'type': 'array', 'mi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: environment Python 3.9.21 pydantic-ai 0.3.0 vllm 0.9.0.1 deploy code： CUDA_VISIBLE_DEVICES=3 nohup python -m vllm.entrypoints.openai.api_server \ --model /data/ckpt/Qwen/Qwen2.5-14B-Instruct\ --tensor-parallel-size 1 \...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: After receiving the request, the service froze bug;stale ### Your current environment Python 3.9.21 pydantic-ai 0.3.0 vllm 0.9.0.1 deploy code： CUDA_VISIBLE_DEVICES=3 nohup python -m vllm.entrypoints.openai.api_s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

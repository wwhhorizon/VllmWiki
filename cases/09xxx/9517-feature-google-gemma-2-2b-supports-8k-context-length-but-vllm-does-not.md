# vllm-project/vllm#9517: [Feature]: google/gemma-2-2b supports 8K context length but vllm does not support it.

| 字段 | 值 |
| --- | --- |
| Issue | [#9517](https://github.com/vllm-project/vllm/issues/9517) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda |
| 症状 | crash;mismatch |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: google/gemma-2-2b supports 8K context length but vllm does not support it.

### Issue 正文摘录

### Your current environment vllm version: 0.6.3.post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug I see on the official site of gemma: https://huggingface.co/google/gemma-2b, context length is 8K. however, when I load it into vllm and try to do inference where max_model_len is set to 8192, I encounter the error below: > Traceback (most recent call last): > File "/home/ubuntu/moa/eval.py", line 170, in > llm = LLM(model= args.llm_name, dtype='bfloat16', max_model_len= max_len, > File "/opt/conda/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 177, in __init__ > self.llm_engine = LLMEngine.from_engine_args( > File "/opt/conda/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 570, in from_engine_args > engine_config = engine_args.create_engine_config() > File "/opt/conda/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 903, in create_engine_config > model_config = self.create_model_config() > File "/opt/conda/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 839, in create_model_config > return ModelConfig( > File "/opt/conda/lib/python3.10/site-packages/vllm/config.py", line 192, in __init__ > self.max_model_len = _get_a...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: google/gemma-2-2b supports 8K context length but vllm does not support it. feature request;stale ### Your current environment vllm version: 0.6.3.post1 ### Model Input Dumps _No response_ ### 🐛 Describe the b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: not support it. feature request;stale ### Your current environment vllm version: 0.6.3.post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug I see on the official site of gemma: https://huggingface.co/google/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: buntu/moa/eval.py", line 170, in > llm = LLM(model= args.llm_name, dtype='bfloat16', max_model_len= max_len, > File "/opt/conda/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 177, in __init__ > self.llm_eng...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: one in model's config.json). This may lead to incorrect model outputs or CUDA errors. To allow overriding this maximum, set the env var VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 ### Before submitting a new issue... - [X] Make sur...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ma-2-2b supports 8K context length but vllm does not support it. feature request;stale ### Your current environment vllm version: 0.6.3.post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug I see on the offic...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

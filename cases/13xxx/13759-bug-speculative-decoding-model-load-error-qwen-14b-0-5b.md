# vllm-project/vllm#13759: [Bug]: Speculative Decoding Model Load Error (Qwen 14b + 0.5b)

| 字段 | 值 |
| --- | --- |
| Issue | [#13759](https://github.com/vllm-project/vllm/issues/13759) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Speculative Decoding Model Load Error (Qwen 14b + 0.5b)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Speculative Decoding can not load by repo folder name, it will report file does not exist. If use a GGUF model, a KeyError will occur: ``` return loader.load_weights(weights) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/miniconda3/envs/vllm/lib/python3.12/site-packages/vllm/model_executor/models/utils.py", line 235, in load_weights autoloaded_weights = set(self._load_module("", self.module, weights)) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/miniconda3/envs/vllm/lib/python3.12/site-packages/vllm/model_executor/models/utils.py", line 196, in _load_module yield from self._load_module(prefix, File "/opt/miniconda3/envs/vllm/lib/python3.12/site-packages/vllm/model_executor/models/utils.py", line 173, in _load_module loaded_params = module_load_weights(weights) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/miniconda3/envs/vllm/lib/python3.12/site-packages/vllm/model_executor/models/qwen2.py", line 412, in load_weights param = params_dict[name] ~~~~~~~~~~~^^^^^^ KeyError: 'embed_tokens.qweight_type' ``` ### PS: Even using a normal model name, still error: ``` File "/opt/miniconda3/envs/vllm/lib/python3.12/site-packages/vllm/mode...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: odel was a GGUF model. ### PPS: Qwen2.5-Coder-14b-AWQ and its 0.5b AWQ version ``` Loading safetensors checkpoint shards: 50% Completed | 1/2 [00:03<00:03, 3.02s/it] Loading safetensors checkpoint shards: 100% Completed...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Speculative Decoding Model Load Error (Qwen 14b + 0.5b) bug;stale ### Your current environment ### 🐛 Describe the bug Speculative Decoding can not load by repo folder name, it will report file does not exist. If...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Speculative Decoding Model Load Error (Qwen 14b + 0.5b) bug;stale ### Your current environment ### 🐛 Describe the bug Speculative Decoding can not load by repo folder name, it will report file does not exist. If...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;crash;nan_inf env_dependency;shape Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: correctness ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;crash;nan_inf env_dependency;shape Your c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

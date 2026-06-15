# vllm-project/vllm#33155: [Bug]: gptoss120B is OOM on one H100 after upgrading from v0.11.2 to v0.14.1

| 字段 | 值 |
| --- | --- |
| Issue | [#33155](https://github.com/vllm-project/vllm/issues/33155) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gptoss120B is OOM on one H100 after upgrading from v0.11.2 to v0.14.1

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug When to use v0.11.2, I can run gpt-oss-120B on single H100 with 85K context length by following comand: ```shell model_name="openai/gpt-oss-120b" max_model_len=$((85 * 1024)) VLLM_LOGGING_LEVEL=DEBUG CUDA_VISIBLE_DEVICES=1 uv run vllm serve \ $model_name \ --host 0.0.0.0 --port $port \ --gpu-memory-utilization 0.97 \ -O3 \ --enable-chunked-prefill --enable-prefix-caching \ --async-scheduling \ --max_num_seqs 100 \ --tool-call-parser openai --enable-auto-tool-choice \ --tensor-parallel-size 1 --max-model-len $max_model_len >> "$LOG_FILE" 2>&1 & ``` But the similar command got OOM even with very little max_model_len and max_num_seqs: ```shell model_name="openai/gpt-oss-120b" max_model_len=$((5 * 1024)) CUDA_VISIBLE_DEVICES=1 uv run vllm serve \ $model_name \ --host 0.0.0.0 --port $port \ --gpu-memory-utilization 0.97 \ -O3 \ --enable-chunked-prefill --enable-prefix-caching \ --async-scheduling \ --max_num_seqs 1 \ --tool-call-parser openai --enable-auto-tool-choice \ --tensor-parallel-size 1 --max-model-len $max_model_len >> "$LOG_FILE" 2>&1 & ``` Log is as following: ``` ^[[0;36m(EngineCore_DP0 pid=70073)^[[0;0m INFO 01-27 00:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 0:32:03 [backends.py:644] Using cache directory: /root/.cache/vllm/torch_compile_cache/ece87d2aa9/rank_0_0/backbone for vLLM's torch.compile ^[[0;36m(EngineCore_DP0 pid=70073)^[[0;0m INFO 01-27 00:32:03 [backends.py:704...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ptoss120B is OOM on one H100 after upgrading from v0.11.2 to v0.14.1 bug;stale ### Your current environment N/A ### 🐛 Describe the bug When to use v0.11.2, I can run gpt-oss-120B on single H100 with 85K context length b...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ON_ATTN') ^[[0;36m(EngineCore_DP0 pid=70073)^[[0;0m INFO 01-27 00:31:44 [mxfp4.py:165] Using Triton backend ^[[0;36m(EngineCore_DP0 pid=70073)^[[0;0m ^[[0;36m(EngineCore_DP0 pid=70073)^[[0;0m INFO 01-27 00:31:55 [defaul...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: gptoss120B is OOM on one H100 after upgrading from v0.11.2 to v0.14.1 bug;stale ### Your current environment N/A ### 🐛 Describe the bug When to use v0.11.2, I can run gpt-oss-120B on single H100 with 85K context...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: environment N/A ### 🐛 Describe the bug When to use v0.11.2, I can run gpt-oss-120B on single H100 with 85K context length by following comand: ```shell model_name="openai/gpt-oss-120b" max_model_len=$((85 * 1024)) VLLM_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

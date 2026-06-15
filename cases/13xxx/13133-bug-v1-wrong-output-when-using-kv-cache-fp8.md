# vllm-project/vllm#13133: [Bug]: [V1] wrong output when using kv cache fp8

| 字段 | 值 |
| --- | --- |
| Issue | [#13133](https://github.com/vllm-project/vllm/issues/13133) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cache;fp8 |
| 症状 | mismatch |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [V1] wrong output when using kv cache fp8

### Issue 正文摘录

### Your current environment KV fp8 is ok when disabling V1 Engine, But when using V1 engine, the output is totally wrong. vllm version 0.7.1, GPU H100 ``` port = 10011 model = "/data/models/qwen2.5_72b-FP8" #cmd = f"VLLM_USE_V1=1 python3 -m vllm.entrypoints.openai.api_server \ cmd = f"VLLM_USE_V1=1 python3 -m vllm.entrypoints.openai.api_server \ --port {port} \ --model {model} \ --dtype auto \ -tp 2 \ --max-model-len 8192 \ --max-num-seqs 512 \ --gpu-memory-utilization 0.9 \ --enable-prefix-caching \ --swap-space 16 \ --disable-log-stats \ --disable-log-requests \ --trust-remote-code --kv-cache-dtype fp8" ``` ### 🐛 Describe the bug When disabling kv fp8, output length is 140. But when enabling it, output length is 1000+, and the text is unreadable. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: [V1] wrong output when using kv cache fp8 bug ### Your current environment KV fp8 is ok when disabling V1 Engine, But when using V1 engine, the output is totally wrong. vllm version 0.7.1, GPU H100 ``` port = 100...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: n using V1 engine, the output is totally wrong. vllm version 0.7.1, GPU H100 ``` port = 10011 model = "/data/models/qwen2.5_72b-FP8" #cmd = f"VLLM_USE_V1=1 python3 -m vllm.entrypoints.openai.api_server \ cmd = f"VLLM_US...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: [V1] wrong output when using kv cache fp8 bug ### Your current environment KV fp8 is ok when disabling V1 Engine, But when using V1 engine, the output is totally wrong. vllm version 0.7.1, GPU H100 ``` port = 100...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: output is totally wrong. vllm version 0.7.1, GPU H100 ``` port = 10011 model = "/data/models/qwen2.5_72b-FP8" #cmd = f"VLLM_USE_V1=1 python3 -m vllm.entrypoints.openai.api_server \ cmd = f"VLLM_USE_V1=1 python3 -m vllm....
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ntion_kv_cache;distributed_parallel;model_support;quantization cache;fp8 mismatch dtype Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

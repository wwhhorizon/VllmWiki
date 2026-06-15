# vllm-project/vllm#19466: [Bug]: [Bug]: Fail to run qwen3-30B-A3B on new version vLLM 0.9.0.1

| 字段 | 值 |
| --- | --- |
| Issue | [#19466](https://github.com/vllm-project/vllm/issues/19466) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [Bug]: Fail to run qwen3-30B-A3B on new version vLLM 0.9.0.1

### Issue 正文摘录

### Your current environment GPU: nvidia t4*8 params: ``` --served-model-name Qwen/Qwen3-30B-A3B --model /data/models/Qwen/Qwen3-30B-A3B --tensor-parallel-size 8 --gpu-memory-utilization 0.9 --max-model-len 131072 --port 8000 --host 0.0.0.0 --trust-remote-code --enable-auto-tool-choice --tool-call-parser hermes --disable-custom-all-reduce --enable-reasoning --reasoning-parser deepseek_r1 --rope-scaling '{"rope_type":"yarn","factor":4.0,"original_max_position_embeddings":32768}' --dtype half ``` logs: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: [Bug]: Fail to run qwen3-30B-A3B on new version vLLM 0.9.0.1 bug;stale ### Your current environment GPU: nvidia t4*8 params: ``` --served-model-name Qwen/Qwen3-30B-A3B --model /data/models/Qwen/Qwen3-30B-A3B --te...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ":"yarn","factor":4.0,"original_max_position_embeddings":32768}' --dtype half ``` logs: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: [Bug]: Fail to run qwen3-30B-A3B on new version vLLM 0.9.0.1 bug;stale ### Your current environment GPU: nvidia t4*8 params: ``` --served-model-name Qwen/Qwen3-30B-A3B --model /data/models/Qwen/Qwen3-30B-A3B --te...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: del_support;moe;quantization attention;cuda;kernel;operator;quantization;triton build_error;crash dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

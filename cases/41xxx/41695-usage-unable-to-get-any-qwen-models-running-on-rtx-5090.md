# vllm-project/vllm#41695: [Usage]: Unable to get any qwen models running on RTX 5090

| 字段 | 值 |
| --- | --- |
| Issue | [#41695](https://github.com/vllm-project/vllm/issues/41695) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | fp8 |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Unable to get any qwen models running on RTX 5090

### Issue 正文摘录

### Your current environment I've tried multiple models, ones I know work on my machine using other applications like ollama, or lmstudio: - Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 - Qwen/Qwen3.5-35B-A3B (works fine with LM Studio `lms load qwen/qwen3.5-35b-a3b --context-length 81920`) - Qwen/Qwen3.6-27B-FP8 An example of serving a model: ``` vllm serve Qwen3-Coder-30B-A3B-Instruct-FP8 \ --host 0.0.0.0 \ --port 8000 \ --max-model-len 16384 \ --dtype auto \ --gpu-memory-utilization 0.95 \ --served-model-name Qwen3-Coder-30B-A3B-Instruct-FP8 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --reasoning-parser qwen3 \ --language-model-only ``` I will either get a OOM or a "No available memory for the cache blocks." no matter how much I lower the gpu memory (that causes issues with claude code and it's context). At this point I'm just looking to the community for a working code model on the 5090, and possibly confirmation on working claude code cli usage. All 5090 issues seem to be made in December and since that's a long time in the industry I just decided to create an issue. ```text [The output of `python collect_env.py`](failed: Connection timed out.) ``` I would run collecti...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ications like ollama, or lmstudio: - Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 - Qwen/Qwen3.5-35B-A3B (works fine with LM Studio `lms load qwen/qwen3.5-35b-a3b --context-length 81920`) - Qwen/Qwen3.6-27B-FP8 An example of s...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: easoning-parser qwen3 \ --language-model-only ``` I will either get a OOM or a "No available memory for the cache blocks." no matter how much I lower the gpu memory (that causes issues with claude code and it's context)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Unable to get any qwen models running on RTX 5090 usage ### Your current environment I've tried multiple models, ones I know work on my machine using other applications like ollama, or lmstudio: - Qwen/Qwen3-Co...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e made in December and since that's a long time in the industry I just decided to create an issue. ```text [The output of `python collect_env.py`](failed: Connection timed out.) ``` I would run collecting env normally b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: Unable to get any qwen models running on RTX 5090 usage ### Your current environment I've tried multiple models, ones I know work on my machine using other applications like ollama, or lmstudio: - Qwen/Qwen3-Co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#20891: [Bug]: High chance of stuck at model download

| 字段 | 值 |
| --- | --- |
| Issue | [#20891](https://github.com/vllm-project/vllm/issues/20891) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;model_support |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: High chance of stuck at model download

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On the latest main branch, it happens ~20% of the time. The progress bar stuck at 0. No way to abort either. Have to `crtl+z` then force kill. ``` INFO 07-13 17:17:22 [gpu_model_runner.py:1732] Starting to load model Qwen/Qwen3-Embedding-8B... INFO 07-13 17:17:22 [gpu_model_runner.py:1737] Loading model from scratch... INFO 07-13 17:17:23 [cuda.py:295] Using Flash Attention backend on V1 engine. INFO 07-13 17:17:23 [weight_utils.py:296] Using model weights format ['*.safetensors'] model-00001-of-00004.safetensors: 0%| | 0.00/4.90G [00:00 main() File "/data/users/quinnzhu/gitrepos/vllm/run_pooling.py", line 19, in main model = LLM( ^^^^ File "/data/users/quinnzhu/gitrepos/vllm/vllm/entrypoints/llm.py", line 274, in __init__ self.llm_engine = LLMEngine.from_engine_args( ^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/data/users/quinnzhu/gitrepos/vllm/vllm/engine/llm_engine.py", line 501, in from_engine_args return engine_cls.from_vllm_config( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/data/users/quinnzhu/gitrepos/vllm/vllm/v1/engine/llm_engine.py", line 124, in from_vllm_config return cls(vllm_config=vllm_config, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/da...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: High chance of stuck at model download bug ### Your current environment ### 🐛 Describe the bug On the latest main branch, it happens ~20% of the time. The progress bar stuck at 0. No way to abort either. Have to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 7] Loading model from scratch... INFO 07-13 17:17:23 [cuda.py:295] Using Flash Attention backend on V1 engine. INFO 07-13 17:17:23 [weight_utils.py:296] Using model weights format ['*.safetensors'] model-00001-of-00004....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: model_runner.py:1737] Loading model from scratch... INFO 07-13 17:17:23 [cuda.py:295] Using Flash Attention backend on V1 engine. INFO 07-13 17:17:23 [weight_utils.py:296] Using model weights format ['*.safetensors'] mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s. development attention_kv_cache;model_support attention;cuda crash env_dependency Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ad bug ### Your current environment ### 🐛 Describe the bug On the latest main branch, it happens ~20% of the time. The progress bar stuck at 0. No way to abort either. Have to `crtl+z` then force kill. ``` INFO 07-13 17...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

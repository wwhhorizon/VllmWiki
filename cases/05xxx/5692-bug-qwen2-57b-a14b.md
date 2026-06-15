# vllm-project/vllm#5692: [Bug]:Qwen2-57B-A14B 两卡 推理报错

| 字段 | 值 |
| --- | --- |
| Issue | [#5692](https://github.com/vllm-project/vllm/issues/5692) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:Qwen2-57B-A14B 两卡 推理报错

### Issue 正文摘录

### Your current environment 环境： torch 2.3.0 vllm 0.5.0.post1 transformers 4.41.2 主要报错情况： moe小一点的模型 '/data/models/qwen/qwen1.5-2.7Bmoe' 不会出问题 对于大一点的就报错如最下面。 代码： from vllm.engine.arg_utils import AsyncEngineArgs from vllm.engine.async_llm_engine import AsyncLLMEngine from vllm.transformers_utils.tokenizer import get_tokenizer engine_args = AsyncEngineArgs( model='/data/models/Qwen/Qwen2-57B-A14B', tokenizer_mode='auto', trust_remote_code=True, dtype='bfloat16', tensor_parallel_size=2, gpu_memory_utilization=0.90 ) engine = AsyncLLMEngine.from_engine_args(engine_args) 报错信息 见最下方。麻烦大神了 ### 🐛 Describe the bug 2024-06-20 02:53:02,678 INFO worker.py:1724 -- Started a local Ray instance. INFO 06-20 02:53:03 config.py:623] Defaulting to use mp for distributed inference INFO 06-20 02:53:03 llm_engine.py:161] Initializing an LLM engine (v0.5.0.post1) with config: model='/data/models/Qwen/Qwen2-57B-A14B', speculative_config=None, tokenizer='/data/models/Qwen/Qwen2-57B-A14B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: n/qwen1.5-2.7Bmoe' 不会出问题 对于大一点的就报错如最下面。 代码： from vllm.engine.arg_utils import AsyncEngineArgs from vllm.engine.async_llm_engine import AsyncLLMEngine from vllm.transformers_utils.tokenizer import get_tokenizer engine_ar...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: n2-57B-A14B', tokenizer_mode='auto', trust_remote_code=True, dtype='bfloat16', tensor_parallel_size=2, gpu_memory_utilization=0.90 ) engine = AsyncLLMEngine.from_engine_args(engine_args) 报错信息 见最下方。麻烦大神了 ### 🐛 Describe t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]:Qwen2-57B-A14B 两卡 推理报错 bug;stale ### Your current environment 环境： torch 2.3.0 vllm 0.5.0.post1 transformers 4.41.2 主要报错情况： moe小一点的模型 '/data/models/qwen/qwen1.5-2.7Bmoe' 不会出问题 对于大一点的就报错如最下面。 代码： from vllm.engine.ar...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: =False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), seed=0, served_model_name=/data/models/Qwen/Qwen2-57B-A14B) Special toke...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]:Qwen2-57B-A14B 两卡 推理报错 bug;stale ### Your current environment 环境： torch 2.3.0 vllm 0.5.0.post1 transformers 4.41.2 主要报错情况： moe小一点的模型 '/data/models/qwen/qwen1.5-2.7Bmoe' 不会出问题 对于大一点的就报错如最下面。 代码： from vllm.engine.ar...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

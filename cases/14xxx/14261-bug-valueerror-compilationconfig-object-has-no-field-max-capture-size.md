# vllm-project/vllm#14261: [Bug]: ValueError: "CompilationConfig" object has no field "max_capture_size"

| 字段 | 值 |
| --- | --- |
| Issue | [#14261](https://github.com/vllm-project/vllm/issues/14261) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: "CompilationConfig" object has no field "max_capture_size"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm using vllm==0.7.3 like this: ```python llm = LLM( model="/path/to/my/local/model", tokenizer="/path/to/my/tokenizer", tokenizer_mode="slow", tensor_parallel_size=1, trust_remote_code=True, dtype="bf16", max_model_len=1024, disable_log_stats=False, skip_tokenizer_init=2, disable_custom_all_reduce=True, enforce_eager=True, enable_chunked_prefill=False ) ``` And I got the error: ``` File "/home/jinyu121/pipeline_vllm.py", line 170, in __init__ self.llm = LLM( ^^^^ File "/usr/local/lib/python3.11/dist-packages/vllm/utils.py", line 1022, in inner return fn(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.11/dist-packages/vllm/entrypoints/llm.py", line 242, in __init__ self.llm_engine = self.engine_class.from_engine_args( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.11/dist-packages/vllm/v1/engine/llm_engine.py", line 90, in from_engine_args vllm_config = engine_args.create_engine_config(usage_context) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.11/dist-packages/vllm/engine/arg_utils.py", line 1334, in create_engine_config config = VllmConfig( ^^^^^^^^^^^ File "...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;frontend_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;slowdown dtype;env_dependency Your curr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: tensor_parallel_size=1, trust_remote_code=True, dtype="bf16", max_model_len=1024, disable_log_stats=False, skip_tokenizer_init=2, disable_custom_all_reduce=True, enforce_eager=True, enable_chunke
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: dist-packages/vllm/config.py", line 3309, in __post_init__ self._set_cudagraph_sizes() File "/usr/local/lib/python3.11/dist-packages/vllm/config.py", line 3401, in _set_cudagraph_sizes self.compilation_config.init_with_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: ValueError: "CompilationConfig" object has no field "max_capture_size" bug ### Your current environment ### 🐛 Describe the bug I'm using vllm==0.7.3 like this: ```python llm = LLM( model="/path/to/my/local/model",
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: reduce=True, enforce_eager=True, enable_chunked_prefill=False ) ``` And I got the error: ``` File "/home/jinyu121/pipeline_vllm.py", line 170, in __init__ self.llm = LLM( ^^^^ File "/usr/local/lib/python3.11/dist-packag...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

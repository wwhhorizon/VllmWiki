# vllm-project/vllm#5363: [Bug]: Falcon fails if `trust_remote_code=True`

| 字段 | 值 |
| --- | --- |
| Issue | [#5363](https://github.com/vllm-project/vllm/issues/5363) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | debug |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Falcon fails if `trust_remote_code=True`

### Issue 正文摘录

### Your current environment v0.4.3 ### 🐛 Describe the bug ```python from vllm import LLM model = LLM("tiiuae/falcon-7b", trust_remote_code=True) ``` ```bash --- Logging error --- Traceback (most recent call last): File "/home/rshaw/.pyenv/versions/3.10.14/lib/python3.10/logging/__init__.py", line 1100, in emit msg = self.format(record) File "/home/rshaw/.pyenv/versions/3.10.14/lib/python3.10/logging/__init__.py", line 943, in format return fmt.format(record) File "/home/rshaw/.pyenv/versions/vllm-upstream-pip/lib/python3.10/site-packages/vllm/logging/formatter.py", line 11, in format msg = logging.Formatter.format(self, record) File "/home/rshaw/.pyenv/versions/3.10.14/lib/python3.10/logging/__init__.py", line 678, in format record.message = record.getMessage() File "/home/rshaw/.pyenv/versions/3.10.14/lib/python3.10/logging/__init__.py", line 368, in getMessage msg = msg % self.args TypeError: %d format: a real number is required, not list Call stack: File " ", line 1, in File "/home/rshaw/.pyenv/versions/vllm-upstream-pip/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 144, in __init__ self.llm_engine = LLMEngine.from_engine_args( File "/home/rshaw/.pyenv/versions/v...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: one, rope_scaling=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=2048, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, disable_custom_all_reduce=False, q...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ironment v0.4.3 ### 🐛 Describe the bug ```python from vllm import LLM model = LLM("tiiuae/falcon-7b", trust_remote_code=True) ``` ```bash --- Logging error --- Traceback (most recent call last): File "/home/rshaw/.pyenv...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: current environment v0.4.3 ### 🐛 Describe the bug ```python from vllm import LLM model = LLM("tiiuae/falcon-7b", trust_remote_code=True) ``` ```bash --- Logging error --- Traceback (most recent call last): File "/home/r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Falcon fails if `trust_remote_code=True` bug;stale ### Your current environment v0.4.3 ### 🐛 Describe the bug ```python from vllm import LLM model = LLM("tiiuae/falcon-7b", trust_remote_code=True) ``` ```bash ---...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), seed=0, served_model_name=tiiuae/falcon-7b) [rank0]: Traceback (most recent call last): [rank0]: File " ", line 1, in [rank0]...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

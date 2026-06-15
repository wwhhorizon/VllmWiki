# vllm-project/vllm#17246: [Bug]: Cannot found `flash_attn_interface` after adding stub files

| 字段 | 值 |
| --- | --- |
| Issue | [#17246](https://github.com/vllm-project/vllm/issues/17246) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | attention |
| 症状 | crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot found `flash_attn_interface` after adding stub files

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The following backtrace showing that `flash_attn_interface` cannot be found was observed after https://github.com/vllm-project/vllm/pull/17228 got merged: ``` Traceback (most recent call last): File "/mnt/vllm/benchmarks/./ds.py", line 3, in llm = LLM(model="/mnt/model/DeepSeek-R1/DeepSeek-R1-UD-Q2_K_XL.gguf", File "/mnt/vllm/vllm/utils.py", line 1161, in inner return fn(*args, **kwargs) File "/mnt/vllm/vllm/entrypoints/llm.py", line 247, in __init__ self.llm_engine = LLMEngine.from_engine_args( File "/mnt/vllm/vllm/engine/llm_engine.py", line 516, in from_engine_args return engine_cls.from_vllm_config( File "/mnt/vllm/vllm/engine/llm_engine.py", line 492, in from_vllm_config return cls( File "/mnt/vllm/vllm/engine/llm_engine.py", line 281, in __init__ self.model_executor = executor_class(vllm_config=vllm_config, ) File "/mnt/vllm/vllm/executor/executor_base.py", line 286, in __init__ super().__init__(*args, **kwargs) File "/mnt/vllm/vllm/executor/executor_base.py", line 52, in __init__ self._init_executor() File "/mnt/vllm/vllm/executor/mp_distributed_executor.py", line 123, in _init_executor self._run_workers("init_worker", all...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: in get_attn_backend_cls from vllm.attention.backends.rocm_aiter_mla import ( File "/mnt/vllm/vllm/attention/backends/rocm_aiter_mla.py", line 11, in from vllm.attention.backends.mla.common import (MLACommonBackend, File...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: /vllm/vllm/worker/model_runner.py", line 1071, in __init__ self.attn_backend = get_attn_backend( File "/mnt/vllm/vllm/attention/selector.py", line 95, in get_attn_backend return _cached_get_attn_backend( File "/mnt/vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: current_platform.get_attn_backend_cls( File "/mnt/vllm/vllm/platforms/rocm.py", line 145, in get_attn_backend_cls from vllm.attention.backends.rocm_aiter_mla import ( File "/mnt/vllm/vllm/attention/backends/rocm_aiter_m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: last): File "/mnt/vllm/benchmarks/./ds.py", line 3, in llm = LLM(model="/mnt/model/DeepSeek-R1/DeepSeek-R1-UD-Q2_K_XL.gguf", File "/mnt/vllm/vllm/utils.py", line 1161, in inner return fn(*args, **kwargs) File "/mnt/vllm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 228 got merged: ``` Traceback (most recent call last): File "/mnt/vllm/benchmarks/./ds.py", line 3, in llm = LLM(model="/mnt/model/DeepSeek-R1/DeepSeek-R1-UD-Q2_K_XL.gguf", File "/mnt/vllm/vllm/utils.py", line 1161, in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#8736: [Bug]: InternVl2-8B-AWQ gives error when trying to run with vllm-openai cuda 11.8 docker image

| 字段 | 值 |
| --- | --- |
| Issue | [#8736](https://github.com/vllm-project/vllm/issues/8736) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;model_support;multimodal_vlm;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: InternVl2-8B-AWQ gives error when trying to run with vllm-openai cuda 11.8 docker image

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Process SpawnProcess-1: Traceback (most recent call last): File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 319, in run_mp_engine engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 113, in from_engine_args return cls( ^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 69, in __init__ self.engine = LLMEngine(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/engine/llm_engine.py", line 317, in __init__ self.model_executor = executor_class( ^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/executor/executor_base.py", line 47, in __init__ self._init_executor() File "/usr/local/lib/python3.12/dist-p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ternVl2-8B-AWQ gives error when trying to run with vllm-openai cuda 11.8 docker image bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Process SpawnProcess-1: Traceback (most r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: InternVl2-8B-AWQ gives error when trying to run with vllm-openai cuda 11.8 docker image bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Process SpawnProcess-1: Traceback
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: InternVl2-8B-AWQ gives error when trying to run with vllm-openai cuda 11.8 docker image bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Process SpawnProcess-1: Tracebac...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ns. development attention_kv_cache;ci_build;model_support;multimodal_vlm;quantization attention;cuda;quantization crash env_dependency Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development attention_kv_cache;ci_build;model_support;multimodal_vlm;quantization att...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

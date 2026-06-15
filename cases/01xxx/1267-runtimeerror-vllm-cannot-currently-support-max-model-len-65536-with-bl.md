# vllm-project/vllm#1267: RuntimeError: vLLM cannot currently support max_model_len=65536 with block_size=16 on GPU with compute capability (8, 9) (required shared memory 264252.0 > available shared memory 101376).

| 字段 | 值 |
| --- | --- |
| Issue | [#1267](https://github.com/vllm-project/vllm/issues/1267) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | sampling |
| 症状 | crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> RuntimeError: vLLM cannot currently support max_model_len=65536 with block_size=16 on GPU with compute capability (8, 9) (required shared memory 264252.0 > available shared memory 101376).

### Issue 正文摘录

I tried running this [model](https://huggingface.co/Open-Orca/LlongOrca-7B-16k) on **1 x RTX 6000 Ada** as: ``` from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="Open-Orca/LlongOrca-7B-16k") ``` But getting this below error once the model loading completes. ``` INFO 10-05 12:28:40 llm_engine.py:205] # GPU blocks: 3028, # CPU blocks: 512 Traceback (most recent call last): File " ", line 1, in File "/env/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 89, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/env/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 229, in from_engine_args engine = cls(*engine_configs, File "/env/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 111, in __init__ self._init_cache() File "/env/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 217, in _init_cache self._run_workers("init_cache_engine", cache_config=self.cache_config) File "/env/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 692, in _run_workers output = executor(*args, **kwargs) File "/env/lib/python3.10/site-packages/vllm/worker/worker.py",...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: RuntimeError: vLLM cannot currently support max_model_len=65536 with block_size=16 on GPU with compute capability (8, 9) (required shared memory 264252.0 > available shared memory 101376). I tried running this [model](h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ently support max_model_len=65536 with block_size=16 on GPU with compute capability (8, 9) (required shared memory 264252.0 > available shared memory 101376). I tried running this [model](https://huggingface.co/Open-Orc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: co/Open-Orca/LlongOrca-7B-16k) on **1 x RTX 6000 Ada** as: ``` from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="Open-Orca/LlongOrca-7B-16k") ``` But get...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: RuntimeError: vLLM cannot currently support max_model_len=65536 with block_size=16 on GPU with compute capability (8, 9) (required shared memory 264252.0 > available shared memory 101376). I tried running this [model](h...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

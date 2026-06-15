# vllm-project/vllm#31344: [Usage]: how to pass param logits_processors in  AsyncEngineArgs?

| 字段 | 值 |
| --- | --- |
| Issue | [#31344](https://github.com/vllm-project/vllm/issues/31344) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to pass param logits_processors in  AsyncEngineArgs?

### Issue 正文摘录

### Your current environment import torch from transformers import LogitsProcessor from transformers.generation.logits_process import _calc_banned_ngram_tokens from typing import List, Set class NoRepeatNGramLogitsProcessor(LogitsProcessor): def __init__(self, ngram_size: int, window_size: int = 100, whitelist_token_ids: set = None): if not isinstance(ngram_size, int) or ngram_size torch.FloatTensor: if len(input_ids) , #高版本 logits_processors_config: list[Dict[str, Any]] = [ { "class": NoRepeatNGramLogitsProcessor, # 传入类对象 "kwargs": { # 初始化参数 "ngram_size": 30, "window_size": 90, "whitelist_token_ids": {128821, 128822} } } ] engine_args = AsyncEngineArgs( model=MODEL_PATH, #hf_overrides={"architectures": ["DeepseekOCRForCausalLM"]}, block_size=256, max_model_len=8192, enforce_eager=False, trust_remote_code=True, tensor_parallel_size=1, gpu_memory_utilization=0.75, logits_processors=logits_processors_config ) engine = AsyncLLMEngine.from_engine_args(engine_args) error: ".local/lib/python3.13/site-packages/vllm/engine/arg_utils.py", line 1189, in create_model_config return ModelConfig( model=self.model, ... ... io_processor_plugin=self.io_processor_plugin, ) File "/.local/lib/python3...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: r: if len(input_ids) , #高版本 logits_processors_config: list[Dict[str, Any]] = [ { "class": NoRepeatNGramLogitsProcessor, # 传入类对象 "kwargs": { # 初始化参数 "ngram_size": 30, "window_size":
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: #hf_overrides={"architectures": ["DeepseekOCRForCausalLM"]}, block_size=256, max_model_len=8192, enforce_eager=False, trust_remote_code=True, tensor_parallel_size=1, gpu_memory_utilization=0.75, logits_proce
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Your current environment import torch from transformers import LogitsProcessor from transformers.generation.logits_process import _calc_banned_ngram_tokens from typing import List, Set class NoRepeatNGramLogitsProcessor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: yncEngineArgs( model=MODEL_PATH, #hf_overrides={"architectures": ["DeepseekOCRForCausalLM"]}, block_size=256, max_model_len=8192, enforce_eager=False, trust_remote_code=True, tensor_parallel_size=1,
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: how to pass param logits_processors in AsyncEngineArgs? usage;stale ### Your current environment import torch from transformers import LogitsProcessor from transformers.generation.logits_process import _calc_ba...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

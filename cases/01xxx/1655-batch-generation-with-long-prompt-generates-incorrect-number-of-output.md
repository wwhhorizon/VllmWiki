# vllm-project/vllm#1655: Batch generation with long prompt generates incorrect number of outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#1655](https://github.com/vllm-project/vllm/issues/1655) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;model_support;sampling_logits;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;sampling |
| 症状 | mismatch |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Batch generation with long prompt generates incorrect number of outputs

### Issue 正文摘录

When a prompt in a batch generation is too long for the model, `llm.generate` returns an unexpected number of outputs: ```python In [11]: prompts = ["This is a short prompt", "This is a very long prompt " * 1000] ...: print(len(prompts)) 2 In [12]: outputs = llm.generate(prompts, sampling_params=sampling_params, use_tqdm=False) WARNING 11-14 04:11:47 scheduler.py:146] Input prompt (6002 tokens) is too long and exceeds limit of 4096 In [13]: print(len(outputs)) 3 ``` It appears the too-long prompt gets doubled up in the output: ```python In [14]: prompts = ["This is a short prompt", "This is a very long prompt " * 1000, "Here's another short ...: prompt"] ...: print(len(prompts)) 3 In [15]: outputs = llm.generate(prompts, sampling_params=sampling_params, use_tqdm=False) WARNING 11-14 04:15:02 scheduler.py:146] Input prompt (6002 tokens) is too long and exceeds limit of 4096 In [16]: outputs[0].prompt[:100] Out[16]: 'This is a short prompt' In [17]: outputs[1].prompt[:100] Out[17]: 'This is a very long prompt This is a very long prompt This is a very long prompt This is a very long' In [18]: outputs[2].prompt[:100] Out[18]: 'This is a very long prompt This is a very long prompt This...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: any prompt was encountered over the size limit. Here's a minimum reproducible script: ```python from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0.01, top_p=0.1, max_tokens=256) llm = LL...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: pip freeze | grep vllm vllm==0.2.1.post1 (eb) kwood@kwood-lab:~$ nvidia-smi Tue Nov 14 04:22:19 2023 +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 535.129.03 Driv...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: umber of outputs When a prompt in a batch generation is too long for the model, `llm.generate` returns an unexpected number of outputs: ```python In [11]: prompts = ["This is a short prompt", "This is a very long prompt...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: after any prompt was encountered over the size limit. Here's a minimum reproducible script: ```python from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0.01, top_p=0.1, max_tokens=256) ll...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: PU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=======================================================================================| | No running processes fou

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

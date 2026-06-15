# vllm-project/vllm#8472: [Bug]: AMD with multi-step enabled crashes

| 字段 | 值 |
| --- | --- |
| Issue | [#8472](https://github.com/vllm-project/vllm/issues/8472) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AMD with multi-step enabled crashes

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Using multi-step on AMD gpu is crashing, the following script reproduce the issue: ``` from vllm import LLM, SamplingParams llm = LLM(model="facebook/opt-125M", disable_sliding_window=True, num_scheduler_steps=8 ) params = SamplingParams(seed=123, max_tokens=500, temperature=1) prompts = ["How to make pizza?"] outputs = llm.generate(prompts, sampling_params=params ) for o in outputs: print('_________') print('### Text') print('_________') for o2 in o.outputs: print(o2.text) ``` The stacktrace: ``` [rank0]: Traceback (most recent call last): [rank0]: File "/tmp/test_async_multi_step2.py", line 11, in [rank0]: outputs = llm.generate(prompts, sampling_params=params ) [rank0]: File "/vllm-workspace/vllm/utils.py", line 1030, in inner [rank0]: return fn(*args, **kwargs) [rank0]: File "/vllm-workspace/vllm/entrypoints/llm.py", line 345, in generate [rank0]: outputs = self._run_engine(use_tqdm=use_tqdm) [rank0]: File "/vllm-workspace/vllm/entrypoints/llm.py", line 686, in _run_engine [rank0]: step_outputs = self.llm_engine.step() [rank0]: File "/vllm-workspace/vllm/engine/llm_engine.py", line 1369, in...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: u is crashing, the following script reproduce the issue: ``` from vllm import LLM, SamplingParams llm = LLM(model="facebook/opt-125M", disable_sliding_window=True, num_scheduler_steps=8 ) params = SamplingParams(seed=12...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: tadata.advance_step(num_seqs, num_queries) [rank0]: AttributeError: 'ROCmFlashAttentionMetadata' object has no attribute 'advance_step' ``` --- I did a priori investigation to the issue and I think that I found the caus...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: AMD with multi-step enabled crashes bug;rocm ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Using multi-step on AMD gpu is crashing, the following script reproduce the iss...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ulti_step_model_runner.py", line 362, in _advance_step [rank0]: attn_metadata.advance_step(num_seqs, num_queries) [rank0]: AttributeError: 'ROCmFlashAttentionMetadata' object has no attribute 'advance_step' ``` --- I di...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: acebook/opt-125M", disable_sliding_window=True, num_scheduler_steps=8 ) params = SamplingParams(seed=123, max_tokens=500, temperature=1) prompts = ["How to make pizza?"] outputs = llm.generate(prompts, sampling_params=p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

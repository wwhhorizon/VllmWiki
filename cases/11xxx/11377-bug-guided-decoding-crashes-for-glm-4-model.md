# vllm-project/vllm#11377: [Bug]: Guided decoding crashes for GLM-4 model

| 字段 | 值 |
| --- | --- |
| Issue | [#11377](https://github.com/vllm-project/vllm/issues/11377) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Guided decoding crashes for GLM-4 model

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi, I got a similar bug as described in https://github.com/vllm-project/vllm/issues/11045, when trying to use guided decoding with the glm-4-9b-chat model. I'm using vllm 0.6.5. - Error when using `BACKEND='xgrammar'` ```plaintext [rank0]: File "/home/sherry/miniconda3/envs/pytorch2.5_cuda12.1/lib/python3.10/site-packages/vllm/worker/model_runner.py", line 1729, in execute_model [rank0]: logits = self.model.compute_logits(hidden_or_intermediate_states, [rank0]: File "/home/sherry/miniconda3/envs/pytorch2.5_cuda12.1/lib/python3.10/site-packages/vllm/model_executor/models/chatglm.py", line 649, in compute_logits [rank0]: logits = self.logits_processor(self.lm_head, hidden_states, [rank0]: File "/home/sherry/miniconda3/envs/pytorch2.5_cuda12.1/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl [rank0]: return self._call_impl(*args, **kwargs) [rank0]: File "/home/sherry/miniconda3/envs/pytorch2.5_cuda12.1/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl [rank0]: return forward_call(*args, **kwargs) [rank0]: File "/home/sherry...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ed_decoding/xgrammar_decoding.py", line 229, in _ensure_ctx [rank0]: compiler = GrammarCompilerCache.get_compiler(self.config) [rank0]: File "/home/sherry/miniconda3/envs/pytorch2.5_cuda12.1/lib/python3.10/site-packages...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Guided decoding crashes for GLM-4 model bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi, I got a similar bug as described in https://github.com/vllm-project/vllm/iss...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ` ```plaintext [rank0]: File "/home/sherry/miniconda3/envs/pytorch2.5_cuda12.1/lib/python3.10/site-packages/vllm/worker/model_runner.py", line 1729, in execute_model [rank0]: logits = self.model.compute_logits(hidden_or...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: h the glm-4-9b-chat model. I'm using vllm 0.6.5. - Error when using `BACKEND='xgrammar'` ```plaintext [rank0]: File "/home/sherry/miniconda3/envs/pytorch2.5_cuda12.1/lib/python3.10/site-packages/vllm/worker/model_runner...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: forward [rank0]: logits = _apply_logits_processors(logits, sampling_metadata) [rank0]: File "/home/sherry/miniconda3/envs/pytorch2.5_cuda12.1/lib/python3.10/site-packages/vllm/model_executor/layers/logits_processor.py",...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

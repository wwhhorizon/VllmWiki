# vllm-project/vllm#40905: [Bug]: IMA in _causal_conv1d_fwd_kernel for long sequence input

| 字段 | 值 |
| --- | --- |
| Issue | [#40905](https://github.com/vllm-project/vllm/issues/40905) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: IMA in _causal_conv1d_fwd_kernel for long sequence input

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Description When running Mamba-based models (e.g., Mamba or Jamba) with long input sequences, vLLM crashes with a CUDA illegal memory access (IMA) inside the Triton kernel _causal_conv1d_fwd_kernel. ### Minimal reproduction: #### Case 1: Mamba model on B200 ```python modelId = "state-spaces/mamba-130m-hf" batch_size = 1 seq_len = 1399013 single_prompt = "word "*seq_len single_prompt = single_prompt.strip() llm = LLM(model=modelId, trust_remote_code=True, hf_token=HF_TOKEN, attention_config={"backend":"FLASH_ATTN"}, max_model_len = seq_len enforce_eager = True) sampling_params = SamplingParams(temperature=0) out = llm.generate([single_prompt]*batch_size, sampling_params) ``` output: ``` Traceback (most recent call last): File "/workspace/./run_vllm.py", line 29, in out = llm.generate([single_prompt]*batch_size, sampling_params) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.11/site-packages/vllm/entrypoints/llm.py", line 500, in generate return self._run_completion( ^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.11/site-packages/vllm/entrypoints/llm.py", line 1859, in _run_completion...

## 现有链接修复摘要

#41617 [Bugfix][Mamba] IMA in causal_conv1d kernel for long sequences

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nt ### 🐛 Describe the bug ### Description When running Mamba-based models (e.g., Mamba or Jamba) with long input sequences, vLLM crashes with a CUDA illegal memory access (IMA) inside the Triton kernel _causal_conv1d_fw...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;kernel;operator;sa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ls (e.g., Mamba or Jamba) with long input sequences, vLLM crashes with a CUDA illegal memory access (IMA) inside the Triton kernel _causal_conv1d_fwd_kernel. ### Minimal reproduction: #### Case 1: Mamba model on B200 ``...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 3.11/site-packages/vllm/v1/engine/core.py", line 451, in step_with_batch_queue (EngineCore pid=2761) exec_future = self.model_executor.execute_model( (EngineCore pid=2761) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: quences, vLLM crashes with a CUDA illegal memory access (IMA) inside the Triton kernel _causal_conv1d_fwd_kernel. ### Minimal reproduction: #### Case 1: Mamba model on B200 ```python modelId = "state-spaces/mamba-130m-h...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41617](https://github.com/vllm-project/vllm/pull/41617) | closes_keyword | 0.95 | [Bugfix][Mamba] IMA in causal_conv1d kernel for long sequences | Fixes #40905 When running Mamba-based models (Mamba/Jamba) with ultra-long sequences (verified at 1.4M tokens), the _causal_conv1d_fwd_kernel triggers a CUDA Illegal Memory Acc |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

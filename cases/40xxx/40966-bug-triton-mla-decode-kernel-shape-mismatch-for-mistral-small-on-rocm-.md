# vllm-project/vllm#40966: [Bug]: Triton MLA decode kernel shape mismatch for Mistral-Small on ROCm when TP > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#40966](https://github.com/vllm-project/vllm/issues/40966) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | precision |
| Operator 关键词 | attention;kernel;operator;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Triton MLA decode kernel shape mismatch for Mistral-Small on ROCm when TP > 1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Reproduce command ``` export VLLM_USE_V1=1 vllm serve /app/model/models--mistralai--Mistral-Small-4-119B-2603/snapshots/8563dea9670952202c9b76635b3f444a2fb40973 \ --tensor-parallel-size 2 \ --max-model-len 32768 \ --gpu-memory-utilization 0.90 \ --port 8800 \ --trust-remote-code \ --enable-prefix-caching \ --enable-chunked-prefill \ --max-num-seqs 128 \ --max-num-batched-tokens 8192 \ --enable-auto-tool-choice \ --tool-call-parser mistral \ --reasoning-parser mistral \ 2>&1 | tee vllm_debug_Mistral.log ``` Specific error message ``` (Worker_TP1 pid=4504) ERROR 04-22 11:16:00 [multiproc_executor.py:971] return self._call_impl(*args, **kwargs) (Worker_TP1 pid=4504) ERROR 04-22 11:16:00 [multiproc_executor.py:971] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP1 pid=4504) ERROR 04-22 11:16:00 [multiproc_executor.py:971] File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1787, in _call_impl (Worker_TP1 pid=4504) ERROR 04-22 11:16:00 [multiproc_executor.py:971] return forward_call(*args, **kwargs) (Worker_TP1 pid=4504) ERROR 04-22 11:16:00 [multiproc_executor.py:971] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP1 p...

## 现有链接修复摘要

#41119 [ROCm][Bugfix]: dynamically align BLOCK_DMODEL with Lv in MLA decode kernel

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: --reasoning-parser mistral \ 2>&1 | tee vllm_debug_Mistral.log ``` Specific error message ``` (Worker_TP1 pid=4504) ERROR 04-22 11:16:00 [multiproc_executor.py:971] return self._call_impl(*args, **kwargs) (Worker_TP1 pi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Triton MLA decode kernel shape mismatch for Mistral-Small on ROCm when TP > 1 bug;rocm ### Your current environment ### 🐛 Describe the bug Reproduce command ``` export VLLM_USE_V1=1 vllm serve /app/model/models--...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Triton MLA decode kernel shape mismatch for Mistral-Small on ROCm when TP > 1 bug;rocm ### Your current environment ### 🐛 Describe the bug Reproduce command ``` export VLLM_USE_V1=1 vllm serve /app/model/models--...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 22 11:16:00 [multiproc_executor.py:971] v = (v.to(tl.float32) * vs).to(q.dtype) (Worker_TP1 pid=4504) ERROR 04-22 11:16:00 [multiproc_executor.py:971] else: (Worker_TP1 pid=4504) ERROR 04-22 11:16:00 [multiproc_executor...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: pid=4504) ERROR 04-22 11:16:00 [multiproc_executor.py:971] attn_out, lse = self.impl.forward_mqa(mqa_q, kv_cache, attn_metadata, self) (Worker_TP1 pid=4504) ERROR 04-22 11:16:00 [multiproc_executor.py:971] ^^^^^^^^^^^^^...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41119](https://github.com/vllm-project/vllm/pull/41119) | closes_keyword | 0.95 | [ROCm][Bugfix]: dynamically align BLOCK_DMODEL with Lv in MLA decode kernel | Fixes #40966 This PR resolves a Triton compilation error, `ValueError('Cannot make_shape_compatible: incompatible dimensions at index 1: 256 and 512')` occurring in MLA-based |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

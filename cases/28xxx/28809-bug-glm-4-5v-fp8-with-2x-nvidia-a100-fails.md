# vllm-project/vllm#28809: [Bug]: GLM-4.5V-FP8 with 2x NVIDIA A100 Fails

| 字段 | 值 |
| --- | --- |
| Issue | [#28809](https://github.com/vllm-project/vllm/issues/28809) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM-4.5V-FP8 with 2x NVIDIA A100 Fails

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Error: ``` buf9 = torch.ops._C.gptq_marlin_gemm.default(buf8, None, arg11_1, None, arg12_1, None, None, None, None, arg13_1, 2814749767172868, s18, 4096, 5472, True, False, True, False) (Worker_TP0 pid=172) ERROR 11-16 05:07:59 [multiproc_executor.py:712] File "/usr/local/lib/python3.12/dist-packages/torch/_ops.py", line 841, in __call__ (Worker_TP0 pid=172) ERROR 11-16 05:07:59 [multiproc_executor.py:712] return self._op(*args, **kwargs) (Worker_TP0 pid=172) ERROR 11-16 05:07:59 [multiproc_executor.py:712] ^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=172) ERROR 11-16 05:07:59 [multiproc_executor.py:712[] RuntimeError: Invalid thread config: thread_m_blocks = 1, thread_k = -1, thread_n = -1, num_threads = -1 for MKN = [2048, 5472, 4096] and num_bits = 8, prob_m_split = 2048, group_size = -1, has_act_order = 0, is_k_full = 1, has_zp = 0, is_zp_float = 0, max_shared_mem_new = 166912 ``` Command: `python3 -m vllm.entrypoints.openai.api_server --port 5000 --host 0.0.0.0 --download-dir /workspace/.cache/huggingface/hub --model zai-org/GLM-4.5V-FP8 --tensor-parallel-size 2 --trust-remote-code --enable-chunked-prefill --enable-prefix-cachi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 11-16 05:07:59 [multiproc_executor.py:712[] RuntimeError: Invalid thread config: thread_m_blocks = 1, thread_k = -1, thread_n = -1, num_threads = -1 for MKN = [2048, 5472, 4096] and num_bits = 8, prob_m_split = 2048, gr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_me...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: GLM-4.5V-FP8 with 2x NVIDIA A100 Fails bug ### Your current environment ### 🐛 Describe the bug Error: ``` buf9 = torch.ops._C.gptq_marlin_gemm.default(buf8, None, arg11_1, None, arg12_1, None, None, None, None, a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: GLM-4.5V-FP8 with 2x NVIDIA A100 Fails bug ### Your current environment ### 🐛 Describe the bug Error: ``` buf9 = torch.ops._C.gptq_marlin_gemm.default(buf8, None, arg11_1, None, arg12_1, None, None, None, None, a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: e, None, None, None, arg13_1, 2814749767172868, s18, 4096, 5472, True, False, True, False) (Worker_TP0 pid=172) ERROR 11-16 05:07:59 [multiproc_executor.py:712] File "/usr/local/lib/python3.12/dist-packages/torch/_ops.p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

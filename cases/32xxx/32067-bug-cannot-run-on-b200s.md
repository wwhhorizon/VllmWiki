# vllm-project/vllm#32067: [Bug]: Cannot Run on B200s

| 字段 | 值 |
| --- | --- |
| Issue | [#32067](https://github.com/vllm-project/vllm/issues/32067) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Cannot Run on B200s

### Issue 正文摘录

### 🐛 the bug I try to run vllm on B200 but it gives me weird error. The following is the minimal code to reproduce the error. ``` # test.py import os os.environ["UNSLOTH_VLLM_STANDBY"] = "1" from unsloth import FastLanguageModel from vllm import SamplingParams model_name = "unsloth/Qwen2-0.5B-Instruct" max_seq_length = 2048 model, tokenizer = FastLanguageModel.from_pretrained( model_name=model_name, max_seq_length=max_seq_length, load_in_4bit=False, fast_inference=True, dtype=None, ) test_prompts = [ "Hello, how are you?", "What is 2+2?", ] outputs = model.fast_generate( prompts=test_prompts, sampling_params=sampling_params, ) ``` Running `python test.py` gives me the following output: ``` 🦥 Unsloth: Will patch your computer to enable 2x faster free finetuning. INFO 01-09 15:52:27 [__init__.py:243] Automatically detected platform cuda. 🦥 Unsloth Zoo will now patch everything to make training faster! INFO 01-09 15:52:35 [vllm_utils.py:702] Unsloth: Patching vLLM v1 graph capture INFO 01-09 15:52:35 [vllm_utils.py:732] Unsloth: Patching vLLM v0 graph capture ==((====))== Unsloth 2025.12.9: Fast Qwen2 patching. Transformers: 4.57.3. vLLM: 0.9.0. \\ /| NVIDIA B200. Num GPUs = 8. Max...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: The following is the minimal code to reproduce the error. ``` # test.py import os os.environ["UNSLOTH_VLLM_STANDBY"] = "1" from unsloth import FastLanguageModel from vllm import SamplingParams model_name = "unsloth/Qwen...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 8: Linux. O^O/ \_/ \ Torch: 2.7.0+cu128. CUDA: 10.0. CUDA Toolkit: 12.8. Triton: 3.3.0 \ / Bfloat16 = TRUE. FA [Xformers = 0.0.30. FA2 = False] "-____-" Free license: http://github.com/unslothai/unsloth Unsloth: Fast downl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug]: Cannot Run on B200s bug ### 🐛 the bug I try to run vllm on B200 but it gives me weird error. The following is the minimal code to reproduce the error. ``` # test.py import os os.environ["UNSLOTH_VLLM_STANDBY"] =...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: s.environ["UNSLOTH_VLLM_STANDBY"] = "1" from unsloth import FastLanguageModel from vllm import SamplingParams model_name = "unsloth/Qwen2-0.5B-Instruct" max_seq_length = 2048 model, tokenizer = FastLanguageModel.from_pr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: gth=max_seq_length, load_in_4bit=False, fast_inference=True, dtype=None, ) test_prompts = [ "Hello, how are you?", "What is 2+2?", ] outputs = model.fast_generate( prompts=test_prompts, sampling_params=sampling_params,...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | /testbed/lib/python3.10/site-packages/torch/lib/libc10_cuda.so) frame #4: <unknown function> + 0x20e0b (0x731d34cf7e0b in /opt/conda/envs/testbed/lib/python3.10/site-packages/torc… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /testbed/lib/python3.10/site-packages/torch/lib/libc10_cuda.so) frame #6: c10::cuda::mempool::~mempool() + 0x1b9 (0x731d34cf9999 in /opt/conda/envs/testbed/lib/python3.10/site-pac… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | /testbed/lib/python3.10/site-packages/torch/lib/libc10_cuda.so) frame #7: <unknown function> + 0xbfe12a (0x731d9917e12a in /opt/conda/envs/testbed/lib/python3.10/site-packages/tor… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | ) frame #10: python() [0x50ed9a] frame #11: python() [0x4ea60b] frame #12: python() [0x4eb0b8] frame #13: python() [0x4eb126] frame #14: python() [0x50e78c] frame #15: python() [0… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | ] frame #14: python() [0x50e78c] frame #15: python() [0x59497e] frame #16: python() [0x5ba91b] frame #17: python() [0x4e1688] frame #18: python() [0x5c8cdc] <omitting python frame… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

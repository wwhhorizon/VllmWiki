# vllm-project/vllm#23194: [Bug]: [TPU] profiling_tpu/profiling.py example crashed when runs on vllm_tpu docker

| 字段 | 值 |
| --- | --- |
| Issue | [#23194](https://github.com/vllm-project/vllm/issues/23194) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: [TPU] profiling_tpu/profiling.py example crashed when runs on vllm_tpu docker

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running `vllm/examples/offline_inference/profiling_tpu/profiling.py` with `v6e-4` and `v2-alpha-v6e` inside the `vllm_tpu` Docker container causes the program to crash. ``` export XLA_HLO_DEBUG=1 export MODEL=Qwen/Qwen2.5-7B-Instruct export VLLM_TPU_PROFILE_DURATION_MS=3000 export VLLM_TPU_PROFILE_DELAY_MS=0 python3 profiling.py \ --model $MODEL \ --input-len 1024 --output-len 1 \ --batch-size 1 --enforce-eager \ --max-model-len 2048 \ --tensor-parallel-size 1 \ --profile-result-dir profiles ``` Error output log ``` root@t1v-n-e177828d-w-0:/workspace/vllm/examples/offline_inference/profiling_tpu# python3 profiling.py --model $MODEL --input-len 1024 --output-len 1 --batch-size 1 --enforce-eager --max-model-len 2048 --tensor-parallel-size 1 --profile-result-dir profiles WARNING:root:libtpu.so and TPU device found. Setting PJRT_DEVICE=TPU. INFO 08-19 17:27:53 [__init__.py:241] Automatically detected platform tpu. INFO 08-19 17:27:53 [tpu.py:208] tpu_commons not found, using vLLM's TpuPlatform Namespace(input_len=1024, output_len=1, batch_size=1, num_iters_warmup=5, num_iters=1, profile_result_dir='profiles', model='Qwen/Qwen2.5-7B-I...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention`

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: : [TPU] profiling_tpu/profiling.py example crashed when runs on vllm_tpu docker bug ### Your current environment ### 🐛 Describe the bug Running `vllm/examples/offline_inference/profiling_tpu/profiling.py` with `v6e-4` a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ontainer causes the program to crash. ``` export XLA_HLO_DEBUG=1 export MODEL=Qwen/Qwen2.5-7B-Instruct export VLLM_TPU_PROFILE_DURATION_MS=3000 export VLLM_TPU_PROFILE_DELAY_MS=0 python3 profiling.py \ --model $MODEL \...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: sk=None, tokenizer=None, tokenizer_mode='auto', trust_remote_code=False, dtype='auto', seed=None, hf_config_path=None, allowed_local_media_path='', revision=None, code_revision=None, rope_scaling={}, rope_theta=None, to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ='builtin', cpu_offload_gb=0, calculate_kv_scales=False, kv_sharing_fast_prefill=False, mamba_cache_dtype='auto', mamba_ssm_cache_dtype='auto', limit_mm_per_prompt={}, media_io_kwargs={}, mm_processor_kwargs=None, mm_pr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: None, use_tqdm_on_load=True, pt_load_map_location='cpu', guided_decoding_backend='auto', guided_decoding_disable_fallback=False, guided_decoding_disable_any_whitespace=False, guided_decoding_disable_additional_propertie...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | python3.12/site-packages/_xlac.cpython-312-x86_64-linux-gnu.so) frame #4: <unknown function> + 0x6bc100d (0x73c5df89200d in /usr/local/lib/python3.12/site-packages/_xlac.cpython-3… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

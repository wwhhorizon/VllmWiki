# vllm-project/vllm#32626: [Bug]: TRTLLM Attention Failure with DP/EP

| 字段 | 值 |
| --- | --- |
| Issue | [#32626](https://github.com/vllm-project/vllm/issues/32626) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;moe;quantization |
| 子分类 |  |
| Operator 关键词 | attention;moe |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TRTLLM Attention Failure with DP/EP

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Deploy with: ``` MODEL := "nvidia/Qwen3-30B-A3B-NVFP4" GPUS := "2" PORT := "8001" launch_dp_ep_: VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_FLASHINFER_MOE_BACKEND=masked_gemm chg run --gpus {{GPUS}} -- vllm serve {{MODEL}} -dp {{GPUS}} --enable-expert-parallel --port {{PORT}} --all2all-backend deepep_low_latency eval: lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args "model={{MODEL}},base_url=http://localhost:{{PORT}}/v1/completions,num_concurrent=1000,tokenized_requests=False" --limit 100 ``` you will hit ``` (EngineCore_DP1 pid=2893355) File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP1 pid=2893355) self.run() (EngineCore_DP1 pid=2893355) File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore_DP1 pid=2893355) self._target(*self._args, **self._kwargs) (EngineCore_DP1 pid=2893355) File "/home/robertgshaw2-redhat/vllm/vllm/v1/engine/core.py", line 939, in run_engine_core (EngineCore_DP1 pid=2893355) raise e (EngineCore_DP1 pid=2893355) File "/home/robertgshaw2-redhat/vllm/vllm/v1/engine/core.py", line 928, in run_engine_core (EngineCore_DP1 pid=28933...

## 现有链接修复摘要

#34009 [Bugfix] Fix DP Attention Padding in Dummy Run | #34187 [Bugfix] Fix DP Attention Padding in Dummy Run

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: in _dummy_run (EngineCore_DP1 pid=2893355) attn_metadata, _ = self._build_attention_metadata( (EngineCore_DP1 pid=2893355) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP1 pid=2893355) File "/home/robertgshaw2-redhat/vll...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ### 🐛 Describe the bug Deploy with: ``` MODEL := "nvidia/Qwen3-30B-A3B-NVFP4" GPUS := "2" PORT := "8001" launch_dp_ep_: VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_FLASHINFER_MOE_BACKEND=masked_gemm chg run --gpus {{GPUS}} -- vl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: # Your current environment ### 🐛 Describe the bug Deploy with: ``` MODEL := "nvidia/Qwen3-30B-A3B-NVFP4" GPUS := "2" PORT := "8001" launch_dp_ep_: VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_FLASHINFER_MOE_BACKEND=masked_gemm ch...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: -NVFP4" GPUS := "2" PORT := "8001" launch_dp_ep_: VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_FLASHINFER_MOE_BACKEND=masked_gemm chg run --gpus {{GPUS}} -- vllm serve {{MODEL}} -dp {{GPUS}} --enable-expert-parallel --port {{PORT...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: }} --enable-expert-parallel --port {{PORT}} --all2all-backend deepep_low_latency eval: lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args "model={{MODEL}},base_url=http://localhost:{{PORT}}/v1/completion...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34009](https://github.com/vllm-project/vllm/pull/34009) | closes_keyword | 0.95 | [Bugfix] Fix DP Attention Padding in Dummy Run | FIX #32626 FIX #33450 Problem: TRTLLM attention requires that num_decode_tokens be divisible by num_requests. However, during DP we sometimes do a dummy run on one of the workers |
| [#34187](https://github.com/vllm-project/vllm/pull/34187) | closes_keyword | 0.95 | [Bugfix] Fix DP Attention Padding in Dummy Run | FIX #32626 FIX #33450 Problem: TRTLLM attention requires that num_decode_tokens be divisible by num_requests. However, during DP we sometimes do a dummy run on one of the workers |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

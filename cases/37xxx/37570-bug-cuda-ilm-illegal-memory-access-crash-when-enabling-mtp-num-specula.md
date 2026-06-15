# vllm-project/vllm#37570: [Bug]: CUDA ILM (Illegal Memory Access) crash when enabling MTP num_speculative_tokens with >1 for zai-org/GLM-4.7-FP8 under load

| 字段 | 值 |
| --- | --- |
| Issue | [#37570](https://github.com/vllm-project/vllm/issues/37570) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: CUDA ILM (Illegal Memory Access) crash when enabling MTP num_speculative_tokens with >1 for zai-org/GLM-4.7-FP8 under load

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Description:** I am experiencing a critical crash (CUDA ILM / Illegal Memory Access error) when serving the `zai-org/GLM-4.7-FP8` model with Multi-Token Prediction (MTP) enabled and num_speculative_tokens with >1 under concurrent requests, same as (close to) https://github.com/vllm-project/vllm/issues/36613. The service runs perfectly fine MTP is enabled and has num_speculative_tokens==1. **Steps to Reproduce:** 1. Start the vLLM(0.17.1) server with the zai-org/GLM-4.7-FP8 model and the following speculative decoding configuration: ``` vllm serve zai-org/GLM-4.7-FP8 \ --tensor-parallel-size 8 \ --speculative-config.method mtp \ --speculative-config.num_speculative_tokens 2 \ --tool-call-parser glm47 \ --reasoning-parser glm45 \ --enable-auto-tool-choice \ --async-scheduling \ --enable-prefix-caching ``` Start benchmark with: ``` vllm bench serve \ --model zai-org/GLM-4.7-FP8 \ --port 8000 \ --save-result \ --save-detailed \ --backend=vllm \ --dataset-name custom \ --dataset-path SOME_DATASET \ --disable-shuffle \ --metric-percentiles "50,90,95,99" \ --percentile-metrics "ttft,tpot,e2el" \ --result-dir "./vllm_bench_results/" \...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: zai-org/GLM-4.7-FP8 \ --port 8000 \ --save-result \ --save-detailed \ --backend=vllm \ --dataset-name custom \ --dataset-path SOME_DATASET \ --disable-shuffle \ --metric-percentiles "50,90,95,99" \ --percentile-metrics...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nt environment ### 🐛 Describe the bug **Description:** I am experiencing a critical crash (CUDA ILM / Illegal Memory Access error) when serving the `zai-org/GLM-4.7-FP8` model with Multi-Token Prediction (MTP) enabled a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ash when enabling MTP num_speculative_tokens with >1 for zai-org/GLM-4.7-FP8 under load bug ### Your current environment ### 🐛 Describe the bug **Description:** I am experiencing a critical crash (CUDA ILM / Illegal Mem...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA ILM (Illegal Memory Access) crash when enabling MTP num_speculative_tokens with >1 for zai-org/GLM-4.7-FP8 under load bug ### Your current environment ### 🐛 Describe the bug **Description:** I am experiencin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: CUDA ILM (Illegal Memory Access) crash when enabling MTP num_speculative_tokens with >1 for zai-org/GLM-4.7-FP8 under load bug ### Your current environment ### 🐛 Describe the bug **Description:** I am experiencin...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | llm-env/.venv/lib/python3.12/site-packages/torch/lib/libc10.so) frame #4: c10::tensorimpl::~tensorimpl() + 0x9 (0x7fcc84f4e369 in /home/ssm-user/mikhail.podvitskii/vllm-env/.venv/… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | venv/lib/python3.12/site-packages/torch/lib/libtorch_python.so) frame #6: <unknown function> + 0x862fe1 (0x7fcbeb062fe1 in /home/ssm-user/mikhail.podvitskii/vllm-env/.venv/lib/pyt… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | venv/lib/python3.12/site-packages/torch/lib/libtorch_python.so) frame #7: vllm::worker_tp3() [0x1635231] frame #8: vllm::worker_tp3() [0x163537b] frame #9: _pyeval_evalframedefaul… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | in vllm::worker_tp3) frame #11: vllm::worker_tp3() [0x16ac442] frame #12: pyrun_stringflags + 0x7e (0x16ac2d6 in vllm::worker_tp3) frame #13: pyrun_simplestringflags + 0x3d (0x177… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | ] frame #15: py_runmain + 0x291 (0x1770c67 in vllm::worker_tp3) frame #16: vllm::worker_tp3() [0x173ecfa] frame #17: vllm::worker_tp3() [0x173eaed] frame #18: <unknown function> +… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | : __libc_start_main + 0x80 (0x7fccc562a6c0 in /lib64/libc.so.6) frame #20: _start + 0x29 (0x17ab069 in vllm::worker_tp3) ``` </details> **happy path:** start the vllm(0.17.1) serv… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

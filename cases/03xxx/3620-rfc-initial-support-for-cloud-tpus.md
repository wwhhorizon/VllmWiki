# vllm-project/vllm#3620: [RFC] Initial Support for Cloud TPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#3620](https://github.com/vllm-project/vllm/issues/3620) |
| 状态 | closed |
| 标签 | RFC;tpu;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cache;cuda;kernel;moe;operator;quantization |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC] Initial Support for Cloud TPUs

### Issue 正文摘录

# Progress - [x] Implement TPU executor that works on a single TPU chip (without tensor parallelism) #5292 - [x] Support single-host tensor parallel inference #5871 - [x] Support multi-host tensor parallel inference #7457 - [ ] Support INT8 quantization - [x] Support MoE models such as Mixtral #6457 - [ ] Benchmark and optimize the TPU backend performance # Project Scope This project focuses on making vLLM compatible with Google cloud TPUs. Our goal is seamless integration so users can easily run vLLM on TPUs for both online and offline inference. We will target common setups, like popular models such as Gemma, using the bfloat16 data type. ## Target TPUs and Models We will focus on the most recent generations of TPUs, namely **TPU v4, v5e, and v5p**, considering their superior performance to previous generations. We will start by making sure vLLM works with dense models such as Gemma. After that, we will expand support to Mixture-of-Experts (MoE) models such as Mixtral. ## Features Not Included (for now) The following features are outside the scope of this initial project, but we'd like to tackle them in the future: - Speculative decoding - GPTQ/AWQ Quantization - Multi-LoRA serv...

## 现有链接修复摘要

#5292 [Hardware] Initial TPU integration

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: r will spin up multiple TPU workers; **one TPU worker per TPU chip**. Specifically, we will use [Ray](https://github.com/ray-project/ray) to connect and manage the TPU workers which may reside in different TPU VMs. Note...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [RFC] Initial Support for Cloud TPUs RFC;tpu;stale # Progress - [x] Implement TPU executor that works on a single TPU chip (without tensor parallelism) #5292 - [x] Support single-host tensor parallel inference #5871 - [...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ] Support multi-host tensor parallel inference #7457 - [ ] Support INT8 quantization - [x] Support MoE models such as Mixtral #6457 - [ ] Benchmark and optimize the TPU backend performance # Project Scope This project f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ale # Progress - [x] Implement TPU executor that works on a single TPU chip (without tensor parallelism) #5292 - [x] Support single-host tensor parallel inference #5871 - [x] Support multi-host tensor parallel inference...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: allel inference #7457 - [ ] Support INT8 quantization - [x] Support MoE models such as Mixtral #6457 - [ ] Benchmark and optimize the TPU backend performance # Project Scope This project focuses on making vLLM compatibl...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5292](https://github.com/vllm-project/vllm/pull/5292) | mentioned | 0.45 | [Hardware] Initial TPU integration | executor that works on a single tpu chip (without tensor parallelism) #5292 - [x] support single-host tensor parallel inference #5871 - [x] support multi-host tensor parallel infe… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

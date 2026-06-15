# vllm-project/vllm#39749: [Roadmap] vLLM Roadmap Q2 2026

| 字段 | 值 |
| --- | --- |
| Issue | [#39749](https://github.com/vllm-project/vllm/issues/39749) |
| 状态 | open |
| 标签 | rocm |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe;operator;quantization |
| 症状 | build_error;nondeterministic;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Roadmap] vLLM Roadmap Q2 2026

### Issue 正文摘录

In #32455, we broke down vLLM’s goal into various special interest groups (SIGs). Please find below the SIG’s area and their roadmap. You can find regular meetings of these SIGs at [this public calendar](https://zoom-lfx.platform.linuxfoundation.org/meetings/vllm). ### Core Slack Channel: #sig-core Members: @WoosukKwon @njhill The team focuses on the vLLM Engine Core including Scheduler, KV Cache Manager, Distributed, Model Runner, KV Connector code path. - [ ] Model Runner V2 hardening and making it default: - [ ] expand testing coverage - [ ] support wide-ep out of the box. - [ ] Continuing to fill gaps [Model Runner V2 Design Docs](https://docs.google.com/document/d/1gFqtDkcoqhy9j-X0ndshzbhapX1uNey1-wBENwGPI80/edit?tab=t.192m4u5k37xt#heading=h.i84xcin8owkj). _Currently, SIG Core’s goal is to focus on a stable and efficient core that is principled, modular and clean. This means MRV1 will stay in Q2 to handle long tail use cases as we enable more use cases for MRV2_ - [ ] KV cache manager rethink for complex KV cache layout - [ ] Offloading: CPU offloading + Disk + overall connector API on this part of the path - [ ] Address known scheduler issues (avoid excessive preemption, pre...

## 现有链接修复摘要

#44127 [KV Offload] Async CPU memory pinning for SimpleCPUOffloadConnector

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 8: th. - [ ] Model Runner V2 hardening and making it default: - [ ] expand testing coverage - [ ] support wide-ep out of the box. - [ ] Continuing to fill gaps [Model Runner V2 Design Docs](https://docs.google.com/document...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [ ] Work out auto-tuning / out-of-box performance improvement ### Large Scale Serving Slack Channel: #sig-large-scale-serving Project board: https://github.com/orgs/vllm-project/projects/47 Members: @tlrmchlsmth The tea...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: the vLLM Engine Core including Scheduler, KV Cache Manager, Distributed, Model Runner, KV Connector code path. - [ ] Model Runner V2 hardening and making it default: - [ ] expand testing coverage - [ ] support wide-ep o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Roadmap] vLLM Roadmap Q2 2026 rocm In #32455, we broke down vLLM’s goal into various special interest groups (SIGs). Please find below the SIG’s area and their roadmap. You can find regular meetings of these SIGs at [t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: @WoosukKwon @njhill The team focuses on the vLLM Engine Core including Scheduler, KV Cache Manager, Distributed, Model Runner, KV Connector code path. - [ ] Model Runner V2 hardening and making it default: - [ ] expand...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#44127](https://github.com/vllm-project/vllm/pull/44127) | mentioned | 0.6 | [KV Offload] Async CPU memory pinning for SimpleCPUOffloadConnector | ks in. Seems like its aligning with the KV cache ofloading roadmap #39749 ## Test Plan ``` python -m pytest tests/v1/simple_kv_offload ``` ## Test Result ```bash 32 pa |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
